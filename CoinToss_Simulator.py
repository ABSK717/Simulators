import matplotlib.pyplot as plt
import numpy as np

# Number of simulations
num_tosses = 100

# Simulate coin tosses (0 for Tails, 1 for Heads)
tosses = np.random.randint(0, 2, num_tosses)

# Count the occurrences of Heads and Tails
counts = np.bincount(tosses)

# Plot the results
plt.bar(['Tails', 'Heads'], counts, color=['blue', 'orange'], alpha=0.7)
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.title('Coin Toss Simulation')
plt.show()
