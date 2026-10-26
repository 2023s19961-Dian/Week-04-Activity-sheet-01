import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

data=pd.read_csv("student_performance.csv")
print(data)

print("Dimensions:")
print(data.shape)

print("DataTypes:")
print(data.dtypes)

print("FirstFewRows:")
print(data.head())

print("Basic summary statistics:")
print(data.describe())

print("Mean:")
print(data["Exam"].mean())

print("Median:")
print(data["Exam"].median())

print("StandardDeviation:")
print(data["Exam"].std())

correlation=data["Study Hours"].corr(data["Exam"])
print("Pearson correlation:")
print(correlation)

plt.figure(figsize=(12, 10))
plt.subplot(2,2,1)
plt.scatter(data["Study Hours"],data["Exam"])
plt.xlabel("Study Hours")
plt.ylabel("Exam Marks")
plt.title("Study Hours vs Exam Marks")

plt.subplot(2,2,2)
plt.hist(data["Exam"],bins=10,edgecolor="black")
plt.xlabel("Exam Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Exam Marks")


plt.subplot(2,2,3)
plt.boxplot(data["Exam"].dropna())
plt.ylabel("Exam Marks")
plt.title("Box Plot of Exam Marks")


plt.subplot(2,2,4)
heatmap_data = data[['Study Hours', 'Assignment']]
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt='.1f')
plt.title("Heatmap of Study Hours vs Assignment Marks")
plt.show()
