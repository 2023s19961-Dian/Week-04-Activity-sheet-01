import numpy as np
import matplotlib.pyplot as plt

# Hypothetical model parameters
arrival_rate = 10
service_rate = 2
counters = np.arange(4, 11)
waiting_times = []
utilizations = []

# Calculate utilization and waiting time
for c in counters:
    arrival_per_counter = arrival_rate / c
    rho = arrival_per_counter / service_rate
    utilizations.append(rho)

    if rho < 1:
        Wq = rho / (service_rate - arrival_per_counter)
        waiting_times.append(Wq)
    else:
        waiting_times.append(np.nan)

waiting_times = np.array(waiting_times)

plt.figure(figsize=(11, 6))

# Plot stable cases
stable = np.isfinite(waiting_times)

plt.scatter(
    counters[stable],
    waiting_times[stable],
    marker="o",
    linewidth=2,
    color="blue",
    label="Stable queue"
)

# Plot unstable cases at a separate visual height
unstable_counters = counters[~stable]
unstable_y = np.full(len(unstable_counters), 5.4)

plt.scatter(
    unstable_counters,
    unstable_y,
    color="red",
    marker="X",
    s=120,
    label="Unstable (no steady-state wait)",
    zorder=5
)


# Five-minute target
plt.axhline(
    y=5,
    color="gray",
    linestyle=":",
    label="5-minute target"
)

plt.xlabel("Number of Counters")
plt.ylabel("Average Queue Waiting Time (minutes)")
plt.title("Effect of Counter Number on Queue Waiting Time")
plt.xticks(counters)
plt.ylim(0, 6.5)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# Display graph
plt.show()
