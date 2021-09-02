import matplotlib.pyplot as plot
import numpy as np
from scipy import signal

# Rata de eșantionare 1000 hz / secundă

t = np.linspace(0, 1, 1000, endpoint=True)

# Trage semnalul undei pătrate

plot.plot(t, signal.square(2 * np.pi * 5 * t))

# Scriem titlu pentru graficul undei pătrate

plot.title('Unda pătrată')

# eticheta axei x pentru graficul undei pătrate

plot.xlabel('Time')

# eticheta axei y pentru graficul undei pătrate

plot.ylabel('Amplitude')

plot.grid(True, which='both')

# Furnizarea axei x și culoarea liniei

plot.axhline(y=0, color='k')

# Setarea valorilor  max și min pentru axa y

plot.ylim(-2, 2)
plot.savefig('static/Img/Img_Teoria/dc_wave.png')
# Afișarea undei pătrate desenată

plot.show()
