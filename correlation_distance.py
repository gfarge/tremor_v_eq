"""
Functions to compute the correlation distance for a given point process defined in time and 1D space.
"""

import numpy as np

#--------------------------------------------------------------------------------

def correlation_matrix(ev_t, ev_x, dt, dx_bin, x_min, x_max):
    """Computes the correlation matrix of a point process in time and space.

    Args:
        ev_t (1D array): Event times (dimension `N`).
        ev_x (1D array): Event locations (dimension `N`).
        dt (float): Duration of time bin to count events (same unit as `ev_t`).
        dx_bin (_type_): Size of spatial bin to count events (same unit as `ev_x`). A time series of activity is computed for each spatial bin, and then the cross-correlation is computed between each pair of time series.
        x_min (_type_): Minimum value of `x` to consider.
        x_max (_type_): Maximum value of `x` to consider.

    Returns:
        cc_matrix: Cross-correlation matrix
    """


#--------------------------------------------------------------------------------

def cross_corr(sig1, sig2, dt, norm=True, no_bias=True):
    """Homemade cross-correlation function.

    Computes the cross-correlation time-series of two signals. Function was
    designed for signals of same length. If signals of different sizes are
    used, correlation lag might be strange, use at your own risk.

    Parameters
    ----------
    sig1, sig2 : 1D arrays
        Signals to cross-correlate, dimensions N and M. Use same discretization
        lenght `dt` for best results.
    dt : float
        Time step used in both signals.
    norm : bool, optional
        By default, normalizes the signals before cross-correlating them. `norm
        = False` turns it off.
    no_bias : bool, optional
        By default, removes the bias due to the variable number of points used
        to compute the correlation at each lag. This option also removes one
        fifth of the cross-correlation at each end, to get rid of edge effects
        due to unbiasing.

    Returns
    -------
    corr : 1D array
        Cross-correlation of the input signals, dimension N + M - 1.
    lag : 1D array
        Time lag for each value of the cross-correlation, dimension N + M - 1.
        Centering around 0 is only ensured if sig1 and sig2 are the same size.
    """

    # >> Normalize signals
    if norm:
        sig1 = (sig1 - np.mean(sig1)) / (np.std(sig1)*len(sig1))
        sig2 = (sig2 - np.mean(sig2)) / np.std(sig2)

    # >> Compute correlation
    corr = np.correlate(sig1.astype(float), sig2.astype(float), 'full')

    # >> Normalize
    if norm:
        corr = corr.astype(float) / (np.linalg.norm(sig1)*np.linalg.norm(sig2))

    # >> Remove bias due to number of points varying at each lag
    if no_bias:
        bias = cross_corr_bias(sig1, sig2)
        corr = corr/bias

    # >> Compute time lag of autocorrelation
    lag = np.arange(0, len(sig1) + len(sig2) - 1) - (len(sig1) - 1)
    lag = lag.astype(float) * dt

    # >> Removes both ends of lag and correlation, to get rid of edge effects
    # due to removing the bias
    if no_bias:
        valid = (abs(lag) < 4/5*max(lag))
        lag = lag[valid]
        corr = corr[valid]

    return corr, lag

#--------------------------------------------------------------------------------

def cross_corr_bias(sig1, sig2):
    """Computes the bias of at each lag of the cross correlation.

    Parameters
    ----------
    sig1, sig2 : 1D array
        Signals to correlate, dimension N and M.

    Returns
    -------
    bias : 1D array
        The bias vector, corresponding to all values of lag (both negative and
        positive), dimension N + M - 1.

    """
    N = len(sig1)
    M = len(sig2)

    # >> Bias for part where signals overlap entirely
    bias_full = [1 for ii in range(max(M, N) - min(M, N) + 1)]

    # >> Bias for part before full overlap
    bias_bef = [ii/min(N, M) for ii in range(1, min(M, N))]

    # >> Bias for part after full overlap
    bias_aft = [ii/min(N, M) for ii in range(min(M, N) - 1, 0, -1)]

    # >> Concatenate
    bias = np.concatenate((bias_bef, bias_full, bias_aft))

    return bias

#------------------------------------------------------------------------------