import json

def SaveQuestion(QuestionData):
    FilePath = "QuestionBank/Questions.json"
    try:
        with open(FilePath, "r") as File:
            Questions = json.load(File)
    except:
        Questions = []
    Questions.append(QuestionData)
    with open(FilePath, "w") as File:
        json.dump(Questions, File, indent=4)

def LoadQuestions(Topic, Difficulty):
    FilePath = "QuestionBank/Questions.json"
    try:
        with open(FilePath, "r") as File:
            Questions = json.load(File)
    except:
        return []
    FilteredQuestions = []
    for Question in Questions:
        if (
            Question["Topic"].lower() == Topic.lower()
            and
            Question["Difficulty"].lower() == Difficulty.lower()
        ):
            FilteredQuestions.append(Question)
    return FilteredQuestions

