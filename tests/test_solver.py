import unittest
import numpy as np
from wave_simulation import (
    Parameters1D,
    Parameters2D,
    initialize_1d,
    initialize_1d_free,
    initialize_2d,
    check_stability_1d,
    check_stability_2d,
    solve_1d_fixed,
    solve_1d_free,
    solve_2d_fixed
)

class TestSolver(unittest.TestCase):
    def test_solve_1d_fixed_no_error(self):
        params = Parameters1D()
        x, t, u, dx, dt = initialize_1d(params)
        check_stability_1d(params.c, dt, dx)
        c_coeff = (params.c * dt / dx) ** 2
        u = solve_1d_fixed(u, params, c_coeff)
        # Verifica che le estremità siano sempre zero
        self.assertTrue(np.all(u[:, 0] == 0))
        self.assertTrue(np.all(u[:, -1] == 0))

    def test_solve_1d_free_no_error(self):
        params = Parameters1D()
        x, t, u, dx, dt = initialize_1d_free(params)
        check_stability_1d(params.c, dt, dx)
        c_coeff = (params.c * dt / dx) ** 2
        u = solve_1d_free(u, params, c_coeff)
        # Verifica che le estremità abbiano derivate spaziali zero
        np.testing.assert_array_almost_equal(u[:, 0], u[:, 1])
        np.testing.assert_array_almost_equal(u[:, -1], u[:, -2])

    def test_solve_2d_fixed_no_error(self):
        params = Parameters2D()
        X, Y, t, u, dx, dy, dt = initialize_2d(params)
        check_stability_2d(params.c, dt, dx, dy)
        c_coeff = (params.c * dt / dx) ** 2
        u = solve_2d_fixed(u, params, c_coeff)
        # Verifica che i bordi siano sempre zero
        self.assertTrue(np.all(u[:, 0, :] == 0))
        self.assertTrue(np.all(u[:, -1, :] == 0))
        self.assertTrue(np.all(u[:, :, 0] == 0))
        self.assertTrue(np.all(u[:, :, -1] == 0))

    def test_solve_1d_fixed_evolution(self):
        # Configurazione con Nt=3 e Nx=5
        params = Parameters1D(Nt=3, Nx=5, L=0.08, T_total=0.02, sigma=0.01)
        x, t, u, dx, dt = initialize_1d(params)
        check_stability_1d(params.c, dt, dx)
        c_coeff = (params.c * dt / dx) ** 2
        u = solve_1d_fixed(u, params, c_coeff)
        # Calcolare l'output atteso manualmente
        expected = np.zeros((3,5))
        expected[0, :] = u[0, :]
        expected[1, :] = u[1, :]
        expected[2, 1:-1] = 2*u[1, 1:-1] - u[0, 1:-1] + c_coeff*(u[1, 2:] - 2*u[1, 1:-1] + u[1, :-2])
        # Estremità fisse a zero
        expected[2, 0] = 0
        expected[2, -1] = 0
        # Verificare che il risultato del solver corrisponda all'atteso
        np.testing.assert_array_almost_equal(u, expected)

    def test_solve_1d_free_evolution(self):
        # Configurazione con Nt=3 e Nx=5 per condizioni al contorno libere
        params = Parameters1D(Nt=3, Nx=5, L=0.08, T_total=0.02, sigma=0.01)
        x, t, u, dx, dt = initialize_1d_free(params)
        check_stability_1d(params.c, dt, dx)
        c_coeff = (params.c * dt / dx) ** 2
        u = solve_1d_free(u, params, c_coeff)
        # Calcolare l'output atteso manualmente con condizioni libere
        expected = np.zeros((3,5))
        expected[0, :] = u[0, :]
        expected[1, :] = u[1, :]
        expected[2, 1:-1] = (
                2 * u[1, 1:-1]
                - u[0, 1:-1]
                + c_coeff * (u[1, 2:] - 2 * u[1, 1:-1] + u[1, :-2])
        )

        # Estremità libere: u[n+1,0] = u[n+1,1] e u[n+1,-1] = u[n+1,-2]
        expected[2, 0] = expected[2, 1]
        expected[2, -1] = expected[2, -2]
        # Verificare che il risultato del solver corrisponda all'atteso
        np.testing.assert_array_almost_equal(u, expected)

if __name__ == '__main__':
    unittest.main()