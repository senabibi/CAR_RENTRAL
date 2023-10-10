import math
def excess():
    print("At the prompt,please enter the following:")
    print("Number of days the vehicle was rented (an integer)")
    print("Odometer reading at the start of the rental period (an integer)")
    print("Odometer reading at the end of the rental period (an integer) ")
def b(d,miles):
    base_day=40*d  
    mileage_charge=miles*0.25
    sum=mileage_charge+base_day    
    return sum
def d(d,miles):
    base_day=60*d 
    upper=(miles/d)
    if upper<=100:
        sum=base_day
    else:
        add=(upper-100)*0.25
        sum=add+base_day
    return sum

def w(d,miles):
    week=math.ceil(d/7)
    base_charge=week*190
    upper=((miles)/week)
    if upper<=900:
        sum=base_charge
    elif 900<upper<1500:
        sum=(base_charge+(100*week))
    elif 1500<upper:
        sum=(base_charge+(200*week)+(((upper-1500)*0.25)*week))
       
    return sum
def s(code,day,start,end,miles,sum):
    print("Customer summary:")
    print(f"\tClassification code:{code}")
    print(f"\trental period (days):{day}")
    print(f"\tOdometer reading at start:{start}")
    print(f"\tOdometer reading at the end: {end}")
    print(f"\tnumber of miles driven:{miles}")
    print(f"\tamount due:${sum}")
def rental():
    excess()
    c=['B','D','W']
    is_ok=False
    code=str(input("Customer code:")).upper()
    if code in c:
        is_ok=True
    while code!='Q' and is_ok:
        day=int(input("Number of days:"))
        start=int(input("Odometer reading at the start:"))
        end=int(input("Odometer reading at the end:"))
        if end>=start:
            miles=(end-start)/10
        else:
            miles=(end+(10**6-start))/10  
        if code=='B':
            sum=b(day,miles)
            s(code,day,start,end,miles,sum)
        elif code=='D':
            sum=d(day,miles)
            s(code,day,start,end,miles,sum)
        elif code=='W':
            sum=w(day,miles)
            s(code,day,start,end,miles,sum)
        code=str(input("Customer code:")).upper()
    
    if code=='Q':
        exit()
rental()
    

