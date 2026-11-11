# Angular scales of the Sun-Earth-Moon system as seen from Alpha Centauri.
import math

# --- Distance to the Alpha Centauri AB system ---
PARALLAX_MAS=747.17    # parallax in milliarcseconds (Kervella et al. 2017)
D_PC=1000.0/PARALLAX_MAS    # distance in parsec: 1pc=parallax of 1 arcsecond

# --- Reference lengths ---
AU_KM= 1.495978707e8    # kilometers in one astronomical unit
EARTH_MOON_KM= 384400.0    # mean Earth-Moon distance in kilometers
RAD_TO_ARCSEC = 180 * 3600 / math.pi    # arcseconds in one radian
R_EARTH_KM= 6371.0    # mean radius of the Earth in kilometers
R_MOON_KM= 1737.4    # mean radius of the Moon in kilometers
A_G_EARTH_LOW= 0.242    # Earth visual geometric albedo, recent estimate (arXiv:2507.22258)
A_G_EARTH_HIGH= 0.367    # Earth visual geometric albedo, classical value (Allen's Astrophysical Quantities)
A_G_MOON= 0.12    # Moon visual geometric albedo (approximate)

def angle_arcsec(size_au, d_pc):
    # Small-angle approximation: angle [arcsec] = length [AU] / distance [pc]
    return size_au / d_pc

sun_earth = angle_arcsec(1.0, D_PC)
earth_moon = angle_arcsec(EARTH_MOON_KM / AU_KM, D_PC)

print(f"Distance to Alpha Centauri: {D_PC:.3f} pc")
print(f"Sun-Earth angle:  {sun_earth * 1000:.0f} mas")
print(f"Earth-Moon angle: {earth_moon * 1000:.2f} mas")

# --- Telescope resolution ---
def rayleigh_arcsec(wavelength_m, diameter_m):
 # Diffraction limit (Rayleigh criterion): angle [rad]=1.22*wavelength/diameter
 return 1.22*wavelength_m/diameter_m*RAD_TO_ARCSEC

telescopes= {
"HST  (2.4 m, 550 nm)": (550e-9, 2.4),
    "JWST (6.5 m, 2.0 um)": (2.0e-6, 6.5),
    "ELT  (39 m, 1.6 um)": (1.6e-6, 39.0),
}

for name, (wavelength_m, diameter_m) in telescopes.items():
 resolution=rayleigh_arcsec(wavelength_m, diameter_m)
 print(f"{name}: {resolution * 1000:.1f} mas | separates Sun-Earth: {resolution < sun_earth} | separates Earth-Moon: {resolution < earth_moon}")

# --- Reflected-light contrast ---
def contrast_full_phase(albedo, radius_km, orbit_km):
 # Planet-to-str flux ratio at full phase: A_g*(R/a)^2
 retun albedo*(radius_km/orbit_km)**2

c_earth_low=contrast_full_phase(A_G_EARTH_LOW, R_EARTH_KM, AU_KM)
c_earth_high=contrast_full_phase(A_G_EARTH_HIGH, R_EARTH_HIGH_KM, AU_KM)
c_moon=contrast_full_phase(A_G_MOON, R_MOON_KM, AU_KM)

print(f"Earth contrast: {c_earth_low:.1e} to {c_earth_high:.1e}")
print(f"Moon contrast:  {c_moon:.1e}")
print(f"The Sun is {1 / c_earth_high:.1e} to {1 / c_earth_low:.1e} times brighter than Earth")