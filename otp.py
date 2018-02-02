#calculates pay, including overtime pay
hours=input("Enter hours")
rate=input("Enter rate")
if float(hours)>40:
    ot=float(hours)-40
    base=40*float(rate)
    otp=float(ot)*float(rate)*1.5
    pay=float(base)+float(otp)
    print("Total pay:", pay)
else:
    pay=float(hours)*float(rate)
    print("Total pay:", pay)
