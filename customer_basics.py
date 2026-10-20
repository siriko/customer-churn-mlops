Customer_name = "john"
Age = 30
Monthly_bill = 85.50
Contract = "Month_to_month"
Has_churned = False 

print(Customer_name)
print(Age)
print(Monthly_bill)
print(Contract)
print(False)

months = 12
Total_bill = Monthly_bill * months
print(Total_bill)

tenure = 3
if tenure < 6:
    print("New customer")
else:
    print("Existing customer")

monthly_bills = [50,75,100,85]
print(monthly_bills)

monthly_bills = [50,75,100,85]
monthly_bills[1] = 95
print(monthly_bills)