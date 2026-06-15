def GetAdaptiveDifficulty(CurrentDifficulty, IsCorrect):

    DifficultyLevels = [
        "Easy",
        "Medium",
        "Hard"
    ]

    CurrentIndex = DifficultyLevels.index(
        CurrentDifficulty
    )

    if IsCorrect:

        if CurrentIndex < 2:

            return DifficultyLevels[
                CurrentIndex + 1
            ]

    else:

        if CurrentIndex > 0:

            return DifficultyLevels[
                CurrentIndex - 1
            ]

    return CurrentDifficulty

