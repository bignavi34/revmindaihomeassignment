import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///sales.db"
)

df = pd.read_csv(
    "../novabite_sales_data.csv"
)

df.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False
)

print("Database seeded successfully.")