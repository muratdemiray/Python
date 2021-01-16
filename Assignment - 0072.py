
if(str(input("Are you a cigarette addict older than 75 years old? (Y/N): ")).lower() == "y"):
    age = True
else:
    age = False

if(str(input("Do you have a severe chronic disease? (Y/N): ")).lower() == "y"):
    chronic = True
else:
    chronic = False

if(str(input("Are you a cigarette addict older than 75 years old? (Y/N): ")).lower() == "y"):
    immune = True
else:
    immune = False

risk = age or chronic or immune    

if  not risk:
    print("You are not in risky group")
else:
    print("You are in risky group")