from wave_simulation.parameters import Parameters2D
from wave_simulation.initialization import initialize_2d
from wave_simulation.stability import check_stability_2d
from wave_simulation.solver import solve_2d_fixed
from wave_simulation.visualization import animate_2d_membrane

def main():
    params = Parameters2D()
    X, Y, t, u, dx, dy, dt = initialize_2d(params)
    check_stability_2d(params.c, dt, dx, dy)
    c_coeff = (params.c * dt / dx) ** 2
    u = solve_2d_fixed(u, params, c_coeff)
    animate_2d_membrane(X, Y, t, u, title="2D Membrane Vibration")

if __name__ == "__main__":
    main()