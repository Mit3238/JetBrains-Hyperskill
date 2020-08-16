import random

print('H A N G M A N')
run = True
while run:
    bool3 = input('Type "play" to play the game, "exit" to quit: ')
    print()
    if bool3 == 'play':
        list1 = ['python', 'java', 'kotlin', 'javascript']
        luck = random.randint(0, len(list1) - 1)
        answer = list1[luck]

        guesses = ''
        lives = 8
        list2 = ['-' for i in range(len(answer))]
        str1 = ''
        for i in list2:
            str1 += i
        bool1 = False
        bool2 = False

        while lives > 0:
            print("\n", str1)
            guess = input("Input a letter: ")

            if len(guess) > 1:
                print('You should input a single letter')
                continue

            if not 96 < ord(guess[-1]) < 123:
                print('It is not an ASCII lowercase letter')
                continue

            for i in guesses:
                if i == guess[-1]:
                    print("You already typed this letter")
                    bool2 = True
                    continue

            if bool2:
                bool2 = False
                continue
            guesses += guess[-1]

            for i in range(len(answer)):
                if guess[-1] == answer[i]:
                    str1 = str1[:i] + answer[i] + str1[i + 1:]
                    bool1 = True

            if bool1 == False:
                lives -= 1
                print("No such letter in the word")
                continue

            bool1 = False
            number = 0
            for i in str1:
                if i != '-':
                    number += 1
            if number == len(str1):
                lives = -1

        if lives == -1:
            print('\n', str1)
            print('You guessed the word!')
            print('You survived!\n')

        else:
            print('You are hanged!\n')

    else:
        run = False
