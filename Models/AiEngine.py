from google import genai
from dotenv import load_dotenv
from Backend.QuestionManager import (
    SaveQuestion,
    GetRandomQuestion
)

import os
import random

load_dotenv()

Client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def GenerateQuestion(Topic, Difficulty):

    SavedQuestion = GetRandomQuestion(Topic, Difficulty)

    if SavedQuestion is not None:

        print("\nLoaded Question From Question Bank 📚")

        return SavedQuestion

    Prompt = f"""
    Generate 1 UNIQUE multiple choice question on {Topic}.

    Difficulty Level: {Difficulty}

    IMPORTANT:
    - Make the question different every time
    - Avoid repeating common questions
    - Keep it beginner friendly if easy
    - Return ONLY in this exact format

    Question:
    Options:
    A)
    B)
    C)
    D)

    Correct Answer:
    Explanation:
    """

    Response = Client.models.generate_content(
        model="gemini-2.5-flash",
        contents=Prompt
    )

    Text = Response.text

    Lines = Text.split("\n")

    Question = ""
    Options = []
    CorrectAnswer = ""
    Explanation = ""

    ExplanationMode = False

    for Line in Lines:

        Line = Line.strip()

        if Line.startswith("Question:"):

            Question = Line.replace("Question:", "").strip()

        elif (
            Line.startswith("A)")
            or Line.startswith("B)")
            or Line.startswith("C)")
            or Line.startswith("D)")
        ):

            Options.append(Line)

        elif Line.startswith("Correct Answer:"):

            CorrectAnswer = (
                Line.replace("Correct Answer:", "")
                .strip()
                .replace(")", "")
            )

        elif Line.startswith("Explanation:"):

            ExplanationMode = True

            Explanation = (
                Line.replace("Explanation:", "")
                .strip()
            )

        elif ExplanationMode:

            Explanation += " " + Line

    QuestionData = {
        "Question": Question,
        "Options": Options,
        "CorrectAnswer": CorrectAnswer,
        "Explanation": Explanation
    }

    SaveQuestion(
        Topic,
        Difficulty,
        QuestionData
    )

    return QuestionData

