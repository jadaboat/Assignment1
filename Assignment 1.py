Question1 
def total_scores():
    num1=float(input("Enter homework score: "))
    num2=float(input("Enter exam score: "))
    num3=float(input("Exter discussion score: "))
    
    add_total=float((num2+num2+num3)/1)
    print("Your total score is: ", add_total)
    
total_scores()

Question 2 
A void function brings no value or result while a fruitful function does otherwise 


Question 3 


Question 4
 
a)
def calculate_GPA(score):
    if score >= 80:
        return 4.0
    elif score >= 75:
        return 3.5
    elif score >= 70:
        return 3.0 
    elif score >= 65:
        return 2.5 
    elif score >= 60:
        return 2.0 
    elif score >= 55:
        return 1.5 
    elif score >= 50:
        return 1.0
    else:
        return 0.0
    
score= 89   
gpa=calculate_GPA(score)
print(gpa)

b)
def calculateGPA(score):
    if score >= 80:
        return 4.0
    elif score >= 75:
        return 3.5
    elif score >= 70:
        return 3.0 
    elif score >= 65:
        return 2.5 
    elif score >= 60:
        return 2.0 
    elif score >= 55:
        return 1.5 
    elif score >= 50:
        return 1.0
    else:
        return 0.0

    
def getHonours(gpa):
    if gpa >= 3.85:
        return "Summa Cum Laude"
    elif calculateGPA(score) >= 3.70:
        return "Magna Cum Laude" 
    elif calculateGPA(score)>= 3.50:
        return "Cum Laude"
    else:
        return "None"

score=float(input("Enter your score: "))   
gpa=calculateGPA(score)
honors=getHonours(gpa)

print("Your GPA is: ",gpa)   
print (" ",honors)

        

Question 5 
import math 
def find_Area():
    r=float(input("Enter radius: "))
    area= math.pi *r *r
    print("Area of circle is:",area)

find_Area()
 

Question 6 
a)  
 def is_triangle(num1,num2,num3):
     
    if num1 > num2 + num3 or num2 > num1 + num3 or num3 > num2 + num1:
        return"False"
    else:
        return"True"
    
trial= is_triangle(3,7,5)
print(trial)


b)
 
def is_triangle(num1,num2,num3):
     
    if num1 > num2 + num3 or num2 > num1 + num3 or num3 > num2 + num1:
        return"False"
    else:
        return"True"
 

def work_trial():
    num1=int(input("Enter l1: "))
    num2=int(input("Enter l2: "))
    num3=int(input("Enter l3: "))

    if is_triangle(num1,num2,num3):
        print ("Triangle is formed")
    else:
        print("Triangle is not formed")
work_trial()
    

