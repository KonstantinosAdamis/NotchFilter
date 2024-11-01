import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the transfer function (e.g., H(s) = R**2 / (2*R + s*L))
numerator = [16e-6]      # Numerator coefficients
denominator = [90.3e-12, 8e-3] # Denominator coefficients
system = signal.TransferFunction(numerator, denominator)

# Frequency response
w, h = signal.freqresp(system)

# DC gain (value at zero frequency)
dc_gain = h[0]

# New transfer function without the DC component
new_numerator = np.array(numerator) / dc_gain
new_denominator = denominator
new_system = signal.TransferFunction(new_numerator, new_denominator)

# Print the original and new transfer functions
print("Original Transfer Function:", system)
print("New Transfer Function (DC removed):", new_system)

# Plot the frequency response
plt.figure()
plt.subplot(2, 1, 1)
plt.title('Original and DC-Removed Transfer Function Frequency Responses')
plt.semilogx(w, 20 * np.log10(abs(h)), label='Original')
plt.semilogx(w, 20 * np.log10(abs(signal.freqresp(new_system)[1])), label='DC-Removed', linestyle='--')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.semilogx(w, np.angle(h), label='Original')
plt.semilogx(w, np.angle(signal.freqresp(new_system)[1]), label='DC-Removed', linestyle='--')
plt.ylabel('Phase (radians)')
plt.xlabel('Frequency (rad/s)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
