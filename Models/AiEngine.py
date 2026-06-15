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
        Difficulty,
        AskedQuestions
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

    Previously Asked Questions:
    {AskedQuestions}

    IMPORTANT RULES:
    - Do NOT repeat previous questions
    - Do NOT ask similar questions
    - Avoid common beginner questions repeatedly
    - Make each question fresh and different
    - All 4 options must contain actual text
    - Return ONLY valid JSON
    - No markdown
    - No code blocks

    JSON Format:

    {{
        "Question": "question here",

        "Options": {{
            "A": "option text",
            "B": "option text",
            "C": "option text",
            "D": "option text"
        }},

        "CorrectAnswer": "A",

        "Explanation": "explanation here"
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
            "\nAI Returned Invalid JSON ⚠️"
        )

        Data = {

            "Question":
            "What does print() do in Python?",

            "Options": {

                "A": "Takes input",

                "B": "Prints output",

                "C": "Creates loops",

                "D": "Deletes variables"
            },

            "CorrectAnswer": "B",

            "Explanation":
            "print() displays output on the screen."
        }

    QuestionData = {

        "Topic": Topic,

        "Difficulty": Difficulty,

        "Question": Data["Question"],

        "Options": Data["Options"],

        "CorrectAnswer": Data["CorrectAnswer"],

        "Explanation": Data["Explanation"]
    }

    SaveQuestion(
        QuestionData
    )

    return QuestionData

