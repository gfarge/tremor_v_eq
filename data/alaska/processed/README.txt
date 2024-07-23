Tremor pre-processing
=====================
- Original catalog: Wech (2016, https://doi.org/10.1130/G37817.1).
- Define depth of events as the depth of the slab interface at the horizontal
  location of the events, using Slab2.0 (better location compared to
  earthquakes).
- Projection along-strike, defined as a polynomial fit of order 2 of the
  tremor locations.
- Trim tremor to January 2013 to October 2015

Earthquake pre-processing
=========================
- Original catalog: ComCat catalog, from January 2013 to January 2016. In lon/lat
  box [-156, -142, 58.5, 65.5].

Earthquake counting
===================
- Limit earthquake catalog to from January 2013 to October 2015
- For each tremor event, count earthquakes of magnitudes larger than [1., 1.5, 1.8, 2.0] at [10, 20,
  30, 50, 100] km from the tremor detection.
- Record which earthquakes are thus counted.
