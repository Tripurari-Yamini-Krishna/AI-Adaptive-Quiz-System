from google import genai
from dotenv import load_dotenv

from Backend.QuestionManager import (
    SaveQuestion,
    GetRandomQuestion
)

import os
import json

load_dotenv()

Client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def GenerateQuestion(
    Topic,
    Difficulty,
    AskedQuestions=[]
):

    SavedQuestion = GetRandomQuestion(
        Topic,
        Difficulty
    )

    if (
        SavedQuestion is not None
        and
        SavedQuestion["Question"]
        not in AskedQuestions
    ):

        print(
            "\nLoaded Question From Question Bank 📚"
        )

        return SavedQuestion

    Prompt = f"""
    Generate 1 UNIQUE multiple choice question.

    Topic: {Topic}

    Difficulty: {Difficulty}

    Return ONLY valid JSON.

    Example format:

    {{
        "Question": "What is Python?",
        "Options": {{
            "A": "A snake",
            "B": "A programming language",
            "C": "A game",
            "D": "A browser"
        }},
        "CorrectAnswer": "B",
        "Explanation": "Python is a programming language."
    }}
    """

    Response = Client.models.generate_content(
        model="gemini-2.5-flash",
        contents=Prompt
    )

    Text = Response.text.strip()

    Text = (
        Text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:

        Data = json.loads(Text)

    except:

        print(
            "\nAI Returned Invalid Format ⚠️"
        )

        return {
            "Topic": Topic,
            "Difficulty": Difficulty,
            "Question": "Fallback Question: What does print() do in Python?",
            "Options": {
                "A": "Takes input",
                "B": "Prints output",
                "C": "Creates loops",
                "D": "Deletes variables"
            },
            "CorrectAnswer": "B",
            "Explanation": "print() displays output."
        }

    QuestionData = {

        "Topic": Topic,

        "Difficulty": Difficulty,

        "Question": Data["Question"],

        "Options": Data["Options"],

        "CorrectAnswer": Data["CorrectAnswer"],

        "Explanation": Data["Explanation"]
    }

    SaveQuestion(QuestionData)

    return QuestionData