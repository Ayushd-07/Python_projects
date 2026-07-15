# Personal Journal Manager

import datetime as dt

class JournalManager:

    def add(self):
        data = input("\nEnter your journal entry : ")

        file = open("journal.txt","a")
        file.write(str(dt.datetime.now()))
        file.write(f"\n{data}\n\n")
        file.close()

        print("\n✅ Entry added successfully...")

    
    def show(self):
        file = open("journal.txt","r")
        data = file.read()
        try:
            if data:
                print("\nYour journal entries : ")
                print("---------------------------")
                print(data)
                file.close()

            else:
                print("\nEmpty file.")

        except FileNotFoundError:
            print("\n❌ No journal entries found.")

        
    def search(self):
        word = input("\nEnter keyword to search : ")

        try:
            file = open("journal.txt","r")
            data = file.readlines()
            file.close()

            found = False
            for line in data:
                if word.lower() in line.lower():
                    print(f"\n{line}")
                    found = True

            if found == False:
                print("\n❌ No matching entry found.")

        except FileNotFoundError:
            print("\n❌ Journal file does not exist.")


    
    def delete(self):
        choice = input("\nAre you sure to delete all entries? (yes/no) : ")

        if choice.lower() == "yes":
            try:
                file = open("journal.txt","r")
                data = file.read()

                if data:
                    with open("journal.txt","w") as file:
                        print("\nAll entries deleted.")
                else:
                    print("\nFile is already empty.")
                
                file.close()
            
            except PermissionError:
                print("❌ No journal entries to delete.")
            
        else:
            print("\n❌ Delete cancelled.")

    
journal = JournalManager()

print("="* 40)
print("   Welcome to Personal Journal Manager")
print("="* 40)

while True:
    print("\n--- 📚 Personal Journal Manager 📚 ---")
    print("1. Add New Entry")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    ch = int(input("\nEnter your choice : "))

    match ch:
        case 1:
            journal.add()
        case 2:
            journal.show()
        case 3:
            journal.search()
        case 4:
            journal.delete()
        case 5:
            print("\nThank you for using Personal Journal! 😊")
            break
        case _:
            print("\n❌ Invalid choice! Please enter 1 to 5.")