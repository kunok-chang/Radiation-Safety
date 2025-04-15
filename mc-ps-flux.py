import numpy as np

def photon_flux_hourly(point_source_emission_hour, distance):
    """
    Calculate the photon flux from a point source, given the hourly emission rate.

    Parameters:
    - point_source_emission_hour (Sp): Number of photons emitted by the point source per hour (photons/hour).
    - distance (r): Distance from the point source to the measurement point (m).

    Returns:
    - Photon flux at the given distance (photons/m^2/hour).
    """
    if distance <= 0:
        raise ValueError("Distance must be greater than zero.")
    return point_source_emission_hour / (4 * np.pi * distance**2)

# Example parameters
Sp_hour = 1.0e6  # Photon emission rate in photons/hour
r = 10  # Distance from the point source in meters

# Calculate photon flux
flux_hourly = photon_flux_hourly(Sp_hour, r)

print(f"Photon flux at {r} meters: {flux_hourly:.4e} photons/m²/hour")
