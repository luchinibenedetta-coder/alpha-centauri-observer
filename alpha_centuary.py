# Angular scales of the Sun-Erth-Moon system as seen from Alpha Centauri.

# --- Distance to the Alpha Centauri AB system ---
PARALLAX_MAS=747.17    # parallax in milliarcseconds (Kervella et al.2017)
D_PC=1000.0/PARALLAX_MAS    # distance in parsec: 1pc=parallax of 1 arcsecond

# --- Reference lenghts ---
AU_KM= 1.495978707e8    # kilometers in one astronomical unit
EARTH_MOON_KM= 384400.0    # mean Earth-Moon distance in kilometers

def angle_arcsex(1.0, d_pc):
    # Small-angle approximation: angle [arcsec] = length [AU] / distance [pc]
    return size_au / d_pc

sun_earth = angle_arcsec(1.0, D_PC)
earth_moon = angle_arcsec(EARTH_MOON_KM / AU_KM, D_PC)

print(f"Distance to Alpha Centauri: {D_PC:.3f} pc")
print(f"Sun-Earth angle:  {sun_earth * 1000:.0f} mas")
print(f"Earth-Moon angle: {earth_moon * 1000:.2f} mas")