import json
import os

FilePath = "Database/PerformanceData.json"

def SavePerformance(
    Topic,
    Score,
    TotalQuestions,
    Percentage
):

    PerformanceData = []

    if os.path.exists(FilePath):

        with open(FilePath, "r") as File:

            try:

                PerformanceData = json.load(File)

            except:

                PerformanceData = []

    AttemptData = {
        "Topic": Topic,
        "Score": Score,
        "TotalQuestions": TotalQuestions,
        "Percentage": Percentage
    }

    PerformanceData.append(AttemptData)

    with open(FilePath, "w") as File:

        json.dump(PerformanceData, File, indent=4)

    print("\nPerformance Saved Successfully")

