import numpy as np
from matplotlib import pyplot as plt
import sounddevice as sd

Fs = 8000
dt = 0.25
n = np.arange(0, int(Fs * dt))

l1 = np.cos(2 * np.pi * 697 / Fs * n)
l2 = np.cos(2 * np.pi * 770 / Fs * n)
l3 = np.cos(2 * np.pi * 852 / Fs * n)
l4 = np.cos(2 * np.pi * 941 / Fs * n)

h1 = np.cos(2 * np.pi * 1209 / Fs * n)
h2 = np.cos(2 * np.pi * 1336 / Fs * n)
h3 = np.cos(2 * np.pi * 1477 / Fs * n)
h4 = np.cos(2 * np.pi * 1633 / Fs * n)

npause = int(Fs * (dt / 2))
p = np.zeros(npause)

sd.play(np.hstack((l1, p, l2, p, l3, p, l4, p, h1, p, h2, p, h3, p, h4, p)), Fs)
sd.wait()  # Required so that the interpreter pauses whilst playing

dtmf1 = l1 + h1
dtmf2 = l1 + h2
dtmf3 = l1 + h3
dtmf4 = l2 + h1
dtmf5 = l2 + h2
dtmf6 = l2 + h3
dtmf7 = l3 + h1
dtmf8 = l3 + h2
dtmf9 = l3 + h3
dtmf_star = l4 + h1
dtmf0 = l4 + h2
dtmf_hashtag = l4 + h3

dtmf = np.hstack((dtmf1, p, dtmf2, p, dtmf3, p, dtmf4, p, dtmf5, p, dtmf6, p, dtmf7, p, dtmf8, p, dtmf9, p, dtmf_star, p, dtmf0, p, dtmf_hashtag))
sd.play(dtmf , Fs)
sd.wait()

plt.plot(dtmf)
plt.show()
