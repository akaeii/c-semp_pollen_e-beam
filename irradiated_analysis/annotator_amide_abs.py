import pandas as pd
from matplotlib import pyplot as plt

# source: https://sci-hub.se/https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-7270.2007.00320.x


def annotator_full(ax):
    ax.set(ylim=(0, 0.16))

    # amide A
    ax.axvspan(3300, 3300, color="#c7e9c0")
    ax.text(3285, 0.12, "Amide A", rotation=90, fontsize=7)
    ax.text(3290, 0.075, "NH Stretching", rotation=90, fontsize=5)

    # amide B
    ax.axvspan(3100, 3100, color="#edf8e9")
    ax.text(3085, 0.12, "Amide B", rotation=90, fontsize=7)
    ax.text(3090, 0.075, "NH Stretching", rotation=90, fontsize=5)

    # amide 1
    ax.axvspan(1600, 1690, color="#006d2c", alpha=0.55)
    ax.text(1635, 0.12, "Amide I", rotation=90, fontsize=7)
    ax.text(1640, 0.075, "C=O Stretching", rotation=90, fontsize=5)

    # amide 2
    ax.axvspan(1480, 1575, color="#31a354", alpha=0.55)
    ax.text(1515, 0.12, "Amide II", rotation=90, fontsize=7)
    ax.text(1520, 0.049, "CN Stretching, NH Bending", rotation=90, fontsize=5)

    # amide 3
    ax.axvspan(1229, 1301, color="#74c476", alpha=0.55)
    ax.text(1255, 0.12, "Amide III", rotation=90, fontsize=7)
    ax.text(1260, 0.049, "CN Stretching, NH Bending", rotation=90, fontsize=5)

    # amide 4
    ax.axvspan(625, 767, color="#a1d99b", alpha=0.55)
    ax.text(690, 0.12, "Amide IV", rotation=90, fontsize=7)
    ax.text(703, 0.0805, "OCN Bending", rotation=90, fontsize=5)

    # # amide 5
    # ax.axvspan(640, 800, color="#f800a4", alpha=0.3)
    # ax.text(625, 0.075, "Amide V", rotation=90, fontsize=7)

    # # amide 6
    # ax.axvspan(537, 606, color="#f800a4", alpha=0.3)
    # ax.text(555, 0.075, "Amide VI", rotation=90, fontsize=7)

    # # amide 7
    # ax.axvspan(200, 200, color="#f800a4", alpha=0.3)
    # ax.text(185, 0.075, "Amide VII", rotation=90, fontsize=7)


def annotator_zoom(ax):
    ax.set(ylim=(0, 0.055))
    ax.set(xlim=(1000, 2000))

    # amide 1
    ax.axvspan(1600, 1690, color="#006d2c", alpha=0.55)
    ax.text(1618, 0.048, "Amide I", fontsize=10)

    # amide 2
    ax.axvspan(1480, 1575, color="#31a354", alpha=0.55)
    ax.text(1497, 0.048, "Amide II", fontsize=10)

    # amide 3
    ax.axvspan(1229, 1301, color="#74c476", alpha=0.55)
    ax.text(1231, 0.048, "Amide III", fontsize=10)


if __name__ == "__main__":
    pass
