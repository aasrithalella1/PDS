import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Loading the dataset
df = pd.read_csv("C:/Users/aasri/OneDrive/Documents/UMKC SPRING/Assignment_1/Q2_Student_Performance/raw_data/StudentsPerformance.csv")

# this displays first few rows
print("First few rows of the dataset:")
print(df.head())


# for creating results directory
results_dir = "C:/Users/aasri/OneDrive/Documents/UMKC SPRING/Assignment_1/Q2_Student_Performance/results"
os.makedirs(results_dir, exist_ok=True)

# Visualization 1: Histogram of Math Scores
plt.figure(figsize=(8, 5))
sns.histplot(df['math score'], bins=10, kde=True, color='skyblue')
plt.title("Math Score Distribution")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.savefig(os.path.join(results_dir, "math_score_distribution.png"))
plt.close()

# Visualization 2: Scatter Plot - Reading vs Writing Scores
plt.figure(figsize=(8, 5))
sns.scatterplot(x='reading score', y='writing score', hue='gender', data=df, palette='Set1')
plt.title("Reading Score vs Writing Score")
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.legend(title='Gender')
plt.savefig(os.path.join(results_dir, "reading_vs_writing.png"))
plt.close()

# Visualization 3: Box Plot - Math Scores by Gender
plt.figure(figsize=(8, 5))
sns.boxplot(x='gender', y='math score', data=df, hue='gender', palette='pastel', legend=False)
plt.title("Math Scores by Gender")
plt.xlabel("Gender")
plt.ylabel("Math Score")
plt.savefig(os.path.join(results_dir, "math_scores_gender.png"))
plt.close()

# Visualization 4: Bar Plot - Test Preparation vs Math Score
plt.figure(figsize=(8, 5))
sns.barplot(x='test preparation course', y='math score', hue='test preparation course', data=df, palette='viridis', legend=False)
plt.title("Test Preparation Course Impact on Math Score")
plt.xlabel("Test Preparation Course")
plt.ylabel("Average Math Score")
plt.savefig(os.path.join(results_dir, "test_prep_math.png"))
plt.close()

# Visualization 5: Correlation Heatmap
plt.figure(figsize=(10, 6))
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt='.2f', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.savefig(os.path.join(results_dir, "correlation_heatmap.png"))
plt.close()

print(f"Visualizations saved in {results_dir}")
