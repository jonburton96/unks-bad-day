print(r'''
                             000      00
                           0000000   0000
              0      00  00000000000000000
            0000 0  000000000000000000000000       0
         000000000000000000000000000000000000000 000
        0000000000000000000000000000000000000000000000
    000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000
              / / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / /
          / / / / / / / / / / / / / /
          / / / / / / / / / / / / /
        / / / / / / / / / / / /
        / / / / / / / / / / /

         ...........IT'S RAINING AGAIN.
''')
import time

while True:
    print("UNK'S BAD DAY")
    time.sleep(2)
    print()

    print("Mechanic: Yeah man, that's gonna run you bout $845..")
    time.sleep(2)

    print("What do you do?")
    time.sleep(2)

    choice0 = input("1: Pay the mechanic\n2: Argue the price\n3: Leave\nChoice: ")

    if choice0 == "1":
        print()
        print("Mechanic: Card not going through, boss man")
        time.sleep(2)

        print("Unk: Just run it again")
        time.sleep(2)

        print("Mechanic: It's coming back insufficient funds, boss man.")
        time.sleep(2)

        print("*Unk checks his bank account...*")
        time.sleep(2)

        print("*Available balance: $8.42*")
        time.sleep(2)

        print("Unk: Ain't no way.....")
        time.sleep(2)

        print("GAME OVER")
        time.sleep(1)

        retry = input("1: Try Again\n2: Quit\nChoice: ")

        if retry == "1":
            continue
        else:
            break

    elif choice0 == "2":
        print()
        print("Unk: $845?!")
        time.sleep(2)

        print("Mechanic: Yep.")
        time.sleep(2)

        print("Unk: For what? You rebuilding the whole car?")
        time.sleep(2)

        print("Mechanic: No. Just fixing it.")
        time.sleep(2)

        print("Unk: Man, that's too much.")
        time.sleep(2)

        print("What do you do?")
        time.sleep(2)

        choice1 = input(
            "1: Keep Arguing\n"
            "2: Call Someone\n"
            "3: Leave\n"
            "4: Mention Warranty\n"
            "Choice: "
        )

        if choice1 == "1":
            print("Unk: Man, you got me messed up.")
            time.sleep(2)

            print("Mechanic: You asked me to fix it.")
            time.sleep(2)

            print("Unk: I asked you to fix it, not to buy the got dang car.")
            time.sleep(3)

            print("Mechanic: Then you might wanna start walking.")
            time.sleep(3)

            print("GAME OVER")
            time.sleep(1)

            retry = input("1: Try Again\n2: Quit\nChoice: ")

            if retry == "1":
                continue
            else:
                break

        elif choice1 == "2":
            print("Unk: Man, watch out...")
            time.sleep(2)

            print("*Phone dialing*")
            time.sleep(4)

            print(".....dialing.....")
            time.sleep(3)

            print("Unk: Hey man, I'm short on this car repair.")
            time.sleep(2)

            print("Friend: How much?")
            time.sleep(2)

            print("Unk: bout $845.")
            time.sleep(2)

            print("Friend: I can't help you with that.")
            time.sleep(2)

            print("Friend: I'ma pray for you.")
            time.sleep(2)

            print("*Call ends*")

            retry = input("1: Try Again\n2: Quit\nChoice: ")

            if retry == "1":
                continue
            else:
                break

        elif choice1 == "4":
            print("Unk: Hold up... what about the warranty?")
            time.sleep(2)

            print("Mechanic: You got a warranty?")
            time.sleep(2)

            print("Unk: I think so.")
            time.sleep(2)

            print("Mechanic: You think?")
            time.sleep(2)

            print("Unk: Man, I don't read all that paperwork.")
            time.sleep(2)

            print("Mechanic: So you don't know if you got one.")
            time.sleep(2)

            print("Unk: ...")
            time.sleep(2)

            print("Unk: Nah, I definitely got one.")
            time.sleep(2)

            print("*Mechanic checks the warranty*")
            time.sleep(3)

            print("Mechanic: You are covered.")
            time.sleep(2)

            print("Unk: Thank You Jesus.")
            time.sleep(3)

            print("*Unk's day just got a little better*")
            time.sleep(2)

            print("GOOD ENDING")
            break

        else:
            print("GAME OVER")
            time.sleep(1)

            retry = input("1: Try Again\n2: Quit\nChoice: ")

            if retry == "1":
                continue
            else:
                break

    elif choice0 == "3":
        print("Unk: Alright, man....")
        time.sleep(3)

        print("GAME OVER")
        time.sleep(1)

        retry = input("1: Try Again\n2: Quit\nChoice: ")

        if retry == "1":
            continue
        else:
            break

    else:
        print("Invalid choice.")
        time.sleep(1)

