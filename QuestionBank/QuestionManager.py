import json
import os
import random


def GetFilePath(Topic, Difficulty):

    return f"QuestionBank/{Topic}_{Difficulty}.json"


def LoadQuestions(Topic, Difficulty):

    FilePath = GetFilePath(Topic, Difficulty)

    if not os.path.exists(FilePath):

        return []

    with open(FilePath, "r") as File:

        return json.load(File)


def SaveQuestion(Topic, Difficulty, QuestionData):

    Questions = LoadQuestions(Topic, Difficulty)

    Questions.append(QuestionData)

    FilePath = GetFilePath(Topic, Difficulty)

    with open(FilePath, "w") as File:

        json.dump(Questions, File, indent=4)


def GetRandomQuestion(Topic, Difficulty):

    Questions = LoadQuestions(Topic, Difficulty)

    if len(Questions) == 0:

        return None

    return random.choice(Questions)

