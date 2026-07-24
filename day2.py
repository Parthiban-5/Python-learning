print("-PROGRAM 1-")
employee_name=input("enter employee name:")
basic_salary=float(input("enter your salary:"))
HRA=(0.2*(basic_salary))
DA=(0.15*(basic_salary))
gross_salary=basic_salary+HRA+DA
print(f"employee name={employee_name}.\n basic salary={basic_salary}.\n HRA={HRA}.\n DA={DA}.\n gross={gross_salary}")
if gross_salary<30000:
    tax=(0.05*gross_salary)
    print("the tax is:",tax)
elif gross_salary>=30000 and gross_salary<=60000:
    tax=(0.10*gross_salary)
    print("the tax is:",tax)    
else:
    tax=(0.20*gross_salary)
    print("the tax is:",tax)    
net_salary=gross_salary-tax
print("the net salary is:",net_salary)

print("-PROGRAM 2-")

customer_name=input("enter customer name :")
product_name=input("enter product name:")
quantity=int(input("enter quantity:"))
price=float(input("enter price per item:"))
total=quantity*price
if total>=5000:
    gst=total*0.2
elif total>=2000:
    gst=total*0.10
else:
    gst=0
final=gst+total
print(f"customer name:{customer_name}.\n product name:{product_name}.\n quantity:{quantity}.\n price per item:{price}.\n total:{total}.\n GST:{gst}.\n FINAL BILL:{final}")