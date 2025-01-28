import numpy as np

def fixed_boundary(u_frame):
    """Apply fixed boundary conditions (u=0 at edges)."""
    u_frame[0] = 0
    u_frame[-1] = 0
    return u_frame

def free_boundary(u, n):
    """Apply free boundary conditions (zero spatial derivative at edges)."""
    u[n + 1, 0] = u[n + 1, 1]
    u[n + 1, -1] = u[n + 1, -2]
    return u