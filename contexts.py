import polars as pl
from dataset import df

## select context
out = df.select(
    [
        pl.sum("nrs"),
        pl.col("names").sort(),
        pl.col("names").first().alias("first name"),
        (pl.mean("nrs") * 10).alias("10xnrs"),
    ]
)
print(out)

## with_columns context
df = df.with_columns(
    [
        pl.sum("nrs").alias("nrs_sum"),
        pl.col("random").count().alias("count"),
    ]
)
print(df)

## groupby context
out = df.groupby("groups").agg(
    [
        pl.sum("nrs"),  # sum nrs by groups
        pl.col("random").count().alias("count"),  # count group members
        # sum random where name != null
        pl.col("random").filter(pl.col("names").is_not_null()).sum().suffix("_sum"),
        pl.col("names").reverse().alias(("reversed names")),
    ]
)
print(out)

