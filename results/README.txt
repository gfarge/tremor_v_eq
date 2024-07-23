Results files
=============
- Read the .pkl files using the python `pickle` package.

- Filenames are made of:
  [region_name]_synch_mc[min_mag_of_counted_eq]_dx[spatial_binning]_cc[correlation_threshold].pkl

- Each files contains a dictionnary of results:
	-- 'corr_length': Tremor correlation distance (in km) in each spatial
	bin along-strike.
	-- 'n_close_eq': Number (rate) of earthquakes per year in "close" vicinity to
	the tremor zone in the spatial bin, ie average number of earthquakes
	that are closer than the chosen distance  to tremor sources in the
	spatial bin. Each key of this dictionnary is the chosen distance in km
	used to count earthquakes, each array is the same size as the
	correlation distance array.
	-- 'dists': Distances (in km) used to count earthquakes around
	tremor sources.
	-- 'cc_thr': Modified cross-correlation threshold used to compute the
	correlation distance.
	-- 'dx': along-strike bin sizes in km.
	-- 'dt': temporal binning (in days) used to compute the spatially-binned counts
	that are then cross correlated.
