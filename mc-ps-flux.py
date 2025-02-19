import numpy as np

# Simulation parameters
num_photons = 100000  # Total number of photons emitted
emission_rate = 1e6  # Photons emitted per hour
r = 10.0  # Distance from the point source (in meters)

# Function to generate isotropic directions for photons
def generate_isotropic_directions(num_photons):
    """Generate isotropic directions for photons."""
    phi = np.random.uniform(0, 2 * np.pi, num_photons)  # Azimuthal angle
    costheta = np.random.uniform(-1, 1, num_photons)  # Cosine of polar angle
    theta = np.arccos(costheta)  # Polar angle
    return theta, phi

# Monte Carlo simulation for flux at distance r
def monte_carlo_flux(num_photons, r):
    """Simulate photon flux at distance r using Monte Carlo."""
    # Generate isotropic directions
    theta, phi = generate_isotropic_directions(num_photons)

    # Direction vectors
    dx = np.sin(theta) * np.cos(phi)
    dy = np.sin(theta) * np.sin(phi)
    dz = np.cos(theta)

    # Scale factors to reach distance r
    distances = r / np.sqrt(dx**2 + dy**2 + dz**2)
    x_hits = distances * dx
    y_hits = distances * dy
    z_hits = distances * dz

    # Check if photons hit the sphere of radius r
    hits_on_sphere = np.isclose(np.sqrt(x_hits**2 + y_hits**2 + z_hits**2), r, atol=1e-3)
    num_hits = np.sum(hits_on_sphere)

    # Calculate flux
    sphere_area = 4 * np.pi * r**2  # Surface area of the sphere
    flux = num_hits / sphere_area  # Flux in photons per square meter
    return flux

# Calculate flux and scale by emission rate
flux = monte_carlo_flux(num_photons, r)
actual_flux = flux * emission_rate  # Flux per hour

# Output results
print(f"Distance: {r} m")
print(f"Simulated Flux: {flux:.4e} photons/m^2")
print(f"Flux per hour: {actual_flux:.4e} photons/m^2/h")