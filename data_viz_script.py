# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# --- Data Loading and Cleaning ---
try:
    # Load a sample dataset (ensure 'sample_data.csv' is in the repo)
    df = pd.read_csv('sample_data.csv')

    # Simple Data Cleaning: Check for and drop rows with any missing values
    df.dropna(inplace=True)

    print(f"Loaded and cleaned {len(df)} rows of data.")

except FileNotFoundError:
    print("Error: 'sample_data.csv' not found. Ensure the file is in the repository.")
    exit()

# --- Exploratory Analysis and Visualization ---

# 1. Calculate Average Score
average_score = df['Score'].mean()
print(f"Average Score across all samples: {average_score:.2f}")

# 2. Visualization: Bar plot of Score by Category
plt.figure(figsize=(10, 6))
df.groupby('Category')['Score'].mean().plot(kind='bar')
plt.title('Average Score by Category')
plt.ylabel('Average Score')
plt.xlabel('Category')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('category_score_bar_chart.png') # Saves the visual output

print("Visualization saved successfully.")
