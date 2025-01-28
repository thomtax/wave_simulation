def check_stability_1d(c: float, dt: float, dx: float) -> float:
    S = c * dt / dx
    print(f"Stability condition for 1D: S = {S:.3f}")
    if S > 1:
        raise ValueError(f"Stability condition not met: S = {S:.3f} > 1")
    return S

def check_stability_2d(c: float, dt: float, dx: float, dy: float) -> float:
    Sx = c * dt / dx
    Sy = c * dt / dy
    print(f"Stability condition for 2D: Sx = {Sx:.3f}, Sy = {Sy:.3f}")
    if (Sx**2 + Sy**2) > 1:
        raise ValueError("Stability condition not met: Sx^2 + Sy^2 > 1")
    return Sx, Sy