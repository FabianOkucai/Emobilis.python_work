# Write a python program that calculates student grade based on their mean score.Create 5 variables to store student marks per subject
def number_of_subjects():
    subjects = ["math","english","chemistry","biology","physcis"]
    print(f"Enter score of your subjects")
 

def calculations():
    
    math = int(input("Enter Math Score: "))
    english = int(input("Enter English Score: "))
    chemistry = int(input("Enter Chemistry Score: "))
    biology = int(input("Enter Biology Score: "))
    physics = int(input("Enter Physics Score: "))
    
    total = math+english+chemistry+biology+physics
    num_subjects = 5
    mean = total/num_subjects
    print(mean)
        

    if mean >= 80 and mean < 100:
        print(f"Here is your score {mean}.You have grade A.Excellent Score ")
    
    elif mean >= 70 and mean < 80:
        print(f"Here is your score {mean}.You have grade B.Good Score")
    elif mean >= 60 and mean < 70:
        print(f"Here is your score {mean}.You have grade C.Above Average")
    elif mean >= 50 and mean < 60:
        print(f"Here is your score {mean}. You have grade D. Below Average.")
    elif mean >= 0 and mean < 50:
        print(f"Here is your score {mean}. You have grade E. Try again.")
    else:
        mean < 0 and mean >100
        print("Invalid score.")
        

def main():
    number_of_subjects()
    calculations()
    
print(main())