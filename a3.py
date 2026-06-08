print("Enter marks obtaained in all 5 subjects:  ")

English = int(input("Enter marks:  ")) 
SST = int(input("Enter marks:  "))
Science = int(input("Enter marks:  "))
Hindi = int(input("Enter marks:  "))
Math = int(input("Enter marks:  "))

total = English + Math + SST + Science + Hindi
avg = total/5

validRange = (0,101)
if avg not in validRange:
    print("Invalid avg")

elif avg in range (80,101):
    print("Grade A")

elif avg in range (65,80):
    print("Grade B")


elif avg in range (41,65):
    print("Grade C")
     
    
else:
    print("Fail")



