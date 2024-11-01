import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define transfer function parameters
omega_c = 8.86e7  # Cutoff frequency in rad/s

# Define the transfer function H(s) = s^2 / (s^2 + omega_c * s)
numerator = [1, 0, 0]  # Coefficients for s^2
denominator = [1, omega_c, 0]  # Coefficients for s^2 + omega_c * s

# Construct the transfer function
system = signal.TransferFunction(numerator, denominator)

# Define frequency range for the analysis
frequencies = np.logspace(0, 8, 1000)  # Frequency range from 1 Hz to 100 MHz
w = 2 * np.pi * frequencies  # Convert frequency to rad/s

# Calculate frequency response
w, mag, phase = signal.bode(system, w=w)

# Create a figure with two subplots: one for magnitude and one for phase
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot the magnitude response
ax1.semilogx(frequencies, mag, color='b', label='Magnitude (dB)')  # Magnitude in dB
ax1.set_title("Frequency Response of the Transfer Function")
ax1.set_xlabel("Frequency [Hz]")
ax1.set_ylabel("Magnitude [dB]", color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid()

# Create a second y-axis for the phase response
ax2 = ax1.twinx()  
ax2.semilogx(frequencies, phase, color='r', label='Phase (degrees)')  # Phase in degrees
ax2.set_ylabel("Phase [degrees]", color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Optional: Add legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
