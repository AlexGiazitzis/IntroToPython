import numpy as np
from matplotlib import pyplot as plt


def mytrf(R, C):
    tc = R * C
    fc = 1 / tc
    f = np.hstack((np.linspace(0, 0.8 * fc, 100), np.linspace(0.81 * fc, 1.10 * fc, 200), np.linspace(1.11 * fc, 100 * fc, 100)))
    tr_f = 1 / (1 + 1j * 2 * np.pi * R * C * f)
    magn = np.abs(tr_f)
    db = 20 * np.log10(magn)
    phase_deg = 180 * np.angle(tr_f) / np.pi  # can be substituted by np.angle(tr_f, deg=True)
    plt.subplot(2, 1, 1)
    plt.semilogx(f, db)
    plt.xlabel("Frequency - Hz")
    plt.ylabel("dB")
    plt.grid(True)
    plt.grid(True, which="minor")
    plt.subplot(2, 1, 2)
    plt.semilogx(f, phase_deg)
    plt.xlabel("Frequency - Hz")
    plt.ylabel("Angle - Degrees")
    plt.grid(True)
    plt.grid(True, which="minor")
    return tr_f, db, phase_deg

# The __name__ variable is a dunder (double underline) variable of Python,
# it exists in all scripts and takes a value based from where the file was called.
# If the file was called from the command line, it would mean that it is run directly,
# as the main program. Hence this if is only executed when it is run as the main program
# and not just from being imported in another file.
if __name__ == "__main__":
    #from matplotlib import pyplot as plt  # unneeded since it's imported above

    #from mytrf import mytrf  # no need to import it in itself

    R = 1000
    C = 1e-6
    tr_f, db, phase_deg = mytrf(R, C)

    R = 2000
    C = 1e-6
    tr_f1, db1, phase_deg1 = mytrf(R, C)
    plt.show()