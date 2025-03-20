import pandas as pd
from matplotlib import pyplot as plt


def annotator(ax):
    ax.set(ylim=(70, 105))

    # amide A
    ax.axvspan(3300, 3300, color="#c7e9c0")
    ax.text(3315, 81.5, "Amide A", rotation=90, fontsize=7)
    ax.text(3310, 74, "NH Stretching", rotation=90, fontsize=5)

    # amide B
    ax.axvspan(3100, 3100, color="#edf8e9")
    ax.text(3115, 81.5, "Amide B", rotation=90, fontsize=7)
    ax.text(3110, 74, "NH Stretching", rotation=90, fontsize=5)

    # #amide 1
    ax.axvspan(1600, 1690, color="#006d2c", alpha=0.55)
    ax.text(1655, 81.5, "Amide I", rotation=90, fontsize=7)
    ax.text(1650, 74, "C=O Stretching", rotation=90, fontsize=5)

    # amide 2
    ax.axvspan(1480, 1575, color="#31a354", alpha=0.55)
    ax.text(1535, 81.5, "Amide II", rotation=90, fontsize=7)
    ax.text(1530, 71.5, "CN Stretching, NH Bending", rotation=90, fontsize=5)

    # amide 3
    ax.axvspan(1229, 1301, color="#74c476", alpha=0.55)
    ax.text(1275, 81.5, "Amide III", rotation=90, fontsize=7)
    ax.text(1270, 71.5, "CN Stretching, NH Bending", rotation=90, fontsize=5)

    # amide 4
    ax.axvspan(625, 767, color="#a1d99b", alpha=0.55)
    ax.text(710, 81.5, "Amide IV", rotation=90, fontsize=7)
    ax.text(710, 74, "OCN Bending", rotation=90, fontsize=5)

    # # amide 5
    # ax.axvspan(640, 800, color="#f800a4", alpha=0.3)
    # ax.text(625, 83, "Amide V", rotation=90, fontsize=7)

    # # amide 6
    # ax.axvspan(537, 606, color="#f800a4", alpha=0.3)
    # ax.text(555, 83, "Amide VI", rotation=90, fontsize=7)

    # # amide 7
    # ax.axvspan(200, 200, color="#f800a4", alpha=0.3)
    # ax.text(185, 83, "Amide VII", rotation=90, fontsize=7)

    # source: https://sci-hub.se/https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-7270.2007.00320.x


if __name__ == "__main__":
    pass
