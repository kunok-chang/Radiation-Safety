import numpy as np

# Simulation parameters
num_photons = 100000  # Total number of photons emitted
emission_rate = 1e6  # Photons emitted per hour per unit length
x = 10.0  # Perpendicular distance from the infinite line source (in meters)

# Function to generate isotropic directions for photons
def generate_isotropic_directions(num_photons):
    """Generate isotropic directions for photons."""
    phi = np.random.uniform(0, 2 * np.pi, num_photons)  # Azimuthal angle
    costheta = np.random.uniform(-1, 1, num_photons)  # Cosine of polar angle
    theta = np.arccos(costheta)  # Polar angle
    return theta, phi

# Monte Carlo simulation for flux at distance x from an infinite line source
def monte_carlo_flux_line_source(num_photons, x):
    """Simulate photon flux at distance x using Monte Carlo."""
    # Generate isotropic directions
    theta, phi = generate_isotropic_directions(num_photons)

    # Direction vectors (photon trajectories)
    dx = np.sin(theta) * np.cos(phi)
    dy = np.sin(theta) * np.sin(phi)
    dz = np.cos(theta)

    # Generate random starting positions along the infinite line source
    line_y = np.random.uniform(-1e3, 1e3, num_photons)  # Line extends from -infinity to infinity (simulated)

    # Compute closest approach distances to the line source
    distances = np.sqrt(x**2 + line_y**2)

    # Count photons that reach the distance x within a small tolerance
    hits_on_circle = np.isclose(distances, x, atol=1e-3)
    num_hits = np.sum(hits_on_circle)

    # Calculate flux per unit length of the line source
    circle_circumference = 2 * np.pi * x  # Circumference of the circle at distance x
    flux = num_hits / (circle_circumference * 2 * 1e3)  # Normalize by line length (-1e3 to 1e3)
    return flux

# Calculate flux and scale by emission rate
flux = monte_carlo_flux_line_source(num_photons, x)
actual_flux = flux * emission_rate # Flux per hour

# Output results
print(f"Distance: {x} m")
print(f"Simulated Flux: {flux:.4e} photons/m^2")
print(f"Flux per hour: {actual_flux:.4e} photons/m^2/h")
