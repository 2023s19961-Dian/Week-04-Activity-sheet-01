
import numpy as np
import matplotlib.pyplot as plt

data = [5, 2, 8, 4, 7, 1, 5, 10, 4, 7,
        3, 6, 3, 5, 2, 7, 4, 9, 5, 11]

print("Mean:", np.mean(data))
print("Median:", np.median(data))


print("Sample variance:", np.var(data, ddof=1))
print("Sample standard deviation:", np.std(data, ddof=1))

updated_data = data.copy()
index = updated_data.index(8)
updated_data[index] = 12


print("Updated data:", updated_data)
print("Mean:", np.mean(updated_data))
print("Median:", np.median(updated_data))
print("Sample variance:", np.var(updated_data, ddof=1))
print("Sample standard deviation:", np.std(updated_data, ddof=1))


plt.hist(updated_data, bins=np.arange(0.5, 13.5, 1),
         edgecolor='black')

plt.title("Self-Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.xticks(range(1, 13))
plt.savefig("Q1_graph.png", bbox_inches="tight")
plt.close()
