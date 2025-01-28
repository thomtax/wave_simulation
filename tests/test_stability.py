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
            check_stability_2d(c=0.25, dt=0.06, dx=0.02, dy=0.02)

    def test_stability_2d_edge_case(self):
        # Caso limite dove Sx^2 + Sy^2 = 1
        c = 0.25
        dx = 0.02
        dy = 0.02
        S = 1 / (2 ** 0.5)
        dt = S * dx / c  # dt = Sx * dx / c
        # Verifichiamo che Sx^2 + Sy^2 = 1 non sollevi un errore
        try:
            Sx, Sy = check_stability_2d(c=c, dt=dt, dx=dx, dy=dy)
            self.assertAlmostEqual(Sx**2 + Sy**2, 1.0)
        except ValueError:
            self.fail("check_stability_2d ha sollevato ValueError quando Sx^2 + Sy^2 = 1")

if __name__ == '__main__':
    unittest.main()