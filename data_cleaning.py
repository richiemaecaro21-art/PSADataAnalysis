import pandas as pd

# Step 1: Load the CSV, skipping the messy top rows
data = pd.read_csv("unemployment_underemployment_2025.csv", skiprows=9)

# Step 2: Show the first few rows
print("Before cleaning:")
print(data.head())

# Step 3: Clean up column names
data.columns = data.columns.str.strip().str.replace("\n", " ")

# Step 4: Remove rows with all NaN values
data = data.dropna(how='all')

# Step 5: Remove commas and convert numeric values where possible
for col in data.columns[1:]:
    data[col] = data[col].astype(str).str.replace(",", "", regex=False)
    data[col] = pd.to_numeric(data[col], errors="coerce")

# Step 6: Drop any remaining empty rows
data = data.dropna(subset=[data.columns[1]])

# Step 7: Save the cleaned version
data.to_csv("cleaned_unemployment_underemployment_2025.csv", index=False)

print("\nAfter cleaning:")
print(data.head())
print("\n✅ Cleaned data saved as 'cleaned_unemployment_underemployment_2025.csv'")









