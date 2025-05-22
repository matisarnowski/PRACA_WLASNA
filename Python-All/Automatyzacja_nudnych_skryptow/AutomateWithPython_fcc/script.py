import pandas as pd

kings_of_poland = pd.read_html(
    "http://pl.wikipedia.org/wiki/W%C5%82adcy_Polski", index_col=[0]
)
print(len(kings_of_poland))

print(f"Legendarni władcy Polski.\n {kings_of_poland[2]}.")
