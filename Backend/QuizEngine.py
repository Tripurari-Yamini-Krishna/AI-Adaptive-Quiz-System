from Models.AiEngine import GenerateQuestion

from Models.AdaptiveEngine import (
    GetAdaptiveDifficulty,
    GetNextDifficulty
)

from Reports.PerformanceTracker import (
    SavePerformance
)

from Models.ExplanationEngine import (
    GenerateExplanation
)

import matplotlib.pyplot as plt


def StartQuiz():

    Topic = input(
        "Enter Quiz Topic: "
    )

    Difficulty = input(
        "Enter Difficulty (Easy/Medium/Hard): "
    )

    Score = 0

    TotalQuestions = 5

    WeakTopics = []

    AskedQuestions = []

    Attempts = []

    Scores = []

    for QuestionNumber in range(
        1,
        TotalQuestions + 1
    ):

        print(
            f"\n========== Question {QuestionNumber} =========="
        )

        QuestionData = GenerateQuestion(
            Topic,
            Difficulty,
            AskedQuestions
        )

        AskedQuestions.append(
            QuestionData["Question"]
        )

        print(
            f"\nQuestion:\n{QuestionData['Question']}"
        )

        print("\nOptions:")

        for Key, Value in (
            QuestionData["Options"].items()
        ):

            print(f"{Key}) {Value}")

        UserAnswer = input(
            "\nEnter Your Answer (A/B/C/D): "
        ).upper()

        CorrectAnswer = (
            QuestionData["CorrectAnswer"]
            .strip()
            .upper()
        )

        if UserAnswer == CorrectAnswer:

            print(
                "\nCorrect Answer 🎉"
            )

            Score += 1

            Difficulty = (
                GetNextDifficulty(
                    Difficulty,
                    True
                )
            )

        else:

            print(
                "\nWrong Answer ❌"
            )

            print(
                f"\nCorrect Answer Was: {CorrectAnswer}"
            )

            WeakTopics.append(
                Topic
            )

            Difficulty = (
                GetNextDifficulty(
                    Difficulty,
                    False
                )
            )

        print("\nExplanation:")

        print(
            QuestionData["Explanation"]
        )

        CurrentPercentage = (
            Score / QuestionNumber
        ) * 100

        Attempts.append(
            QuestionNumber
        )

        Scores.append(
            CurrentPercentage
        )

    Percentage = (
        Score / TotalQuestions
    ) * 100

    print(
        "\n========== FINAL RESULT =========="
    )

    print(
        f"\nFinal Score: {Score}/{TotalQuestions}"
    )

    print(
        f"Percentage: {Percentage}%"
    )

    if Percentage >= 80:

        print(
            "Excellent Performance 🔥"
        )

    elif Percentage >= 50:

        print(
            "Good Job 😌"
        )

    else:

        print(
            "Needs Improvement 📚"
        )

    RecommendedDifficulty = (
        GetAdaptiveDifficulty(
            Percentage
        )
    )

    print(
        f"\nRecommended Difficulty Level: {RecommendedDifficulty}"
    )

    SavePerformance(
        Topic,
        Score,
        TotalQuestions,
        Percentage
    )

    plt.plot(
        Attempts,
        Scores,
        marker="o"
    )

    plt.xlabel(
        "Question Number"
    )

    plt.ylabel(
        "Current Percentage"
    )

    plt.title(
        "Live Quiz Performance"
    )

    plt.grid(True)

    plt.show()

    if len(WeakTopics) > 0:

        print(
            "\nWeak Topics Detected:"
        )

        for WeakTopic in set(
            WeakTopics
        ):

            print(
                f"\nTopic: {WeakTopic}"
            )

            print(
                "\nAI Explanation:"
            )

            try:

                Explanation = (
                    GenerateExplanation(
                        WeakTopic
                    )
                )

                print(Explanation)

            except:

                print("Explanation Service Busy Right Now ⚠️")

                