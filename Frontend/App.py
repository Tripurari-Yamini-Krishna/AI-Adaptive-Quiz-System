import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from Models.AiEngine import (
    GenerateQuestion
)

from Backend.AdaptiveLogic import (
    GetAdaptiveDifficulty
)

st.set_page_config(
    page_title="AI Adaptive Quiz System",
    page_icon="🧠",
    layout="centered"
)

# =========================
# SESSION STATES
# =========================

if "QuestionData" not in st.session_state:
    st.session_state.QuestionData = None

if "Score" not in st.session_state:
    st.session_state.Score = 0

if "QuestionNumber" not in st.session_state:
    st.session_state.QuestionNumber = 1

if "TotalQuestions" not in st.session_state:
    st.session_state.TotalQuestions = 5

if "Answered" not in st.session_state:
    st.session_state.Answered = False

if "AskedQuestions" not in st.session_state:
    st.session_state.AskedQuestions = []

if "CurrentDifficulty" not in st.session_state:
    st.session_state.CurrentDifficulty = "Easy"

# =========================
# TITLE
# =========================

st.title("🧠 AI Adaptive Quiz System")

# =========================
# INPUTS
# =========================

Topic = st.text_input(
    "Enter Quiz Topic"
)

Difficulty = st.selectbox(

    "Select Starting Difficulty",

    [
        "Easy",
        "Medium",
        "Hard"
    ]
)

# =========================
# GENERATE QUESTION
# =========================

if st.button("Generate Question"):

    st.session_state.Score = 0

    st.session_state.QuestionNumber = 1

    st.session_state.AskedQuestions = []

    st.session_state.CurrentDifficulty = (
        Difficulty
    )

    QuestionData = GenerateQuestion(
        Topic,
        st.session_state.CurrentDifficulty,
        st.session_state.AskedQuestions
    )

    st.session_state.QuestionData = (
        QuestionData
    )

    st.session_state.Answered = False

    st.session_state.AskedQuestions.append(
        QuestionData["Question"]
    )

# =========================
# DISPLAY QUESTION
# =========================

if st.session_state.QuestionData is not None:

    QuestionData = (
        st.session_state.QuestionData
    )

    st.header(
        f"Question {st.session_state.QuestionNumber} / {st.session_state.TotalQuestions}"
    )

    st.subheader(
        f"Difficulty: {st.session_state.CurrentDifficulty}"
    )

    st.write(
        QuestionData["Question"]
    )

    # =========================
    # OPTIONS
    # =========================

    Options = QuestionData["Options"]

    UserAnswer = st.radio(

        "Choose Your Answer",

        [
            f"A) {Options['A']}",
            f"B) {Options['B']}",
            f"C) {Options['C']}",
            f"D) {Options['D']}"
        ]
    )

    SelectedAnswer = UserAnswer[0]

    # =========================
    # SUBMIT ANSWER
    # =========================

    if (
        st.button("Submit Answer")
        and
        not st.session_state.Answered
    ):

        st.session_state.Answered = True

        CorrectAnswer = (
            QuestionData["CorrectAnswer"]
            .strip()
            .upper()
        )

        if SelectedAnswer == CorrectAnswer:

            st.success(
                "Correct Answer 🎉"
            )

            st.session_state.Score += 1

            NewDifficulty = (
                GetAdaptiveDifficulty(
                    st.session_state.CurrentDifficulty,
                    True
                )
            )

        else:

            st.error(
                f"Wrong Answer ❌ Correct Answer Was: {CorrectAnswer}"
            )

            NewDifficulty = (
                GetAdaptiveDifficulty(
                    st.session_state.CurrentDifficulty,
                    False
                )
            )

        st.session_state.CurrentDifficulty = (
            NewDifficulty
        )

        st.info(
            f"Next Difficulty: {NewDifficulty}"
        )

        st.subheader(
            "Explanation"
        )

        st.write(
            QuestionData["Explanation"]
        )

    # =========================
    # NEXT QUESTION
    # =========================

    if st.session_state.Answered:

        if (
            st.session_state.QuestionNumber
            <
            st.session_state.TotalQuestions
        ):

            if st.button("Next Question"):

                st.session_state.QuestionNumber += 1

                NewQuestion = GenerateQuestion(
                    Topic,
                    st.session_state.CurrentDifficulty,
                    st.session_state.AskedQuestions
                )

                st.session_state.QuestionData = (
                    NewQuestion
                )

                st.session_state.AskedQuestions.append(
                    NewQuestion["Question"]
                )

                st.session_state.Answered = False

                st.rerun()

        else:

            st.success(
                "Quiz Completed 🎉"
            )

            st.subheader(
                "Final Score"
            )

            st.write(
                f"{st.session_state.Score} / {st.session_state.TotalQuestions}"
            )

            Percentage = (
                st.session_state.Score
                /
                st.session_state.TotalQuestions
            ) * 100

            st.write(
                f"Percentage: {Percentage:.2f}%"
            )

# =========================
# SIDEBAR
# =========================

st.sidebar.title("📊 Quiz Stats")

st.sidebar.write(
    f"Score: {st.session_state.Score}"
)

st.sidebar.write(
    f"Question: {st.session_state.QuestionNumber} / {st.session_state.TotalQuestions}"
)

st.sidebar.write(
    f"Current Difficulty: {st.session_state.CurrentDifficulty}"
)

