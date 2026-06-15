import json
def DetectWeakTopics():
    FilePath = "Reports/PerformanceData.json"
    try:
        with open(FilePath, "r") as File:
            PerformanceData = json.load(File)
    except:
        return []
    WeakTopics = []
    for Entry in PerformanceData:
        Topic = Entry["Topic"]
        Percentage = Entry["Percentage"]
        if Percentage < 50:
            WeakTopics.append(Topic)
    WeakTopics = list(set(WeakTopics))
    return WeakTopics
