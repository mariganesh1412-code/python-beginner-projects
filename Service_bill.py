print("VEHICLE SERVICE BILL")
print("--------------------")

customer = input("Enter customer name: ")
vehicle = input("Enter vehicle number: ")

parts_cost = float(input("Enter spare parts cost: "))
labour_charge = float(input("Enter labour charge: "))

total = parts_cost + labour_charge

print("\n------ SERVICE BILL ------")
print("Customer Name:", customer)
print("Vehicle Number:", vehicle)
print("Spare Parts Cost: Rs.", parts_cost)
print("Labour Charge: Rs.", labour_charge)
print("--------------------------")
print("TOTAL BILL: Rs.", total)
print("--------------------------")
print("Thank you for your service!")
