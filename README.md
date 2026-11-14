# Alpha-Centauri Observer

## Introduction
This project investigates whether an observer located in the Alpha Centauri system could detect and study the Earth–Moon system using astronomical instruments similar to, or more advanced than, those available today. The study considers whether the Earth could be detected next to the Sun, whether the Moon could also be observed, and whether the Earth's motion could be reconstructed from its apparent position and changes in brightness.

The analysis focuses on the main physical and observational challenges: the distance between the two stellar systems, the angular separation between the objects, the amount of light reflected or emitted by the Earth and the Moon, and the limits of astronomical instruments. Particular attention is given to **albedo**, which describes how much incoming radiation a body reflects. Together with the illumination geometry and the phase of the planet, albedo determines the amount of reflected light that could reach a distant observer. An important part of the project is also distinguishing between **direct imaging**, **indirect detection**, and **physical characterization**, since each method provides different information and requires different instrumental capabilities.

At a distance of approximately 1.34 pc (4.37 light-years), corresponding to the distance of Alpha Centauri A, the Earth–Sun separation would appear to be about 0.747 arcseconds. This angular separation is not extremely small in itself. However, detecting the Earth close to the Sun is much more difficult than simply separating the two objects in terms of angular distance. The main problem is the large difference in brightness between them: the light reflected by the Earth is several orders of magnitude weaker than the light coming directly from the Sun. This difference depends, among other factors, on the Earth's albedo and on its phase angle. For this reason, reducing the amount of stellar light reaching the detector is one of the main requirements for direct imaging.

The project therefore also considers methods that do not require a direct image of the planet. In ideal configuration, where the Earth's orbit is seen edge-on, the Earth could periodically pass in front of the Sun from the observer's point of view. During such a transit, the apparent brightness of the Sun would decrease by approximately 84 parts per million (ppm), for about 13 hours. In principle, this signal could be detected through repeated, high-precision photometric observations. However, this result applies to only a favourable orbit configuration and does not describe what an observer at the actual position of Alpha Centauri would see.

The geometry of the real system is different: Alpha Centauri has an adopted ecliptic latitude of approximately -42.6°, which is far outside the narrow range of angles required to observe an Earth transit across the Sun. The ideal edge-on configuration is studied separately as a special case, useful for understanding what could be achieved with transit observations under more favourable conditions.

Detecting the Moon would be even more difficult as its maximum angular separation from the Earth would be approximately 1.92 milliarcseconds (mas), and the amount of reflected light it contributes would be much lower than that of the Earth. Its albedo, size and illumination phase all affect its reflected-light signal. Both its direct detection and the measurement of its effects on the observed brightness would therefore require more demanding observations.

Another objective of the project is to study the apparent motion of the Earth as seen from Alpha Centauri. The Earth's annual orbital motion is combined with the relative proper motion of the two stellar systems. As a result, the apparent path is not simply a fixed ellipse: the Earth's orbital motion is added to the gradual displacement caused by the motion of the Sun relative to Alpha Centauri. The corresponding three-dimensional motion is also considered.

Finally, the project examines whether an observer at Alpha Centauri could study the Earth's atmosphere through spectroscopy. Particular attention is given to the possible detection of atmospheric absorption features associated with oxygen (O₂), ozone (O₃), and methane (CH₄). The analysis distinguishes between the theoretical presence of these features in the Earth's spectrum and the practical difficulty of measuring them with real instruments.

Overall, the possibility of observing the Earth from Alpha Centauri cannot be answered with a simple yes or no. It depends on what is meant by observation, on the geometry of the system, on the physical properties of the observed bodies, and on the instruments available. Direct imaging, transit photometry, astrometric measurements, and atmospheric spectroscopy provide different types of information and are affected by different limitations.

## System definition and physical parameters
Before asking what an observer could see, we have to say precisely where the observer is looking at. The observer is placed in the Alpha Centauri system, and the object of study is the Earth-Moon pair orbiting the Sun. The distance of Alpha Centauri is about 2.76x10^5 AU, while the two main stars, A and B, are separated by only a few tens of AU. For every order-of-magnitude estimate below, the exact position of the observer inside the system is therefore irrelevant, and I use the values for the barycentre of the system throughout. 
The distance and the motion of the system come from the astrometric analysis of Kervella, Thévenin and Lovis (2017). They give a parallax of π = 747.17 +/- 0.61 mas for the barycentre, from which the distance follows as d = 1/π = 1.338 pc, or 4.364 light-years. The proper motion of a barycentre is μ_α = -3619.9 +/- 3.9 mas/yr in right ascension (the cos(δ) factor is already included) and μ_δ = +693.8 +/- 3.9 mas/yr in declination, and the radial velocity is -22.332 +/- 0.005 km/s, the minus sign meaning that the system is approaching the SUn. If one uses Alpha Centauri A alone, the distance is about 1.332 pc, a difference of roughly 0.5% which does not change any conclusion. For the sky position I use the J2000 coordinates of ALpha Centauri A, α = 14h 39m 36.494s = 219.902° and δ = -60° 50' 02.37" = -60.834°, which are needed later to compute the ecliptic latitude of the observer.
For the Sun and the Earth I adopt the nominal values of IAU 2015 Resolution B3, R_Sun = 695 700 km and G*M_Sun = 1.32712 x 10^20 m^3 s^-2, together with the mean radii R_Earth = 6371 km and R_Moon = 1737.4 km, and a mean Earth-Moon distance of 348 000 km. The reflectivity of the two bodies is described by the geometric albedo  A_g, the ratio between the brightness of a planet seen at full phase and that of a flat Lambertian disc of the same size. For the Moon I use A_g = 0.12. For the Earth the value is less obvious, and I keep two. The recent determination by Robinson (2026), A_g = 0.242 (+0.005 / -0.004), is the one I consider best. The older value A_g = 0.367, which comes from historical Earthshine data (Danjon) and appears to in ALlen's *Astrophysical Quantities* (Cox 2000), is retained only to bracket the result, since Robinson argues that it overestimates the true albedo.
The basic tool for converting a physical size into what the observer sees is the small-angle relation. By definition of the parsec, an object of size s at a distance d subtends an angle 

```
θ [arcsec] = s [AU] / d [pc]
```

Applying this to the quantities of interest gives the angular scale of the whole problem. The SUn-Earth separation of 1 AU appears as 747 mas, which is not tiny at all by the standards of modern telescopes. The Earth-Moon distance, by contrast, shrinks to only 1.92 mas. The Sun itself has an angular diameter of 6.95 mas, the Earth of 0.064 mas and the Moon of 0.017 mas, so both planetary bodies are point sources for any conceivable instrument.

| Object | Size | Angle seen from Alpha Centauri |
|---|---|---|
| Sun-Earth distance | 1 AU | 747 mas |
| Earth-Moon distance (mean) | 384 400 km | 1.92 mas |
| Sun (diameter) | 1.39 x 10^6 km | 6.95 mas |
| Earth (diameter) | 12 742 km | 0.064 mas |
| Moon (diameter) | 3475 km | 0.017 mas |

Brightness is expressed in magnitudes, with

```
m1 - m2 = -2.5 * log10(F1 / F2)
m = M + 5 * log10(d / 10 pc)
```

Taking an absolute V maginitude M_V = 4.83 for the Sun. the Sun seen from Alpha Centauri has an apparent magnitude m_Sun = 0.46, about as bright as Alpha Centauri A itself appears to us. This is the glare against which the Earth must be detected.

## Angular resolution
The first requirement for seeing two objects as separate is that the telescope can tell them apart. Because of diffraction, a point source observed through a circular aperture of diameter D does not form a point in the image, but the Airy pattern

```
I(θ) / I0 = [ 2 * J1(x) / x ]^2        with   x = π * D * θ / λ
```

where J1 is the Bessel function of the first kind. The central peak is surrounded by faint rings, and the first dark dings falls at x = 3.8317. Two equally bright sources are conventionally considered resolved when the peak of one falls on the first zero of the other, which is the Rayleigh criterion

```
θ_R = 1.22 * λ / D
```

Applying it to three representative instruments shows that the Sun-Eath separation of 747 mas is comfortably within reach of all of them, whereas the Earth-Moon separation of 1.92 mas is not within reach of any.
| Instrument | λ | D | θ_R | Sun-Earth (747 mas) | Earth-Moon (1.92 mas) |
|---|---|---|---|---|---|
| HST | 550 nm | 2.4 m | 57.7 mas | resolved | not resolved |
| JWST | 2 μm | 6.5 m | 77.4 mas | resolved | not resolved |
| ELT | 1.6 μm | 39 m | 10.3 mas | resolved | not resolved |

To resolve the Earth-Moon pair with a single mirror, one would need 

```
D >= 1.22 * λ / (1.92 mas) ~ 72 m at 550 nm      (~ 210 m at 1.6 μm)
```

which exceeds the size of any telescope that exists or is under construction. AN interferometer improves on this: for two equally bright sources of separations observed with a baseline B, the fringe visibility is

```
V = abs( cos( π * B * s / λ ) )
```

which first vanishes at s = λ / (2*B). This is the conventional resolution of an interferometer, and it is the reason why long baselines are the natural route towards the Moon. It is important to stress, however, that resolution is only a necessary condition. The Sun-Earth pair is resolved with a wide margin, and yet the Earth cannot be seen, because the light of the Sun spills over it.

## Planet-star contrast and reflected light
A planet shines almost entirely by reflected starlight, and a simple model shows how little of it reaches the observer. Replace the planet with a flat Lambertian disc of radius r and unit albedo, facing both the star and the observer. At the orbital distance a it intercepts the flux F_a = L / (4π a^2) over an area π R^2 and it re-emits that energy isotropically with a radiance F_a / π. At a distance d the flux received from the disc is therefore F_a R^2 / d^2, while the direct flux from the star is L / (4π d^2). The ratio of the two is (R/a)^2, and it does not depend on d. A real planet is not accounted for by two corrections: the geometric albedo A_g, and a phase function Φ(α) normalised to Φ(0) = 1, where α is the phase angle, that is the angle-Sun-planet-observer. The contrast, defined as the ratio between planet flux and star flux is

```
c = F_planet / F_star = A_g * (R / a)^2 * Φ(α)

Φ_Lambert(α) = [ sin(α) + (π - α) * cos(α) ] / π
```

The Lambert phase function is a convenient idealisation, and the table below shows how quickly the reflected light drops as the planet moves away from the full phase. The real Earth does not follow it exactly: Robinson (2026) finds that it is sub-Lambertian at gibbous phases and super-Lambertian at crescent phases. The Lambert values should therefore be read as indicative.

| α | 0° | 30° | 42.6° | 60° | 90° | 120° | 150° |
|---|---|---|---|---|---|---|---|
| Φ_Lambert | 1.00 | 0.88 | 0.78 | 0.61 | 0.32 | 0.110 | 0.015 |

At full phase (Φ = 1), and with (R_Earth / a)^2 = 1.81 x 10^-9, the Earth has a contrast of 4.4 x 10^-10 for A_g = 0.242 and 6.7 x 10^-10 for A_g = 0.367. The Moon, with a smaller radius and a lower albedo, reaches only

```
c_Moon = 0.12 * (R_Moon / a)^2 = 1.6 x 10^-11
```

In plain terms, the Sun outshines the Earth by a factor between 1.5 and 2.3 billion, and the Moon by about 6x10^10. These are upper limits, because the Earth is never at full phase for the real Alpha Centauri.
Reflected light is not the only option. The Earth also emits its own thermal radiation, and in the infrared the contrast is considerably more fabourable. With a bond albedo A_B = 0.3 and a solar constant S = 1361 W/m^2, the equilibrium temperature is

```
T_eq = [ (1 - A_B) * S / (4 * σ) ]^(1/4) = 255 K
```

At 10 μm the ratio of the Planck functions of the Earth and of the Sun is (e^x_Sun - 1) / (e^x_Earth - 1), with x = 14388 / (λ[μm] * T[K]), so that

```
c(10 μm) ~ (R_Earth / R_Sun)^2 * (e^0.249 - 1) / (e^5.65 - 1)
         ~ 8.4 x 10^-5 * 1.0 x 10^-3
         ~ 8 x 10^-8
```

This is about two orders of magnitude better than in the visible. The price is a coarser resolution, which scales with λ, but even the ELT at 10 μm (64.5 mas) is far below the 747 mas of the Sun-Earth separation. The estimate uses T_eq as if it were a brightness tempreature; a real brightness temperatutre in an atmospheric window would change the result by a factor of order 2.

The last piece of the contrast problem is the light of the star itself, diffracted by the telescope. Far from the centre of the pattern, for x' = θ / (λ/D) >> 1, one can use the asymptotic form of the Bessel function, J1(x) ~ sqrt(2 / (π*x)) * cos(x - 3π/4), and average over the oscillations, which gives a smooth halo

```
< I / I0 > ~ 4 / ( π^4 * x'^3 )
```

Evaluated at the position of the Earth (747 mas) for an ideal circular aperture with no obstruction and no atmosphere, the halo is still bigger than the planet in every case considered.

| Telescope | x' at 747 mas | Halo | Halo / c_Earth |
|---|---|---|---|
| HST, 550 nm | 15.8 | 1.0 x 10^-5 | ~ 2 x 10^4 |
| ELT, 550 nm | 257 | 2.4 x 10^-9 | ~ 5 |
| ELT, 1.6 μm | 88 | 6.0 x 10^-8 | ~ 10^2 |

Even a perfect large telescope therefore needs a coronagraph, an instrument that suppresses the starlight before it reaches the detector. In real instruments the limit comes from speckles, obstructions and wavefront errors rather than from ideal diffracrion. To place the Earth in context, a review of adaprive optics for high-contrast imaging (arXiv:1701.00836) quotes performances of order 10^-5 at o.5" and below 10^-6 at a few resolution elements for ground-based systems, which I treat as an order of magnitude. The Roman Coronagraph Instrument has a 10^-7 flux-ratio detection limit (5σ, single band) at 575 nm and 6-9 λ/D for stars of V ~ 5. Imaging an Earth twin requires 10^-10 or better, which is the requirement of the HabEx study (arXiv:1809.09674), and the Habitable Worlds Observatory is expected to need a similar level.
