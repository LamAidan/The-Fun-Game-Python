#!/usr/bin/env python3
import sys

gScore = 0


def print_line() -> None:
    print("\n----------------------------------------\n")


def print_main_menu() -> None:
    print_line()
    print(f"THE FUN GAME (Score: {gScore})\n")
    print("1. Politics")
    print("2. Geography")
    print("3. EE Basics")
    print("4. Quit")


def get_choice_in_range(min_val: int, max_val: int) -> int:
    while True:
        try:
            line = input().strip()
        except EOFError:
            return max_val  # match C behavior on EOF

        try:
            val = int(line)
        except ValueError:
            print(f"Please enter a number from {min_val} to {max_val}: ", end="")
            continue

        if min_val <= val <= max_val:
            return val

        print(f"Please enter a number from {min_val} to {max_val}: ", end="")


def ask_question_repeat_or_quit(
    question: str,
    a1: str,
    a2: str,
    a3: str,
    a4: str,
    correct_choice: int,
) -> int:
    while True:
        print(f"{question}\n")
        print(f"1\t{a1}")
        print(f"2\t{a2}")
        print(f"3\t{a3}")
        print(f"4\t{a4}")
        print("5\tQuit (back to main menu)\n")

        print("Enter your selection: ", end="")
        choice = get_choice_in_range(1, 5)

        print_line()  # line after question input

        if choice == 5:
            print("Quit selected.")
            return -1

        if choice == correct_choice:
            print("Correct!")
            return 1

        print("Incorrect! Try again (or choose 5 to quit).\n")


def play_politics() -> None:
    global gScore
    print_line()
    print("Politics Question\n")

    result = ask_question_repeat_or_quit(
        "Who's the 40th president of the United States?",
        "George W. Bush",
        "Bill Clinton",
        "Richard Nixon",
        "Ronald Reagan",
        4,
    )

    if result == 1:
        gScore += 1

    print_line()
    print("Returning to main menu...")


def play_geography() -> None:
    global gScore
    print_line()
    print("Geography Question\n")

    result = ask_question_repeat_or_quit(
        "What is the capital of Canada?",
        "Toronto",
        "Ottawa",
        "Vancouver",
        "Montreal",
        2,
    )

    if result == 1:
        gScore += 1

    print_line()
    print("Returning to main menu...")


def play_ee() -> None:
    global gScore
    print_line()
    print("EE Basics Question\n")

    result = ask_question_repeat_or_quit(
        "What is the unit of electrical resistance?",
        "Volt",
        "Ampere",
        "Ohm",
        "Watt",
        3,
    )

    if result == 1:
        gScore += 1

    print_line()
    print("Returning to main menu...")


def main() -> int:
    while True:
        print_main_menu()
        print("\nEnter your selection: ", end="")
        selection = get_choice_in_range(1, 4)

        print_line()  # line after menu input

        if selection == 1:
            play_politics()
        elif selection == 2:
            play_geography()
        elif selection == 3:
            play_ee()
        elif selection == 4:
            print(f"Thanks for playing! Final score: {gScore}")
            print_line()
            break

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
