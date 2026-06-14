def GetAdaptiveDifficulty(Percentage):
    if Percentage >= 80:
        return "Hard"
    elif Percentage >= 50:
        return "Medium"
    else:
        return "Easy"

def GetNextDifficulty(CurrentDifficulty, IsCorrect):
    if CurrentDifficulty == "Easy":
        if IsCorrect:
            return "Medium"
        else:
            return "Easy"
    elif CurrentDifficulty == "Medium":
        if IsCorrect:
            return "Hard"
        else:
            return "Easy"
    elif CurrentDifficulty == "Hard":
        if IsCorrect:
            return "Hard"
        else:
            return "Medium"
    return "Easy"
