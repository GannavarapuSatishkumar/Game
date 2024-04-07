from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Main window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="#9b59b6")
round1 = 1

# Pictures
rock_img = ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_img = ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.jpg"))
rock_img_com = ImageTk.PhotoImage(Image.open("rock1.jpg"))
paper_img_com = ImageTk.PhotoImage(Image.open("paper1.jpg"))
scissor_img_com = ImageTk.PhotoImage(Image.open("scissor1.jpg"))

# Insert pictures
user_label = Label(root, image=scissor_img, bg="#9b59b6")
comp_label = Label(root, image=scissor_img_com, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Scores
playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# Indicators
user_indicator = Label(root, font=50, text="User", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="Computer", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# Messages
msg = Label(root, font=20, bg="#9b59b6", fg="white", text="You Lose!")
msg.grid(row=3, column=2)

# Update messages
def updateMessage(x):
    msg['text'] = x

# Update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# Update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# Check winner
def checkWin(player, computer):
    global round1
    if player == computer:
        updateMessage("It's Tie Game!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore()
    else:
        pass
    if round1 > 4:
        determineWinner()
        root.destroy()
    else:
        round1 += 1
    print(round1)

# Update choices
choices = ["rock", "paper", "scissor"]
def updateChoice(x):
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_com)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_com)
    else:
        comp_label.configure(image=scissor_img_com)
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkWin(x, compChoice)

# Buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FF3E4D", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#FF3E4D", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

# Determine winner after the game
def determineWinner():
    player_score = int(playerScore["text"])
    computer_score = int(computerScore["text"])
    if player_score > computer_score:
        updateMessage("You Win the Game!")
    elif player_score < computer_score:
        updateMessage("Computer Wins the Game!")
    else:
        updateMessage("It's a Tie Game!")

# Run the GUI
root.mainloop()
