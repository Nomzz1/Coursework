def game():
    #Import modules
    import random
    import time
    import json
    #Introduction
    time.sleep(0.1)
    print("\n")
    print("░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░██╗")
    print("░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗╚═╝")
    print("░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║░░░")
    print("░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║░░░")
    print("░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝██╗")
    print("░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░╚═╝")
    print("\n")
    print("████████╗██╗░░██╗███████╗  ██████╗░██╗░█████╗░███████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗")
    print("╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗██║██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝")
    print("░░░██║░░░███████║█████╗░░  ██║░░██║██║██║░░╚═╝█████╗░░  ██║░░██╗░███████║██╔████╔██║█████╗░░")
    print("░░░██║░░░██╔══██║██╔══╝░░  ██║░░██║██║██║░░██╗██╔══╝░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░")
    print("░░░██║░░░██║░░██║███████╗  ██████╔╝██║╚█████╔╝███████╗  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗")
    print("░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═════╝░╚═╝░╚════╝░╚══════╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝")
    print("\n")
    time.sleep(2)
    print("This is a two player dice game.")
    print("There are 5 rounds.")
    time.sleep(2)
    print("Each round, the players will roll two dice.")
    print("The numbers you roll will decide how many points you will gain or lose.")
    time.sleep(2)
    print("Both players start with zero points.")
    print("Your score cannot go below zero.")
    time.sleep(2)
    print("That's all the rules, Enjoy!")
    print("Press ENTER to continue.")
    input()
    time.sleep(0.1)
    #Authorisation of players
    auth_file = open("Auth_Players.txt","r+")
    p1 = input("Enter Player 1 name: ")
    auth = ""
    for line in auth_file:
        if p1 in line:
            auth = "YES"
        else:
            auth = "NO"
    while auth != "YES":
        print("You are not authorized, please enter the password to play.")
        password = input("Enter the password: ")
        if password == "password123":
            auth_file.write(p1+", ")
            auth = "YES"
        else:
            print("Wrong password, try again.")
            auth = "NO"
    print("Player 1 authorised, enjoy the game!")
    auth_file2 = open("Auth_Players.txt","r+")
    p2 = input("Enter Player 2 name: ")
    auth2 = ""
    for line in auth_file2:
        if p2 in line:
            auth2 = "YES"
        else:
            auth2 = "NO"
    while auth2 != "YES":
        print("You are not authorized, please enter the password to play.")
        password = input("Enter the password: ")
        if password == "password123":
            auth_file.write(p2+", ")
            auth2 = "YES"
        else:
            print("Wrong password, try again.")
            auth2 = "NO"
    auth_file.close()
    print("Player 2 authorized, enjoy the game!")
    #Dice funtion with return value
    def dice():
        global roll
        roll = random.randint(1,6)
        return roll
    #Set variables
    rounds = 5
    p1_score = 0
    p2_score = 0
    #Making sure the value doesn't go below zero
    def zero(x):
        if x < 0:
            x = 0
        return x
    #While loop using rounds
    while rounds != 0:
        #Actual game
        if rounds == 5:
            print("\n")
            print("██████╗░░█████╗░██╗░░░██╗███╗░░██╗██████╗░  ░░███╗░░")
            print("██╔══██╗██╔══██╗██║░░░██║████╗░██║██╔══██╗  ░████║░░")
            print("██████╔╝██║░░██║██║░░░██║██╔██╗██║██║░░██║  ██╔██║░░")
            print("██╔══██╗██║░░██║██║░░░██║██║╚████║██║░░██║  ╚═╝██║░░")
            print("██║░░██║╚█████╔╝╚██████╔╝██║░╚███║██████╔╝  ███████╗")
            print("╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░  ╚══════╝")
            print("\n")
        if rounds == 4:
            print("\n")
            print("██████╗░░█████╗░██╗░░░██╗███╗░░██╗██████╗░  ██████╗░")
            print("██╔══██╗██╔══██╗██║░░░██║████╗░██║██╔══██╗  ╚════██╗")
            print("██████╔╝██║░░██║██║░░░██║██╔██╗██║██║░░██║  ░░███╔═╝")
            print("██╔══██╗██║░░██║██║░░░██║██║╚████║██║░░██║  ██╔══╝░░")
            print("██║░░██║╚█████╔╝╚██████╔╝██║░╚███║██████╔╝  ███████╗")
            print("╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░  ╚══════╝")
            print("\n")
        if rounds == 3:
            print("\n")
            print("██████╗░░█████╗░██╗░░░██╗███╗░░██╗██████╗░  ██████╗░")
            print("██╔══██╗██╔══██╗██║░░░██║████╗░██║██╔══██╗  ╚════██╗")
            print("██████╔╝██║░░██║██║░░░██║██╔██╗██║██║░░██║  ░█████╔╝")
            print("██╔══██╗██║░░██║██║░░░██║██║╚████║██║░░██║  ░╚═══██╗")
            print("██║░░██║╚█████╔╝╚██████╔╝██║░╚███║██████╔╝  ██████╔╝")
            print("╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░  ╚═════╝░")
            print("\n")
        if rounds == 2:
            print("\n")
            print("\██████╗░░█████╗░██╗░░░██╗███╗░░██╗██████╗░  ░░██╗██╗")
            print("\██╔══██╗██╔══██╗██║░░░██║████╗░██║██╔══██╗  ░██╔╝██║")
            print("\██████╔╝██║░░██║██║░░░██║██╔██╗██║██║░░██║  ██╔╝░██║")
            print("\██╔══██╗██║░░██║██║░░░██║██║╚████║██║░░██║  ███████║")
            print("\██║░░██║╚█████╔╝╚██████╔╝██║░╚███║██████╔╝  ╚════██║")
            print("\╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░  ░░░░░╚═╝")
            print("\n")
        if rounds == 1:
            print("\n")      
            print("██████╗░░█████╗░██╗░░░██╗███╗░░██╗██████╗░  ███████╗")
            print("██╔══██╗██╔══██╗██║░░░██║████╗░██║██╔══██╗  ██╔════╝")
            print("██████╔╝██║░░██║██║░░░██║██╔██╗██║██║░░██║  ██████╗░")
            print("██╔══██╗██║░░██║██║░░░██║██║╚████║██║░░██║  ╚════██╗")
            print("██║░░██║╚█████╔╝╚██████╔╝██║░╚███║██████╔╝  ██████╔╝")
            print("╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░  ╚═════╝░")
            print("\n")
        print(p1+": Press ENTER to roll your dice.")
        input()
        print(p1,"rolls two dice...")
        time.sleep(2)
        roll1 = dice()
        roll2 = dice()
        print(p1,"rolled a",roll1,"and a",roll2)
        check = roll1 + roll2
        print("This means",check,"points will be added to",p1+"'s score")
        p1_score += check
        rem = check%2
        time.sleep(2)
        if rem == 1:
            print("However,",check,"is an odd number, so 5 points will be taken away from",p1+"'s score")
            p1_score -= 5
        else:
            print("However,",check,"is an even number, so 10 points will be added to",p1+"'s score")
            p1_score += 10
        p1_score = zero(p1_score)
        if roll1 == roll2:
            print(p1,"has rolled a double!")
            print("This means",p1,"gets to roll again!")
            time.sleep(2)
            rolld = dice()
            print("You rolled a",str(rolld)+"!")
            print(rolld,"will get added to your score!")
            p1_score += rolld
        time.sleep(2)
        p1_score = zero(p1_score)
        print(p1+"'s score at the end of this round is",p1_score)
        time.sleep(2)
        print("\n")
        print(p2+": Press ENTER to roll your dice.")
        input()
        print(p2,"rolls two dice...")
        time.sleep(2)
        roll1 = dice()
        roll2 = dice()
        print(p2,"rolled a",roll1,"and a",roll2)
        check = roll1 + roll2
        print("This means",check,"points will be added to",p2+"'s score")
        p2_score += check
        rem = check%2
        time.sleep(2)
        if rem == 1:
            print("However,",check,"is an odd number, so 5 points will be taken away from",p2+"'s score")
            p2_score -= 5
        else:
            print("However,",check,"is an even number, so 10 points will be added to",p2+"'s score")
            p2_score += 10
        p2_score = zero(p2_score)
        if roll1 == roll2:
            print(p2,"has rolled a double!")
            print("This means",p2,"gets to roll again!")
            time.sleep(2)
            rolld = dice()
            print("You rolled a",str(rolld)+"!")
            print(rolld,"will get added to your score!")
            p2_score += rolld
        time.sleep(2)
        p2_score = zero(p2_score)
        print(p2+"'s score at the end of this round is",p2_score)
        time.sleep(2)
        rounds -= 1
    #Extra rounds with on dice if it's a draw
    while p1_score == p2_score:
        print("It's a Draw!")
        time.sleep(1)
        print("You will each roll one die until one of you is victorious.")
        roll1 = dice()
        roll2 = dice()
        print("Player 1 rolled a",str(roll1)+"!")
        print("Player 2 rolled a",str(roll2)+"!")
        p1_score += roll1
        p2_score += roll2
    #Deciding who wins
    print("The game has ended")
    print("Scores are being calculated...")
    time.sleep(2)
    print("\n")
    print("░██╗░░░░░░░██╗██╗███╗░░██╗███╗░░██╗███████╗██████╗░██╗")
    print("░██║░░██╗░░██║██║████╗░██║████╗░██║██╔════╝██╔══██╗██║")
    print("░╚██╗████╗██╔╝██║██╔██╗██║██╔██╗██║█████╗░░██████╔╝██║")
    print("░░████╔═████║░██║██║╚████║██║╚████║██╔══╝░░██╔══██╗╚═╝")
    print("░░╚██╔╝░╚██╔╝░██║██║░╚███║██║░╚███║███████╗██║░░██║██╗")
    print("░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝")
    print("\n")
    if p1_score > p2_score:
        print(p1,"Wins!")
    if p1_score < p2_score:
        print(p2,"Wins!")
    #Highscore system
    print("\n")
    print("██╗░░░░░███████╗░█████╗░██████╗░███████╗██████╗░██████╗░░█████╗░░█████╗░██████╗░██████╗░")
    print("██║░░░░░██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗")
    print("██║░░░░░█████╗░░███████║██║░░██║█████╗░░██████╔╝██████╦╝██║░░██║███████║██████╔╝██║░░██║")
    print("██║░░░░░██╔══╝░░██╔══██║██║░░██║██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██║██╔══██╗██║░░██║")
    print("███████╗███████╗██║░░██║██████╔╝███████╗██║░░██║██████╦╝╚█████╔╝██║░░██║██║░░██║██████╔╝")
    print("╚══════╝╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░")
    leaderboard = open("leaderboard.json", "r+")
    ldb = eval(leaderboard.read())
    leaderboard.close()
    ldb = dict(ldb)
    ldb_new = dict(ldb)
    time.sleep(2)
    print("\n")
    print("Here are the top 5 highscores:")
    print("\n")
    print("Name: Highscore")
    ldb = dict(sorted(ldb.items(), key=lambda item:item[1], reverse = True))
    ldb = dict(list(ldb.items())[0:5])
    for keys, values in ldb.items():
        print(str(keys)+":", values)
    ldblist = []
    for keys in ldb_new:
        ldblist += keys
    if p1 in ldblist:
        if ldb_new[p1] < p1_score:
            ldb_new[p1] = p1_score
    else:
        ldb_new.update({p1:p1_score})
    if p2 in ldblist:
        if ldb_new[p2] < p2_score:
            ldb_new[p2] = p2_score
    else:
        ldb_new.update({p2:p2_score})
        time.sleep(2)
    print("\nHere are the top 5 highscores after your scores have been added:\n")
    print("Name: Highscore")
    ldb_save = open("leaderboard.json","w")
    json.dump(ldb_new, ldb_save)
    ldb_save.close()
    ldb_new = dict(sorted(ldb_new.items(), key=lambda item:item[1], reverse = True))
    ldb_new = dict(list(ldb_new.items())[0:5])
    for keys, values in ldb_new.items():
        print(str(keys)+":", values)
    time.sleep(2)
    print("I hope you have enjoyed playing the game.\nSee you next time!")
    print("\n")
    print("░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗")
    print("██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝")
    print("██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░")
    print("██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░")
    print("╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗")
    print("░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝")
    input()
game()
