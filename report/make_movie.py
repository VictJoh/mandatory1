import sys

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, ".")
from Wave2D import Wave2D_Neumann

# made with help from claude

N = 40
sol = Wave2D_Neumann()
data = sol(N, 80, cfl=1 / np.sqrt(2), mx=2, my=2, store_data=2)
xij, yij = sol.create_mesh(N)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(5, 4), dpi=80)
ax.set_zlim(-1.05, 1.05)
frames = []
for n, val in data.items():
    surf = ax.plot_surface(xij, yij, val, cmap="coolwarm", vmin=-1, vmax=1, linewidth=0)
    frames.append([surf])

ani = animation.ArtistAnimation(fig, frames, interval=100, blit=True)
ani.save("report/neumannwave.gif", writer="pillow", fps=10)
