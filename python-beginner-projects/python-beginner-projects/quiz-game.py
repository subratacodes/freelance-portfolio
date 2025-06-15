# Quiz Game
score = 0

answer1 = input("What is the capital of India? ")
if answer1.lower() == "delhi":
    score += 1

answer2 = input("Who is the CEO of Tesla? ")
if answer2.lower() == "elon musk":
    score += 1

print("You got", score, "out of 2!")
