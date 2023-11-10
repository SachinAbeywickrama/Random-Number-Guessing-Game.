import random

def start_again():
    again2 = input("Do you want to play again : ")
    print()
    if again2 == 'yes':
        point = 100
        print("___________________________________________________________________________________________________")
        print()
        print(f'Attempt                 Guess                     Results')
        print()
        print("___________________________________________________________________________________________________")
        return point
    elif again2 == 'no':
        exit()
    else:
        print("Invalid Response!!")

num_list = [1, 2, 3, 4, 5, 6]
random_list = random.sample(num_list, 4)

print()
Name = input("Enter your Name : ")

print()
print("--------------------------------- Hi", "<", Name, ">", " Welcome to GameInt -------------------------------")
print()
print("Number to Guess - XXXX")
print(f'                                                              Colour mapping:')
print(f'                                                                 1-White 2-Blue 3-Red')
print(f'                                                                 4-Yellow 5-Green 6-Purple')
print()
print(f'Attempt                      Guesses                        Results')
print("___________________________________________________________________________________________________")
print()

count = 1
point = 0

while count < 9:
    try:
        G1, G2, G3, G4 = map(int, input(f'{count}                  > ').split())

        if any(G > 6 for G in [G1, G2, G3, G4]):
            print("\n                                          Invalid colour code\n")
            continue

        Guess_list = [G1, G2, G3, G4]

        output1 = "1" if Guess_list[0] == random_list[0] else "0" if Guess_list[0] in random_list else "."
        output2 = "1" if Guess_list[1] == random_list[1] else "0" if Guess_list[1] in random_list else "."
        output3 = "1" if Guess_list[2] == random_list[2] else "0" if Guess_list[2] in random_list else "."
        output4 = "1" if Guess_list[3] == random_list[3] else "0" if Guess_list[3] in random_list else "."

        print(f'                                      {output1} {output2}')
        print(f'                                      {output3} {output4}')
        print("___________________________________________________________________________________________________")

        count += 1

        point += output1.count("1") + output2.count("1") + output3.count("1") + output4.count("1")

        print(f"                                                                      You have scored {point} points")
        print("\n\n___________________________________________________________________________________________________")
        print()

        if Guess_list == random_list:
            count = 1
            print("                             Congratulations!!!! You have won the game....")
            print(f'                                         You Got {point} points.')
            num_list = [1, 2, 3, 4, 5, 6]
            random_list = random.sample(num_list, 4)
            point = start_again()

        if all(item == 0 for item in Guess_list):
            print("                             You have ended the game!!!")
            print()
            num_list = [1, 2, 3, 4, 5, 6]
            random_list = random.sample(num_list, 4)
            point = start_again()

        if count > 8:
            count = 1
            print("\n YOU LOSE THE GAME!! \n")
            num_list = [1, 2, 3, 4, 5, 6]
            random_list = random.sample(num_list, 4)
            point = start_again()

    except ValueError:
        print(" Enter valid numbers ")
        print("____________________________________________________________________________________________")
        count += 1
        if count > 8:
            print("\n YOU LOSE THE GAME!! \n")
            num_list = [1, 2, 3, 4, 5, 6]
            random_list = random.sample(num_list, 4)
            point = start_again()
            count = 1
