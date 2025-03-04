import pandas as pd
#i have loaded the dataset
df = pd.read_csv("C:/Users/aasri/OneDrive/Documents/UMKC SPRING/Assignment_1/Q1_Frailty_Dataset/raw_data/frailty_data.csv")

# this will show total rows and columns
print("Total no of Row and columns")
print(df.shape)

# first 10 rows
print("Dataset:")
print(df.head(10))

# Summary statistics of the dataset
print("\nSummary statistics:")
summary = df.describe()

# this saves the processed data as a new file
df.to_csv("cleaned_frailty_data.csv", index=False)
summary.to_csv("summary_statistics.csv")

print("Data processing completed. summary of the dataset:")
print(summary)

# Count of the no of participants with and without frailty
print("\nFrailty counts:")
print(df['Frailty'].value_counts())