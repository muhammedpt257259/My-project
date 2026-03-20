
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data
data = {
    "Category": ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
    "Values": [10, 15, 14, 20, 22, 19, 30, 29, 35]
}

df = pd.DataFrame(data)

# Create violin plot
sns.violinplot(x="Category", y="Values", data=df)

# Title and labels
plt.title("Violin Plot Example")
plt.xlabel("Category")
plt.ylabel("Values")

# Show plot
plt.show()