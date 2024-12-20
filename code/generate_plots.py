import numpy as np
import matplotlib.pyplot as plt

timings = np.loadtxt('timingsCarc.txt')
threads = np.arange(1, len(timings) + 1)

# Strong Scaling Plot (Timing vs Thread Count)
plt.figure()
plt.plot(threads, timings, marker='o', linestyle='-')
plt.xlabel("Number of Threads")
plt.ylabel("Timing (seconds)")
plt.title("Strong Scaling Plot")
plt.grid(True)
plt.savefig("strong_scaling_plot.png", dpi=300)

# Parallel Efficiency Plot (Efficiency vs Thread Count)
T1 = timings[0]  # Time with 1 thread
efficiency = T1 / (timings * threads)

plt.figure()
plt.plot(threads, efficiency, marker='o', linestyle='-')
plt.xlabel("Number of Threads")
plt.ylabel("Efficiency")
plt.title("Strong Scaling  Efficiency Plot")
plt.grid(True)
plt.savefig("parallel_efficiency_plot.png", dpi=300)

print("Plots saved as 'strong_scaling_plot.png' and 'parallel_efficiency_plot.png'")
