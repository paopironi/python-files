import random

dict = {"r": "Rock", "p": "Paper", "s": "Scissors"}
computer_dict = {1: "Rock", 2: "Paper", 3: "Scissors"}
outcome_dict = {
    "Rock-Paper": ["Paper covers Rock! You Lose", 0, 1],
    "Paper-Rock": ["Paper covers Rock! You Win", 1, 0],
    "Paper-Scissors": ["Scissors cut Paper! You Lose", 0, 1],
    "Scissors-Paper": ["Scissors cut Paper! You Win", 1, 0],
    "Rock-Scissors": ["Rock smashes Scissors! You Win", 1, 0],
    "Scissors-Rock": ["Rock smashes Scissors! You Lose", 0, 1],
}
player_score = 0
computer_score = 0


def play():
    global player_score, computer_score
    player = input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ")
    print("You played %s" % (dict[player]))
    computer = random.randint(1, 3)
    print("Computer played %s" % (computer_dict[computer]))
    outcome = dict[player] + "-" + computer_dict[computer]
    if dict[player] == computer_dict[computer]:
        print("Both players selected %s. It's a tie!" % (dict[player]))
        play_again()
        return
    print(outcome_dict[outcome][0])
    player_score = player_score + outcome_dict[outcome][1]
    computer_score = computer_score + outcome_dict[outcome][2]
    play_again()


def play_again():
    play_again = input("Play again? (y/n): ")
    if play_again == "y":
        play()
    else:
        print("Final Scores:")
        print("Computer: %d" % (computer_score))
        print("Player: %d" % (player_score))
        return


play()
