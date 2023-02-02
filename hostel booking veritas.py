import random
import datetime
  
# Global List Declaration
name = []
phno = []
add = []
matricno = []
datebooked = []
price = []
p = []
roomno = []
bunkno = []
hostelname = []
paymentid = []
session = []
bunktype=[]
# Global Variable Declaration
  
i = 0
  
# Home Function
def Home():
     
    print("          ------VERITAS UNIVERSITY ABUJA -------             ")
    print("  Student affairs unit  ")
    print(" HOSTEL BOOKING  ")
    print(" 1 Hostel Booking")
    print(" 2 Hostel Info")
    print(" 3 Payment")
    print(" 4 Record")
    print(" 0 Exit")
  
    ht=int(input("->"))
     
    if ht == 1:
        print(" ")
        Hostel_Booking()
     
    elif ht == 2:
        print(" ")
        Hostel_Info()
     
    elif ht == 3:
        print(" ")
        Payment()
    elif ht == 4:
        print(" ")
        Record()
     
    else:
        print ("item is not omn the menu list")
        Home ()

 
# Function used in booking
  
def date(c):
     
    if c[2] >= 2021 and c[2] <= 2024:
         
        if c[1] != 0 and c[1] <= 12:
             
            if c[1] == 2 and c[0] != 0 and c[0] <= 31:
                 
                if c[2]%4 == 0 and c[0] <= 29:
                    pass
                 
                elif c[0]<29:
                    pass
                 
                else:
                    print("date not valid\n")
                    name.pop(i)
                    matricno (i)
                    phno.pop(i)
                    add.pop(i)
                    datebooked.pop(i)
                    session.pop(i)
                    Hostel_Booking()
             
             
            # if month is odd & less than equal
            # to 7th  month
            elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
                pass
             
            # if month is even & less than equal to 7th
            # month and not 2nd month
            elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:
                pass
             
            # if month is even & greater than equal
            # to 8th  month
            elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
                pass
             
            # if month is odd & greater than equal
            # to 8th  month
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30: 
                pass
             
            else:
               print("date not valid\n")
               name.pop(i)
               matricno (i)
               phno.pop(i)
               add.pop(i)
               datebooked.pop(i)
               session.pop(i)
               Hostel_Booking()
                 
        else:
            print("date not valid\n")
            name.pop(i)
            phno.pop(i)
            add.pop(i)
            datebooked.pop(i)
            session.pop(i)
            Hostel_Booking()
             
    else:
        print("date not valid\n")
        name.pop(i)
        phno.pop(i)
        add.pop(i)
        datebooked.pop(i)
        session.pop(i)
        Hostel_Booking()
  
  
# Booking function
def Hostel_Booking():
      # used global keyword to
        # use global variable 'i'
        global i
        print(" Book Hostels")
        print(" ")
        print("please fill all fields in block letters")
         
        while 1:
            n = str(input("Name: "))
            mn = str(input("Matric no: "))
            p1 = str(input("Phone No.: "))
            a = str(input("Address: "))
            
             
            # checks if any field is not empty
            if n!="" and p1!="" and a!="" and mn!="":
                name.append(n)
                add.append(a)
                phno.append(p1)
                break
                 
            else:
                 print("Name, Maric no, Phone no. & Address cannot be empty..!!")
                 Hostel_Booking()
              
        ses=str(input("session: "))
        session.append(ses)

          
        print(" ....SELECT HOSTEL ....")
        print(" 1. Male Hostel a-j")
        print(" 2. Male hostel k ")
        print(" 3. Malee hostel l ")
        print(" 4. Male hostel m ")
        print(("\t\tPress 5 for Hostel price"))
         
        ch=int(input("->"))
         
        # if-conditions to display Hosstels
        # type of hostels and it's price
        if ch==5:
            print(" 1. Male hostel a- j __ 130,000 naira")
            print(" 2. Male hostel k ______160,000 naira")
            print(" 3. Male hostel l _____ 180,000 naira")
            print(" 4. Male hostel m _____ 230,000 naira")
            ch=int(input("->"))
        if ch==1:
            hostelname.append('Male hostel a-j')
            print ("Male hostel a-j") 
            price.append(130000)
            print("Price- 130.000")
        elif ch==2:
            hostelname.append('Male hostel k')
            print("Male hostel k")
            price.append(160000)
            print("Price- 160,000")
        elif ch==3:
            hostelname.append('Male hostel l')
            print("Male hostel l")
            price.append(180000)
            print("Price- 180,000")
        elif ch==4:
            hostelname.append('Male hostel m')
            print("male hostel m")
            price.append(230000)
            print("Price- 230,000")
        else:
            print(" pick the hostels listed above..!!")

        coo=str(input("date booked: "))
        datebooked.append(coo)
        coo=coo.split('/')
        co=coo
        co[0]=int(co[0])
        co[1]=int(co[1])
        co[2]=int(co[2])

       
 
        
        
        # randomly generating room no. 
        rn = random.randint(1,200)
        bk = random.randint(1, 4)
        
         
        # checks if allotted room no. 
        # room no already not allotted
        while rn in roomno:
            rn = random.randint(1,300)
            bk = random.randint(1,5)
    
        p.append(0)
               
        if mn not in matricno:
            matricno.append(mn)
        elif mn in matricno:
            for n in range(0,i):
                if mn== matricno[n]:
                    if p[n]==1:
                        matricno.append(mn)
        elif mn in matricno:
            for n in range(0,i):
                if mn== matricno[n]:
                    if p[n]==0:
                        print("\tMatric no. already exists and payment yet not done..!!")
                        name.pop(i)
                        add.pop(i)
                        datebooked.pop(i)
                        session.pop(i)
                        phno.pop(i)
                        Hostel_Booking()
        print("")
        print("***HOSTEL AND ROOM BOOKED SUCCESSFULLY***\n")
        print (hostelname)
        print("Room No. - ",rn)
        print ("Bunk No.- ",bk)
        bt=random.randint(1,4)
        if bt ==1 or bt == 3:
            btt = ("up bunk")
            print(btt)
        else:
            bt ==2 or bt ==4
            btt = ("down bunk")
            print (btt)
        roomno.append(rn)
        bunkno.append(bk)
        bunktype.append(btt)
        
        i=i+1
        n=int(input("0-BACK\n ->"))
        if n==0:
            Home()
        else:
            exit()
 
# HoSTEL INFORMATION
def Hostel_Info():
    print("         ------ HOSTELS INFO ------")
    print()
    print("MALE HOTEL A-J")
    print("---------------------------------------------------------------")
    print("Room amenities include: Bunks, ceiling fan,")
    print("tiled floor, wooden door")
    print("toilet and bathroom is located outside\n")
    print ()
    print("MALE HOSTEL K")
    print("---------------------------------------------------------------")
    print("Room amenities include: 3 bunks , ceiling fans")
    print("rooms are arranged in corridors,  ")
    print("an attached toilet and bathroom in hostel + Window")
    print ()
    print("MALE HOSTEL L ")
    print("---------------------------------------------------------------")
    print("Room amenities include: 3 bunks or 4 bunks, ceiling fans")
    print("room are arranged in corridors")
    print("an attached toilet and bathroom in gostel + window")
    print ()
    print("MALE HOSTEL M")
    print("---------------------------------------------------------------")
    print("Room amenities include: 2 bunks, ceiling fan")
    print("1 storey building with a common room in each storey ")
    print("toilet is located in each of the rooms")
    print("toilet has showers, wc and washing basin")
    print()
    n=int(input("0-BACK\n ->"))
    if n==0:
        Home()
    else:
        exit()
 
      
                  
# PAYMENT FUNCTION            
def Payment():
    pid = random.randint(1,3000)
     
    ph=str(input("maric number: "))
    global i
    f=0
     
    for n in range(0,i):
        if ph==matricno[n] :
             
            # checks if payment is
            # not already done
             if p[n]==0:
                f=1
                print(" Payment")
                print(" --------------------------------")
                print("  MODE OF PAYMENT")
                  
                print("  1- Credit/Debit Card")
                print("  2- bank transfer")
                print("  3- ussd")
                print("  4- Cash")
                x=int(input("-> "))
                print("\n  Amount: ",(price[n]))
                if x == 2:
                    print("ACCOUNT NAME: veritas university Abuja")
                    print("ACCOUNT NUMBER: 2245340123")
                    print("BANK NAME: wema Bank plc")
                elif x == 4:
                    print("visit the schools bursary unit for payment")
                elif x==3:
                    ussd=str(input("USSD CODE: "))
                elif x == 1:
                    card = input("Card name: ")
                    cardnumber =input("Card Number: ")
                    cvv=input("CVV: ")
                    print ()
                    print("Please confirm card details")
                    print("Card name: ",card)
                    print("Card number: ",cardnumber)
                    print("cvv: ",cvv)
                    print("Are the details correct")
                    print ()
                    y = str(input("y/n:-"))
                    if y ==("n"):
                        Payment()
                    else:
                        y==("y")
                        print ("Payment made successfully!")
                continue
                print("\n            Pay For ",hostelname[n],"\t")
                print("  (y/n)")
                ch=str(input("->"))
                 
                if ch=='y' or ch=='Y':
                    print("\n\n --------------------------------")
                    print("           veritas university Abuja  ")
                    print(" ------------------------------------")
                    print("              Hostel pyment")
                    print(" ------------------------------------")
                    print ("VUNA             payment id: ", pid,"\n")
                    print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
                    print("\n Date booked: ",datebooked[n],"\t\n session: ",session[n],"\t matric no: ", matricno[n],"\t")
                    print("\n hostel : ",hostelname[n],"\t\n Room Charges: ",price[n],"\t")
                    print(" room no: \t", roomno[n], "\t\n bunk no: ",bunkno[n],"\t")
                    print(" Bunk type: ", bunktype[n])
                    print(" --------------------------------")
                    print("\n Total Amount: ",price[n],"\t")
                    print(" --------------------------------")
                    print(" print payment receipt      [::]" )
                    print(" --------------------------------\n")
                    paymentid.append(pid)
             else:
                 
                for j in range(n+1,i):
                    if ph==matricno[j] :
                        if p[j]==0:
                            pass
                         
                        else:
                            f=1
                            print("\n\tPayment has been Made :)\n\n")
    if f==0:   
        print("Invalid matric no Id")
         
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()
 
# RECORD FUNCTION
def Record():
     
    # checks if any record exists or not    
    if matricno!=[]:
        print(" *** HOSTEL RECORD ***\n")
        print ("-------------------------------------")
        for n in range(0,i):
            print("| Name : ", name[n])
            print("|matric no : ",matricno[n])
            print("| phone no. : ",phno[n])
            print("| Address :",add[n])
            print("| date booked|: ",datebooked[n])
            print("| hostel : " ,hostelname[n])
            print("| session : ",session[n])
            print("|room no : ",roomno[n])
            print("|bunk no : ", bunkno[n])
            print("|bunk type: ", bunktype[n])
            print("| amount paid : ", price[n])
            print ("----------------------------------")
            print ()
    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
         
    else:
        exit()
 
# Driver Code
Home()
