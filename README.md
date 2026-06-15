AI Adaptive Quiz System

This project is an AI-powered quiz app built with Python and the Gemini API. It creates quiz questions on the fly, adapts to how you’re doing, keeps track of your stats, saves your quiz history, and spots weak topics so you can improve.


Features

- Uses Gemini API to generate questions
- Changes difficulty based on how well you’re performing
- Easy, Medium, and Hard question levels
- Keeps track of your results and progress
- Highlights topics you need to work on
- Explains answers using AI
- Stores questions in a bank
- Avoids repeating questions you’ve already seen
- Visualizes your results with Matplotlib
- Clean, modular design to keep things organized


Technologies Used

- Python
- Gemini API
- JSON
- Matplotlib
- Git & GitHub


Project Structure

AI-Adaptive-Quiz-System/
├── Backend/
│   ├── AdaptiveLogic.py
│   ├── QuestionManager.py
│   └── QuizEngine.py
├── Database/
│   └── PerformanceData.json
├── Models/
│   ├── AiEngine.py
│   ├── AnalyticsEngine.py
│   └── ExplanationEngine.py
├── QuestionBank/
│   └── Questions.json
├── Reports/
│   ├── AnalyticsDashboard.py
│   ├── PerformanceChart.py
│   └── PerformanceTracker.py
├── Main.py
├── README.md
└── Requirements.txt


How to Install

1. Clone the repository:
   git clone https://github.com/your-username/AI-Adaptive-Quiz-System.git
2. Open the project folder:
   cd AI-Adaptive-Quiz-System
3. Create a virtual environment:
   python -m venv Venv
4. Activate the virtual environment:
   On Windows:
       Venv\Scripts\activate
   On Mac/Linux:
       source Venv/bin/activate
5. Install the required packages:
   pip install -r Requirements.txt
Set Environment Variables
Make a `.env` file in the root folder and add your Gemini API key:
GEMINI_API_KEY=your_api_key_here
Run the Project
Run the main file:
python Main.py


How the Adaptive Difficulty Works

- High score, You get harder questions.
- Average score, Medium difficulty.
- Low score, The app gives you easier questions.


What’s Next
- A web interface
- User accounts and login
- Leaderboard
- Database integration
- Timed quizzes
- Deeper analytics


Author
Tripurari Yamini Krishna