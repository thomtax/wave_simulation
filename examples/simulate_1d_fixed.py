from wave_simulation.parameters import Parameters1D
from wave_simulation.initialization import initialize_1d
from wave_simulation.stability import check_stability_1d
from wave_simulation.solver import solve_1d_fixed
from wave_simulation.visualization import animate_1d

def main():
    params = Parameters1D()
    x, t, u, dx, dt = initialize_1d(params)
    check_stability_1d(params.c, dt, dx)
    c_coeff = (params.c * dt / dx) ** 2
    u = solve_1d_fixed(u, params, c_coeff)
    animate_1d(x, t, u, title="1D Wave with Fixed Boundaries")

if __name__ == "__main__":
    main()