import numpy as np
from wave_simulation.parameters import Parameters1D, Parameters2D

def initialize_1d(params: Parameters1D):
    x, dx = params.spatial_grid()
    t, dt = params.temporal_grid()

    u = np.zeros((params.Nt, params.Nx))
    # Initial condition: two Gaussian pulses
    u[0, :] = (
        np.exp(-((x - params.L / 3) ** 2) / (2 * params.sigma ** 2)) +
        np.exp(-((x - 2 * params.L / 3) ** 2) / (2 * params.sigma ** 2))
    )
    u[1, :] = u[0, :]  # Zero initial velocity

    return x, t, u, dx, dt

def initialize_1d_free(params: Parameters1D):
    x, dx = params.spatial_grid()
    t, dt = params.temporal_grid()

    u = np.zeros((params.Nt, params.Nx))
    # Initial condition: single Gaussian pulse at center
    u[0, :] = np.exp(-((x - params.L / 2) ** 2) / (2 * params.sigma ** 2))
    u[1, :] = u[0, :]  # Zero initial velocity

    return x, t, u, dx, dt

def initialize_2d(params: Parameters2D):
    X, Y, dx, dy = params.spatial_grid()
    t, dt = params.temporal_grid()

    u = np.zeros((params.Nt, params.Nx, params.Ny))
    # Initial condition: Gaussian perturbation at the center
    sigma = params.sigma
    u0 = np.exp(-((X - params.Lx / 2) ** 2 + (Y - params.Ly / 2) ** 2) / (2 * sigma ** 2))
    u[0, :, :] = u0
    u[1, :, :] = u0  # Zero initial velocity

    return X, Y, t, u, dx, dy, dt