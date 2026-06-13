from Models.AiEngine import GenerateQuestion
from Models.ExplanationEngine import GenerateExplanation
from Reports.PerformanceTracker import SavePerformance
from Reports.AnalyticsDashboard import GenerateDashboard


def UpdateDifficulty(CurrentDifficulty, IsCorrect):

    DifficultyLevels = ["Easy", "Medium", "Hard"]

    CurrentIndex = DifficultyLevels.index(CurrentDifficulty)

    if IsCorrect:

        if CurrentIndex < 2:

            return DifficultyLevels[CurrentIndex + 1]

    else:

        if CurrentIndex > 0:

            return DifficultyLevels[CurrentIndex - 1]

    return CurrentDifficulty


def StartQuiz():

    Topic = input("Enter Quiz Topic: ")

    Difficulty = input("Enter Difficulty (Easy/Medium/Hard): ")

    Score = 0

    TotalQuestions = 5

    WeakTopics = []

    for QuestionNumber in range(1, TotalQuestions + 1):

        print(f"\n========== Question {QuestionNumber} ==========")

        QuestionData = GenerateQuestion(Topic, Difficulty)

        print("\nQuestion:")

        print(QuestionData["Question"])

        print("\nOptions:")

        for Option in QuestionData["Options"]:

            print(Option)

        UserAnswer = input("\nEnter Your Answer (A/B/C/D): ").upper()

        CorrectAnswer = QuestionData["CorrectAnswer"]

        if UserAnswer == CorrectAnswer:

            print("\nCorrect Answer 🎉")

            Score += 1

            Difficulty = UpdateDifficulty(Difficulty, True)

            print(f"Difficulty Increased To: {Difficulty}")

        else:

            print("\nWrong Answer ❌")

            print(f"\nCorrect Answer Was: {CorrectAnswer}")

            WeakTopics.append(Topic)

            Difficulty = UpdateDifficulty(Difficulty, False)

            print(f"Difficulty Decreased To: {Difficulty}")

        print("\nExplanation:")

        print(QuestionData["Explanation"])

    Percentage = (Score / TotalQuestions) * 100

    print("\n========== FINAL RESULT ==========")

    print(f"\nFinal Score: {Score}/{TotalQuestions}")

    print(f"Percentage: {Percentage}%")

    if Percentage >= 80:

        print("Excellent Performance 🔥")

        RecommendedDifficulty = "Hard"

    elif Percentage >= 50:

        print("Good Job 👍")

        RecommendedDifficulty = "Medium"

    else:

        print("Needs Improvement 📚")

        RecommendedDifficulty = "Easy"

    print(f"\nRecommended Difficulty Level: {RecommendedDifficulty}")

    SavePerformance(
        Topic,
        Score,
        TotalQuestions,
        Percentage
    )

    if len(WeakTopics) > 0:

        print("\nWeak Topics Detected:")

        for WeakTopic in set(WeakTopics):

            print(f"\nTopic: {WeakTopic}")

            print("\nAI Explanation:")

            Explanation = GenerateExplanation(WeakTopic)

            print(Explanation)

    GenerateDashboard()

