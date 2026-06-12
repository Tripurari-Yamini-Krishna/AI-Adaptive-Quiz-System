from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

Client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def GenerateQuestion(topic, difficulty):

    Prompt = f"""
    Generate 1 multiple choice question on {topic}.

    Difficulty Level: {difficulty}

    Return in this format:

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

    return Response.text

