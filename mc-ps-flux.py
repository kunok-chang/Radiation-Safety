import numpy as np

def monte_carlo_photon_flux(Sp_hour, distance, num_samples=1000000):
    """
    Calculate photon flux using Monte Carlo simulation.

    Parameters:
    - Sp_hour (int): Number of photons emitted per hour (photons/hour).
    - distance (float): Distance from the point source (m).
    - num_samples (int): Number of photons to simulate (Monte Carlo samples).

    Returns:
    - Estimated photon flux (photons/m^2/hour).
    """
    # Define the cross-sectional area at the given distance
    cross_sectional_area = 4 * np.pi * distance**2
    
    # Generate random angles for photon emission
    theta = np.arccos(1 - 2 * np.random.rand(num_samples))  # Polar angle (0 to π)
    phi = 2 * np.pi * np.random.rand(num_samples)           # Azimuthal angle (0 to 2π)

    # Photon direction vectors (normalized)
    x_dir = np.sin(theta) * np.cos(phi)
    y_dir = np.sin(theta) * np.sin(phi)
    z_dir = np.cos(theta)

    # Check if photons intersect the surface area at distance r
    # All photons start from the origin and travel outward
    r_intersect = distance * z_dir / np.abs(z_dir)  # Intersection test along z-direction
    
    # Count photons passing through the spherical shell at distance r
    photons_through_area = np.sum(r_intersect > 0)

    # Estimate flux
    flux = (photons_through_area / num_samples) * (Sp_hour / cross_sectional_area)
    return flux

# Example parameters
Sp_hour = 1.0e6  # Photon emission rate in photons/hour
distance = 10     # Distance from the point source in meters
num_samples = 1000000  # Number of photons to simulate

# Calculate photon flux using Monte Carlo
estimated_flux = monte_carlo_photon_flux(Sp_hour, distance, num_samples)

print(f"Estimated photon flux at {distance} meters: {estimated_flux:.4e} photons/m²/hour")
