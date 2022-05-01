import polars as pl

from .dataset import dataset

print(dataset[["state", "party"]].head(10).to_dict(False))

q = (
    dataset.lazy()
    .groupby("state")
    .agg(
        [
            (pl.col("party") == "Anti-Administration").sum().alias("anti"),
            (pl.col("party") == "Pro-Administration").sum().alias("pro"),
        ]
    )
    .inspect()
    .sort("pro", reverse=True)
    .limit(5)
)

df = q.collect()
