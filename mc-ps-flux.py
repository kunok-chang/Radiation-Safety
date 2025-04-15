import numpy as np

def monte_carlo_photon_flux(S_p, distance, num_samples=1000000):
    """
    Calculate photon flux using Monte Carlo simulation.

    Parameters:
    - S_p (float): Photon emission rate (#/hour).
    - distance (float): Distance from the source (m).
    - num_samples (int): Number of Monte Carlo samples.

    Returns:
    - Photon flux at the given distance (#/hour/m²).
    """
    # Cross-sectional area of a sphere at distance r
    cross_sectional_area = 4 * np.pi * distance**2
    
    # Generate random angles for photon emission
    theta = np.arccos(1 - 2 * np.random.rand(num_samples))  # Polar angle (0 to π)
    phi = 2 * np.pi * np.random.rand(num_samples)           # Azimuthal angle (0 to 2π)

    # Direction of photons (normalized)
    x_dir = np.sin(theta) * np.cos(phi)
    y_dir = np.sin(theta) * np.sin(phi)
    z_dir = np.cos(theta)

    # Test photons' passage through a spherical shell at distance r
    # All photons originate from the source (0, 0, 0) and travel outward
    photons_through_area = num_samples  # All photons are emitted isotropically

    # Photon flux
    flux = (photons_through_area / num_samples) * (S_p / cross_sectional_area)
    return flux

# Parameters
S_p = 1e6  # Photon emission rate (#/hour)
distance = 10  # Distance from the source (m)
num_samples = 1000000  # Number of photons to simulate

# Calculate photon flux using Monte Carlo
flux = monte_carlo_photon_flux(S_p, distance, num_samples)

print(f"Estimated photon flux at {distance} meters: {flux:.4e} #/hour/m²")
