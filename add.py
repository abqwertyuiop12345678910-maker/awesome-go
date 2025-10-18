"""
SmartAdder — A big Python program that performs different types of addition.
Author: Abhishek S Angadi
"""

import time
import sys
import os
from datetime import datetime

# ---------------------------------------------------------
# Logger Utility
# ---------------------------------------------------------
class Logger:
    def __init__(self, filename="adder_log.txt"):
        self.filename = filename

    def log(self, message):
        with open(self.filename, "a") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

# ---------------------------------------------------------
# Smart Adder Core Class
# ---------------------------------------------------------
class SmartAdder:
    def __init__(self, logger):
        self.logger = logger
        self.history = []

    def add_two_numbers(self, a, b):
        result = a + b
        self._record(a, b, result)
        return result

    def add_multiple_numbers(self, numbers):
        result = sum(numbers)
        self._record(*numbers, result)
        return result

    def add_from_file(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found!")

        numbers = []
        with open(filename, "r") as f:
            for line in f:
                try:
                    num = float(line.strip())
                    numbers.append(num)
                except ValueError:
                    pass  # ignore non-numeric lines

        if not numbers:
            raise ValueError("No valid numbers found in file!")

        result = sum(numbers)
        self._record(*numbers, result)
        return result

    def _record(self, *args):
        *nums, result = args
        entry = {
            "numbers": nums,
            "result": result,
            "time": datetime.now().strftime("%H:%M:%S")
        }
        self.history.append(entry)
        self.logger.log(f"Added {nums} => {result}")

    def show_history(self):
        print("\n=== ADDITION HISTORY ===")
        for i, entry in enumerate(self.history, 1):
            nums = ", ".join(map(str, entry["numbers"]))
            print(f"{i}. {nums} = {entry['result']} (at {entry['time']})")

    def clear_history(self):
        self.history = []
        open(self.logger.filename, "w").close()
        print("History cleared!")

# ---------------------------------------------------------
# Input Helper Functions
# ---------------------------------------------------------
def get_numbers_from_user():
    nums = []
    while True:
        val = input("Enter a number (or 'done' to finish): ").strip()
        if val.lower() == "done":
            break
        try:
            nums.append(float(val))
        except ValueError:
            print("⚠️  Invalid input. Please enter a number.")
    return nums

# ---------------------------------------------------------
# Menu System
# ---------------------------------------------------------
def show_menu():
    print("""
===========================
 SMART ADDER MAIN MENU
===========================
1. Add two numbers
2. Add multiple numbers
3. Add numbers from file
4. Show addition history
5. Clear history
6. Exit
===========================
""")

# ---------------------------------------------------------
# Main Program Loop
# ---------------------------------------------------------
def main():
    logger = Logger()
    adder = SmartAdder(logger)

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = adder.add_two_numbers(a, b)
                print(f"✅ Result: {a} + {b} = {result}")
            except ValueError:
                print("⚠️ Invalid input! Please enter valid numbers.")

        elif choice == "2":
            nums = get_numbers_from_user()
            if nums:
                result = adder.add_multiple_numbers(nums)
                print(f"✅ Sum of {nums} = {result}")
            else:
                print("⚠️ No numbers entered!")

        elif choice == "3":
            filename = input("Enter filename: ").strip()
            try:
                result = adder.add_from_file(filename)
                print(f"✅ Sum of numbers from '{filename}' = {result}")
            except Exception as e:
                print(f"⚠️ Error: {e}")

        elif choice == "4":
            adder.show_history()

        elif choice == "5":
            adder.clear_history()

        elif choice == "6":
            print("👋 Exiting SmartAdder... Goodbye!")
            time.sleep(1)
            sys.exit()

        else:
            print("⚠️ Invalid choice! Please try again.")

        input("\nPress Enter to continue...")

# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
a
