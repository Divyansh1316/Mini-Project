from tkinter import*
from tkinter import messagebox
import random,os

#functionality

def clear():
    bathsoapEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    facewashEntry.delete(0,END)
    hairsprayEntry.delete(0,END)
    hairgelEntry.delete(0,END)
    bodylotionEntry.delete(0,END)
    riceEntry.delete(0,END)
    oilEntry.delete(0,END)
    daalEntry.delete(0,END)
    wheatEntry.delete(0,END)
    sugarEntry.delete(0,END)
    teaEntry.delete(0,END)
    pepsiEntry.delete(0,END)
    colaEntry.delete(0,END)
    frootiEntry.delete(0,END)
    maazaEntry.delete(0,END)
    gatoradeEntry.delete(0,END)
    limcaEntry.delete(0,END)
    
    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    hairsprayEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    bodylotionEntry.insert(0,0)
    riceEntry.insert(0,0)
    oilEntry.insert(0,0)
    daalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    sugarEntry.insert(0,0)
    teaEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    colaEntry.insert(0,0)
    frootiEntry.insert(0,0)
    maazaEntry.insert(0,0)
    gatoradeEntry.insert(0,0)
    limcaEntry.insert(0,0)
    
    cosmeticstaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    drinkstaxEntry.delete(0,END)

    cosmeticspriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    drinkspriceEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    addressEntry.delete(0,END)

    textArea.delete(1.0,END) #1.0 means row 1 column 0

if not os.path.exists("bills"):
    os.mkdir("bills")

def save_bill():
    global billnumber
    result=messagebox.askyesno("Confirm","Do you want to save the bill ?")
    if result:
        bill_content=textArea.get(1.0,END) #stores everything on the bill area to the variable from start to end
        file=open(f"bills/{billnumber}.txt","w")
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Suceess",f"Bill number {billnumber}is saved succesfull")
        billnumber=random.randint(500,1000)

billnumber=random.randint(500,1000)

def bill_area():
    if(nameEntry.get()=="" or phoneEntry.get()=="" or addressEntry.get()==""):
        messagebox.showerror("Error","Customer details are required") #this prints this message when no name is provided
    elif cosmeticspriceEntry.get()=="" and grocerypriceEntry.get()=="" and drinkspriceEntry.get()=="":
        messagebox.showerror("Error","No products are selected") 
    elif cosmeticspriceEntry.get()=="0 Rs" and grocerypriceEntry.get()=="0 Rs" and drinkspriceEntry.get()=="0 Rs":
        messagebox.showerror("Error","No products are selected") 
    else:
        textArea.delete(1.0,END)
        textArea.insert(END,"\t\t**WELCOME CUSTOMER**\n") #since nothing is inserted so END positin will be the starting position only
        textArea.insert(END,f"\nBill Number : {billnumber}\n")
        textArea.insert(END,f"\nCustomer Name : {nameEntry.get()}\n")
        textArea.insert(END,f"\nCustomer Ph no. : {phoneEntry.get()}\n")
        textArea.insert(END,f"\nCustomer Address : {addressEntry.get()}\n")
        textArea.insert(END,"\n======================================================")
        textArea.insert(END,"\nProduct\t\t\tQuantity\t\t\tPrice")
        textArea.insert(END,"\n======================================================")
     
        if(bathsoapEntry.get()!="0"):
            textArea.insert(END,f"\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs") #we had to make soapprice global as its in another function.
        if(facecreamEntry.get()!="0"):
            textArea.insert(END,f"\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs")
        if(facewashEntry.get()!="0"):
            textArea.insert(END,f"\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs")
        if(hairsprayEntry.get()!="0"):
            textArea.insert(END,f"\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs")
        if(hairgelEntry.get()!="0"):
            textArea.insert(END,f"\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs")
        if(bodylotionEntry.get()!="0"):
            textArea.insert(END,f"\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs")
     
        if(riceEntry.get()!="0"):
            textArea.insert(END,f"\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs")
        if(oilEntry.get()!="0"):
            textArea.insert(END,f"\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs")
        if(daalEntry.get()!="0"):
            textArea.insert(END,f"\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs")
        if(wheatEntry.get()!="0"):
            textArea.insert(END,f"\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs")
        if(sugarEntry.get()!="0"):
            textArea.insert(END,f"\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs")
        if(teaEntry.get()!="0"):
            textArea.insert(END,f"\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs")
     
        if(pepsiEntry.get()!="0"):
            textArea.insert(END,f"\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs") 
        if(colaEntry.get()!="0"):
            textArea.insert(END,f"\nCola\t\t\t{colaEntry.get()}\t\t\t{colaprice} Rs")
        if(frootiEntry.get()!="0"):
            textArea.insert(END,f"\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs")
        if(maazaEntry.get()!="0"):
            textArea.insert(END,f"\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs")
        if(gatoradeEntry.get()!="0"):
            textArea.insert(END,f"\nGatorade\t\t\t{gatoradeEntry.get()}\t\t\t{gatoradeprice} Rs")
        if(limcaEntry.get()!="0"):
            textArea.insert(END,f"\nLimca\t\t\t{limcaEntry.get()}\t\t\t{limcaprice} Rs")
        
        textArea.insert(END,"\n------------------------------------------------------")
        if(cosmeticstaxEntry.get()!="0.0 Rs"):
            textArea.insert(END,f"\nCosmetics Tax\t\t\t{cosmeticstaxEntry.get()}")
        if(grocerytaxEntry.get()!="0.0 Rs"):
            textArea.insert(END,f"\nGroceries Tax\t\t\t{grocerytaxEntry.get()}")
        if(drinkstaxEntry.get()!="0.0 Rs"):
            textArea.insert(END,f"\nDrinks Tax\t\t\t{drinkstaxEntry.get()}")
        textArea.insert(END,f"\nMembership Discount \t\t\t {membership_discount:.2f} Rs")
        textArea.insert(END,f"\nFlat Discount \t\t\t {flat_discount:.2f} Rs")
        textArea.insert(END,f"\nTotal Bill \t\t\t {totalbill:.2f} Rs")
        textArea.insert(END,"\n------------------------------------------------------")
        save_bill()

def total():
    #cosmetics price calculation
    
    global soapprice,facecreamprice,facewashprice,hairsprayprice,hairgelprice,bodylotionprice
    global riceprice,oilprice,daalprice,wheatprice,sugarprice,teaprice
    global pepsiprice,colaprice,frootiprice,maazaprice,gatoradeprice,limcaprice
    global totalbill,membership_discount,flat_discount
    
    soapprice=int(bathsoapEntry.get())*20 #get is used to take input from user and store it in soapvalue variable. also it will return a string, so we have to convert it into an integer. here 20 is price of 1 soap
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairsprayprice=int(hairsprayEntry.get())*150
    hairgelprice=int(hairgelEntry.get())*80
    bodylotionprice=int(bodylotionEntry.get())*60
    
    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticspriceEntry.delete(0,END) #this will delete the repeated text when we hit total button multiple times, i.e 0
    cosmeticspriceEntry.insert(0,f"{totalcosmeticprice} Rs") #insert is used to display the data on the field
    
    cosmeticstax=totalcosmeticprice*0.12
    cosmeticstaxEntry.delete(0,END)
    cosmeticstaxEntry.insert(0,str(cosmeticstax)+" Rs")    
    
    #grocery price calculation

    riceprice=int(riceEntry.get())*100
    daalprice=int(daalEntry.get())*70
    oilprice=int(oilEntry.get())*60
    sugarprice=int(sugarEntry.get())*50
    teaprice=int(teaEntry.get())*80
    wheatprice=int(wheatEntry.get())*180
    
    totalgroceryprice=riceprice+daalprice+oilprice+sugarprice+teaprice+wheatprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,str(totalgroceryprice)+" Rs")
    
    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocerytax)+" Rs")    
    
    #Cold drink price calculation pepsi cola frooti maaza gatorade limca

    pepsiprice=int(pepsiEntry.get())*20
    colaprice=int(colaEntry.get())*30
    frootiprice=int(frootiEntry.get())*10
    maazaprice=int(maazaEntry.get())*15
    gatoradeprice=int(gatoradeEntry.get())*50
    limcaprice=int(limcaEntry.get())*40
    
    totaldrinksprice=pepsiprice+colaprice+frootiprice+maazaprice+gatoradeprice+limcaprice
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,str(totaldrinksprice)+" Rs")

    drinkstax=totaldrinksprice*0.08
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,str(drinkstax)+" Rs")

    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinksprice+cosmeticstax+grocerytax+drinkstax
    
    flat_discount=0
    membership_discount=0

    if totalbill>500:
        flat_discount=totalbill*0.05
        totalbill-=flat_discount
    
    if membership_var.get()==1:
        if totalbill>250:
            membership_discount+=totalbill*0.02
            if totalgroceryprice>250:
                membership_discount+=totalgroceryprice*0.02
        totalbill-=membership_discount

#GUI
root=Tk()   #root is an object of Tk() class, which represents the main window
root.geometry("1290x685")
headlingLabel=Label(root,text="GEU Shopping Mart",font=("Outfit",30,"bold"),bg="yellow") #headlingLable is an object of the Label class, and since we want it to display in the window so we have passed root as an argument we cant see this as we haven't positioned it yet so we have to use pack method.
headlingLabel.pack(side="top",fill=X,pady=10) #this brings the text to the top and fills it in the X axis

customer_details_frame=LabelFrame(root,text="Customer Details",font=("Outfit",15,"bold")) #we cant see this as we haven't positioned it yet so we have to use pack method.
customer_details_frame.pack(fill=X,padx=10) #this will help it position the labelframe, but the content is only displayed when there is something present in the labelframe.

#main difference between Label and LabelFrame is that LabelFrame is a container which can store other widgets inside it.

nameLabel=Label(customer_details_frame,text="Name",font=("Outfit",15,"bold")) #this creates a name field/label
nameLabel.grid(row=0,column=0,padx=40) #this adds in the form of rows and columns and adds padding on left and right side of Name
nameEntry=Entry(customer_details_frame,font=("Outfit",10)) #adds an entry field or a box for adding name
nameEntry.grid(row=0,column=1,padx=8) #used for positioning

phoneLabel=Label(customer_details_frame,text="Phone Number",font=("Outfit",15,"bold"))
phoneLabel.grid(row=0,column=2,padx=40,pady=2)
phoneEntry=Entry(customer_details_frame,font=("Outfit",10))
phoneEntry.grid(row=0,column=3,padx=8)

addressLabel=Label(customer_details_frame,text="Address",font=("Outfit",15,"bold"))
addressLabel.grid(row=0,column=4,padx=40,pady=2)
addressEntry=Entry(customer_details_frame,font=("Outfit",10)) 
addressEntry.grid(row=0,column=5,padx=8) 

membership_var=IntVar()
membership_checkbox=Checkbutton(customer_details_frame,text="Member",variable=membership_var,font=("Outfit",15,"bold"))
membership_checkbox.grid(row=0,column=6,padx=8)
'''
searchButtom=Button(customer_details_frame,text="Search",font=("Outfit",15,"bold"))
searchButtom.grid(row=0,column=6,padx=10,pady=8)
'''

productsFrame=Frame(root)
productsFrame.pack(pady=10) #pack also moves content next to prev content

cosmeticsFrame=LabelFrame(productsFrame,text="Cosmetic",font=("Outfit",15,"bold"))
cosmeticsFrame.grid(row=0,column=0) #here we are using grid method as cosmetic is one of the elements of the grid

'''
for drop-down box
bathsoapLabel=Label(cosmeticsFrame,text="Bath Soap",font=("Outfit",15,"bold"))
bathsoapLabel.grid(row=0,column=0,pady=8)

bathsoapEntry=ttk.Combobox(cosmeticsFrame,text="Face Cream",font=("Outfit",15,"bold"))
bathsoapEntry.grid(row=0,column=1)
'''

bathsoapLabel=Label(cosmeticsFrame,text="Bath Soap",font=("Outfit",15,"bold"))
bathsoapLabel.grid(row=0,column=0,pady=8,padx=10,sticky="w") #sticky is used to align it to the left

bathsoapEntry=Entry(cosmeticsFrame,font=("Outfit",15,"bold"),width=10)
bathsoapEntry.grid(row=0,column=1,pady=8,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text="Face Cream",font=("Outfit",15,"bold"))
facecreamLabel.grid(row=1,column=0,pady=8,padx=10,sticky="w")

facecreamEntry=Entry(cosmeticsFrame,font=("Outfit",15,"bold"),width=10)
facecreamEntry.grid(row=1,column=1,pady=8,padx=10)
facecreamEntry.insert(0,0)


facewashLabel=Label(cosmeticsFrame,text="Face Wash",font=("Outfit",15,"bold"))
facewashLabel.grid(row=2,column=0,pady=8,padx=10,sticky="w")

facewashEntry=Entry(cosmeticsFrame,font=("Outfit",15,"bold"),width=10)
facewashEntry.grid(row=2,column=1,pady=8,padx=10)
facewashEntry.insert(0,0)

hairsprayLabel=Label(cosmeticsFrame,text="Hair Spray",font=("Outfit",15,"bold"))
hairsprayLabel.grid(row=3,column=0,pady=8,padx=10,sticky="w")

hairsprayEntry=Entry(cosmeticsFrame,font=("Outfit",15,"bold"),width=10)
hairsprayEntry.grid(row=3,column=1,pady=8,padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text="Hair Gel",font=("Outfit",15,"bold"))
hairgelLabel.grid(row=4,column=0,pady=8,padx=10,sticky="w")

hairgelEntry=Entry(cosmeticsFrame,font=("Outfit",15,"bold"),width=10)
hairgelEntry.grid(row=4,column=1,pady=8,padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticsFrame,text="Body Lotion",font=("Outfit",15,"bold"))
bodylotionLabel.grid(row=5,column=0,pady=8,padx=10,sticky="w")

bodylotionEntry=Entry(cosmeticsFrame,font=("Outfit",15,"bold"),width=10)
bodylotionEntry.grid(row=5,column=1,pady=8,padx=10)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text="Grocery",font=("Outfit",15,"bold"))
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text="Rice",font=("Outfit",15,"bold"))
riceLabel.grid(row=0,column=0,pady=8,padx=10,sticky="w")

riceEntry=Entry(groceryFrame,font=("Outfit",15,"bold"),width=10)
riceEntry.grid(row=0,column=1,pady=8,padx=10)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text="Oil",font=("Outfit",15,"bold"))
oilLabel.grid(row=1,column=0,pady=8,padx=10,sticky="w")

oilEntry=Entry(groceryFrame,font=("Outfit",15,"bold"),width=10)
oilEntry.grid(row=1,column=1,pady=8,padx=10)
oilEntry.insert(0,0)

daalLabel=Label(groceryFrame,text="Daal",font=("Outfit",15,"bold"))
daalLabel.grid(row=2,column=0,pady=8,padx=10,sticky="w")

daalEntry=Entry(groceryFrame,font=("Outfit",15,"bold"),width=10)
daalEntry.grid(row=2,column=1,pady=8,padx=10)
daalEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text="Wheat",font=("Outfit",15,"bold"))
wheatLabel.grid(row=3,column=0,pady=8,padx=10,sticky="w")

wheatEntry=Entry(groceryFrame,font=("Outfit",15,"bold"),width=10)
wheatEntry.grid(row=3,column=1,pady=8,padx=10)
wheatEntry.insert(0,0)

sugarLabel=Label(groceryFrame,text="Sugar",font=("Outfit",15,"bold"))
sugarLabel.grid(row=4,column=0,pady=8,padx=10,sticky="w")

sugarEntry=Entry(groceryFrame,font=("Outfit",15,"bold"),width=10)
sugarEntry.grid(row=4,column=1,pady=8,padx=10)
sugarEntry.insert(0,0)

teaLabel=Label(groceryFrame,text="Tea",font=("Outfit",15,"bold"))
teaLabel.grid(row=5,column=0,pady=8,padx=10,sticky="w")

teaEntry=Entry(groceryFrame,font=("Outfit",15,"bold"),width=10)
teaEntry.grid(row=5,column=1,pady=8,padx=10)
teaEntry.insert(0,0)

drinksFrame=LabelFrame(productsFrame,text="Drinks",font=("Outfit",15,"bold"))
drinksFrame.grid(row=0,column=2)

pepsiLabel=Label(drinksFrame,text="Pepsi",font=("Outfit",15,"bold"))
pepsiLabel.grid(row=0,column=0,pady=8,padx=10,sticky="w")

pepsiEntry=Entry(drinksFrame,font=("Outfit",15,"bold"),width=10)
pepsiEntry.grid(row=0,column=1,pady=8,padx=10)
pepsiEntry.insert(0,0)

colaLabel=Label(drinksFrame,text="Coca Cola",font=("Outfit",15,"bold"))
colaLabel.grid(row=1,column=0,pady=8,padx=10,sticky="w")

colaEntry=Entry(drinksFrame,font=("Outfit",15,"bold"),width=10)
colaEntry.grid(row=1,column=1,pady=8,padx=10)
colaEntry.insert(0,0)

frootiLabel=Label(drinksFrame,text="Frooti",font=("Outfit",15,"bold"))
frootiLabel.grid(row=2,column=0,pady=8,padx=10,sticky="w")

frootiEntry=Entry(drinksFrame,font=("Outfit",15,"bold"),width=10)
frootiEntry.grid(row=2,column=1,pady=8,padx=10)
frootiEntry.insert(0,0)

maazaLabel=Label(drinksFrame,text="Maaza",font=("Outfit",15,"bold"))
maazaLabel.grid(row=3,column=0,pady=8,padx=10,sticky="w")

maazaEntry=Entry(drinksFrame,font=("Outfit",15,"bold"),width=10)
maazaEntry.grid(row=3,column=1,pady=8,padx=10)
maazaEntry.insert(0,0)

gatoradeLabel=Label(drinksFrame,text="Gatorade",font=("Outfit",15,"bold"))
gatoradeLabel.grid(row=4,column=0,pady=8,padx=10,sticky="w")

gatoradeEntry=Entry(drinksFrame,font=("Outfit",15,"bold"),width=10)
gatoradeEntry.grid(row=4,column=1,pady=8,padx=10)
gatoradeEntry.insert(0,0)

limcaLabel=Label(drinksFrame,text="Limca",font=("Outfit",15,"bold"))
limcaLabel.grid(row=5,column=0,pady=8,padx=10,sticky="w")

limcaEntry=Entry(drinksFrame,font=("Outfit",15,"bold"),width=10)
limcaEntry.grid(row=5,column=1,pady=8,padx=10)
limcaEntry.insert(0,0)

billFrame=Frame(productsFrame)
billFrame.grid(row=0,column=3,padx=10)

billareaLabel=Label(billFrame,text="Bill Area",font=("Outfit",15,"bold"))
billareaLabel.pack()

scrollbar=Scrollbar(billFrame,orient="vertical")
scrollbar.pack(side="right",fill="y")

textArea=Text(billFrame,height=17,width=55,yscrollcommand=scrollbar.set) #this will make it scroll
textArea.pack()
scrollbar.config(command=textArea.yview) #confirguring the scroll bar to see the vertical view

billmenuFrame=LabelFrame(root,text="Bill Menu",font=("Outfit",15,"bold"))
billmenuFrame.pack()

cosmeticspriceLabel=Label(billmenuFrame,text="Cosmetics Price",font=("Outfit",15,"bold"))
cosmeticspriceLabel.grid(row=0,column=0,pady=8,padx=10,sticky="w")

cosmeticspriceEntry=Entry(billmenuFrame,font=("Outfit",15,"bold"),width=10)
cosmeticspriceEntry.grid(row=0,column=1,pady=8,padx=10)

grocerypriceLabel=Label(billmenuFrame,text="Grocery Price",font=("Outfit",15,"bold"))
grocerypriceLabel.grid(row=1,column=0,pady=8,padx=10,sticky="w")

grocerypriceEntry=Entry(billmenuFrame,font=("Outfit",15,"bold"),width=10)
grocerypriceEntry.grid(row=1,column=1,pady=8,padx=10)

drinkspriceLabel=Label(billmenuFrame,text="Drinks Price",font=("Outfit",15,"bold"))
drinkspriceLabel.grid(row=2,column=0,pady=8,padx=10,sticky="w")

drinkspriceEntry=Entry(billmenuFrame,font=("Outfit",15,"bold"),width=10)
drinkspriceEntry.grid(row=2,column=1,pady=8,padx=10)

cosmeticstaxLabel=Label(billmenuFrame,text="Cosmetics Tax",font=("Outfit",15,"bold"))
cosmeticstaxLabel.grid(row=0,column=2,pady=8,padx=10,sticky="w")

cosmeticstaxEntry=Entry(billmenuFrame,font=("Outfit",15,"bold"),width=10)
cosmeticstaxEntry.grid(row=0,column=3,pady=8,padx=10)

grocerytaxLabel=Label(billmenuFrame,text="Grocery Tax",font=("Outfit",15,"bold"))
grocerytaxLabel.grid(row=1,column=2,pady=8,padx=10,sticky="w")

grocerytaxEntry=Entry(billmenuFrame,font=("Outfit",15,"bold"),width=10)
grocerytaxEntry.grid(row=1,column=3,pady=8,padx=10)

drinkstaxLabel=Label(billmenuFrame,text="Drinks Tax",font=("Outfit",15,"bold"))
drinkstaxLabel.grid(row=2,column=2,pady=8,padx=10,sticky="w")

drinkstaxEntry=Entry(billmenuFrame,font=("Outfit",15,"bold"),width=10)
drinkstaxEntry.grid(row=2,column=3,pady=8,padx=10)

buttonFrame=Frame(billmenuFrame) #we used Frame instead of LabelFrame as LabelFrame adds border and we didn't want that
buttonFrame.grid(row=0,column=4,rowspan=3) #to make button at center or at 3 row spaces so add rowspan=3

totalButton=Button(buttonFrame,text="Total",font=("Outfit",15,"bold"),width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text="Bill",font=("Outfit",15,"bold"),width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

clearButton=Button(buttonFrame,text="Clear",font=("Outfit",15,"bold"),width=8,pady=10,command=clear)
clearButton.grid(row=0,column=2,pady=20,padx=5)

root.mainloop() #this holds the ui window at screen