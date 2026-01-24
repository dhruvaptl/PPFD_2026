expance=int(input("enter your expance"))
income=int(input("enter your income"))
with open ("f1.txt","a") as file:
    file.write(f"Income- {income}\n")
    file.write(f"Expense- {expance}\n")
with open ("f1.txt","r") as file:
    file.read()
balance=income-expance
print("income:",income)    
print("balance:",balance)   
print("expance:",expance)