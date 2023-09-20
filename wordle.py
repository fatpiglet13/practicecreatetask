answer = "carat"
guess = input("Guess a 5 letter word ")

print(guess)

def checkletter(letter, answer):
    if letter in answer:
        if letter == answer[0]:
            return "Green"
        else:
            return "Yellow"
    else:
        return "Grey"\

data = ""
for letter in guess:
    data += checkletter(letter, answer)
print(data)
