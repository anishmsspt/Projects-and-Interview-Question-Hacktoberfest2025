import time
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("=" * 50)
    print("          COUNTDOWN TIMER          ")
    print("=" * 50)
    print()

def print_large_number(num):
    digits = {
        '0': ["  ███  ", " █   █ ", "█     █", "█     █", "█     █", " █   █ ", "  ███  "],
        '1': ["   █   ", "  ██   ", "   █   ", "   █   ", "   █   ", "   █   ", " █████ "],
        '2': [" █████ ", "█     █", "      █", " █████ ", "█      ", "█      ", "███████"],
        '3': [" █████ ", "█     █", "      █", " █████ ", "      █", "█     █", " █████ "],
        '4': ["█      ", "█    █ ", "█    █ ", "███████", "     █ ", "     █ ", "     █ "],
        '5': ["███████", "█      ", "█      ", "██████ ", "      █", "█     █", " █████ "],
        '6': [" █████ ", "█     █", "█      ", "██████ ", "█     █", "█     █", " █████ "],
        '7': ["███████", "█    █ ", "    █  ", "   █   ", "  █    ", "  █    ", "  █    "],
        '8': [" █████ ", "█     █", "█     █", " █████ ", "█     █", "█     █", " █████ "],
        '9': [" █████ ", "█     █", "█     █", " ██████", "      █", "█     █", " █████ "]
    }

    num_str = str(num)
    for row in range(7):
        line = ""
        for digit in num_str:
            if digit in digits:
                line += digits[digit][row] + "  "
        print(line.center(50))

def countdown_timer():
    clear_screen()
    print_banner()

    try:
        seconds = int(input("Enter countdown duration (seconds): "))

        if seconds <= 0:
            print("Please enter a positive number!")
            return

        print(f"\nStarting countdown from {seconds}...\n")
        time.sleep(2)

        for i in range(seconds, 0, -1):
            clear_screen()
            print_banner()
            print()
            print_large_number(i)
            print()
            print(f"Seconds remaining: {i}".center(50))
            print()
            time.sleep(1)

        clear_screen()
        print_banner()
        print()
        print("╔════════════════════════════════════════════════╗")
        print("║                                                ║")
        print("║              ⏰ TIME'S UP! ⏰                  ║")
        print("║                                                ║")
        print("╔════════════════════════════════════════════════╗")
        print()

        for _ in range(3):
            print("🔔 BEEP! 🔔".center(50))
            time.sleep(0.5)
            sys.stdout.write("\033[F")
            print(" " * 50)
            sys.stdout.write("\033[F")
            time.sleep(0.5)

        print("🔔 BEEP! 🔔".center(50))
        print()

    except ValueError:
        print("Invalid input! Please enter a number.")
    except KeyboardInterrupt:
        print("\n\nCountdown cancelled by user.")

def main():
    while True:
        countdown_timer()
        print()
        again = input("Start another countdown? (y/n): ").lower()
        if again != 'y':
            print("\nThank you for using Countdown Timer!")
            break

if __name__ == "__main__":
    main()
