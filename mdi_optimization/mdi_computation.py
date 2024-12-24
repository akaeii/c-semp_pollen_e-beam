import pandas as pd
import glob
import os


def mdi_compute(input_dir: str, output_path: str):
    os.makedirs(output_path, exist_ok=True)
    # Loading Data
    csv_paths = glob.glob(f"{input_dir}/*_scans.csv")
    scan_no_dict = {
        path.split("/")[-1].replace(".csv", ""): pd.read_csv(path) for path in csv_paths
    }
    wave_no = pd.read_csv(f"{input_dir}/wave_no.csv")

    # Computing MDI
    lp = 3996.73391
    rp = 599.51009
    i = wave_no["wave_no"]

    result_df = pd.DataFrame()

    for key, df in scan_no_dict.items():

        mdi_results = []

        for sample in df.columns[1:]:
            p = df[sample]
            md_lp = sum(((p**2) + ((i - lp)) ** 2) ** 0.5)
            md_rp = sum(((p**2) + ((rp - i)) ** 2) ** 0.5)
            mdi = md_rp - md_lp
            mdi_results.append(mdi)

        result_df[f"{key}_mdi"] = pd.Series(mdi_results)

    result_df.to_csv(f"{output_path}/master_mdi.csv", index=False)


def smdi_compute(input_dir: str, output_path: str):
    os.makedirs(output_path, exist_ok=True)

    # Loading Data
    csv_paths = glob.glob(f"{input_dir}/*_scans.csv")
    scan_no_dict = {
        path.split("/")[-1].replace(".csv", ""): pd.read_csv(path) for path in csv_paths
    }

    # Computing SMDI
    for key, df in scan_no_dict.items():
        result_df = pd.DataFrame()
        mdi = df.iloc[1:, 0]
        min_mdi = min(mdi)
        max_mdi = max(mdi)
        smdi = (mdi - min_mdi) / (max_mdi - min_mdi)

        result_df[f"{key}_smdi"] = smdi
        result_df.to_csv(f"{output_path}/{key}.csv", index=False)


if __name__ == "__main__":
    mdi_compute("cleaned_csvs", "mdi_results")
    # smdi_compute("mdi_results", "smdi_results")
