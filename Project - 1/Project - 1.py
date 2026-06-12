print("==========================================")
print("  WELCOME TO THE PERSONAL DATA COLLECTOR")
print("========================================== \n")


name = input("enter your name : ")
age = int(input("enter your age : "))
height = float(input("enter your height in ft : "))
num = int(input("enter your favourite number : "))

print("\nthank you! for providing your information. 😊")

birth_year = 2026 - age
cm = height * 30.48

print("\n\n========== USER DETAILS ==========")

print("\nname : ",name)
print(f"(type : {type(name)}  &  memory address : {id(name)})")

print("\nage : ",age)
print(f"(type : {type(age)}  &  memory address : {id(age)})")

print("\nheight : ",height)
print(f"(type : {type(height)}  &  memory address : {id(height)})")

print("\nfavourite number : ",num)
print(f"(type : {type(num)}  &  memory address : {id(num)})")

print(f"\n\nbirth year : {birth_year} (based on your age of {age})")
print(f"height in cm : {cm:.2f} (based on your height of {height} ft)")

print("\n\nthank you! for using the personal data collector. 😊")
print("good bye!")
