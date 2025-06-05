import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

taxi = pd.read_parquet(
    "./datasets/yellow_tripdata_2021-05.parquet",
    engine="auto",
    columns=["trip_distance"],
    storage_options=None,
    use_nullable_dtypes=False,
)

taxi.query("trip_distance > 0 and trip_distance <= 50", inplace=True)

number_of_bins = 50
interval_width = (
    taxi["trip_distance"].max() - taxi["trip_distance"].min()
) / number_of_bins
print(f"Good interval width for {number_of_bins} bins is {interval_width}")

abs_frequency, intervals = np.histogram(taxi["trip_distance"], bins=50)
print(
    "Automatically calculated intervals",
    abs_frequency,
    intervals,
    len(abs_frequency),
    len(intervals),
)

interval_range = pd.interval_range(start=0, freq=1, end=50, closed="right")
taxi["bin"] = pd.cut(taxi["trip_distance"], bins=interval_range)
print(taxi.head())
freq_table = pd.crosstab(index=taxi["bin"], columns="trip_distance")
print(freq_table)

taxi.plot.hist(column="trip_distance", bins=50)
plt.show()
