def GetAdaptiveDifficulty(Percentage):
    if Percentage >= 80:
        return "Hard"
    elif Percentage >= 50:
        return "Medium"
    else:
        return "Easy"
    