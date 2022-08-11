import polars as pl
from dataset import df

## filtering and conditionals
out = df.select(
    [
        pl.col("names").filter(pl.col("names").str.contains(r"am$")).count(),
    ]
)
print(out)


## when -> then -> otherwise construct
out = df.select(
    [
        pl.when(pl.col("random") > 0.5).then(0).otherwise(pl.col("random")) * pl.sum("nrs"),
    ]
)
print(out)


## window expressions
df = df[
    [
        pl.col("*"),  # select all
        pl.col("random").sum().over("groups").alias("sum[random]/groups"),
        pl.col("random").list().over("names").alias("random/name"),
    ]
]
print(df)
