import pandas as pd
from matplotlib import pyplot as plt

taxi = pd.read_parquet(
    "./datasets/yellow_tripdata_2021-05.parquet",
    engine="auto",
    columns=None,
    storage_options=None,
    use_nullable_dtypes=False,
)
probe = []
for f in range(1000):
    df_probe = taxi["tip_amount"][f]
    print(df_probe)
    probe.append(df_probe)
plt.plot(probe)
plt.hlines(
    xmin=0, xmax=1000, y=taxi["tip_amount"].mean(), linestyles="solid", colors="red"
)
plt.hlines(xmin=0, xmax=1000, y=0, linestyles="solid", colors="green")
plt.hlines(xmin=0, xmax=1000, y=5, linestyles="solid", colors="orange")
plt.show()
