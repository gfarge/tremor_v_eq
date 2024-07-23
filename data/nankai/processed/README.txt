Tremor pre-processing
=====================
- Original catalog: World Tremor Database (Idehara et al, 2014,
  doi:10.1186/1880-5981-66-66) catalog for Nankai. "Clustered" version,
  selecting only events having a neighbor at least within a space-time window
  defined by epicentral distance of 10 km and time difference of 1 hour. From
  Apr 2004 to Apr 2013.
- Projection along-strike, defined as a polynomial fit of order 10 of the
  tremor locations.
- Trimming sources far from strike (avoid mislocations that count earthquakes
  too far). Maximum across-strike distance of 50 km. Maximum along-strike
  distance of 800 (remove fuzzy sources in Tokai).

Earthquake pre-processing
=========================
- Original catalog: JMA catalog, from January 2004 to April 2013. In lon/lat
  box [130, 140, 31, 37], to limit computation times.

Earthquake counting
===================
- For each tremor event, count earthquakes of magnitudes larger than [1., 1.5, 1.8, 2.0] at [10, 20,
  30, 50, 100] km from the tremor detection.
- Record which earthquakes are thus counted.
