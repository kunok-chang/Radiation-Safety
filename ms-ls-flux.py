import numpy as np

def f(z, x):
	return 1 / (x**2 + z**2)

def monte_carlo_flux_infinite_line(S_L, distance, length=1000, num_samples=1000000):
    """
    Calculate photon flux from an infinite line source using Monte Carlo simulation.

    Parameters:
    - S_L (float): Photon emission rate per unit length (#/hour/m).
    - distance (float): Distance from the line source (m).
    - length (float): Length of the line for simulation approximation (m).
    - num_samples (int): Number of Monte Carlo samples.

    Returns:
    - Photon flux at the given distance (#/hour/m²).
    """
    # Approximate the infinite line with a finite segment of `length`
    line_half_length = length / 2
    
    # Randomly sample photon emission points along the line source
    z_positions = np.random.uniform(-line_half_length, line_half_length, num_samples)
    
    # Integrate using Monte Carlo Method
    function_values = f(z_positions, x)
    
    # Calculate photon flux
    flux = S_L * (length / num_samples) * np.sum(function_values) / (4*np.pi)
    return flux

# Parameters
S_L = 1e6  # Photon emission rate per unit length (#/hour/m)
distance = 10  # Distance from the line source (m)
length = 10000  # Length of line segment to simulate infinite behavior
num_samples = 1000000  # Number of Monte Carlo samples

# Calculate photon flux using Monte Carlo
flux = monte_carlo_flux_infinite_line(S_L, distance, length, num_samples)

print(f"Estimated photon flux at {distance} meters: {flux:.4e} #/hour/m²")
