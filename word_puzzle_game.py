import random

def shuffle(wrd):
    word = random.sample(wrd, k = len(wrd))
    return ' '.join(word)

def problemWord(word, score):
    problemword = shuffle(word)
    print()
    print("Arrange the letter from a valid word")
    print()
    print(problemword)
    print()
    userInput = input()
    if userInput.upper() == word:
        print()
        print("Correct")
        score += 1
    else:
        print()
        print("Wrong")
        score -= 1
    return score
def main():
    score = 0
    mylist = ['APPLE', 'BANANA', 'MANGO', 'PINEPLE', 'BEER']
    mylist = random.sample(mylist, k = len(mylist))
    for word in mylist:
        score = problemWord(word, score)
    print()
    print("Your net score is:",score)
    print()

main()
