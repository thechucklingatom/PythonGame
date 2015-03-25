#Putnam_Robert
#only need to import random
import random

#Element block
class Element:
    """Parent class for all the moves"""
    #set returnString for use by children
    returnString = ["",""]
    #general initialize
    def __init__(self, name):
        self._name = name
    #returns name for compareTo
    def name(self):
        return self._name
    #will throw error if not implemented in child or called here
    def compareTo(self, Element):
        raise NotImplementedError("Not yet implemented")
#Rock
class Rock(Element):
    """Rock move"""
    def compareTo(self, Element):
        #assume that play 1 is being compared to play 2
        if(Element.name() == "Rock"):
            Element.returnString[0] = "Rock bounces off Rock"
            Element.returnString[1] = "Tie"
        elif(Element.name() == "Paper"):
            Element.returnString[0] = "Paper covers Rock"
            Element.returnString[1] = "Lose"
        elif(Element.name() == "Scissors"):
            Element.returnString[0] = "Rock crushes Scissors"
            Element.returnString[1] = "Win"
        elif(Element.name() == "Lizard"):
            Element.returnString[0] = "Rock crushes Lizard"
            Element.returnString[1] = "Win"
        elif(Element.name() == "Spock"):
            Element.returnString[0] = "Spock vaporizes Rock"
            Element.returnString[1] = "Lose"
        return Element.returnString
#Paper
class Paper(Element):
    """Paper move"""
    def compareTo(self, Element):
        #assume that play 1 is being compared to play 2
        if(Element.name() == "Rock"):
            Element.returnString[0] = "Paper covers Rock"
            Element.returnString[1] = "Win"
        elif(Element.name() == "Paper"):
            Element.returnString[0] = "Paper flutters around Paper"
            Element.returnString[1] = "Tie"
        elif(Element.name() == "Scissors"):
            Element.returnString[0] = "Scissors cuts Paper"
            Element.returnString[1] = "Lose"
        elif(Element.name() == "Lizard"):
            Element.returnString[0] = "Lizard eats Paper"
            Element.returnString[1] = "Lose"
        elif(Element.name() == "Spock"):
            Element.returnString[0] = "Paper Disproves Spock"
            Element.returnString[1] = "Win"
        return Element.returnString
#Scissors
class Scissors(Element):
    """Scissors move"""
    def compareTo(self, Element):
        #assume that play 1 is being compared to play 2
        if(Element.name() == "Rock"):
            Element.returnString[0] = "Rock crushes Scissors"
            Element.returnString[1] = "Lose"
        elif(Element.name() == "Paper"):
            Element.returnString[0] = "Scissors cuts Paper"
            Element.returnString[1] = "Win"
        elif(Element.name() == "Scissors"):
            Element.returnString[0] = "Scissors sharpens Scissors"
            Element.returnString[1] = "Ties"
        elif(Element.name() == "Lizard"):
            Element.returnString[0] = "Scissors decapitates Lizard"
            Element.returnString[1] = "Win"
        elif(Element.name() == "Spock"):
            Element.returnString[0] = "Spock smashes Scissors"
            Element.returnString[1] = "Lose"
        return Element.returnString
#Lizard
class Lizard(Element):
    """Lizard move"""
    def compareTo(self, Element):
        #assume that play 1 is being compared to play 2
        if(Element.name() == "Rock"):
            Element.returnString[0] = "Rock smashes Lizard"
            Element.returnString[1] = "Lose"
        elif(Element.name() == "Paper"):
            Element.returnString[0] = "Lizard eats paper"
            Element.returnString[1] = "Win"
        elif(Element.name() == "Scissors"):
            Element.returnString[0] = "Scissors decapitates Lizard"
            Element.returnString[1] = "Lose"
        elif(Element.name() == "Lizard"):
            Element.returnString[0] = "Lizard dances with Lizard"
            Element.returnString[1] = "Tie"
        elif(Element.name() == "Spock"):
            Element.returnString[0] = "Lizard poisons Spock"
            Element.returnString[1] = "Win"
        return Element.returnString
#Spock
class Spock(Element):
    """Spock move"""
    def compareTo(self, Element):
        #assuming that play 1 is being compared to play 2
        #I feel like there was a more elegant way to do this
        #but I was unable to figure it out.
        if(Element.name() == "Rock"):
            Element.returnString[0] = "Spock vaporizes Rock"
            Element.returnString[1] = "Win"
        elif(Element.name() == "Paper"):
            Element.returnString[0] = "Paper disproves Spock"
            Element.returnString[1] = "Lose"
        elif(Element.name() == "Scissors"):
            Element.returnString[0] = "Spock crushes Scissors"
            Element.returnString[1] = "Win"
        elif(Element.name() == "Lizard"):
            Element.returnString[0] = "Lizard poisons Spock"
            Element.returnString[1] = "Lose"
        elif(Element.name() == "Spock"):
            Element.returnString[0] = "Spock doesn't comprehend other Spock"
            Element.returnString[1] = "Tie"
        return Element.returnString
#element declaration and initialization
rock = Rock('Rock')
paper = Paper('Paper')
scissors = Scissors('Scissors')
lizard = Lizard('Lizard')
spock = Spock('Spock')

#player classese block
class Player:
    """Parent class for all of the player objects"""
    #declared for iterativeBot
    botIter = 0
    #initialization method, inherited by the children
    def __init__(self, name):
        self._name = name
    #returns the name, also inherited by the children, allows for checking
    #which bot it is.
    def name(self):
       return self._name 
    #play is not implemented here and will throw an error if called from here
    #or a child that did not implement it
    def play(self):
        raise NotImplementedError("Not yet implemented")
#StupidBot
class StupidBot(Player):
    """Always plays rock"""
    def play(self):
        #Bot is dumb, but will smash opposition with rock!
        return rock
#RandomBot
class RandomBot(Player):
    """randomly picks a move to throw it"""
    def play(self):
        #This is going between 0 and 29 because when I had just 0-4 it
        #didn't feel random enough and I would get a bit of repitition
        rand = random.randint(0, 29)
        if(rand % 5 == 0):
            return rock
        elif(rand % 5 == 1):
            return paper
        elif(rand % 5 == 2):
            return scissors
        elif(rand % 5 == 3):
            return lizard
        elif(rand % 5 == 4):
            return spock
#IterativeBot
class IterativeBot(Player):
    """Walkes through each of the moves in order"""
    def play(self):
        #assumes the user is not going to play past the int overflow limit
        #usues the mod (%) to just allow for many plays
        #could also just set it to the next number or even play
        #usues the the player class to hold the botIter var
        if(Player.botIter %5 == 0):
            Player.botIter += 1
            return rock
        elif(Player.botIter %5 == 1):
            Player.botIter += 1
            return paper
        elif(Player.botIter %5 == 2):
            Player.botIter += 1
            return scissors
        elif(Player.botIter %5 == 3):
            Player.botIter += 1
            return lizard
        elif(Player.botIter %5 == 4):
            Player.botIter += 1
            return spock
#LastPlayBot class
class LastPlayBot(Player):
    """bot that plays the last move that was played""" 
    def play(self):
        #uses the global play var for its last play
        global play
        return play
#Human class
class Human(Player):
    """class for human player"""
    def play(self):
        playInput = 0
        #askes the user what they would like to play
        print("(1) : Rock\n(2) : Paper\n(3) : Scissors\n(4) : Lizard\n(5) : Spock")
        playInput = int(input("Enter your move: "))
        #checks that it is valid and says if it isn't
        while(0 >= playInput or playInput >= 6):
            print("Invalid move. Please try again")
            playInput = input("Enter your move: ")
        if(playInput == 1):
            return rock
        elif(playInput == 2):
            return paper
        elif(playInput == 3):
            return scissors
        elif(playInput == 4):
            return lizard
        elif(playInput == 5):
            return spock
        else:
            #it should only hit this if a decimel number is entered.
            return rock
#MyBot class
class MyBot(Player):
    """My bot class"""
    def play(self):
        rand = random.randint(0,29)
        #picks between too random moves both with coverage on the other moves
        #lizard beats all the options rock loses to and rock beats everything lizard loses to
        if(rand % 2 == 0):
            return rock
        elif(rand % 2 == 1):
            return lizard
        else:
            #only on some critical failure will this happen
            return paper
#make the bots
stupid = StupidBot('StupidBot')
randBot = RandomBot('RandomBot')
iterative = IterativeBot('IterativeBot')
last = LastPlayBot('LastPlayBot')
human = Human('Human')
mybot = MyBot('MyBot')
#set up the global last play var and set default for userInput
play = rock
userInput = ""
winsP1 = 0
winsP2 = 0

#Print out the welcoming intro to the gmae.
print("Welcome to Rock, Paper, Scissors, Lizard, Spock, implemented by Putnam_Robert")
print("We will be doing best of five games\n")

while(userInput.lower() != "quit"):
    #start UI
    print("Please choose two players")
    print("(1) Human\n(2) StupidBot\n(3) RandomBot\n(4) IterativeBot\n(5) LastPlayBot\n(6) MyBot")
    input1 = int(input("Select player 1: "))
    input2 = int(input("Select player 2: "))
    #set player1 based on their selection
    if(input1 == 1):
        player1 = human
    elif(input1 == 2):
        player1 = stupid
    elif(input1 == 3):
        player1 = randBot
    elif(input1 == 4):
        player1 = iterative
    elif(input1 == 5):
        player1 = last
    elif(input1 == 6):
        player1 = mybot
    else:
        #if they enter something outside the range they get stupid bot
        print("Invalid selection for player one, picking StupidBot by default.")
        player1 = stupid
    #set player2 based on their selection
    if(input2 == 1):
        player2 = human
    elif(input2 == 2):
        player2 = stupid
    elif(input2 == 3):
        player2 = randBot
    elif(input2 == 4):
        player2 = iterative
    elif(input2 == 5):
        player2 = last
    elif(input2 == 6):
        player2 = mybot
    else:
        #again they get stupid bot if they enter something invalid.
        print("Invalid selection for player two, picking StupidBot by default.")
        player2 = stupid
    #prints the two bots that were selected
    print("{} vs {}. Go!".format(player1.name(), player2.name()))
    #runs through 5 games
    for i in range(0, 5):
        #show the global wins vars to make sure they are accessed everywhere
        global winsP1
        global winsP2
        #sets the plays
        play1 = player1.play()
        play2 = player2.play()
        #if one of the bots is the last play bot set the other bots play to its next
        if(player1.name() == "LastPlayBot"):
            global play
            play = play2
        elif(player2.name() == "LastPlayBot"):
            global play
            play = play1
        #this is the string with the info and who wins
        results = play1.compareTo(play2)
        #prints what happened with player1 as the focus
        print(results[0])
        #increments the wins var depending on who wins, or declare a tie
        if(results[1] == "Win"):
            print("{} wins!\n".format(player1.name()))
            winsP1+=1
        elif(results[1] == "Lose"):
            print("{} wins!\n".format(player2.name()))
            winsP2+=1
        else:
            print("This game is a tie.\n")
        #end for
    global winsP1
    global winsP2
    #figures out who wins and prints the results
    if(winsP1 > winsP2):
        print("{} wins! {} to {}!\n".format(player1.name(), winsP1, winsP2))
    elif(winsP2 > winsP1):
        print("{} wins! {} to {}!\n".format(player2.name(), winsP2, winsP1))
    else:
        print("The match was a draw!\n")
    #reset the wins so that they are 0 again for the next match
    winsP1 = 0
    winsP2 = 0
    #asks if they want to keep playing
    userInput = input("Press enter to play again, or type quit to quit.\n")
    #end while
print("Thanks for playing!!")
#end of program, not the prettiest thing I've ever made but it was interesting