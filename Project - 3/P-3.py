print("=========================================")
print("  Welcome to the Student Data Organizer")
print("=========================================")

students = []

while True:
    print("\n1. Add Student")
    print("2. Display All Student")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("\nEnter Your Choice : "))

    match choice:
        # add
        case 1:
            id = int(input("\nEnter Student ID : "))
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            grade = input("Enter Grade : ")
            dob = input("Enter Date Of Birth (YYYY-MM-DD) : ")
            sub = input("Enter Subjects (comma-separated) : ")
            subjects = set(sub.split(","))

            info = (id,dob)

            student = {
                "ID" : info[0],
                "Name" : name,
                "Age" : age,
                "Grade" : grade,
                "DOB" : info[1],
                "Subjects" : subjects
            }
            
            students.append(student)
            print("\n✅ Student Added Successfully...")  


        # display all
        case 2:
            if len(students) == 0:
                print("\n❌ No Records Found!")

            for stu in students:
                print()
                print(f"Student ID : {stu["ID"]} | Name : {stu["Name"]} | Age : {stu["Age"]} | Grade : {stu["Grade"]} | DOB : {stu["DOB"]} | Subjects : {", ".join(stu["Subjects"])}")


        # update
        case 3:
            id = int(input("\nSearch ID : "))
            found = False

            if found == False:
                print("\nStudent Not Found!")

            for stu in students:
                if stu["ID"] == id:
                    while True:
                        print("\n1. Update Name")
                        print("2. Update Age")
                        print("3. Update New Subject")
                        print("4. Back")

                        c = int(input("\nEnter Your Choice : "))

                        match c:
                            # name
                            case 1:
                                name = input("\nEnter Update Name : ")
                                stu["Name"] = name
                                print("✅ Name Updated Successfully!")

                            # age
                            case 2:
                                age = int(input("\nEnter Update Age : "))
                                stu["Age"] = age
                                print("✅ Age Updated Successfully!")

                            # subject
                            case 3:
                                new_sub = input("\nEnter New Subject : ")
                                stu["Subjects"].add(new_sub)
                                print("✅ Subject Added Successfully!")

                            # break
                            case 4:
                                print("\nThank You! 😊")
                                break

                            # invalid
                            case _:
                                print("\n❌ Invalid Choice! Please Try Again.")


        # delete
        case 4:
            id = int(input("\nEnter Delete ID : "))
            found = False

            for stu in students:
                if stu["ID"] == id:
                    students.remove(stu)
                    found = True
                    print("\n✅ Delete Record Successfully...")

            if found == False:
                print("\n❌ Student Not Found!")


        # display subjects
        case 5:
            allsub = set()

            for stu in students:
                allsub.update(stu["Subjects"])
            
            if len(allsub) == 0:
                print("\n❌ No Subjects Found!")
            else:
                print("\nSubjects Offered")
                print("--------------------")
                for subs in allsub:
                    print(subs)


        # exit
        case 6:
            print("\nThank You for Using Student Data Organizer! 😊")
            print("Visit Again. Have a Great Day!")
            break


        # invalid
        case _:
            print("\n❌ Invalid Choice! Please Try Again.")
