import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/aasri/OneDrive/Documents/UMKC SPRING/Assignment_1/Q1_Frailty_Dataset/raw_data/frailty_data.csv")

# This will show rows and columns
print("Total no of Row and columns")
print(df.shape)

# Displays first 10 rows
print("Dataset:")
print(df.head(10))

# Summary statistics
print("\nSummary statistics:")
summary = df.describe()

# Save processed data as a new CSV file
df.to_csv("cleaned_frailty_data.csv", index=False)
summary.to_csv("summary_statistics.csv")


# Display the summary
print("Data processing completed. summary of the dataset:")
print(summary)

# Count the number of participants with and without frailty
print("\nFrailty counts:")
print(df['Frailty'].value_counts())
