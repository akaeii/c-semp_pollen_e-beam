import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def filter_conifers(input_dir, output_dir):
    zim_sheet = pd.read_excel(
        f"{input_dir}/zimmerman_data_sheet_2.xlsx", sheet_name="FTIR"
    )

    zim_wave_no = zim_sheet.iloc[0, 2:]
    zim_wave_no.to_csv(
        f"{output_dir}/zim_wave_no.csv", header=["zim_wave_no"], index=False
    )

    sample_names = zim_sheet.iloc[:, 1]

    order_pinales = sample_names[
        sample_names.str.contains(pat="^PPin", regex=True, na=False)
    ]

    pinales_samples = np.array_split(order_pinales, len(order_pinales) / 3)

    zimmer_pinales_ftir_abs_ave = pd.DataFrame()

    for chunk in pinales_samples:
        species = zim_sheet.iloc[chunk.index[0], 0]
        sample_abs = pd.DataFrame()
        for index, sample in zip(chunk.index, chunk):
            sample_abs[sample] = zim_sheet.iloc[index, 2:]

        sample_abs["average"] = sample_abs.iloc[:, :].mean(axis=1)
        zimmer_pinales_ftir_abs_ave[species] = sample_abs["average"]

    zimmer_pinales_ftir_abs_ave.to_csv(
        "data/zimmer_pinales_ftir_abs_ave.csv", index=False
    )


if __name__ == "__main__":
    filter_conifers("data", "data")
