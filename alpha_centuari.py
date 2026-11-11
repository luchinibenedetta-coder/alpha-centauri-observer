# Angular scales of the Sun-Earth-Moon system as seen from Alpha Centauri.

# --- Distance to the Alpha Centauri AB system ---
PARALLAX_MAS=747.17    # parallax in milliarcseconds (Kervella et al.2017)
D_PC=1000.0/PARALLAX_MAS    # distance in parsec: 1pc=parallax of 1 arcsecond

# --- Reference lengths ---
AU_KM= 1.495978707e8    # kilometers in one astronomical unit
EARTH_MOON_KM= 384400.0    # mean Earth-Moon distane in à
RAD_TO_ARCSEC = 180 * 3600 / math.pi    # arcseconds in one radian

def angle_arcsec(size_au, d_pc):
    # Small-angle approximation: angle [arcsec] = length [AU] / distance [pc]
    return size_au / d_pc

sun_earth = angle_arcsec(1.0, D_PC)
earth_moon = angle_arcsec(EARTH_MOON_KM / AU_KM, D_PC)

print(f"Distance to Alpha Centauri: {D_PC:.3f} pc")
print(f"Sun-Earth angle:  {sun_earth * 1000:.0f} mas")
print(f"Earth-Moon angle: {earth_moon * 1000:.2f} mas")

# --- telescope resolution ---
def rayleigh_arcsec(wavelength_m, diameter_m):
 # Diffraction limit (Rayleigh criterion): angle [rad]=1.22*wavelength/diameter
 return 1.22*wavelength_m/diameter_m*RAD_TO_ARCSEC

telescpes={
    "HST  (2.4 m, 550 nm)": (550e-9, 2.4),
    "JWST (6.5 m, 2.0 um)": (2.0e-6, 6.5),
    "ELT  (39 m, 1.6 um)": (1.6e-6, 39.0),
}

for name, (wavelength_m, diameter_m) in telescopes.items():
 resolution=rayleigh_arcsec(wavelength_m, diameter_m)
 print(f"{name}:{resolution*1000:.1f}mas|separates Sun-Earth:{resolution < sun_earth}|separates Earth-Moon:{resolution<earth_moon}")