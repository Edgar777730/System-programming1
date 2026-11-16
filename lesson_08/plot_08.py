"""Задание 8. Графики по замерам из measure_08.py.

Запуск из корня репозитория, после measure_08.py:

    python lesson_08/plot_08.py

Картинки сохраняются в lesson_08/screens/ поверх заглушек.
"""

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).parent
SCREENS = HERE / "screens"


def read_results():
    """Прочитать results_08.csv: {имя функции: ([n, ...], [секунды, ...])}."""
    series = defaultdict(lambda: ([], []))
    with open(HERE / "results_08.csv", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            sizes, times = series[row["function"]]
            sizes.append(int(row["n"]))
            times.append(float(row["seconds"]))
    return series


def read_k_results():
    """Прочитать results_08_k.csv: ([k, ...], [секунды, ...])."""
    ks, times = [], []
    with open(HERE / "results_08_k.csv", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            ks.append(int(row["k"]))
            times.append(float(row["seconds"]))
    return ks, times


def plot_linear(series):
    """График 1: время от n на обычных осях."""
    fig, ax = plt.subplots(figsize=(10, 6))
    for name, (sizes, times) in series.items():
        ax.plot(sizes, times, marker="o", label=name)
    ax.set_title("Время от размера входа")
    ax.set_xlabel("n, элементов")
    ax.set_ylabel("время, с")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.savefig(SCREENS / "01-lineinyi.png", dpi=120, bbox_inches="tight")
    plt.close(fig)


def plot_log_log(series):
    """График 2: те же линии, но обе оси логарифмические."""
    fig, ax = plt.subplots(figsize=(10, 6))
    for name, (sizes, times) in series.items():
        ax.plot(sizes, times, marker="o", label=name)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title("Время от размера входа (логарифмические оси)")
    ax.set_xlabel("n, элементов (log)")
    ax.set_ylabel("время, с (log)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.savefig(SCREENS / "02-log-log.png", dpi=120, bbox_inches="tight")
    plt.close(fig)


def plot_k(ks, times):
    """График 3: время window_sum_slices от k при постоянном n."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(ks, times, marker="o", color="tab:orange", label="window_sum_slices")
    ax.set_title("Время window_sum_slices от длины окна k (при n = 10 000)")
    ax.set_xlabel("k, длина окна")
    ax.set_ylabel("время, с")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.savefig(SCREENS / "03-ot-k.png", dpi=120, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    SCREENS.mkdir(exist_ok=True)
    plot_linear(read_results())
    plot_log_log(read_results())
    plot_k(*read_k_results())
    print("Графики сохранены в", SCREENS)
