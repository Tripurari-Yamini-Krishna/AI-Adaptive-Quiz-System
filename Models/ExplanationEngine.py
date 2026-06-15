from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
Client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def GenerateExplanation(topic):
    Prompt = f"""
    Explain the topic {topic} in a simple and beginner friendly way.
    Give examples if possible.
    """
    try:
        Response = Client.models.generate_content(
            model="gemini-2.5-flash",
            contents=Prompt
        )
        return Response.text
    except Exception as Error:
        return f"""
AI Explanation Could Not Be Generated Right Now.
Reason:
{Error}
Try Again Later.
"""