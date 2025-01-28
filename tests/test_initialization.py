import unittest
import numpy as np
from wave_simulation import Parameters1D, Parameters2D, initialize_1d, initialize_1d_free, initialize_2d

class TestInitialization(unittest.TestCase):
    def test_initialize_1d_shape(self):
        params = Parameters1D()
        x, t, u, dx, dt = initialize_1d(params)
        self.assertEqual(u.shape, (params.Nt, params.Nx))

    def test_initialize_1d_free_shape(self):
        params = Parameters1D()
        x, t, u, dx, dt = initialize_1d_free(params)
        self.assertEqual(u.shape, (params.Nt, params.Nx))

    def test_initialize_2d_shape(self):
        params = Parameters2D()
        X, Y, t, u, dx, dy, dt = initialize_2d(params)
        self.assertEqual(u.shape, (params.Nt, params.Nx, params.Ny))

    def test_initialize_1d_initial_conditions(self):
        params = Parameters1D()
        x, t, u, dx, dt = initialize_1d(params)
        # Verifica che la prima riga di u corrisponda alla somma di due gaussiane
        expected = (
            np.exp(-((x - params.L / 3) ** 2) / (2 * params.sigma ** 2)) +
            np.exp(-((x - 2 * params.L / 3) ** 2) / (2 * params.sigma ** 2))
        )
        np.testing.assert_array_almost_equal(u[0, :], expected)
        # Verifica che la seconda riga sia identica alla prima (zero velocità iniziale)
        np.testing.assert_array_almost_equal(u[1, :], u[0, :])

    def test_initialize_2d_initial_conditions(self):
        params = Parameters2D()
        X, Y, t, u, dx, dy, dt = initialize_2d(params)
        # Verifica che la prima griglia di u sia una perturbazione gaussiana al centro
        sigma = params.sigma
        expected = np.exp(-((X - params.Lx / 2) ** 2 + (Y - params.Ly / 2) ** 2) / (2 * sigma ** 2))
        np.testing.assert_array_almost_equal(u[0, :, :], expected)
        # Verifica che la seconda griglia sia identica alla prima (zero velocità iniziale)
        np.testing.assert_array_almost_equal(u[1, :, :], u[0, :, :])

if __name__ == '__main__':
    unittest.main()