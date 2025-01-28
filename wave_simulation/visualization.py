import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from wave_simulation.parameters import Parameters1D, Parameters2D

def animate_1d(x, t, u, title="1D Wave Simulation"):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, T_grid = np.meshgrid(x, t)

    def update(frame):
        ax.clear()
        ax.plot_surface(
            X[:frame + 1, :],
            T_grid[:frame + 1, :],
            u[:frame + 1, :],
            cmap='viridis',
            edgecolor='none'
        )
        ax.set_xlabel('Position (m)')
        ax.set_ylabel('Time (s)')
        ax.set_zlabel('Amplitude')
        ax.set_title(title)
        ax.view_init(elev=30, azim=45)

    anim = animation.FuncAnimation(fig, update, frames=len(t), interval=30, repeat=False)
    plt.show()

def animate_2d_membrane(X, Y, t, u, title="2D Membrane Simulation"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    def update(frame):
        ax.clear()
        ax.plot_surface(
            X, Y, u[frame, :, :],
            cmap='viridis',
            edgecolor='none'
        )
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('Amplitude')
        ax.set_title(f"{title} - Time = {t[frame]:.2f} s")
        ax.view_init(elev=30, azim=45)
        ax.set_zlim(-1, 1)

    anim = animation.FuncAnimation(fig, update, frames=range(0, len(t), 5), interval=50, repeat=False)
    plt.show()

def animate_2d_surface(t, X, Y, u, title="2D Surface Wave Simulation"):
    fig, ax = plt.subplots(figsize=(8, 6))
    cax = ax.imshow(u[0, :, :], extent=[X.min(), X.max(), Y.min(), Y.max()],
                    cmap='viridis', origin='lower', vmin=-1, vmax=1)
    fig.colorbar(cax)
    ax.set_title(title)
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')

    def animate(frame):
        cax.set_data(u[frame, :, :])
        ax.set_title(f"{title} - Time = {t[frame]:.2f} s")
        return cax,

    anim = animation.FuncAnimation(fig, animate, frames=len(t), interval=30, blit=True)
    plt.show()