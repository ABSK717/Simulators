import matplotlib.pyplot as plt
import numpy as np

# Number of simulations
num_simulations = 1000



# Roll two dice
dice1 = np.random.randint(1, 7, num_simulations)
dice2 = np.random.randint(1, 7, num_simulations)

# Sum the results of the two dice
sums = dice1 + dice2

# Calculate the frequency of each possible sum
sum_values, frequencies = np.unique(sums, return_counts=True)

# Calculate the probabilities
probabilities = frequencies / num_simulations

# Plot the probability distribution
plt.bar(sum_values, probabilities, color='red', alpha=1)
plt.xlabel('Sum of Two Dice')
plt.ylabel('Probability')
plt.title('Probability Distribution of Rolling Two Dice')
plt.xticks(sum_values)
plt.grid(True)
plt.show()
