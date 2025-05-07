import random

def roll_dice():
    """Бросок костей (1-6)"""
    return random.randint(1, 6)

def play_round(player_name):
    """Раунд для игрока или компьютера"""
    input(f"{player_name}, нажми Enter, чтобы бросить кости...")
    dice = roll_dice()
    print(f"{player_name} выбросил(а) {dice}!")
    return dice

def main():
    print("🎲 Добро пожаловать в игру 'Кости против Компьютера'! 🎲")
    print("Правила: 3 раунда, побеждает тот, у кого сумма очков больше.\n")
    player1 = input("Имя первого игрока: ")
    player2 = input("Имя второго игрока: ")
    computer = "🤖 Компьютер"
    scores = {player1: 0, player2: 0, computer: 0}

    for round_num in range(1, 4):
        print(f"\n=== Раунд {round_num} ===")
        scores[player1] += play_round(player1)
        scores[player2] += play_round(player2)
        scores[computer] += roll_dice()  # Компьютер бросает автоматически
        print(f"Текущие очки: {player1} - {scores[player1]}, {player2} - {scores[player2]}, {computer} - {scores[computer]}")

    # Определяем победителя
    max_score = max(scores.values())
    winners = [name for name, score in scores.items() if score == max_score]

    if len(winners) > 1 and computer in winners:
        print(f"\n🔥 Победил {computer} (ничья между игроками)!")
    elif len(winners) > 1:
        print(f"\n🤝 Ничья между {', '.join(winners)}!")
    else:
        print(f"\n🏆 Победил(а) {winners[0]} с результатом {max_score} очков!")

if __name__ == "__main__":
    main()