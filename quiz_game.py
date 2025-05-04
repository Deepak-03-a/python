# python quiz game 

questions = ("How many overs are played in ODI cricket ?",
            "Who is the prime minister of India ?",
            "Who is the cheif Minister of A.P ?",
            "India got Independence in the which year ?",
            "Who is the Captain of Indain Hockey team ?")

options = (("A.49", "B.50", "C.20", "D.90"),
           ("A.Modi", "B.Chandra babu", "C.Deepak", "D.You"),
           ("A.Pavan kalyan", "B.your daddy", "C.Chanrda babu", "D.Jagan"),
           ("A.1942", "B.1943", "C.1944", "D.1945"),
           ("A.Harmanpreet singh", "B.Harbajan Singh", "C.Yuvaraj singh", "D.Manpreet singh") )

answers = ("A", "D", "D", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
        
    guess = input("Enter(A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct annswer ")
    question_num += 1
    
print("-------------------------") 
print("         RESULTS         ")  
print("-------------------------") 

print("answers: ", end="")
for answer in answers:
    print(answer , end=" ")
print()


print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/ len(questions) * 100)
print(f"Your score is: {score}%")
    