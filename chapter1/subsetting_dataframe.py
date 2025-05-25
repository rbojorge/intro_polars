import polars as pl

# Load the CSV into a DataFrame
csv_path = "/Users/rbojorge/Library/CloudStorage/GoogleDrive-rbojorge@gmail.com/My Drive/Digital Brain/2 Areas/code/intro_polars/datasets/electric_vehicles.csv"
ev_df = pl.read_csv(csv_path)

# Create a Series from the brand column
print(ev_df["brand"])

# Extract the brand, model and price columns
print(ev_df[["brand", "model", "price"]])

# Print the last three rows of the brand and price columns
print(ev_df[-3:,["brand", "price"]])

# Select the model, accel and price columns
print(ev_df.select("model","accel","price"))

# Select the brand, model and price columns
print(ev_df.select(["brand", "model", "price"]))