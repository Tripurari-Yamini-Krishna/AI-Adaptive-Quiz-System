import json
from datetime import datetime

def SavePerformance(Topic, Score, TotalQuestions, Percentage):
    FilePath = "Reports/PerformanceData.json"
    try:
        with open(FilePath, "r") as File:
            PerformanceData = json.load(File)
    except:
        PerformanceData = []
    PerformanceData.append({
        "Topic": Topic,
        "Score": Score,
        "TotalQuestions": TotalQuestions,
        "Percentage": Percentage,
        "Date": str(datetime.now())
    })
    with open(FilePath, "w") as File:
        json.dump(PerformanceData, File, indent=4)
        