print("========================================================")
print("   Welcome to Pattern generator and Number analyzer!")
print("========================================================")

while True:
    print("\n\n1. Pattern generate")
    print("2. Number analysis")
    print("3. Exit")

    choice = int(input("\nenter your choice  : "))

    match choice:
        # Pattern generate
        case 1:
            print("\n1. Right side triangle")
            print("2. Left side triangle")

            a = int(input("\nEnter triangle shape : "))
            n = int(input("\nenter the number of rows : "))
            match a:
                # Right side
                case 1:
                    for i in range(1,n+1):
                        for _ in range(n-i):
                            print(" ", end= " ")
                        for j in range(1,i+1):
                            print("*", end= " ")
                        print()

                # Left side
                case 2:
                    for i in range(1,n+1):
                        for j in range(1,i+1):
                            print("*", end= " ")
                        print()

                # Invalid
                case _:
                    print("\n❌ Invalid choice! Please try again.")
                    break


        # Number analsis
        case 2:
            start = int(input("\nenter start number : "))
            end = int(input("enter end number : "))

            total = 0

            for i in range(start,end+1):
                if i % 2 == 0:
                    print(f"{i} is Even Number.")
                else:
                    print(f"{i} is Odd Number.")
                
                total += i
            
            print("\nSum of all numbers : ", total)


        # Exit        
        case 3:
            print("\nThank You! Visit Again. 😊")
            break


        # Invalid
        case _:
            print("\n❌ Invalid choice! Please try again.")

            
