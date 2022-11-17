from random import randrange

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is a tribute to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]


def new_game():
    play_again()
    game_limit = 5
    attempt_limit = 3

    while game_limit > 0 and attempt_limit > 0:
        again = input('play again Y or N:')
        if again == 'Y':
            play_again()
            game_limit -= 1
        elif again == 'N':
            break
        else:
            print('only Y and N allowed')
            attempt_limit -= 1


def check_answer(answer, right_answer):
    score = 0
    if answer == right_answer:
        score += 1
    return score


def display_score(score):
    print('the score is:', score)


def is_not_acceptable(answer):
    if answer in 'ABCD':
        return False
    else:
        return True


def add_question():
    question = input('Enter new question:')
    answer = input('Enter the correct answer:')

    list_of_wrong_answers = []
    for i in range(3):
        list_of_wrong_answers.append(input('Enter wrong answer:'))

    right_index = randrange(1, 3)
    print(right_index)
    letter_options = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
    right_letter = letter_options[right_index]
    questions[question] = right_letter
    letter_options[right_index] = ' '

    new_list_of_answers = []

    for el in letter_options.values():
        if el == ' ':
            new_list_of_answers.append(right_letter + '.' + answer)
            print(right_letter)
        else:
            new_list_of_answers.append(el + '.' + list_of_wrong_answers.pop())
            print(el)

    options.append(new_list_of_answers)

    print(questions, options)
    new_game()


def play_again():
    count = 0
    score = 0
    for el in questions.keys():
        question = el
        right_answer = questions[el]
        print(question)
        print('Options:', options[count])
        count += 1

        not_acceptable = True
        limit = 4
        answer = ''
        while not_acceptable and limit > 0:
            answer = input('enter answer only A B C and D:')
            not_acceptable = is_not_acceptable(answer)
            limit -= 1
        score += check_answer(answer, right_answer)
    display_score(score)


def main():
    count = 5
    while count > 0:
        option = input('Play game or Add questions? enter P or A')
        if option == 'P':
            new_game()
            count = 0
        elif option == 'A':
            add_question()
            count = 0
        else:
            print('enter P or A only')
            count -= 1
            continue

main()
