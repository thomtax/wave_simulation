import numpy as np
from wave_simulation.parameters import Parameters1D, Parameters2D
from wave_simulation.boundary_conditions import fixed_boundary, free_boundary
import sys

def solve_1d_fixed(u: np.ndarray, params: Parameters1D, c_coeff: float):
    for n in range(1, params.Nt - 1):
        u[n + 1, 1:-1] = (
            2 * u[n, 1:-1] - u[n - 1, 1:-1] +
            c_coeff * (u[n, 2:] - 2 * u[n, 1:-1] + u[n, :-2])
        )
        # Apply fixed boundary conditions
        u[n + 1, :] = fixed_boundary(u[n + 1, :])

        if n % 50 == 0:
            print(f"1D Fixed Boundary: Simulation at time step {n}/{params.Nt}")

    return u

def solve_1d_free(u: np.ndarray, params: Parameters1D, c_coeff: float):
    for n in range(1, params.Nt - 1):
        u[n + 1, 1:-1] = (
            2 * u[n, 1:-1] - u[n - 1, 1:-1] +
            c_coeff * (u[n, 2:] - 2 * u[n, 1:-1] + u[n, :-2])
        )
        # Apply free boundary conditions
        u = free_boundary(u, n)

        if n % 50 == 0:
            print(f"1D Free Boundary: Simulation at time step {n}/{params.Nt}")

    return u

def solve_2d_fixed(u: np.ndarray, params: Parameters2D, c_coeff: float):
    for n in range(1, params.Nt - 1):
        u[n + 1, 1:-1, 1:-1] = (
            2 * u[n, 1:-1, 1:-1] - u[n - 1, 1:-1, 1:-1] +
            c_coeff * (
                u[n, 2:, 1:-1] + u[n, :-2, 1:-1] +
                u[n, 1:-1, 2:] + u[n, 1:-1, :-2] -
                4 * u[n, 1:-1, 1:-1]
            )
        )
        # Apply fixed boundary conditions (u=0 at edges)
        u[n + 1, 0, :] = 0
        u[n + 1, -1, :] = 0
        u[n + 1, :, 0] = 0
        u[n + 1, :, -1] = 0

        if n % 50 == 0:
            print(f"2D Fixed Boundary: Simulation at time step {n}/{params.Nt}")

    return u