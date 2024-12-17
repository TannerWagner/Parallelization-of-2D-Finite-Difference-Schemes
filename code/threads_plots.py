import numpy as np
import matplotlib.pyplot as plt

timings = np.loadtxt('timings.txt')

# thread counts for labeling
thread_counts = [1, 2, 3]

# timing data
plt.figure(figsize=(10, 6))
for i, thread_count in enumerate(thread_counts):
    plt.plot(range(1, timings.shape[1] + 1), timings[i], marker='o', label=f'{thread_count} Thread{"s" if thread_count > 1 else ""}')

plt.title('Local Machine Timings for Different Thread Counts')
plt.xlabel('Timing Instance')
plt.ylabel('Timing (s)')
plt.xticks(range(1, timings.shape[1] + 1))  
plt.legend(title="Thread Count")
plt.grid(True)
plt.savefig('local_timings_plot.png', dpi=300)
plt.show()
