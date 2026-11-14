# Angular scales of the Sun-Earth-Moon system as seen from Alpha Centauri.
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
GM_SUN_KM3_S2 = 1.32712440018e11    # nominal solar gravitational parameter, km^3/s^2 (IAU 2015)


def angle_arcsec(size_au, d_pc):
    # Small-angle approximation: angle [arcsec]= length [AU] / distance [pc]
    return size_au / d_pc

sun_earth= angle_arcsec(1.0, D_PC)
earth_moon= angle_arcsec(EARTH_MOON_KM / AU_KM, D_PC)

print(f"Distance to Alpha Centauri: {D_PC:.3f} pc")
print(f"Sun-Earth angle: {sun_earth * 1000:.0f} mas")
print(f"Earth-Moon angle: {earth_moon * 1000:.2f} mas")


# --- Telescope resolution ---
def rayleigh_arcsec(wavelength_m, diameter_m):
    # Diffraction limit (Rayleigh criterion): angle [rad]=1.22*wavelength/diameter
    return 1.22*wavelength_m/diameter_m*RAD_TO_ARCSEC

telescopes= {
    "HST (2.4 m, 550 nm)": (550e-9, 2.4),
    "JWST (6.5 m, 2.0 um)": (2.0e-6, 6.5),
    "ELT (39 m, 1.6 um)": (1.6e-6, 39.0),
}

for name, (wavelength_m, diameter_m) in telescopes.items():
    resolution= rayleigh_arcsec(wavelength_m, diameter_m)
    print(f"{name}: {resolution*1000:.1f} mas | separates Sun-Earth: {resolution<sun_earth} | separates Earth-Moon: {resolution<earth_moon}")

# --- Reflected-light contrast ---

def contrast_full_phase(albedo, radius_km, orbit_km):
    # Planet-to-star flux ratio at full phase: A_g*(R/a)^2
    return albedo*(radius_km/orbit_km)**2

c_earth_low= contrast_full_phase(A_G_EARTH_LOW, R_EARTH_KM, AU_KM)
c_earth_high= contrast_full_phase(A_G_EARTH_HIGH, R_EARTH_KM, AU_KM)
c_moon= contrast_full_phase(A_G_MOON, R_MOON_KM, AU_KM)

print(f"Earth contrast: {c_earth_low:.1e} to {c_earth_high:.1e}")
print(f"Moon contrast:  {c_moon:.1e}")
print(f"The Sun is {1/c_earth_high:.1e} to {1/c_earth_low:.1e} times brighter than Earth")

# --- Transit ---

def transit_depth(r_planet_km, r_star_km):
    # Fraction of starlight blocked: ratio of the two disk areas
    return (r_planet_km/r_star_km)**2


def circular_speed_kms(a_km):
    # Circular orbit: gravity provides the centripetal force, v=sqrt(GM/a)
    return math.sqrt(GM_SUN_KM3_S2/a_km)


def transit_duration_h(r_planet_km, r_star_km, a_km):
    # Central transit, first to fourth contact: the planet travels 2*(R_star + R_planet)
    return 2*(r_star_km + r_planet_km)/circular_speed_kms(a_km)/3600

depth_earth= transit_depth(R_EARTH_KM, R_SUN_KM)
depth_moon= transit_depth(R_MOON_KM, R_SUN_KM)
duration= transit_duration_h(R_EARTH_KM, R_SUN_KM, AU_KM)

print(f"Earth transit depth: {depth_earth * 1e6:.1f} ppm")
print(f"Moon transit depth: {depth_moon * 1e6:.1f} ppm")
print(f"Transit duration: {duration:.1f} h")

# --- Signal-to-noise: how many transits are needed ---
SNR_THRESHOLD= 7.0    # detection threshold (signal-to-noise ratio)
MIN_TRANSITS= 3    # transits needed to confirm periodic signal


def transits_needed(depth, noise, snr_threshold):
    # S/N of one transit=depth/noise; adding N transits improves it by sqrt(N)
    return math.ceil((snr_threshold*noise/depth)**2)

# Noise levels in ppm: order of magnitude from the Kepler mission design (arXiv:1001.0268)
for noise_ppm in (10, 15, 20):
    noise= noise_ppm*1e-6
    snr_earth= depth_earth/noise
    n_earth= max(transits_needed(depth_earth, noise, SNR_THRESHOLD), MIN_TRANSITS)
    n_moon= transits_needed(depth_moon, noise, SNR_THRESHOLD)
    print(f"Noise {noise_ppm} ppm | Earth: S/N {snr_earth:.1f} per transit, {n_earth} transits needed | Moon: {n_moon} transits needed")

# --- Apparent orbit of the Earth as seen from Alpha Centauri ---
RA_DEG= 219.90206    # right ascension of Alpha Centauri A, J2000
DEC_DEG= -60.83399    # declination of Alpha Centauri A, J2000
OBLIQUITY_DEG= 23.439281    # obliquity of the ecliptic, J2000


def ecliptic_latitude_deg(ra_deg, dec_deg, obliquity_deg):
    # Equatorial to ecliptic latitude: sin(beta)=sin(dec)*cos(eps)-cos(dec)*sin(eps)*sin(ra)
    ra= math.radians(ra_deg)
    dec= math.radians(dec_deg)
    eps= math.radians(obliquity_deg)
    sin_beta= math.sin(dec)*math.cos(eps)-math.cos(dec)*math.sin(eps)*math.sin(ra)
    return math.degrees(math.asin(sin_beta))

beta= ecliptic_latitude_deg(RA_DEG, DEC_DEG, OBLIQUITY_DEG)
a_app= angle_arcsec(1.0, D_PC)    # semi-major axis of the apparent orbit, arcsec
b_app= a_app*abs(math.sin(math.radians(beta)))    # semi-minor axis, arcsec

print(f"Ecliptic latitude of Alpha Centauri: {beta:.1f} deg")
print(f"Apparent orbit of the Earth: {a_app:.3f} x {b_app:.3f} arcsec (b/a = {b_app/a_app:.2f})")

transit_window_deg= math.degrees(R_SUN_KM/AU_KM)    # a transit needs |latitude| below this
print(f"A transit needs |latitude| < {transit_window_deg:.2f} deg -> transit seen from Alpha Centauri: {abs(beta) < transit_window_deg}")

# --- Proper motion of the Sun as seen from Alpha Centauri ---
PM_RA_MAS_YR= -3619.9    # proper motion in right ascension (times cos dec), system barycentre (Kervella et al. 2017)
PM_DEC_MAS_YR= 693.8    # proper motion in declination, system barycentre (Kervella et al. 2017)
V_RADIAL_KMS= 22.332    # speed at which the system approaches the Sun, km/s (Kervella et al. 2017)
KMS_PER_ARCSEC_YR_PC= 4.74047    # speed corresponding to 1 arcsec/yr at 1 pc, km/s
SECONDS_PER_YEAR= 3.15576e7    # seconds in a Julian year

pm_arcsec_yr= math.hypot(PM_RA_MAS_YR, PM_DEC_MAS_YR)/1000    # total proper motion, arcsec/yr
v_transverse= KMS_PER_ARCSEC_YR_PC*pm_arcsec_yr*D_PC    # speed across the line of sight, km/s
v_total= math.hypot(v_transverse, V_RADIAL_KMS)    # total relative speed, km/s
helix_pitch_au= v_total*SECONDS_PER_YEAR/AU_KM    # distance the Sun travels in one year, AU
orbital_speed= 2*math.pi*a_app    # maximum apparent speed of the Earth on its orbit, arcsec/yr

print(f"Proper motion: {pm_arcsec_yr:.3f} arcsec/yr")
print(f"Transverse speed: {v_transverse:.1f} km/s | total relative speed: {v_total:.1f} km/s")
print(f"Maximum apparent orbital speed of the Earth: {orbital_speed:.2f} arcsec/yr")
print(f"Earth appears to move backwards at times (loops): {orbital_speed > pm_arcsec_yr}")
print(f"Helix pitch: {helix_pitch_au:.1f} AU per year")

# --- Vector tools to describe directions on the sky ---
def unit_vector(ra_deg, dec_deg):
    # Unit vector pointing towards a given right ascension and declination
    ra= math.radians(ra_deg)
    dec= math.radians(dec_deg)
    return (math.cos(dec)*math.cos(ra), math.cos(dec)*math.sin(ra), math.sin(dec))

def dot(a, b):
    # Dot product: how much of one vector lies along the other
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def cross(a, b):
    # Cross product: a vector perpendicular to both a and b
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def normalize(a):
    # Same direction, length 1
    length= math.sqrt(dot(a,a))
    return (a[0]/length, a[1]/length, a[2]/length)

# --- Axes of the apparent orbit of the Earth ---
eps= math.radians(OBLIQUITY_DEG)
line_of_sight= unit_vector(RA_DEG, DEC_DEG)    # from the Sun towards Alpha Centauri
ecliptic_pole= (0.0, -math.sin(eps), math.cos(eps))    # north pole of the ecliptic, equatorial coordinates
major_axis= normalize(cross(ecliptic_pole, line_of_sight))    # long axis of the apparent orbit
minor_axis= cross(line_of_sight, major_axis)    # short axis, perpendicular on the sky

print(f"Major axis . line of sight: {dot(major_axis, line_of_sight):.3f}")
print(f"Minor axis . line of sight: {dot(minor_axis, line_of_sight):.3f}")
print(f"Major axis . minor axis: {dot(major_axis, minor_axis):.3f}")
print(f"Length of the minor axis: {math.sqrt(dot(minor_axis, minor_axis)):.3f}")

# --- Drift of the Sun seen from Alpha Centauri, compared with the apparent orbit ---
ra= math.radians(RA_DEG)
dec= math.radians(DEC_DEG)
east= (-math.sin(ra), math.cos(ra), 0.0)    # direction of increasing right ascension
north= (-math.sin(dec)*math.cos(ra), -math.sin(dec)*math.sin(ra), math.cos(dec))    # direction of increasing declination

# Seen from Alpha Centauri the Sun drifts opposite to the proper motion seen from the Sun (arcsec/yr)
drift= tuple(-(PM_RA_MAS_YR*east[i] + PM_DEC_MAS_YR*north[i])/1000 for i in range(3))
drift_along= dot(drift, major_axis)    # component along the long axis, arcsec/yr
drift_across= dot(drift, minor_axis)    # component along the short axis, arcsec/yr
drift_angle= math.degrees(math.atan2(abs(drift_across), abs(drift_along)))

print(f"Drift along the long axis: {abs(drift_along):.2f} arcsec/yr | across: {abs(drift_across):.2f} arcsec/yr")
print(f"Angle between drift and long axis: {drift_angle:.1f} deg")
print(f"Loops (exact condition, along the long axis): {orbital_speed>abs(drift_along)}")

# --- Apparent trajectory of the Earth over a few years ---
YEARS= 3    # length of the simulated observation, years
N_POINTS= 1500    # number of points along the path

t= np.linspace(0, YEARS, N_POINTS)    # time, years
omega= 2*math.pi    # angular frequency of the Earth's orbit, rad/yr
sun_x= drift_along*t    # position of the Sun along the long axis, arcsec
sun_y= drift_across*t    # position of the Sun along the short axis, arcsec
earth_x= sun_x + a_app*np.cos(omega*t)    # Earth = Sun drift + apparent orbit, arcsec
earth_y= sun_y - b_app*np.sin(omega*t)    # minus sign: the Earth moves clockwise on the sky

velocity_x= np.gradient(earth_x, t)    # apparent velocity along the long axis, arcsec/yr
backward_fraction= np.mean(velocity_x*np.sign(drift_along) < 0)    # fraction of time the Earth moves against the drift

print(f"Earth path over {YEARS} years: x from {earth_x.min():.2f} to {earth_x.max():.2f} arcsec, y from {earth_y.min():.2f} to {earth_y.max():.2f} arcsec")
print(f"Fraction of time the Earth moves backwards along the drift: {backward_fraction:.0%}")

# --- Animation: apparent trajectory of the Earth ---
SUN_COLOR, SUN_EDGE, EARTH_COLOR= "gold", "darkorange", "tab:blue"
STEP= 10    # use one point every STEP, to keep the GIF light
FPS= 25    # frames per second of the GIF

fig, ax= plt.subplots(figsize=(10, 4))
ax.set_aspect("equal")
ax.set_xlim(-1, 12.5)
ax.set_ylim(-0.8, 3.4)
ax.set_xlabel("arcsec, along the long axis")
ax.set_ylabel("arcsec, along the short axis")
ax.set_title("Apparent trajectory of the Earth seen from Alpha Centauri (symbols enlarged)", fontsize=10)

sun_path, = ax.plot([], [], "--", color=SUN_EDGE, lw=1, label="Sun")
earth_path, = ax.plot([], [], color=EARTH_COLOR, lw=1.2, label="Earth")
sun_dot, = ax.plot([], [], "o", color=SUN_COLOR, mec=SUN_EDGE, ms=12, zorder=3)
earth_dot, = ax.plot([], [], "o", color=EARTH_COLOR, ms=5, zorder=3)
time_text= ax.text(0.02, 0.92, "", transform=ax.transAxes)
ax.legend(frameon=False, loc="upper right", fontsize=9)


def update(i):
    # Draw everything from the start up to point i
    sun_path.set_data(sun_x[:i + 1], sun_y[:i + 1])
    earth_path.set_data(earth_x[:i + 1], earth_y[:i + 1])
    sun_dot.set_data([sun_x[i]], [sun_y[i]])
    earth_dot.set_data([earth_x[i]], [earth_y[i]])
    time_text.set_text(f"t = {t[i]:.2f} yr")
    return sun_path, earth_path, sun_dot, earth_dot, time_text

animation= FuncAnimation(fig, update, frames=range(0, N_POINTS, STEP), interval=1000/FPS, blit=True)
animation.save("apparent_trajectory.gif", writer="pillow", fps=FPS)
print("Saved apparent_trajectory.gif")
