import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import mysql.connector as con

main_window = tk.Tk()
main_window.title("Blood Bank Management System")
main_window.geometry("1500x775")

# Create variables to use

first_name = tk.StringVar
last_name = tk.StringVar
blood_group = tk.StringVar
age = tk.StringVar
gender = tk.StringVar
date_of_req_donation = tk.StringVar
date_of_receiving = tk.StringVar
phone_number = tk.StringVar
house_name = tk.StringVar
area  = tk.StringVar
city = tk.StringVar
pincode = tk.StringVar
blood_bag_number = tk.IntVar
search_blood_group = tk.StringVar
hb_content = tk.StringVar
blood_amount = tk.StringVar
blood_type = tk.StringVar
blood_cost = tk.StringVar
blood_description = tk.StringVar
employee_id = tk.IntVar
donor_id = tk.IntVar
receiver_id = tk.IntVar
emp_first_name = tk.StringVar
emp_last_name = tk.StringVar
emp_phone_number = tk.StringVar
emp_house_name = tk.StringVar
emp_area  = tk.StringVar
emp_city = tk.StringVar
emp_pincode = tk.StringVar

# Create functions

def show_table():
    search_blood_group = searchbloodtext.get()
    searchbloodtext.delete(0,END)
    blood =  tk.Tk()
    blood.title("Blood table")
    blood.geometry("1200x500")
    scroll_y = ttk.Scrollbar(blood, orient = VERTICAL)
    blood_table = ttk.Treeview(blood, column=('BloodBagNumber', 'HaemoglobinContent', 'BloodAmount', 'BloodType', 'Cost', 'Description'), yscrollcommand= scroll_y.set)
    scroll_y.pack(side=RIGHT, fill= Y)
    scroll_y = ttk.Scrollbar(command= blood_table.yview)

    blood_table.heading('BloodBagNumber', text="Blood Bag Number",anchor='c')
    blood_table.heading('HaemoglobinContent', text="Haemoglobin Content",anchor='c')
    blood_table.heading('BloodAmount', text="Blood Amount",anchor='c')
    blood_table.heading('BloodType', text="Blood Group",anchor='c')
    blood_table.heading('Cost', text="Cost",anchor='c')
    blood_table.heading('Description', text="Availability",anchor='c')
    blood_table['show'] = 'headings'
    blood_table.pack(fill=BOTH, expand=1)

    mydb = con.connect(host = 'localhost', user = 'root', passwd = 'qwerty', database = 'bloodbank')
    cur = mydb.cursor()
    cur.execute("select * from blood where BloodType = '{}'".format(search_blood_group))
    r_set = cur.fetchall()
    for i in r_set:
        blood_table.insert("",END, values= (i[0],i[1],i[2],i[3],i[4],i[5]))
    blood.mainloop()
    mydb.close()

def donation():
    first_name = bldfnametext.get()
    last_name = bldlnametext.get()
    blood_group = bldbloodgrptext.get()
    age = bldagetext.get()
    gender = bldgendertext.get()
    date_of_req_donation = blddonorreqdatetext.get()
    phone_number = bldphnumbertext.get()
    house_name = bldhousenametext.get()
    area = bldareatext.get()
    city = bldcitytext.get()
    pincode = bldpincodetext.get()
    emp_first_name = empfnametext.get()
    emp_last_name = emplnametext.get()
    emp_phone_number = empphnumbertext.get()
    emp_house_name = emphousenametext.get()
    emp_area = empareatext.get()
    emp_city = empcitytext.get()
    emp_pincode = emppincodetext.get()
    hb_content = bloodhbcontenttext.get()
    blood_amount = bloodbloodamounttext.get()
    blood_type = bloodbloodtypetext.get()
    blood_cost = bloodbloodcosttext.get()
    blood_description = bloodblooddescriptiontext.get()
    employee_id = empemployeeidtext.get()
    
    mydb = con.connect(host = 'localhost', user = 'root', passwd = 'qwerty', database = 'bloodbank')
    
    cur = mydb.cursor()
    cur.execute("insert into blood (HaemoglobinContent, BloodAmount, BloodType, Cost, Description) values (%s, %s, %s, %s, %s)",(hb_content, blood_amount, blood_type, blood_cost, blood_description))
    mydb.commit()
    
    cur2 = mydb.cursor()
    cur2.execute("select BloodBagNumber from blood where HaemoglobinContent = '{}' and Bloodtype  = '{}' and BloodAmount = '{}' and Cost = '{}' and Description = '{}'".format(hb_content,blood_type,blood_amount,blood_cost,blood_description))
    result = cur2.fetchone()
    blood_bag_number = result[0]
    print(blood_bag_number)
    mydb.close()
    
    mydb2 = con.connect(host = 'localhost', user = 'root', passwd = 'qwerty', database = 'bloodbank')
    cur3 = mydb2.cursor()
    query = ("insert into blooddonor (FirstName, LastName, BloodType, Age, Gender, DateOfDonation, PhoneNumber, HouseName, Area, City, PinCode, Blood_BloodBagNumber) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    values = (first_name, last_name,blood_group,age,gender,date_of_req_donation,phone_number,house_name,area,city,pincode,blood_bag_number)
    cur3.execute(query,values)
    mydb2.commit()
    
    cur4 = mydb2.cursor()
    cur4.execute("select DonorID from blooddonor where Blood_BloodBagNumber = '{}'".format(blood_bag_number))
    result2 = cur4.fetchone()
    donor_id = result2[0]
    print(donor_id)
    mydb2.close()

    mydb3 = con.connect(host = 'localhost', user = 'root', passwd = 'qwerty', database = 'bloodbank')
    if(employee_id == ''):
        cur5 = mydb3.cursor()
        query2 = ("insert into employee (EmpFirstName, EmpLastName, EmpSalary, EmpHouseName, EmpArea, EmpCity, EmpPinCode, EmpPhoneNumber, BloodBagNumber) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values2 = (emp_first_name, emp_last_name, '40000', emp_house_name, emp_area, emp_city, emp_pincode, emp_phone_number, blood_bag_number)
        cur5.execute(query2,values2)
        mydb3.commit()

        cur6 = mydb3.cursor()
        cur6.execute("select EmpID from employee where BloodBagNumber = '{}'".format(blood_bag_number))
        result3 = cur6.fetchone()
        employee_id = result3[0]
        print(employee_id)
        mydb3.close()

    mydb4 = con.connect(host = 'localhost', user = 'root', passwd = 'qwerty', database = 'bloodbank')
    cur7 = mydb4.cursor()
    query3 = ("insert into employee_has_blooddonor (Employee_EmpID, BloodDonor_DonorID) values (%s, %s)")
    values3 = (employee_id, donor_id)
    cur7.execute(query3,values3)
    mydb4.commit()
    print("Done")

    for i in bldinputlist:
        i.delete(0,END)
    for i in empinputlist:
        i.delete(0,END)
    for i in bloodinputlist:
        i.delete(0,END)

    messagebox.showinfo("Blood Donation", "Blood Donated successfully")

def receiving():
    emp_first_name = empfnametext.get()
    emp_last_name = emplnametext.get()
    emp_phone_number = empphnumbertext.get()
    emp_house_name = emphousenametext.get()
    emp_area = empareatext.get()
    emp_city = empcitytext.get()
    emp_pincode = emppincodetext.get()
    employee_id = empemployeeidtext.get()
    first_name = bldfnametext.get()
    last_name = bldlnametext.get()
    blood_group = bldbloodgrptext.get()
    age = bldagetext.get()
    gender = bldgendertext.get()
    date_of_req_donation = blddonorreqdatetext.get()
    date_of_receiving = blddoreceivingtext.get()
    blood_bag_number = bldbloodbagnumbertext.get()

    mydb = con.connect(host = 'localhost', user = 'root', passwd = 'qwerty', database = 'bloodbank')
    cur = mydb.cursor()
    query1 = ("insert into receipant (RecFirstName, RecLastName, RecBloodType, RecAge, RecGender, DateOfRequest, DateOfReceiving, Blood_BloodBagNumber) values (%s, %s, %s, %s, %s, %s, %s, %s)")
    values1 = (first_name, last_name, blood_group, age, gender, date_of_req_donation, date_of_receiving, blood_bag_number)
    cur.execute(query1,values1)
    mydb.commit()

    cur2 = mydb.cursor()
    cur2.execute("select RecID from receipant where Blood_BloodBagNumber = '{}'".format(blood_bag_number))
    result = cur2.fetchone()
    receiver_id = result[0]
    print(receiver_id)
    mydb.close()

    mydb2 = con.connect(host = 'localhost', user = 'root', passwd = 'qwerty', database = 'bloodbank')
    cur3 = mydb2.cursor()
    cur3.execute("update blood set Description = 'unavailable' where BloodBagNumber = '{}'".format(blood_bag_number))
    mydb2.commit()
    mydb2.close()

    mydb3 = con.connect(host = 'localhost', user = 'root', passwd = 'qwerty', database = 'bloodbank')
    if(employee_id == ''):
        cur4 = mydb3.cursor()
        query2 = ("insert into employee (EmpFirstName, EmpLastName, EmpSalary, EmpHouseName, EmpArea, EmpCity, EmpPinCode, EmpPhoneNumber, BloodBagNumber) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values2 = (emp_first_name, emp_last_name, '40000', emp_house_name, emp_area, emp_city, emp_pincode, emp_phone_number, blood_bag_number)
        cur4.execute(query2,values2)
        mydb3.commit()

        cur5 = mydb3.cursor()
        cur5.execute("select EmpID from employee where BloodBagNumber = '{}'".format(blood_bag_number))
        result2 = cur5.fetchone()
        employee_id = result2[0]
        print(employee_id)
        mydb3.close()
    
    mydb4 = con.connect(host = 'localhost', user = 'root', passwd = 'qwerty', database = 'bloodbank')
    cur6 = mydb4.cursor()
    query3 = ("insert into employee_has_receipant (Employee_EmpID, Receipant_RecID) values (%s, %s)")
    values3 = (employee_id, receiver_id)
    cur6.execute(query3,values3)
    mydb4.commit()
    print("Done")

    for i in bldinputlist:
        i.delete(0,END)
    for i in empinputlist:
        i.delete(0,END)
    for i in bloodinputlist:
        i.delete(0,END)

    messagebox.showinfo("Blood Reception", "Blood Received successfully")


# Create main window

mainlabel = tk.Label(main_window, text="BLOOD BANK MANAGEMENT SYSTEM", font = ("Rockwell" ,25 ,"bold" ), pady = 10).pack(side=TOP, fill=X)

# Create Frames to get input

leftframe = tk.LabelFrame(main_window, text= "Blood Donor/Receiver Information", font=  ("Rockwell", 16, "bold"),bd = 5, relief = RIDGE)
leftframe.place(x=10, y=60, height=490, width = 725)
rightframetop = tk.LabelFrame(main_window, text= "Employee Information", font=  ("Rockwell", 16, "bold"),bd = 5, relief = RIDGE)
rightframetop.place(x=765, y=60, height=300, width = 725)
rightframebelow = tk.LabelFrame(main_window, text= "Blood Information (For donation only)", font=  ("Rockwell", 16, "bold"),bd = 5, relief = RIDGE)
rightframebelow.place(x=765, y=370, height=205, width = 725)

# Labels of left side

bldfname = tk.Label(leftframe, text = "First Name:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 0, column= 0)
bldfnametext = tk.Entry(leftframe, font= ("Rockwell", 12),  width = 45, textvariable= first_name)
bldfnametext.grid(row=0,column=1)
bldlname = tk.Label(leftframe, text = "Last Name:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 1, column= 0)
bldlnametext = tk.Entry(leftframe, font= ("Rockwell", 12),  width = 45, textvariable= last_name)
bldlnametext.grid(row=1,column=1)
bldbloodgrp = tk.Label(leftframe, text = "Blood Group:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 2, column= 0)
bldbloodgrptext = tk.Entry(leftframe, font= ("Rockwell", 12),  width = 45, textvariable= blood_group)
bldbloodgrptext.grid(row=2,column=1)
bldage = tk.Label(leftframe, text = "Age:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 3, column= 0)
bldagetext = tk.Entry(leftframe, font= ("Rockwell", 12),  width = 45, textvariable= age)
bldagetext.grid(row=3,column=1)
bldgender = tk.Label(leftframe, text = "Gender:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 4, column= 0)
bldgendertext = tk.Entry(leftframe, font= ("Rockwell", 12),  width = 45, textvariable= gender)
bldgendertext.grid(row=4,column=1)
blddonorreqdate = tk.Label(leftframe, text = "Date of donation/request:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 5, column= 0)
blddonorreqdatetext = tk.Entry(leftframe, font= ("Rockwell", 12),  width = 45, textvariable= date_of_req_donation)
blddonorreqdatetext.grid(row=5,column=1)
blddoreceiving = tk.Label(leftframe, text = "Date of receiving (for reciver):", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 6, column= 0)
blddoreceivingtext = tk.Entry(leftframe, font= ("Rockwell", 12),  width = 45, textvariable= date_of_receiving)
blddoreceivingtext.grid(row=6,column=1)
bldphnumber = tk.Label(leftframe, text = "Contact Number (for donor):", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 7, column= 0)
bldphnumbertext = tk.Entry(leftframe, font= ("Rockwell", 12),  width = 45, textvariable= phone_number)
bldphnumbertext.grid(row=7,column=1)
bldhousename = tk.Label(leftframe, text = "House Name(for donor):", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 8, column= 0)
bldhousenametext = tk.Entry(leftframe, font= ("Rockwell", 12),  width = 45, textvariable= house_name)
bldhousenametext.grid(row=8,column=1)
bldarea = tk.Label(leftframe, text = "Area(for donor):", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 9, column= 0)
bldareatext = tk.Entry(leftframe, font= ("Rockwell", 12),  width = 45, textvariable= area)
bldareatext.grid(row=9,column=1)
bldcity = tk.Label(leftframe, text = "City(for donor):", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 10, column= 0)
bldcitytext = tk.Entry(leftframe, font= ("Rockwell", 12),  width = 45, textvariable= city)
bldcitytext.grid(row=10,column=1)
bldpincode = tk.Label(leftframe, text = "Pin Code(for donor):", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 11, column= 0)
bldpincodetext = tk.Entry(leftframe, font= ("Rockwell", 12),  width = 45, textvariable= pincode)
bldpincodetext.grid(row=11, column=1)
bldbloodbagnumber =  tk.Label(leftframe, text = "Blood Bag No.(for receiver):", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 12, column= 0)
bldbloodbagnumbertext = tk.Entry(leftframe, font= ("Rockwell", 12),  width = 45, textvariable= blood_bag_number)
bldbloodbagnumbertext.grid(row=12,column=1)

# Labels of right side bottom

bloodhbcontent = tk.Label(rightframebelow, text = "HB content:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 0, column= 0)
bloodhbcontenttext = tk.Entry(rightframebelow, font= ("Rockwell", 12),  width = 57, textvariable= hb_content)
bloodhbcontenttext.grid(row=0,column=1)
bloodbloodamount = tk.Label(rightframebelow, text = "Blood Amount:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 1, column= 0)
bloodbloodamounttext = tk.Entry(rightframebelow, font= ("Rockwell", 12),  width = 57, textvariable= blood_amount)
bloodbloodamounttext.grid(row=1,column=1)
bloodbloodtype = tk.Label(rightframebelow, text = "Blood Type:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 2, column= 0)
bloodbloodtypetext = tk.Entry(rightframebelow, font= ("Rockwell", 12),  width = 57, textvariable= blood_type)
bloodbloodtypetext.grid(row=2,column=1)
bloodbloodcost = tk.Label(rightframebelow, text = "Blood Cost:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 3, column= 0)
bloodbloodcosttext = tk.Entry(rightframebelow, font= ("Rockwell", 12),  width = 57, textvariable= blood_cost)
bloodbloodcosttext.grid(row=3,column=1)
bloodblooddescription = tk.Label(rightframebelow, text = "Blood availability:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 4, column= 0)
bloodblooddescriptiontext = tk.Entry(rightframebelow, font= ("Rockwell", 12),  width = 57, textvariable= blood_description)
bloodblooddescriptiontext.grid(row=4,column=1)

# Labels of right side top

empfname = tk.Label(rightframetop, text = "First Name:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 0, column= 0)
empfnametext = tk.Entry(rightframetop, font= ("Rockwell", 12),  width = 40, textvariable= emp_first_name)
empfnametext.grid(row=0,column=1)
emplname = tk.Label(rightframetop, text = "Last Name:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 1, column= 0)
emplnametext = tk.Entry(rightframetop, font= ("Rockwell", 12),  width = 40, textvariable= emp_last_name)
emplnametext.grid(row=1,column=1)
empphnumber = tk.Label(rightframetop, text = "Contact Number:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 2, column= 0)
empphnumbertext = tk.Entry(rightframetop, font= ("Rockwell", 12),  width = 40, textvariable= emp_phone_number)
empphnumbertext.grid(row=2,column=1)
emphousename = tk.Label(rightframetop, text = "House Name:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 3, column= 0)
emphousenametext = tk.Entry(rightframetop, font= ("Rockwell", 12),  width = 40, textvariable= emp_house_name)
emphousenametext.grid(row=3,column=1)
emparea = tk.Label(rightframetop, text = "Area:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 4, column= 0)
empareatext = tk.Entry(rightframetop, font= ("Rockwell", 12),  width = 40, textvariable= emp_area)
empareatext.grid(row=4,column=1)
empcity = tk.Label(rightframetop, text = "City:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 5, column= 0)
empcitytext = tk.Entry(rightframetop, font= ("Rockwell", 12),  width = 40, textvariable= emp_city)
empcitytext.grid(row=5,column=1)
emppincode = tk.Label(rightframetop, text = "Pin Code:", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 6, column= 0)
emppincodetext = tk.Entry(rightframetop, font= ("Rockwell", 12),  width = 40, textvariable= emp_pincode)
emppincodetext.grid(row=6,column=1)
empemployeeid =  tk.Label(rightframetop, text = "Employee ID(registered employees):", font = ("Rockwell", 12, "bold"),padx=5, pady= 5).grid(row= 7, column= 0)
empemployeeidtext = tk.Entry(rightframetop, font= ("Rockwell", 12),  width = 40, textvariable= employee_id)
empemployeeidtext.grid(row = 7,column=1)

# list of text input variable names

empinputlist = [empfnametext,emplnametext,empphnumbertext,emphousenametext,empareatext,empcitytext,emppincodetext]
blddonorinputlist = [bldfnametext, bldlnametext,bldbloodgrptext, bldagetext,bldgendertext, blddonorreqdatetext, bldphnumbertext, bldhousenametext, bldareatext, bldcitytext, bldpincodetext]
bldreceiverinputtext = [bldfnametext, bldlnametext,bldbloodgrptext, bldagetext,bldgendertext, blddonorreqdatetext,blddoreceivingtext]
bldinputlist = [bldfnametext, bldlnametext,bldbloodgrptext, bldagetext,bldgendertext, blddonorreqdatetext, blddoreceivingtext, bldphnumbertext, bldhousenametext, bldareatext, bldcitytext, bldpincodetext]
bloodinputlist = [bloodhbcontenttext, bloodbloodamounttext, bloodbloodtypetext, bloodbloodcosttext, bloodblooddescriptiontext]

# Create buttons and their labels

Donatebldbtn = tk.Button(main_window, text="Donate Blood", font = ("Rockwell", 12, "bold"),padx=10, pady= 10, bg= "red", fg="White",command=donation).place(x=10, y= 575)
receivebldbtn = tk.Button(main_window, text="Receive Blood", font = ("Rockwell", 12, "bold"),padx=10, pady= 10, bg= "red", fg="White",command=receiving).place(x=175, y= 575)
searchblood =  tk.Label(main_window, text="Search using blood group:", font = ("Rockwell", 12, "bold"),padx=10, pady= 10).place(x=10, y= 650)
searchbloodtext = tk.Entry(main_window, font = ("Rockwell", 12), width = 60)
searchbloodtext.place(x=240, y= 662)
searchbloodbutton = tk.Button(main_window, text="Search", font = ("Rockwell", 12, "bold"),padx=5, pady= 5, bg= "red", fg="White",command=show_table).place(x=800, y= 650)

main_window.mainloop()