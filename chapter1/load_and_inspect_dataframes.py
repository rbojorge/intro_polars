import polars as pl

# Load the CSV into a DataFrame
csv_path = "/Users/rbojorge/Library/CloudStorage/GoogleDrive-rbojorge@gmail.com/My Drive/Digital Brain/2 Areas/code/intro_polars/datasets/electric_vehicles.csv"
ev_df = pl.read_csv(csv_path)

# Print the first three rows
print(ev_df.head(3))

# Print number of rows and columns of the df
print(f"Dataframe total shape: {ev_df.shape}")

# Print the column names of the df
print(f"Dataframe columns: {ev_df.columns}")

# Print the Dataframe column names and dtypes
print(ev_df.schema)

# Print the first values in a vertical format
print(ev_df.glimpse())
