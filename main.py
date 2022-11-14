questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]


def new_game():
    play_again()
    gamelimit = 5
    attmeptlimit =15
    playagain = 'Y'
    while gamelimit > 0 and attmeptlimit > 0 :
        playagain = input('play again Y or N:')
        if playagain == 'Y':
            playagain = play_again()
            gamelimit -= 1
        elif playagain == 'N':
            break
        else:
            print('only Y and N allowed')
            attmeptlimit -= 1


def check_answer(answer, rightanswer):
    score = 0
    if answer == rightanswer:
        score += 1
    return score



def display_score(score):
    print('the score is:', score)

def isnotacceptable(answer):
    if answer in 'ABCD':
        return False
    else:
        return True

def play_again():
    question = ''
    rightanswer = ''
    count = 0
    score = 0
    for el in questions.keys():
        question = el
        rightanswer = questions[el]
        print(question)
        print('Options:', options[count])
        count +=1

        notacceptable = True
        limit = 4
        while notacceptable and limit > 0:
            answer = input('enter answer only A B C and D:')
            notacceptable = isnotacceptable(answer)
            limit -= 1
        score += check_answer(answer, rightanswer)
    display_score(score)



def main():
    new_game()

main()