# Alpha-Centauri Observer

## Introduction
This project investigates whether an observer located in the Alpha Centauri system can detect and study the Earth–Moon system using astronomical instruments similar to, or more advanced than, those available today. The study considers whether the Earth can be detected next to the Sun, whether the Moon can also be observed, and whether the Earth's motion can be reconstructed from its apparent position and changes in brightness.

The analysis focuses on the main physical and observational challenges: the distance between the two stellar systems, the angular separation between the objects, the amount of light reflected or emitted by the Earth and the Moon, and the limits of astronomical instruments. Particular attention is given to **albedo**, which describes how much incoming radiation a body reflects. Together with the illumination geometry and the phase of the planet, albedo determines the amount of reflected light that could reach a distant observer. An important part of the project is also distinguishing between **direct imaging**, **indirect detection**, and **physical characterization**, since each method provides different information and requires different instrumental capabilities.

At a distance of approximately 1.34 pc (4.37 light-years), corresponding to the distance of Alpha Centauri A, the Earth–Sun separation would appear to be about 0.747 arcseconds. This angular separation is not extremely small in itself. However, detecting the Earth close to the Sun is much more difficult than simply separating the two objects in terms of angular distance. The main problem is the large difference in brightness between them: the light reflected by the Earth is several orders of magnitude weaker than the light coming directly from the Sun. This difference depends, among other factors, on the Earth's albedo and on its phase angle. For this reason, reducing the amount of stellar light reaching the detector is one of the main requirements for direct imaging.

The project therefore also considers methods that do not require a direct image of the planet. In ideal configuration, where the Earth's orbit is seen edge-on, the Earth could periodically pass in front of the Sun from the observer's point of view. During such a transit, the apparent brightness of the Sun would decrease by approximately 84 parts per million (ppm), for about 13 hours. In principle, this signal could be detected through repeated, high-precision photometric observations. However, this result applies to only a favourable orbit configuration and does not describe what an observer at the actual position of Alpha Centauri would see.

The geometry of the real system is different: Alpha Centauri has an adopted ecliptic latitude of approximately -42.6°, which is far outside the narrow range of angles required to observe an Earth transit across the Sun. The ideal edge-on configuration is studied separately as a special case, useful for understanding what could be achieved with transit observations under more favourable conditions.

Detecting the Moon would be even more difficult as its maximum angular separation from the Earth would be approximately 1.92 milliarcseconds (mas), and the amount of reflected light it contributes would be much lower than that of the Earth. Its albedo, size and illumination phase all affect its reflected-light signal. Both its direct detection and the measurement of its effects on the observed brightness would therefore require more demanding observations.

Another objective of the project is to study the apparent motion of the Earth as seen from Alpha Centauri. The Earth's annual orbital motion is combined with the relative proper motion of the two stellar systems. As a result, the apparent path is not simply a fixed ellipse: the Earth's orbital motion is added to the gradual displacement caused by the motion of the Sun relative to Alpha Centauri. The corresponding three-dimensional motion is also considered.

Finally, the project examines whether an observer at Alpha Centauri could study the Earth's atmosphere through spectroscopy. Particular attention is given to the possible detection of atmospheric absorption features associated with oxygen (O₂), ozone (O₃), and methane (CH₄). The analysis distinguishes between the theoretical presence of these features in the Earth's spectrum and the practical difficulty of measuring them with real instruments.

Overall, the possibility of observing the Earth from Alpha Centauri cannot be answered with a simple yes or no. It depends on what is meant by observation, on the geometry of the system, on the physical properties of the observed bodies, and on the instruments available. Direct imaging, transit photometry, astrometric measurements, and atmospheric spectroscopy provide different types of information and are affected by different limitations.

## System definition and physical parameters
Before asking what an observer could see, the observer and the observed object have to be defined. The observer was placed in the Alpha Centauri system, and the object of study is the Earth-Moon pair orbiting the Sun. The distance of Alpha Centauri is about 2.76x10^5 AU, while the two main stars, A and B, are separated by only a few tens of AU. For every order-of-magnitude estimate below, the exact position of the observer inside the system is therefore irrelevant, and the values for the barycentre of the system were used throughout. 
The parallax of the barycentre is π=747.17 +/- 0.61 mas (Kervella 2017), ehich gave a distance d=1/π=1.338 pc, or 4.364 light-years. The proper motion is μ_α=-3619.9 +/- 3.9 mas/yr in right ascension (the cos(δ) factor was already included) and μ_δ=+693.8 +/- 3.9 mas/yr in declination, and the radial velocity is -22.332 +/- 0.005 km/s, the minus sign meaning that the system is approaching the Sun. For Alpha Centauri A alone, the distance is about 1.332 pc, a difference of roughly 0.5% which does not change any conclusion. The sky position was taken to be that of Alpha Centauri A (J2000): α=14h 39m 36.494s=219.902° and δ=-60° 50' 02.37"=-60.834°. It is needed later to compute the ecliptic latitude of the observer.
For the Sun the nominal values R_Sun=695 700 km and G*M_Sun=1.32712 x 10^20 m^3 s^-2 were used (IAU 2015). The mean radii R_Earth=6371 km and R_Moon=1737.4 km, and a mean Earth-Moon distance of 348 000 km (NASA Moon Fact Sheet). The reflectivity of a body is described by the geometric albedo  A_g, the ratio between the brightness of the body at full phase and that of a flat Lambertian disc of the same size. For the Moon A_g=0.12 was adopted. For the Earth two values were used: 0.242 (Robinson 2026) and 0.367 (Cox 2000). They bracketed the uncertainty, and the conclusions did not depend on which one was chosen. 

The basic tool for converting a physical size into what the observer sees was the small-angle relation. By definition of the parsec, an object of size s at a distance d subtends an angle 

```
θ[arcsec]=s[AU]/d[pc]
```

Applying it gives the angular scale of the whole problem. The Sun-Earth separation of 1 AU appears as 747 mas, which was not tiny by the standards of modern telescopes. The Earth-Moon distance, shrinks to only 1.92 mas. The Sun had an angular diameter of 6.95 mas, the Earth of 0.064 mas and the Moon of 0.017 mas, so both planetary bodies are point sources for any conceivable instrument.

| Object | Size | Angle seen from Alpha Centauri |
|---|---|---|
| Sun-Earth distance | 1 AU | 747 mas |
| Earth-Moon distance (mean) | 384 400 km | 1.92 mas |
| Sun (diameter) | 1.39 x 10^6 km | 6.95 mas |
| Earth (diameter) | 12 742 km | 0.064 mas |
| Moon (diameter) | 3475 km | 0.017 mas |

Brightness is expressed in magnitudes, with

```
m1-m2=-2.5*log10(F1/F2)
m=M+5*log10(d/10 pc)
```

With an absolute V maginitude M_V=4.83 for the Sun, the Sun seen from Alpha Centauri has an apparent magnitude m_Sun=0.46, about as bright as Alpha Centauri A appears to us. This is the glare against which the Earth has to be detected.

## Angular resolution
The first requirement for seeing two objects as separate is that the telescope can tell them apart. Because of diffraction, a point source observed through a circular aperture of diameter D does not form a point in the image, but the Airy pattern

```
I(θ)/I0 = [2*J1(x)/x ^2        with   x=π*D*θ/λ
```

where J1 is the Bessel function of the first kind. The central peak was surrounded by faint rings, and the first dark dings falls at x=3.8317. Two equally bright sources are conventionally considered resolved when the peak of one falls on the first zero of the other, which gives the Rayleigh criterion

```
θ_R=1.22*λ/D
```

Three representative instruments were compared. The Sun-Eath separation of 747 mas is within reach of all of them, whereas the Earth-Moon separation of 1.92 mas is within the reach of none.

| Instrument | λ | D | θ_R | Sun-Earth (747 mas) | Earth-Moon (1.92 mas) |
|---|---|---|---|---|---|
| HST | 550 nm | 2.4 m | 57.7 mas | resolved | not resolved |
| JWST | 2 μm | 6.5 m | 77.4 mas | resolved | not resolved |
| ELT | 1.6 μm | 39 m | 10.3 mas | resolved | not resolved |

To resolve the Earth-Moon pair with a single mirror, the required diameter is

```
D>=1.22*λ/(1.92 mas)~72m at 550 nm      (~210m at 1.6μm)
```

which exceeds the size of any telescope that exists or is under construction. An interferometer does better: for two equally bright sources of separations observed with a baseline B, the fringe visibility is

```
V=abs(cos(π*B*s/λ))
```

which first vanishes at s=λ/(2*B). This is the conventional resolution of an interferometer, and it is the reason why long baselines are the natural route towards the Moon. Resolution, however, is only a necessary condition. The Sun-Earth pair is resolved with a wide margin and yet the Earth cannot be seen, because the light of the Sun spilled over it.

## Planet-star contrast and reflected light
A planet shines almost entirely by reflected starlight, and a simple model shows how little of it reaches the observer. The planet was replaced by a Lambertian disc of radius R and unit albedo, facing both the star and the observer. At the orbital distance a the disc intercepts the flux F_a= L/(4π a^2) over an area π R^2 and it re-emits that energy isotropically with a radiance F_a/π. At a distance d the flux received from the disc is  F_a R^2/d^2, while the direct flux from the star is L/(4π d^2). The ratio of the two is (R/a)^2, and does not depend on d. A real planet is not described by two corrections: the geometric albedo A_g, and a phase function Φ(α) normalised to Φ(0)=1, where α is the phase angle, that is the angle-Sun-planet-observer. The contrast, defined as the ratio between planet flux and star flux is

```
c=F_planet/F_star=A_g*(R/a)^2*Φ(α)

Φ_Lambert(α)=[sin(α)+(π - α)*cos(α)]/π
```

The Lambert phase function is an idealisation, and the real Earth deviates from it by an amount that was not quantified here. The table shows how quickly the reflected light drops as the planet moves away from full phase.

| α | 0° | 30° | 42.6° | 60° | 90° | 120° | 150° |
|---|---|---|---|---|---|---|---|
| Φ_Lambert | 1.00 | 0.88 | 0.78 | 0.61 | 0.32 | 0.110 | 0.015 |

At full phase (Φ = 1), and with (R_Earth / a)^2=1.81x10^-9, the Earth has a contrast of 4.4x10^-10 for A_g=0.242 and 6.7x10^-10 for A_g=0.367. The Moon, with a smaller radius and a lower albedo, reaches only

```
c_Moon=0.12*(R_Moon/a)^2=1.6x10^-11
```

The Sun therefore outshines the Earth by a factor between 1.5 and 2.3 billion, and the Moon by about 6x10^10. These are upper limits, because the Earth is never at full phase for the real Alpha Centauri.

Reflected light is not the only option. The Earth also emits its own thermal radiation, and in the infrared the contrast is considerably better. With a bond albedo A_B=0.3 and a solar constant S=1361 W/m^2, the equilibrium temperature is

```
T_eq=[(1-A_B)*S/(4 * σ)]^(1/4)=255 K
```

At 10 μm the ratio of the Planck functions of the Earth and of the Sun is (e^x_Sun-1)/(e^x_Earth-1), with x=14388/(λ[μm]*T[K]), so that

```
c(10 μm) ~ (R_Earth/R_Sun)^2 * (e^0.249-1)/(e^5.65-1)
         ~ 8.4x10^-5*1.0x10^-3
         ~ 8x10^-8
```

This is about two orders of magnitude better than in the visible. The price is a coarser resolution, which scales with λ, but even the ELT at 10 μm (64.5 mas) is far below the 747 mas of the Sun-Earth separation. The estimate uses T_eq as if it were a brightness tempreature; a real brightness temperatutre in an atmospheric window would change the result by a factor of order 2.

The last piece of the contrast problem is the light of the star itself, diffracted by the telescope. Far from the centre of the pattern, for x'=θ/(λ/D)>> 1, one can use the asymptotic form of the Bessel function, J1(x)~sqrt(2/(π*x))*cos(x-3π/4), and average over the oscillations, which gives a smooth halo

```
<I/I0>~4/(π^4*x'^3)
```

Evaluated at the position of the Earth (747 mas) for an ideal circular aperture with no obstruction and no atmosphere, the halo is still bigger than the planet in every case considered.

| Telescope | x' at 747 mas | Halo | Halo / c_Earth |
|---|---|---|---|
| HST, 550 nm | 15.8 | 1.0 x 10^-5 | ~ 2 x 10^4 |
| ELT, 550 nm | 257 | 2.4 x 10^-9 | ~ 5 |
| ELT, 1.6 μm | 88 | 6.0 x 10^-8 | ~ 10^2 |

Even a perfect large telescope therefore needs a coronagraph, an instrument that suppresses the starlight before it reaches the detector. In real instruments the limit comes from speckles, obstructions and wavefront errors rather than from ideal diffracrion. To place the Earth in context, a review of adaprive optics for high-contrast imaging (arXiv:1701.00836) quotes performances of order 10^-5 at o.5" and below 10^-6 at a few resolution elements for ground-based systems, which I treat as an order of magnitude. The Roman Coronagraph Instrument has a 10^-7 flux-ratio detection limit (5σ, single band) at 575 nm and 6-9 λ/D for stars of V ~ 5. Imaging an Earth twin requires 10^-10 or better, which is the requirement of the HabEx study (arXiv:1809.09674), and the Habitable Worlds Observatory is expected to need a similar level.

## Photon flux and instrumental limitations
A different question is whether the planet sends enough photons to be measured at all. The number of photons detected from a source of apparent magnitude m is

```
N=F0*10^(-0.4*m)*A*ε*t
```
where F0~9x10^5 photons s^-1 cm^-2 is the flux of a zero-magnitude star in the V band (approximate), A the collecting area, ε = 0.3 an assumed overall efficiency, and t the exposure time. For a source with no background S/N=sqrt(N). The magnitude of the planet follows from its contrast through m=m_Sun-2.5*log10(c).

| Object | m | HST (4.5 m^2) | ELT (~ 980 m^2) |
|---|---|---|---|
| Sun | 0.46 | 7.9 x 10^9 photons/s | 1.7 x 10^12 photons/s |
| Earth, full phase | 23.6 | 4.3 photons/s | 940 photons/s |
| Earth, quadrature | 24.9 | 1.4 photons/s | 300 photons/s |
| Moon, full phase | 27.4 | 0.13 photons/s | 28 photons/s |

A few photons per second reach HST from the Earth, and hundreds reach the ELT, so an exposure of a few minutes connects thousands of photons even from the Moon. The photon budget is not the obstacle. The obstacle is that these photons are buried in the diffracted and scattered light of a source nine orders of magnitude brighter, so the problem is one of contrast and not of flux. The three requirements side by side:

| Requirement | Earth | Moon |
|---|---|---|
| Resolution | satisfied | not satisfied (any single telescope) |
| Photons | satisfied | satisfied |
| Contrast (~ 5 x 10^-10, ~ 2 x 10^-11) | not satisfied today | not satisfied even for planned instruments |

## Orbital geometry and the meaning of alignment
The problem states that Earth and Alpha Centauri are "aligned". Taken literally the statement is empty: two points always lie on a line. The word acquires physical content only when the Sun is included, and there are two meaningful readings. The first is that the Sun, the Earth and the observer are collinear, which happens at a single instant per orbit with α=180° in a transit and a α=0° in an occultation. The second, more useful, is that the observer lies close to the orbital plane of the Earth, so that the Earth can cross the solar disc. The second reading was the one adopted from there on.

Let i be the inclination, the angle between the normal to the orbit and the line of sight. For a circular orbit radius a, the impact parameter in solar radii is

```
b =(a/R_Sun)*cos(i)
```

and a transit takes place if b<1 (more precisely b<1+R_Earth/R_Sun if grazing transits are included). Since a/R_Sun=215, this requires

```
cos(i)<R_Sun/a=4.65x10^-3
->  the angle (i - 90°), in absolute value, must be smaller than 0.27° = 959 arcsec
```

The observer has to lie within a band of about half a degree around the ecliptic plane. For an observer in a random direction the geometric probability is p=R_Sun/a=0.47%, about one chance in 215.

Alpha Centauri in not in a random direction, and its position is known. Its ecliptic latitude β follows from the equatorial coordinates (α, δ) and the obliquity ε = 23.4393°:

```
sin(β)=sin(δ)*cos(ε)-cos(δ)*sin(ε)*sin(α)
->β=-42.6°
```

This is about 160 half-widths away from the transit window, so the real Alpha Centauri never sees the Earth cross the Sun. The edge-on geometry is a hypothetical scenario, which was studied separately because it is the only one in which transit techniques work.

The same geometry fixes the phaase angle at which the Earth is seen. For a circular orbit with orbital longitude φ, cos(α)=-cos(φ)*cos(β), and the apparent separation from the Sun in s=a*sqrt(1-cos(α)^2)=a*sin(α), for any inclination. The inclination only limits the range of α:

```
abs(β)<=α<=180°-abs(β)      ->      42.6°<=α<=137.4°
```

The Earth is therefore never at full phase and never at new phase. Its best illumination occurs at α=42.6°, where the illuminated fraction is k=(1+cos(α))/2=0.87 and the Lambert phase function is  Φ=0.78, at the minimum separation of 0.506". This gives a Lambert contrast of about 4.2x10^-10 for A_g=0.30, slightly lower than the full-phase value, which is why the latter is an upper limit.

How long would such alignment last? The relative proper motion of the two systems changes the direction of the observer, as seen from the Sun, by μ=3.686"/yr. The window is about 1918" wide, so crossing it takes at least about 250 years (a lower bound, since only the component of μ perpendicular to the ecliptic matters). The configuration is extremely rare and very short-lived on human time scale.
