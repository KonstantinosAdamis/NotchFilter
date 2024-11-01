import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Constants
R = 8e-3  # Resistance term in denominator
L = 90.3e-12  # Capacitance term in denominator
numerator_gain = 16e-6  # Gain in numerator

# Frequency to notch (in Hz)
f_notch = 0  # Notching out 0 Hz
omega_0 = 2 * np.pi * f_notch  # Angular frequency for notch

# Define the transfer function components
numerator = [1, 0, omega_0**2]  # s^2 + ω₀^2
denominator = [R * L, R, 0]  # (R*L)s + R

# Construct transfer function
system = signal.TransferFunction(numerator, denominator)

# Frequency response
w, mag, phase = signal.bode(system)

# Plot magnitude response
plt.figure(figsize=(10, 6))
plt.semilogx(w / (2 * np.pi), mag)  # Convert rad/s to Hz for x-axis
plt.title("Notch Filter Magnitude Response")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")
plt.grid()
plt.show()

