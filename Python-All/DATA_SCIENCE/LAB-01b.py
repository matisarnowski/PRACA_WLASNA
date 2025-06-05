import pandas as pd
from matplotlib import pyplot as plt

taxi = pd.read_parquet(
    "./datasets/yellow_tripdata_2021-05.parquet",
    engine="auto",
    columns=None,
    storage_options=None,
    use_nullable_dtypes=False,
)

print(taxi)

taxi = taxi.groupby(["payment_type"]).count()

taxi.rename(
    index={
        0: "Credit card",
        1: "Cash",
        2: "No charge",
        3: "Dispute",
        4: "Unknown",
    },
    inplace=True,
)
print(taxi)
taxi.loc["Other"] = taxi.loc["Dispute"] + taxi.loc["Unknown"]
taxi.drop(["Dispute", "Unknown"], inplace=True)

print(taxi)

fig, ax = plt.subplots()
ax.bar(taxi.index, taxi["VendorID"], color="C0")

plt.show()
