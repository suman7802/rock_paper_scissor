import random

smile = "\U0001f600 "
a = "You Got 1 Point!"
b = "Computer Got 1 Point!"
r = "Rock"
p = "Paper"
s = "scissor"

while True:
    EC = input("To start/continue press 1\nTO exit/stop press 0\n")
    if EC == '0':
        break
    elif EC == '1':
        chance = 0
        human_score = 0
        computer_score = 0
        while True:
            chance = chance + 1
            if chance > 3:
                if human_score == computer_score:
                    print("Game Over", "\nyour score", human_score, "\ncomputer score", computer_score)
                    break
                elif human_score > computer_score:
                    print(f"YOU WIN {smile}", "\nyour score", human_score, "\ncomputer score", computer_score)
                    break
                else:
                    print("YOU LOSE", "\nyour score", human_score, "\ncomputer score", computer_score)
                    break
            computer = random.randint(0, 2)
            A = computer
            option1 = ["Rock", "Paper", "scissor"]
            # print(option1[A])  # cheating
            human = int(input("1 for rock 2 for paper 3 for seasor "))
            B = human - 1
            option2 = ["Rock", "Paper", "scissor"]
            #  print(option2[B])  # print section human

            if option1[A] == option2[B]:
                print(f"TIE! ", "Computer:", option1[A])
                if chance < 3:
                    print("Try Again")
            elif option1[A] == r and option2[B] == p:
                print(a, "Computer:", option1[A])
                human_score = human_score + 1
            elif option1[A] == p and option2[B] == s:
                print(a, "Computer:", option1[A])
                human_score = human_score + 1
            elif option1[A] == s and option2[B] == r:
                print(a, "Computer:", option1[A])
                human_score = human_score + 1
            else:
                print(b, "Computer:", option1[A])
                computer_score = computer_score + 1
        continue
    else:
        print("INPUT ERROR")