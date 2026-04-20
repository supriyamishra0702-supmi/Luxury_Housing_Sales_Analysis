import pandas as pd
from sqlalchemy import create_engine

# 1. LOAD DATA
print("Loading data...")

df = pd.read_csv('Luxury_Housing_Bangalore.csv')

# 2. CLEANING & HANDLING NULLS
print("Cleaning data...")
# Convert Ticket Price to numbers (Handling 'Cr' and whitespace)
df['Ticket_Price_Cr'] = pd.to_numeric(
    df['Ticket_Price_Cr'].astype(str)
    .str.replace('Cr', '', case=False)
    .str.replace('₹', '')
    .str.strip(), 
    errors='coerce'
)

# FIX: Remove rows where Ticket_Price_Cr is null (Your 10,000 missing values)
df = df.dropna(subset=['Ticket_Price_Cr'])

# Fill missing Amenity Scores with the median
if 'Amenity_Score' in df.columns:
    df['Amenity_Score'] = df['Amenity_Score'].fillna(df['Amenity_Score'].median())

# 3. FEATURE ENGINEERING
print("Creating new features...")
# Calculate Price per Sqft (Standard Real Estate Metric)
if 'Unit_Size_Sqft' in df.columns:
    df['Price_per_Sqft'] = (df['Ticket_Price_Cr'] * 10000000) / df['Unit_Size_Sqft']

# Create a numeric flag for bookings (1 for Booked, 0 for otherwise)
if 'Booking_Status' in df.columns:
    df['Booking_Flag'] = df['Booking_Status'].apply(lambda x: 1 if str(x).lower() == 'booked' else 0)

# 4. LOAD TO SQL & EXCEL
print("Saving results...")
# Create SQL database for project documentation
engine = create_engine('sqlite:///real_estate.db')
df.to_sql('luxury_housing', con=engine, if_exists='replace', index=False)

# Export to Excel for Power BI Web 
df.to_excel('cleaned_luxury_data.xlsx', index=False)

print(f"✅ DONE! Total rows ready for analysis: {len(df)}")
print("✅ SQL Database 'real_estate.db' updated.")
print("✅ Excel File 'cleaned_luxury_data.xlsx' created.")
