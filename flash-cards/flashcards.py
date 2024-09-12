# flashcards.py

# import the json module from python3
import json

# open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)

# initialize total as the length of the cards array
total = len(data["cards"])
#initialize score as 0
score = 0

for i in data["cards"]:
    guess = input(i["q"] + ">")

    if guess == i["a"]:
        #increment score up one
        score += 1
        #interpolate score and total into the response
        print(f"Correct! Currect score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")


print(f"Thanks for playing! You scored: {score} out of {total} correct!")