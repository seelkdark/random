import random

def guess_number():
    print("Загадайте число от 1 до 100 и нажмите Enter, когда будете готовы.")
    input("Нажмите Enter, чтобы продолжить...")

    low = 1
    high = 100
    attempts = 0
    feedback = ''

    while feedback != 'c':
        # Компьютер делает прогноз
        guess = random.randint(low, high)
        attempts += 1
        print(f"Компьютер предполагает, что ваше число - {guess}.")

        # Получаем обратную связь от пользователя
        feedback = input("Введите 'h', если загаданное число больше; 'l', если меньше; и 'c', если угадано: ").lower()

        if feedback == 'h':
            low = guess + 1  # Увеличиваем нижнюю границу
        elif feedback == 'l':
            high = guess - 1  # Уменьшаем верхнюю границу
        elif feedback == 'c':
            print(f"Компьютер угадал ваше число {guess} за {attempts} попыток!")
        else:
            print("Пожалуйста, введите 'h', 'l' или 'c'.")


if __name__ == "__main__":
    guess_number()