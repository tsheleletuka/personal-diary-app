import os 
from datetime import datetime
from fpdf import FPDF
import csv


#Set the path for the diary.txt within the specific folder
BASE_DIR = r"D:\Coding\Python\Github_Projects\Personal_Diary_App"
DIARY_FILE = os.path.join(BASE_DIR, "diary.txt")

def authenticate():
    PASSWORD = "mysecret123"        

    for attempt in range(3):
        entered = input("🔐 Enter password to access your diary: ")
        if entered == PASSWORD:
            print("Access granted!\n")
            return True
        else:
            print("Incorrect password.")
    print("too many failed attempts. Exiting.")
    return False

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

def delete_entry():
    if not os.path.exists(DIARY_FILE):
        print("No entries found.\n")
        return

    with open(DIARY_FILE, "r", encoding="utf-8") as file:
        entries = file.read().split("-" * 40 + "\n")
    
    entries = [e.strip() for e in entries if e.strip()]

    if not entries:
        print("No entries to delete. \n")
        return

    print("\n Select an entry to delete:\n")

    for idx, entry in enumerate(entries, start=1):
        short_entry = entry[:50].replace('\n', ' ')
        print(f"{idx}. {short_entry}...")

        
    try:
        choice = int(input("\nEnter the number of the entry to delete: "))

        if 1 <= choice <= len(entries):
            confirm = input("Are you sure you want to delete this entry? (y/n): ").lower()
            if confirm =='y':
                del entries[choice - 1]
                with open(DIARY_FILE, "w", encoding="utf-8") as file:
                    for entry in entries:
                        file.write(entry + "\n" + "-" * 40 + "\n")
                print("Entry deleted.\n")
            else:
                print("Cancelled.\n")
        else:
            print("Invalid selection.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def export_to_pdf():
    if not os.path.exists(DIARY_FILE):
        print("No entries found.\n")
        return

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(DIARY_FILE, "r", encoding="utf-8") as file:
        for line in file:
            pdf.multi_cell(0,10, txt=line.strip())

    output_path = os.path.join(BASE_DIR, "diary_export.pdf")
    pdf.output(output_path)

    print(f"PDF exported successfully to {output_path}\n")


def export_to_csv():
    if not os.path.exists(DIARY_FILE):
        print("No entries found to export.\n")
        return

    csv_file_path = os.path.join(BASE_DIR, "diary-export.csv")
    
    with open(DIARY_FILE, "r", encoding="utf-8") as file:
        entries = file.read().split("-" * 40)

    with open(csv_file_path, "w", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Timestamp", "Diary Entry"])

        for entry in entries:
            if entry.strip():
                lines = entry.strip().split("\n", 1)
                if len(lines) == 2:
                    timestamp = lines[0].strip()
                    content = lines[1].replace("\n", " ").strip()  # Replace line breaks with space
                    writer.writerow([timestamp, content])

    print(f"CSV exported successfully to {csv_file_path}\n")


def main():
    if not authenticate():
        return  # Exit if password check fails

    while True:
        print("📘 Personal Diary App")
        print("1. Write a new entry")
        print("2. View all entries")
        print("3. Search by keyword")
        print("4. Delete an entry")
        print("5. Export to PDF")
        print("6. Export to CSV")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            write_entry()

        elif choice == "2":
            view_entries()

        elif choice == "3":
            search_entries()

        elif choice == "4":
            delete_entry()

        elif choice == "5":
            export_to_pdf()

        elif choice == "6":
            export_to_csv()

        elif choice == "7":
            print("Goodbye! 👋")
            break


        else:
            print("Invalid option. Try again!\n")

if __name__ == "__main__":
    main()