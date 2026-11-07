import random


def get_choices():
    player_choice = input("Masukkan Pilihan (Gunting, Kertas, Batu) : ")
    options = ["Gunting", "Kertas", "Batu"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"Pilihan kamu {player}, pilihan computer {computer}")
    if player == computer:
        return "Ini Seimbang"
    elif player == "Batu":
        if computer == "Gunting":
            return "Batu menghancurkan Gunting! Kamu Menang"
        else:
            return "Kertas membungkus Batu! Kamu Kalah"
    elif player == "Kertas":
        if computer == "Batu":
            return "Kertas membungkus Batu! Kamu Menang"
        else:
            return "Gunting memotong Kertas! Kamu Kalah"
    elif player == "Gunting":
        if computer == "Kertas":
            return "Gunting memotong Kertas! Kamu Menang"
        else:
            return "Batu menghancurkan Gunting! Kamu Kalah"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
