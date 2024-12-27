import pandas as pd
from matplotlib import pyplot as plt


def annotator(ax):

    ax.set(xlim=(600, 4000))

    # # single bond region
    # ax.axvspan(2500, 4000, color="yellow", alpha=0.2)
    # ax.text(3450, 101.5, "Single Bond Region", fontsize=8)

    # # triple bond region
    # ax.axvspan(2000, 2500, color="blue", alpha=0.2)
    # ax.text(2470, 101.5, "Triple Bond Region", fontsize=8)

    # # double bond region
    # ax.axvspan(1500, 2000, color="green", alpha=0.2)
    # ax.text(1970, 101.5, "Double Bond Region", fontsize=8)

    # # fingerprint region
    # ax.axvspan(600, 1500, color="grey", alpha=0.15)
    # ax.text(1250, 101.5, "Fingerprint Region", fontsize=8)

    # #amide 1
    ax.axvspan(1630, 1635, color="#6817c5", alpha=0.3)
    ax.text(1650, 83, "Amide I", rotation=90, fontsize=7, fontweight="bold")

    # amide 2
    ax.axvspan(1517, 1526, color="#e76f51", alpha=0.5)
    ax.text(1541, 83, "Amide II", rotation=90, fontsize=7, fontweight="bold")

    # amide 3
    ax.axvspan(1230, 1238, color="#f800a4", alpha=0.3)
    ax.text(1253, 83, "Amide III", rotation=90, fontsize=7, fontweight="bold")


if __name__ == "__main__":
    spec = pd.read_csv("sample_input.csv", names=["wave_no", "abs"])
    spec["trans"] = (10 ** -spec["abs"]) * 100

    fig1, axis = plt.subplots(1, 1, figsize=(10, 5))

    axis.plot(spec["wave_no"], spec["trans"])

    annotator(axis)
    axis.invert_xaxis()

    axis.set_title("ANNOTATED AUTOMATICALLYYY", pad=30)

    fig1.tight_layout()
    plt.show()
