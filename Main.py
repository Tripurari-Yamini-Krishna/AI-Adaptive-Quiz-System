from Models.AiEngine import GenerateQuestion

Topic = input("Enter Quiz Topic: ")
Difficulty = input("Enter Difficulty (Easy/Medium/Hard): ")

Question = GenerateQuestion(Topic, Difficulty)

print("\nGenerated Quiz Question:\n")
print(Question)

