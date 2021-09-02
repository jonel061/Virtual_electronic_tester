import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')


fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-3, 3))
linie, = ax.plot([], [], lw=3)

def init():
    linie.set_data([], [])
    return linie,
def animacie(i):
    x = np.linspace(-1, 5, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    linie.set_data(x, y)
    return linie,

anim = FuncAnimation(fig, animacie, init_func=init,
                               frames=200, interval=20, blit=True)


anim.save('sinus_wave.gif', writer='Jonel')