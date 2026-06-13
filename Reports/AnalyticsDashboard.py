import json
import matplotlib.pyplot as plt


def GenerateDashboard():

    FilePath = "Reports/PerformanceData.json"

    try:

        with open(FilePath, "r") as File:

            PerformanceData = json.load(File)

    except:

        print("No Performance Data Found")

        return

    Attempts = []
    Percentages = []

    Count = 1

    for Entry in PerformanceData:

        Attempts.append(f"Attempt {Count}")

        Percentages.append(Entry["Percentage"])

        Count += 1

    plt.figure(figsize=(8, 5))

    plt.plot(Attempts, Percentages, marker="o")

    plt.title("Quiz Performance Analytics")

    plt.xlabel("Attempts")

    plt.ylabel("Percentage Score")

    plt.ylim(0, 100)

    plt.grid(True)

    plt.savefig("Reports/PerformanceChart.png")

    plt.show()
    