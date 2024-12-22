import glob
import pprint
import pandas as pd
import os


def concatenate(input_path: str, output_path: str):
    os.makedirs(output_path, exist_ok=True)

    scan_no = [16, 24, 32, 48, 64, 72]
    scan_no_paths = {
        i: glob.glob(f"{input_path}/*/*{i} [Ss]cans.[0-9].dpt") for i in scan_no
    }

    sample_df = pd.read_table(
        scan_no_paths[16][0], delimiter=",", names=["wave_no", "abs"]
    )
    wave_no = sample_df["wave_no"]
    wave_no.to_csv(f"{output_path}/wave_no.csv", index=False)

    for no, path_list in scan_no_paths.items():
        concatenated_data = pd.DataFrame()

        for count, path in enumerate(path_list, start=1):
            sample_name = f"sample_{count}"
            data = pd.read_table(path, delimiter=",", names=["wave_no", sample_name])

            if concatenated_data.empty == True:
                concatenated_data = data

            else:
                concatenated_data = pd.merge(
                    left=concatenated_data, right=data, on="wave_no", how="outer"
                )

        # concatenated_data = concatenated_data.drop(columns=["wave_no"])
        concatenated_data.to_csv(f"{output_path}/{no}_scans.csv", index=False)


def clean(input_path: str, output_path: str):
    os.makedirs(output_path, exist_ok=True)
    scan_no = [16, 24, 32, 48, 64, 72]
    df_path = glob.glob(f"{input_path}/*_scans.csv")

    for no, path in zip(scan_no, df_path):
        if no == 72:
            anomalous = "sample_11"
        else:
            anomalous = "sample_12"

        df = pd.read_csv(path)
        df = df.drop(columns=anomalous)
        df.to_csv(f"{output_path}/{no}_scans.csv", index=False)


if __name__ == "__main__":
    # concatenate("optimization_samples", "concatenated_csvs")
    #clean("concatenated_csvs", "cleaned_csvs")
