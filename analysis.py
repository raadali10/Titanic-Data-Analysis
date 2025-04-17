import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (since it's in the same folder)
df = pd.read_csv("tested.csv")

# Basic info
print("First 5 rows:\n", df.head())
print("\nSummary statistics:\n", df.describe())

# Gender counts
gender_counts = df['Sex'].value_counts()
print("\nGender Counts:\n", gender_counts)

# Survival rates by gender
survival_by_gender = df.groupby('Sex')['Survived'].mean()
print("\nSurvival Rates by Gender:\n", survival_by_gender)

# Plot survival rates
survival_by_gender.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("survival_rate_by_gender.png")
plt.show()
