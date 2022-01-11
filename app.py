import pandas as pd
from helpers import get_files, get_confidence_level

# Saved requests from https://apis.estated.com/v4/property
csv_files = get_files()

# Combine csv files
df = pd.concat([pd.read_csv(f) for f in csv_files])

# Add confidence levels column
df['confidence_level'] = get_confidence_level(
    df,
    column_name='forecast_standard_deviation'
)

# Check new column
print(df['confidence_level'])