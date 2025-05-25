import polars as pl

# Load the CSV into a DataFrame
csv_path = "/Users/rbojorge/Library/CloudStorage/GoogleDrive-rbojorge@gmail.com/My Drive/Digital Brain/2 Areas/code/intro_polars/datasets/electric_vehicles.csv"
ev_df = pl.read_csv(csv_path)

# Sort with longest range first
sorted_ev_df = ev_df.sort("range")
print(sorted_ev_df)

# Print a summary of the DataFrame
print(ev_df.describe())

# Get the most expensive 4 vehicles
expensive_df = ev_df.top_k(4, by="price")

print(expensive_df)

# Find the four cheapest vehicles
cheap_df = ev_df.bottom_k(4, by="price")

print(cheap_df)