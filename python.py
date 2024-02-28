salary =  input("salary  per  day or month : ")

if(salary == "day"):
    day = int(input("salary/day : "))
    tax_d = day*(0.05,0.25) [day > 5000]
    print("tax :", tax_d)

elif(salary == "month"):
    month = int(input("salary/month : "))
    tax_m = month*(0.05,0.25) [month > 50000]
    print("tax :", tax_m)

else:
    print("error")