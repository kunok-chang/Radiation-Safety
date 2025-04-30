import numpy as np
import matplotlib.pyplot as plt

# Define material properties
MU = 0.1  # Linear attenuation coefficient (1/cm)
GRID_SIZE = 10.0  # Simulation grid size (cm)
PHOTON_COUNT = 1000  # Number of photons to simulate

# Generate random direction
def random_direction():
    phi = np.random.uniform(0, 2 * np.pi)  # Random azimuthal angle
    theta = np.random.uniform(0, np.pi)    # Random polar angle
    return np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)

# Simulate photon transport
def simulate_photon():
    position = np.array([0.0, 0.0, 0.0])  # Start at origin
    direction = np.array(random_direction())
    path = [position.copy()]
    
    while np.linalg.norm(position) < GRID_SIZE:
        # Calculate distance to next interaction
        step = -np.log(np.random.uniform()) / MU
        position += step * direction
        
        # Record position
        path.append(position.copy())
        
        # Determine interaction: absorb or scatter
        if np.random.uniform() < 0.5:  # 50% chance of absorption
            break
        else:  # Scatter
            direction = np.array(random_direction())
    
    return np.array(path)

# Run Monte Carlo simulation
all_paths = []
for _ in range(PHOTON_COUNT):
    path = simulate_photon()
    all_paths.append(path)

# Visualization
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
for path in all_paths[:100]:  # Plot only the first 100 photons
    ax.plot(path[:, 0], path[:, 1], path[:, 2], alpha=0.5)

ax.set_xlim([-GRID_SIZE, GRID_SIZE])
ax.set_ylim([-GRID_SIZE, GRID_SIZE])
ax.set_zlim([-GRID_SIZE, GRID_SIZE])
ax.set_xlabel("X (cm)")
ax.set_ylabel("Y (cm)")
ax.set_zlabel("Z (cm)")
ax.set_title("Monte Carlo Photon Transport Simulation")
plt.show()
