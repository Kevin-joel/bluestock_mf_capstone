import pandas as pd
import os

processed_path = "data/processed"

for file in os.listdir(processed_path):

    if file.endswith(".csv"):

        print("\n" + "="*70)
        print(f"FILE: {file}")

        df = pd.read_csv(
            os.path.join(processed_path, file)
        )

        print("\nRows, Columns:")
        print(df.shape)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicates:")
        print(df.duplicated().sum())

        print("\nData Types:")
        print(df.dtypes)