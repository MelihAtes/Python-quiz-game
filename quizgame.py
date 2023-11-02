questions = ("Who is the author of the book '1984'?", 
             "What is the formula of the Pythagorean Theorem?", 
             "What does 'E' represent in Albert Einstein's famous equation 'E = mc^2'?", 
             "What is the scientific name of the human species?", 
             "How many elements are in the periodic table?")

             

options = (("A. Aldous Huxley" , "B. Stephen Edwin King", "C. George Orwell", "D. Antoine de Saint-Exupéry", "E. Yuval Noah Harari "), 
           ("A. i² = −1", "B. x_(n+1)=3.95[x(n)][1-x(n)]", "C. ΔU = Q - W", "D. c^2 = a^2 + b^2", "E. F = G * (m1 * m2) / r^2"), 
           ("A. Electron", "B. Environment", "C. Entropi", "D. Euler's Number", "E. Energy"), 
           ("A. Homo Erectus", "B. Homo Sapiens Sapiens", "C. Greg", "D. Multicellular Organism", "E. Destroyer of Species"), 
           ("A. 118", "B. 119", "C. 120", "D. 98327732", "E. 42"))

answers = ("C", "D", "E", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("enter (A, B, C, D, E): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else: 
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1 

print("-----------")
print("  Results  ")
print("-----------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"final score: {score}%")