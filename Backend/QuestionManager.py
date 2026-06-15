import json
import random

FilePath = "QuestionBank/Questions.json"


def SaveQuestion(QuestionData):

    try:

        with open(FilePath, "r") as File:

            Questions = json.load(File)

    except:

        Questions = []

    Questions.append(QuestionData)

    with open(FilePath, "w") as File:

        json.dump(
            Questions,
            File,
            indent=4
        )


def GetRandomQuestion(
    Topic,
    Difficulty,
    AskedQuestions
):

    try:

        with open(FilePath, "r") as File:

            Questions = json.load(File)

    except:

        return None

    FilteredQuestions = []

    for Question in Questions:

        if (

            Question["Topic"].lower()
            ==
            Topic.lower()

            and

            Question["Difficulty"].lower()
            ==
            Difficulty.lower()

            and

            Question["Question"]
            not in AskedQuestions
        ):

            FilteredQuestions.append(
                Question
            )

    if len(FilteredQuestions) == 0:

        return None

    return random.choice(
        FilteredQuestions
    )