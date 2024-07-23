Tremor pre-processing
=====================
- Original catalog: PNSN catalog, from August 2009 to June 2024.
- Depth modeled with slab from Bostock et al (2019,
  https://doi.org/10.1016/j.lithos.2019.02.019), vertical projection onto slab.
- Projection along-strike, defined as a polynomial fit of order 4.
- Trimming sources far from strike (avoid mislocations that count earthquakes
  too far). Maximum across-strike distance of 100 km.
- Trim times from August 2009 to June 2024

Earthquake pre-processing
=========================
- Original catalog: ComCat catalog, from August 2009 to June 2024.
- Cut catalog to same period as tremor.

Earthquake counting
===================
- For each tremor event, count earthquakes of magnitudes larger than [1., 1.5, 1.8, 2.0] at [10, 20,
  30, 50, 100] km from the tremor detection.
- Record which earthquakes are thus counted.
