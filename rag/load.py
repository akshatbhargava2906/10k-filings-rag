import polars as pl

df = pl.read_parquet("data\sample.parquet")

print(df.head(5))