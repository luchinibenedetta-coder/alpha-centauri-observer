# Angular scales of the Sun-Earth-Moon system as seen from Alpha Centauri.
import math

# --- Distance to the Alpha Centauri AB system ---
PARALLAX_MAS=747.17    # parallax in milliarcseconds (Kervella et al. 2017)
D_PC=1000.0/PARALLAX_MAS    # distance in parsec: 1pc=parallax of 1 arcsecond

# --- Reference lengths ---
AU_KM= 1.495978707e8    # kilometers in one astronomical unit
EARTH_MOON_KM= 384400.0    # mean Earth-Moon distance in kilometers
RAD_TO_ARCSEC= 180 * 3600 / math.pi    # arcseconds in one radian
R_EARTH_KM= 6371.0    # mean radius of the Earth in kilometers
R_MOON_KM= 1737.4    # mean radius of the Moon in kilometers
A_G_EARTH_LOW= 0.242    # Earth visual geometric albedo, recent estimate (arXiv:2507.22258)
A_G_EARTH_HIGH= 0.367    # Earth visual geometric albedo, classical value (Allen's Astrophysical Quantities)
A_G_MOON= 0.12    # Moon visual geometric albedo (approximate)
R_SUN_KM = 695700.0    # nominal solar radius in kilometers (IAU 2015)
GM_SUN_KM3_S2 = 1.32712440018e11    # nominal solar gravitational parameter,km^3/s^2 (IAU 2015)

def angle_arcsec(size_au, d_pc):
    # Small-angle approximation: angle [arcsec]= length [AU] / distance [pc]
    return size_au / d_pc

sun_earth= angle_arcsec(1.0, D_PC)
earth_moon= angle_arcsec(EARTH_MOON_KM / AU_KM, D_PC)

print(f"Distance to Alpha Centauri:{D_PC:.3f} pc")
print(f"Sun-Earth angle:{sun_earth * 1000:.0f} mas")
print(f"Earth-Moon angle:{earth_moon * 1000:.2f} mas")

# --- Telescope resolution ---
def rayleigh_arcsec(wavelength_m, diameter_m):
 # Diffraction limit (Rayleigh criterion): angle [rad]=1.22*wavelength/diameter
 return 1.22*wavelength_m/diameter_m*RAD_TO_ARCSEC

telescopes= {
"HST(2.4 m, 550 nm)":(550e-9, 2.4),
    "JWST(6.5 m, 2.0 um)":(2.0e-6, 6.5),
    "ELT(39 m, 1.6 um)":(1.6e-6, 39.0),
}

for name, (wavelength_m, diameter_m) in telescopes.items():
 resolution= rayleigh_arcsec(wavelength_m, diameter_m)
 print(f"{name}:{resolution*1000:.1f} mas|separates Sun-Earth: {resolution<sun_earth}|separates Earth-Moon:{resolution<earth_moon}")

# --- Reflected-light contrast ---
def contrast_full_phase(albedo, radius_km, orbit_km):
 # Planet-to-star flux ratio at full phase: A_g*(R/a)^2
 return albedo*(radius_km/orbit_km)**2

c_earth_low=contrast_full_phase(A_G_EARTH_LOW, R_EARTH_KM, AU_KM)
c_earth_high=contrast_full_phase(A_G_EARTH_HIGH, R_EARTH_KM, AU_KM)
c_moon=contrast_full_phase(A_G_MOON, R_MOON_KM, AU_KM)

print(f"Earth contrast: {c_earth_low:.1e} to {c_earth_high:.1e}")
print(f"Moon contrast:  {c_moon:.1e}")
print(f"The Sun is {1/c_earth_high:.1e} to {1/c_earth_low:.1e} times brighter than Earth")

# --- Transit ---
def transit_depth(r_planet_km,r_star_km):
    # Fraction of starlight blocked: ratio of the two disk areas
    return (r_planet_km/r_star_km)**2

def circular_speed_kms(a_km):
    # Circular orbit: gravity provides the centripetal force,v=sqrt(GM/a)
    return math.sqrt(GM_SUN_KM3_S2/a_km)

def transit_duration_h(r_planet_km,r_star_km,a_km):
    # Central transit,first to fourth contact:the planet travels 2*(R_star + R_planet)
    return 2*(r_star_km + r_planet_km)/circular_speed_kms(a_km)/3600

depth_earth=transit_depth(R_EARTH_KM,R_SUN_KM)
depth_moon=transit_depth(R_MOON_KM,R_SUN_KM)
duration=transit_duration_h(R_EARTH_KM,R_SUN_KM,AU_KM)

print(f"Earth transit depth:{depth_earth * 1e6:.1f} ppm")
print(f"Moon transit depth:{depth_moon * 1e6:.1f} ppm")
print(f"Transit duration:{duration:.1f} h")

# --- Signal-to-noise: how many transits are needed ---
SNR_TRESHOLD= 7.0    # detection treshold (signal-to-noise ratio)
MIN_TRANSITS= 3    # transits needed to confirm periodic signal

def transits_needed(depth, noise, snr_treshold):
    # S/N of one transit=depth/noise; adding N transits improves it by sqrt(N)
    return math.ceil((snr_treshold*noise/depth)**2)

# Noise levels in ppm: order of magnitude from the Kepler mission design (arXiv:1001.0268)
for noise_ppm in (10, 15, 20):
    noise=noise_ppm*1e-6
    snr_earth=depth_earth/noise
    n_earth=max(transits_needed(depth_earth, noise, SNR_TRESHOLD), MIN_TRANSITS)
    n_moon=transits_needed(depth_moon, noise, SNR_TRESHOLD)
    print(f''Noise{noise_ppm}ppm|Earth:S/N{snr_earth:.1f} per transit, {n_earth} transits needed|Moon:{n:moon} transits needed")
