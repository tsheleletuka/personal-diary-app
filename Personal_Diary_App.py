import os 
from datetime import datetime


#Set the path for the diary.txt within the specific folder
BASE_DIR = r"D:\Coding\Python\Github_Projects\Personal_Diary_App"
DIARY_FILE = os.path.join(BASE_DIR, "diary.txt")

def write_entry():
    entry = input("Write your diary entry: \n>")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(DIARY_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}]\n{entry}\n{'-'*40}\n")
    print("✅ Entry saved!\n")

def view_entries():
    if not os.path.exists(DIARY_FILE):
        print("No entries found yet.\n")
        return
    print("\n📖 All Diary Entries: \n")

    with open(DIARY_FILE, "r", encoding="utf-8") as file:
        print(file.read())

def search_entries():
    keyword = input("Enter keyword to search: ").lower()
    found = False

    with open(DIARY_FILE, "r", encoding="utf-8") as file:
        entries = file.read().split("-" * 40)
        for entry in entries:
            if keyword in entry.lower():
                print(f"\n🔍 Match Found:\n{entry.strip()}\n{'-'*40}")
                
                found = True

    if not found:
        print("no matching entries found.\n")
        

def main():
    while True:
        print("📘 Personal Diary App")
        print("1. Write a new entry")
        print("2. View all entries")
        print("3. Search by keyword")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            write_entry()

        elif choice == "2":
            view_entries()

        elif choice == "3":
            search_entries()

        elif choice == "4":
            print("Goodbye! 👋")
            break


        else:
            print("Invalid option. Try again!\n")

if __name__ == "__main__":
    main()