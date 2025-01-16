import pandas as pd
from matplotlib import pyplot as plt


def annotator(ax):

    # amide A
    ax.axvspan(3300, 3300, color="#c7e9c0")
    ax.text(3315, 80, "Amide A", rotation=90, fontsize=7)

    # amide B
    ax.axvspan(3100, 3100, color="#edf8e9")
    ax.text(3115, 80, "Amide B", rotation=90, fontsize=7)

    # #amide 1
    ax.axvspan(1600, 1690, color="#006d2c", alpha=0.55)
    ax.text(1655, 80, "Amide I", rotation=90, fontsize=7)

    # amide 2
    ax.axvspan(1480, 1575, color="#31a354", alpha=0.55)
    ax.text(1535, 80, "Amide II", rotation=90, fontsize=7)

    # amide 3
    ax.axvspan(1229, 1301, color="#74c476", alpha=0.55)
    ax.text(1275, 80, "Amide III", rotation=90, fontsize=7)

    # amide 4
    ax.axvspan(625, 767, color="#a1d99b", alpha=0.55)
    ax.text(710, 80, "Amide IV", rotation=90, fontsize=7)

    # # amide 5
    # ax.axvspan(640, 800, color="#f800a4", alpha=0.3)
    # ax.text(625, 83, "Amide V", rotation=90, fontsize=7)

    # # amide 6
    # ax.axvspan(537, 606, color="#f800a4", alpha=0.3)
    # ax.text(555, 83, "Amide VI", rotation=90, fontsize=7)

    # # amide 7
    # ax.axvspan(200, 200, color="#f800a4", alpha=0.3)
    # ax.text(185, 83, "Amide VII", rotation=90, fontsize=7)

    # x_axis must be inverted
    # source: https://sci-hub.se/https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-7270.2007.00320.x


if __name__ == "__main__":
    pass
