from dataclasses import dataclass
import numpy as np

@dataclass
class Parameters1D:
    L: float = 1.0           # Length of the string (meters)
    T_total: float = 6.0     # Total simulation time (seconds)
    c: float = 0.25          # Wave propagation speed (m/s)
    sigma: float = 0.04      # Standard deviation for Gaussian pulse (meters)
    Nx: int = 250            # Number of spatial points
    Nt: int = 600            # Number of time points

    def spatial_grid(self):
        x = np.linspace(0, self.L, self.Nx)
        dx = x[1] - x[0]
        return x, dx

    def temporal_grid(self):
        t = np.linspace(0, self.T_total, self.Nt)
        dt = t[1] - t[0]
        return t, dt

@dataclass
class Parameters2D:
    Lx: float = 1.0          # Length along x (meters)
    Ly: float = 1.0          # Length along y (meters)
    T_total: float = 5.0     # Total simulation time (seconds)
    c: float = 0.25           # Wave propagation speed (m/s)
    sigma: float = 0.05       # Standard deviation for Gaussian perturbation (meters)
    Nx: int = 101             # Number of spatial points along x
    Ny: int = 101             # Number of spatial points along y
    Nt: int = 500             # Number of time points

    def spatial_grid(self):
        x = np.linspace(0, self.Lx, self.Nx)
        y = np.linspace(0, self.Ly, self.Ny)
        dx = x[1] - x[0]
        dy = y[1] - y[0]
        X, Y = np.meshgrid(x, y, indexing='ij')
        return X, Y, dx, dy

    def temporal_grid(self):
        t = np.linspace(0, self.T_total, self.Nt)
        dt = t[1] - t[0]
        return t, dt