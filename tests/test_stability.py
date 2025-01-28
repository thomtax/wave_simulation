import unittest
from wave_simulation import check_stability_1d, check_stability_2d

class TestStability(unittest.TestCase):
    def test_stability_1d_met(self):
        # Caso in cui la condizione di stabilità è soddisfatta
        S = check_stability_1d(c=0.25, dt=0.01, dx=0.02)
        self.assertAlmostEqual(S, 0.125)

    def test_stability_1d_fail(self):
        # Caso in cui la condizione di stabilità NON è soddisfatta
        with self.assertRaises(ValueError):
            check_stability_1d(c=0.25, dt=0.05, dx=0.01)

    def test_stability_2d_met(self):
        # Caso in cui la condizione di stabilità 2D è soddisfatta
        Sx, Sy = check_stability_2d(c=0.25, dt=0.01, dx=0.02, dy=0.02)
        self.assertAlmostEqual(Sx, 0.125)
        self.assertAlmostEqual(Sy, 0.125)

    def test_stability_2d_fail(self):
        # Caso in cui la condizione di stabilità 2D NON è soddisfatta
        with self.assertRaises(ValueError):
            check_stability_2d(c=0.25, dt=0.05, dx=0.02, dy=0.02)

    def test_stability_2d_edge_case(self):
        # Caso limite dove Sx^2 + Sy^2 = 1
        Sx = 0.70710678
        Sy = 0.70710678
        # Impostiamo dt in modo tale che c * dt / dx = Sx
        c = 0.25
        dx = c * 0.70710678 / 0.70710678  # risulta dx = c * dt / Sx
        dt = Sx * dx / c
        # Sx^2 + Sy^2 = 1
        with self.assertRaises(ValueError):
            check_stability_2d(c=c, dt=dt, dx=dx, dy=dx)  # Supera il limite

if __name__ == '__main__':
    unittest.main()