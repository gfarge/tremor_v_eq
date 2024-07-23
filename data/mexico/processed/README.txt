Tremor pre-processing
=====================
- Original catalog: World Tremor Database (Idehara et al, 2014,
  doi:10.1186/1880-5981-66-66) catalog for Jalisco-colima. From January 2006 to
  June 2007.
- Projection along-strike, defined as a polynomial fit of order 2 of the
  tremor locations.
- Trimming sources far from strike (avoid locations that count earthquakes
  too far). Maximum across-strike distance of 30 km.

Earthquake pre-processing
=========================
- Original catalog: Mexico SSN catalog, from January 2000 to April 2024. In lon/lat
  box [-107, -101, 17, 21].
- The catalog has an evolving, relatively high Mc~3.5-4.

Earthquake counting
===================
- For each tremor event, count earthquakes of magnitudes larger than M3.7, at
  [10, 20, 30, 50, 100] km from the tremor detection.
- Record which earthquakes are thus counted.
- Using the measured b-value (~1.2) for the catalog (as cut previously
