from tkinter import *

from tkinter import filedialog,messagebox import random
import time import requests

#functions


def reset(): textReciept.delete(1.0,END) e_Butter_Chicken.set('0') e_Chicken_Kolapuri.set('0') e_Telangana_Chicken.set('0') e_Mutton_Kheema.set('0') e_Mutton_Curry.set('0') e_Fish_Pulusu.set(0) e_Veg_Kofta.set('0') e_Butter_Panner.set('0') e_Mushroom.set('0') e_Chicken_Dum_Biryani.set('0') e_Chicken_Frypiece_Biryani.set('0') e_Chicken_Biryani_spl.set('0')
e_Mutton_Nallighosh_Biryani.set('0') e_Mutton_Juicy_Biryani.set("0") e_Fish_Biryani.set('0') e_Prawn_Biryani.set('0') e_Veg_Pulao.set('0') e_Panner_Biryani.set('0') e_Chicken_Mangolia.set('0') e_Chicken_Manchuria.set('0') e_Chicken_Drumsticks.set('0') e_Chicken_kabab.set('0') e_Egg_Manchuria.set('0') e_Veg_Manchuria.set('0') e_Fried_Mushroom.set('0') e_BabyCorn.set('0') e_Panner_Tikka.set('0')
textButter_Chicken.config(state=DISABLED) textChicken_Kolapuri.config(state=DISABLED) textTelangana_Chicken.config(state=DISABLED) textMutton_Kheema.config(state=DISABLED) textMutton_Curry.config(state=DISABLED) textFish_Pulusu.config(state=DISABLED) textVeg_Kofta.config(state=DISABLED) textButter_Panner.config(state=DISABLED) textMushroom.config(state=DISABLED) textChicken_Dum_Biryani.config(state=DISABLED) textChicken_Frypiece_Biryani.config(state=DISABLED) textChicken_Biryani_Spl.config(state=DISABLED) textMutton_Nallighosh_Biryani.config(state=DISABLED) textMutton_Juicy_Biryani.config(state=DISABLED) textFish_Biryani.config(state=DISABLED) textPrawn_Biryani.config(state=DISABLED) textVeg_Pulao.config(state=DISABLED) textPanner_Biryani.config(state=DISABLED)
 
textChicken_Mangolia.config(state=DISABLED) textChicken_Manchuria.config(state=DISABLED) textChicken_Drumsticks.config(state=DISABLED) textChicken_kabab.config(state=DISABLED) textEgg_Manchuria.config(state=DISABLED) textVeg_Manchuria.config(state=DISABLED) textFried_Mushroom.config(state=DISABLED) textBabyCorn.config(state=DISABLED) textPanner_Tikka.config(state=DISABLED)


var1.set(0) var2.set(0) var3.set(0) var4.set(0) var5.set(0) var6.set(0) var7.set(0) var8.set(0) var9.set(0) var10.set(0) var11.set(0) var12.set(0) var13.set(0) var14.set(0) var15.set(0) var16.set(0) var17.set(0) var18.set(0) var19.set(0) var20.set(0) var21.set(0) var22.set(0) var23.set(0) var24.set(0) var25.set(0) var26.set(0) var27.set(0)

costofMaincoursevar.set('') costofBiryanivar.set('') costofStartersvar.set('') costofSubtotalvar.set('') costofServicetaxvar.set('') costofTotalcostvar.set('')





def send():
def send_msg(): message=textarea.get(1.0,END) number=numberfield.get()
auth='YhKOpRoCA1MEdIcexnQUJb0GNT7XrByH9jagDvwV45ikL3zl8Wl5FOApSawH9kxcojL84KPzifJum0qB' url='https://www.fast2sms.com/dev/bulk'
 
params={ 'authorization':auth, 'message':message, 'numbers':number, 'sender-id':'CHKSMS',
"route":'p', 'language':'english'

}
response=requests.get(url,params=params) dic=response.json()
result=dic.get('return') if result==True:
messagebox.showinfo('send successfully','message sent successfully')

else:
messagebox.showerror('error','something went wrong')


root2=Toplevel() root2.title("Send Bill") root2.geometry('485x485+50+50')



numberLabel=Label(root2,text='Mobile Number',font=("arial",18,'bold')) numberLabel.pack() numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24) numberfield.pack()
billLabel=Label(root2,text="Bill Details",font=("arial",18,'bold underline')) billLabel.pack()



textarea=Text(root2,font=("arial",12,'bold'),width=42,height=14) textarea.pack()
textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n') if costofMaincoursevar.get()!=0:
textarea.insert(END, f'cost of Main course\t\t\t{priceofMaincourse}\n') if costofBiryanivar.get()!=0:
textarea.insert(END, f'cost of Biryani\t\t\t{priceofBiryani}\n') if costofStartersvar.get()!=0:
textarea.insert(END, f'cost of Starters\t\t\t{priceofStarters}\n') textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}\n') textarea.insert(END, f'Service Tax\t\t\t{50}\n') textarea.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}\n')
sendButton = Button(root2, text='SEND', font=("arial", 19, 'bold'), command=send_msg) sendButton.pack()
root2.mainloop() def save():
url=filedialog.asksaveasfile(mode="w", defaultextension='.txt')
 
bill_data=textReciept.get(1.0,END) url.write(bill_data)
url.close()



messagebox.showinfo('Information','Your Bill is Save') def receipt():
global billnumber, date textReciept.delete(1.0,END) x=random.randint(0,1000) billnumber="BILL"+str(x) date=time.strftime("%d/%m/%Y")
textReciept.insert(END,"Receipt ref:\t\t"+billnumber+'\t\t'+date+'\n') textReciept.insert(END,'*********************\n') textReciept.insert(END,'Items:\t\tCost of Items(Rs)\n') textReciept.insert(END, '*********************\n')
if e_Butter_Chicken.get()!='0':
textReciept.insert(END,f'Butter Chicken\t\t\t{int(e_Butter_Chicken.get())*349}\n\n') if e_Chicken_Kolapuri.get()!='0':
textReciept.insert(END,f'Chicken Kolapuri\t\t\t{int(e_Chicken_Kolapuri.get())*369}\n\n') if e_Telangana_Chicken.get()!='0':
textReciept.insert(END,f'Telangana Chicken Chicken\t\t\t{int(e_Telangana_Chicken.get())*369}\n\n') if e_Mutton_Kheema.get()!='0':
textReciept.insert(END,f'Mutton Kheema\t\t\t{int(e_Mutton_Kheema.get())*449}\n\n') if e_Mutton_Curry.get()!='0':
textReciept.insert(END,f'Mutton curry \t\t\t{int(e_Mutton_Curry.get())*424}\n\n') if e_Fish_Pulusu.get()!='0':
textReciept.insert(END,f'Fish Pulusu\t\t\t{int(e_Fish_Pulusu.get())*489}\n\n') if e_Veg_Kofta.get()!='0':
textReciept.insert(END,f'Veg Kofta\t\t\t{int(e_Veg_Kofta.get())*299}\n\n') if e_Butter_Panner.get()!='0':
textReciept.insert(END,f'Butter Panner\t\t\t{int(e_Butter_Panner.get())*199}\n\n') if e_Mushroom.get()!='0':
textReciept.insert(END,f'Mushroom\t\t\t{int(e_Mushroom.get())*169}\n\n') if e_Chicken_Dum_Biryani.get()!='0':
textReciept.insert(END,f'Chicken Dum Biryani\t\t\t{int(e_Chicken_Dum_Biryani.get())*380}\n\n') if e_Chicken_Frypiece_Biryani.get()!='0':
textReciept.insert(END,f'Chicken Frypiece Biryani\t\t\t{int(e_Chicken_Frypiece_Biryani.get())*399}\n\n') if e_Chicken_Biryani_spl.get()!='0':
textReciept.insert(END,f'Chicken Biryani Spl\t\t\t{int(e_Chicken_Biryani_spl.get())*399}\n\n') if e_Mutton_Nallighosh_Biryani.get()!='0':
textReciept.insert(END,f'Mutton Nallighosh Biryani\t\t\t{int(e_Mutton_Nallighosh_Biryani.get())*449}\n\n') if e_Mutton_Juicy_Biryani.get()!='0':
textReciept.insert(END,f'Mutton Juicy Biryani\t\t\t{int(e_Mutton_Juicy_Biryani.get())*469}\n\n') if e_Fish_Biryani.get()!='0':
textReciept.insert(END,f'Fish Biryani\t\t\t{int(e_Fish_Biryani.get())*510}\n\n') if e_Prawn_Biryani.get()!='0':
textReciept.insert(END,f'Prawn Biryani\t\t\t{int(e_Prawn_Biryani.get())*470}\n\n') if e_Veg_Pulao.get()!='0':
textReciept.insert(END,f'Veg Pulao\t\t\t{int(e_Veg_Pulao.get())*220}\n\n') if e_Panner_Biryani.get()!='0':
textReciept.insert(END,f'Panner Biryani\t\t\t{int(e_Panner_Biryani.get())*250}\n\n') if e_Chicken_Mangolia.get()!='0':
 
textReciept.insert(END,f'Chicken Mangolia\t\t\t{int(e_Chicken_Mangolia.get())*210}\n\n') if e_Chicken_Manchuria.get()!='0':
textReciept.insert(END,f'Chicken Manchuria\t\t\t{int(e_Chicken_Manchuria.get())*189}\n\n') if e_Chicken_Drumsticks.get()!='0':
textReciept.insert(END,f'Chicken Drumsticks\t\t\t{int(e_Chicken_Drumsticks.get())*210}\n\n') if e_Chicken_kabab.get()!='0':
textReciept.insert(END,f'Chicken Kabab\t\t\t{int(e_Chicken_kabab.get())*240}\n\n') if e_Egg_Manchuria.get()!='0':
textReciept.insert(END,f'Egg Manchuria\t\t\t{int(e_Egg_Manchuria.get())*199}\n\n') if e_Veg_Manchuria.get()!='0':
textReciept.insert(END,f'Veg Manchuria\t\t\t{int(e_Veg_Manchuria.get())*170}\n\n') if e_Fried_Mushroom.get()!='0':
textReciept.insert(END,f'Fried Mushroom\t\t\t{int(e_Fried_Mushroom.get())*170}\n\n') if e_BabyCorn.get()!='0':
textReciept.insert(END,f'Baby Corn\t\t\t{int(e_BabyCorn.get())*190}\n\n') if e_Panner_Tikka.get()!='0':
textReciept.insert(END,f'Panner Tikka\t\t\t{int(e_Panner_Tikka.get())*199}\n\n') textReciept.insert(END, '*********************\n')
if costofMaincoursevar.get()!='0 Rs':
textReciept.insert(END, f'cost of Main course\t\t\t{priceofMaincourse}\n\n') if costofBiryanivar.get()!='0 Rs':
textReciept.insert(END, f'cost of Biryani\t\t\t{priceofBiryani}\n\n') if costofStartersvar.get()!='0 Rs':
textReciept.insert(END, f'cost of Starters\t\t\t{priceofStarters}\n\n') textReciept.insert(END, f'Sub Total\t\t\t{subtotalofItems}\n\n') textReciept.insert(END, f'Service Tax\t\t\t{50}\n\n') textReciept.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}\n\n') textReciept.insert(END, '*********************\n')

def totalcost():
global priceofMaincourse , priceofBiryani , priceofStarters , subtotalofItems


item1=int(e_Butter_Chicken.get()) item2=int(e_Chicken_Kolapuri.get()) item3=int(e_Telangana_Chicken.get()) item4=int(e_Mutton_Kheema.get()) item5=int(e_Mutton_Curry.get()) item6=int(e_Fish_Pulusu.get()) item7=int(e_Veg_Kofta.get()) item8=int(e_Butter_Panner.get()) item9=int(e_Mushroom.get())

item10=int(e_Chicken_Dum_Biryani.get()) item11=int(e_Chicken_Frypiece_Biryani.get()) item12=int(e_Chicken_Biryani_spl.get()) item13=int(e_Mutton_Nallighosh_Biryani.get()) item14=int(e_Mutton_Juicy_Biryani.get()) item15=int(e_Fish_Biryani.get()) item16=int(e_Prawn_Biryani.get()) item17=int(e_Veg_Pulao.get()) item18=int(e_Panner_Biryani.get())


item19=int(e_Chicken_Mangolia.get()) item20=int(e_Chicken_Manchuria.get()) item21=int(e_Chicken_Drumsticks.get()) item22=int(e_Chicken_kabab.get())
 
item23=int(e_Egg_Manchuria.get()) item24=int(e_Veg_Manchuria.get()) item25=int(e_Fried_Mushroom.get()) item26=int(e_BabyCorn.get()) item27=int(e_Panner_Tikka.get())




priceofMaincourse=(item1*349)+(item2*369)+(item3*369)+(item4*449)+(item5*424)+(item6*489)+(item7*299)+(item8* 199)+(item9*169)

priceofBiryani=(item10*350)+(item11*399)+(item12*399)+(item13*449)+(item14*469)+(item15*510)+(item16*470)+(ite m17*220)+(item18*250)

priceofStarters=(item19*210)+(item20*189)+(item21*210)+(item22*240)+(item23*199)+(item24*170)+(item25*170)+(ite m26*190)+(item27*199)
costofMaincoursevar.set(str(priceofMaincourse)+'Rs') costofBiryanivar.set(str(priceofBiryani)+"Rs") costofStartersvar.set(str(priceofStarters)+"Rs")

subtotalofItems=priceofStarters+priceofMaincourse+priceofBiryani costofSubtotalvar.set(str(subtotalofItems)+ "Rs")

costofServicetaxvar.set('50 Rs')


tottalcost=subtotalofItems+50 costofTotalcostvar.set(str(tottalcost)+"Rs")





def Butter_Chicken(): if var1.get()==1:
textButter_Chicken.config(state=NORMAL) textButter_Chicken.delete(0,END) textButter_Chicken.focus()
else:
textButter_Chicken.config(state=DISABLED) e_Butter_Chicken.set("0")

def Chicken_Kolapuri(): if var2.get()==1:
textChicken_Kolapuri.config(state=NORMAL) textChicken_Kolapuri.delete(0,END) textChicken_Kolapuri.focus()
else:
textChicken_Kolapuri.config(state=DISABLED) e_Chicken_Kolapuri.set("0")
 
def Telangana_Chicken(): if var3.get()==1:
textTelangana_Chicken.config(state=NORMAL) textTelangana_Chicken.delete(0,END) textTelangana_Chicken.focus()
else:
textTelangana_Chicken.config(state=DISABLED) e_Telangana_Chicken.set("0")


def Mutton_Kheema(): if var4.get()==1:
textMutton_Kheema.config(state=NORMAL) textMutton_Kheema.delete(0,END) textMutton_Kheema.focus()
else:
textMutton_Kheema.config(state=DISABLED) e_Mutton_Kheema.set("0")

def Mutton_Curry(): if var5.get()==1:
textMutton_Curry.config(state=NORMAL) textMutton_Curry.delete(0,END) textMutton_Curry.focus()
else:
textMutton_Curry.config(state=DISABLED) e_Mutton_Curry.set("0")


def Fish_Pulusu(): if var6.get()==1:
textFish_Pulusu.config(state=NORMAL) textFish_Pulusu.delete(0,END) textFish_Pulusu.focus()
else:
textFish_Pulusu.config(state=DISABLED) e_Fish_Pulusu.set("0")


def Veg_Kofta(): if var7.get()==1:
textVeg_Kofta.config(state=NORMAL) textVeg_Kofta.delete(0,END) textVeg_Kofta.focus()
else:
textVeg_Kofta.config(state=DISABLED) e_Veg_Kofta.set("0")


def Butter_Panner(): if var8.get()==1:
textButter_Panner.config(state=NORMAL) textButter_Panner.delete(0,END) textButter_Panner.focus()
else:
textButter_Panner.config(state=DISABLED) e_Butter_Panner.set("0")
def Mushroom(): if var9.get()==1:
 
textMushroom.config(state=NORMAL) textMushroom.delete(0,END) textMushroom.focus()
else:
textMushroom.config(state=DISABLED) e_Mushroom.set("0")


def Chicken_Dum_Biryani(): if var10.get()==1:
textChicken_Dum_Biryani.config(state=NORMAL) textChicken_Dum_Biryani.delete(0,END) textChicken_Dum_Biryani.focus()
else:
textChicken_Dum_Biryani.config(state=DISABLED) e_Chicken_Dum_Biryani.set("0")

def Chicken_Frypiece_Biryani(): if var11.get()==1:
textChicken_Frypiece_Biryani.config(state=NORMAL) textChicken_Frypiece_Biryani.delete(0,END) textChicken_Frypiece_Biryani.focus()
else:
textChicken_Frypiece_Biryani.config(state=DISABLED) e_Chicken_Frypiece_Biryani.set("0")

def Chicken_Biryani_Spl(): if var12.get()==1:
textChicken_Biryani_Spl.config(state=NORMAL) textChicken_Biryani_Spl.delete(0,END) textChicken_Biryani_Spl.focus()
else:
textChicken_Biryani_Spl.config(state=DISABLED) e_Chicken_Biryani_spl.set("0")




def Mutton_Nallighosh_Biryani(): if var13.get()==1:
textMutton_Nallighosh_Biryani.config(state=NORMAL) textMutton_Nallighosh_Biryani.delete(0,END) textMutton_Nallighosh_Biryani.focus()
else:
textMutton_Nallighosh_Biryani.config(state=DISABLED) e_Mutton_Nallighosh_Biryani.set("0")


def Mutton_Juicy_Biryani(): if var14.get()==1:
textMutton_Juicy_Biryani.config(state=NORMAL) textMutton_Juicy_Biryani.delete(0,END) textMutton_Juicy_Biryani.focus()
else:
textMutton_Juicy_Biryani.config(state=DISABLED) e_Mutton_Juicy_Biryani.set("0")
 
def Fish_Biryani(): if var15.get()==1:
textFish_Biryani.config(state=NORMAL) textFish_Biryani.delete(0,END) textFish_Biryani.focus()
else:
textFish_Biryani.config(state=DISABLED) e_Fish_Biryani.set("0")


def Prawn_Biryani(): if var16.get()==1:
textPrawn_Biryani.config(state=NORMAL) textPrawn_Biryani.delete(0,END) textPrawn_Biryani.focus()
else:
textPrawn_Biryani.config(state=DISABLED) e_Prawn_Biryani.set("0")


def Veg_Pulao():
if var17.get()==1: textVeg_Pulao.config(state=NORMAL) textVeg_Pulao.delete(0,END) textVeg_Pulao.focus()
else:
textVeg_Pulao.config(state=DISABLED) e_Veg_Pulao.set("0")


def Panner_Biryani(): if var18.get()==1:
textPanner_Biryani.config(state=NORMAL) textPanner_Biryani.delete(0,END) textPanner_Biryani.focus()
else:
textPanner_Biryani.config(state=DISABLED) e_Prawn_Biryani.set("0")



def Chicken_Mangolia(): if var19.get()==1:
textChicken_Mangolia.config(state=NORMAL) textChicken_Mangolia.delete(0,END) textChicken_Mangolia.focus()
else:
textChicken_Mangolia.config(state=DISABLED) e_Chicken_Mangolia.set("0")


def Chicken_Manchuria(): if var20.get()==1:
textChicken_Manchuria.config(state=NORMAL) textChicken_Manchuria.delete(0,END) textChicken_Manchuria.focus()
else:
textChicken_Manchuria.config(state=DISABLED)
 
e_Chicken_Manchuria.set("0")



def Chicken_Drumsticks(): if var21.get()==1:
textChicken_Drumsticks.config(state=NORMAL) textChicken_Drumsticks.delete(0,END) textChicken_Drumsticks.focus()
else:
textChicken_Drumsticks.config(state=DISABLED) e_Chicken_Drumsticks.set("0")


def Chicken_Kabab(): if var22.get()==1:
textChicken_kabab.config(state=NORMAL)
textChicken_kabab.delete(0,END) 
textChicken_kabab.focus()
else:
textChicken_kabab.config(state=DISABLED)
e_Chicken_kabab.set("0")


def Egg_Manchuria(): if var23.get()==1:
textEgg_Manchuria.config(state=NORMAL)
textEgg_Manchuria.delete(0,END) 
textEgg_Manchuria.focus()
else:
textEgg_Manchuria.config(state=DISABLED)
e_Egg_Manchuria.set("0")

def Veg_Manchuria(): if var24.get()==1:
textVeg_Manchuria.config(state=NORMAL)
textVeg_Manchuria.delete(0,END) 
textVeg_Manchuria.focus()
else:
textVeg_Manchuria.config(state=DISABLED) 
e_Veg_Manchuria.set("0")

def Fried_Mushroom(): if var25.get()==1:
textFried_Mushroom.config(state=NORMAL) 
textFried_Mushroom.delete(0,END)
textFried_Mushroom.focus()
else:
textFried_Mushroom.config(state=DISABLED) 
e_Fried_Mushroom.set("0")


def Baby_Corn():
if var26.get()==1: textBabyCorn.config(state=NORMAL)
  textBabyCorn.delete(0,END)
  textBabyCorn.focus()
 
else:
textBabyCorn.config(state=DISABLED)
e_BabyCorn.set("0")

def Panner_Tikka(): if var27.get()==1:
textPanner_Tikka.config(state=NORMAL) textPanner_Tikka.delete(0,END) textPanner_Tikka.focus()
else:
textPanner_Tikka.config(state=DISABLED) e_Panner_Tikka.set("0")


root=Tk() root.geometry("1350x750+0+0")
root.title("Fine Dining With Contactless Ordering System") root.config(bg="light yellow") topFrame=Frame(root,bd=10,relief=RIDGE,bg="light yellow") topFrame.pack(side=TOP)


labelTitle=Label(topFrame,text="MENU",font=("times new roman",30,"bold"),fg="dark green",bd=9,bg="light green",width=51)
labelTitle.grid(row=0,column=0)



#frames menuFrame=Frame(root,bd=10,relief=RIDGE) menuFrame.pack(side=LEFT)


costFrame=Frame(menuFrame,bd=4,relief=RIDGE) costFrame.pack(side=BOTTOM)


maincourseFrame=LabelFrame(menuFrame,text="Main Course",font=("arial",19,"bold"),bd=10,relief=RIDGE) maincourseFrame.pack(side=LEFT) biryanisFrame=LabelFrame(menuFrame,text="Biryani",font=("arial",19,"bold"),bd=10,relief=RIDGE) biryanisFrame.pack(side=LEFT) startersFrame=LabelFrame(menuFrame,text="Starters",font=("arial",19,"bold"),bd=10,relief=RIDGE) startersFrame.pack(side=LEFT)


rightFrame=Frame(root,bd=15,relief=RIDGE) rightFrame.pack(side=RIGHT) calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE) calculatorFrame.pack()


recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE) recieptFrame.pack() buttonFrame=Frame(rightFrame,bd=2,relief=RIDGE) buttonFrame.pack()
 
#variables var1=IntVar() var2=IntVar() var3=IntVar() var4=IntVar() var5=IntVar() var6=IntVar() var7=IntVar() var8=IntVar() var9=IntVar() var10=IntVar() var11=IntVar() var12=IntVar() var13=IntVar() var14=IntVar() var15=IntVar() var16=IntVar() var17=IntVar() var18=IntVar() var19=IntVar() var20=IntVar() var21=IntVar() var22=IntVar() var23=IntVar() var24=IntVar() var25=IntVar() var26=IntVar() var27=IntVar()

e_Butter_Chicken=StringVar() e_Chicken_Kolapuri=StringVar() e_Telangana_Chicken=StringVar() e_Mutton_Kheema=StringVar() e_Mutton_Curry=StringVar() e_Fish_Pulusu=StringVar() e_Veg_Kofta=StringVar() e_Butter_Panner=StringVar() e_Mushroom=StringVar()

e_Chicken_Dum_Biryani=StringVar() e_Chicken_Frypiece_Biryani=StringVar() e_Chicken_Biryani_spl=StringVar() e_Mutton_Nallighosh_Biryani=StringVar() e_Mutton_Juicy_Biryani=StringVar() e_Fish_Biryani=StringVar() e_Prawn_Biryani=StringVar() e_Veg_Pulao=StringVar() e_Panner_Biryani=StringVar()


e_Chicken_Mangolia=StringVar() e_Chicken_Manchuria=StringVar() e_Chicken_Drumsticks=StringVar() e_Chicken_kabab=StringVar() e_Egg_Manchuria=StringVar() e_Veg_Manchuria=StringVar() e_Fried_Mushroom=StringVar()
 
e_BabyCorn=StringVar() e_Panner_Tikka=StringVar()


costofMaincoursevar=StringVar() costofBiryanivar=StringVar() costofStartersvar=StringVar() costofSubtotalvar=StringVar() costofServicetaxvar=StringVar() costofTotalcostvar=StringVar()

e_Butter_Chicken.set("0") e_Chicken_Kolapuri.set("0") e_Telangana_Chicken.set("0") e_Mutton_Kheema.set('0') e_Mutton_Curry.set("0") e_Fish_Pulusu.set("0") e_Veg_Kofta.set("0") e_Butter_Panner.set("0") e_Mushroom.set("0")

e_Chicken_Dum_Biryani.set("0") e_Chicken_Frypiece_Biryani.set("0") e_Chicken_Biryani_spl.set("0") e_Mutton_Nallighosh_Biryani.set("0") e_Mutton_Juicy_Biryani.set("0") e_Fish_Biryani.set("0") e_Prawn_Biryani.set("0") e_Veg_Pulao.set("0") e_Panner_Biryani.set("0")



e_Chicken_Mangolia.set("0") e_Chicken_Manchuria.set("0") e_Chicken_Drumsticks.set("0") e_Chicken_kabab.set("0") e_Egg_Manchuria.set("0") e_Veg_Manchuria.set("0") e_Fried_Mushroom.set("0") e_BabyCorn.set("0") e_Panner_Tikka.set("0")



##maincourse
Butter_Chicken =Checkbutton(maincourseFrame,text="Butter Chicken- 349",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var1,command=Butter_Chicken) Butter_Chicken.grid(row=0,column=0,sticky=W)
Chicken_Kolapuri =Checkbutton(maincourseFrame,text="Chicken kolapuri- 369",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var2,command=Chicken_Kolapuri) Chicken_Kolapuri.grid(row=1,column=0,sticky=W)
Telangana_Chicken =Checkbutton(maincourseFrame,text="Telangana Chicken- 369",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var3,command=Telangana_Chicken) Telangana_Chicken.grid(row=2,column=0,sticky=W) Mutton_Kheema=Checkbutton(maincourseFrame,text="Mutton Kheema- 449",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var4,command=Mutton_Kheema)
 
Mutton_Kheema.grid(row=3,column=0,sticky=W) Mutton_Curry=Checkbutton(maincourseFrame,text="Mutton Curry- 424",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var5,command=Mutton_Curry) Mutton_Curry.grid(row=4,column=0,sticky=W) Fish_Pulusu=Checkbutton(maincourseFrame,text="Fish Pulusu- 489",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var6,command=Fish_Pulusu) Fish_Pulusu.grid(row=5,column=0,sticky=W) Veg_Kofta=Checkbutton(maincourseFrame,text="Veg Kofta- 299",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var7,command=Veg_Kofta) Veg_Kofta.grid(row=6,column=0,sticky=W) Butter_Panner=Checkbutton(maincourseFrame,text="Butter Panner- 199",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var8,command=Butter_Panner) Butter_Panner.grid(row=7,column=0,sticky=W) Mushroom=Checkbutton(maincourseFrame,text="Mushroom- 169",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var9,command=Mushroom) Mushroom.grid(row=8,column=0,sticky=W)


#entry fields for maincourse textButter_Chicken=Entry(maincourseFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Butte r_Chicken)
textButter_Chicken.grid(row=0,column=1) textChicken_Kolapuri=Entry(maincourseFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Ch icken_Kolapuri)
textChicken_Kolapuri.grid(row=1,column=1) textTelangana_Chicken=Entry(maincourseFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_T elangana_Chicken)
textTelangana_Chicken.grid(row=2,column=1) textMutton_Kheema=Entry(maincourseFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Mut ton_Kheema)
textMutton_Kheema.grid(row=3,column=1) textMutton_Curry=Entry(maincourseFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Mutto n_Curry)
textMutton_Curry.grid(row=4,column=1) textFish_Pulusu=Entry(maincourseFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Fish_Pul usu)
textFish_Pulusu.grid(row=5,column=1) textVeg_Kofta=Entry(maincourseFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Veg_Koft a)
textVeg_Kofta.grid(row=6,column=1) textButter_Panner=Entry(maincourseFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Butter_Panner) textButter_Panner.grid(row=7,column=1)

textMushroom=Entry(maincourseFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Mushroo m)
textMushroom.grid(row=8,column=1)


#Biryaniframe Chicken_Dum_Biryani=Checkbutton(biryanisFrame,text="Chicken Dum Biryani-
350",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var10,command=Chicken_Dum_Biryani) Chicken_Dum_Biryani.grid(row=0,column=0,sticky=W) Chicken_Frypiece_Biryani=Checkbutton(biryanisFrame,text="Chicken Frypiece Biryani- 399",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var11,command=Chicken_Frypiece_Biryani) Chicken_Frypiece_Biryani.grid(row=1,column=0,sticky=W) Chicken_Biryani_Spl=Checkbutton(biryanisFrame,text="Chicken Biryani Spl- 399",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var12,command=Chicken_Biryani_Spl) Chicken_Biryani_Spl.grid(row=2,column=0,sticky=W) Mutton_Nallighosh_Biryani=Checkbutton(biryanisFrame,text="Mutton Nallighosh Biryani- 449",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var13,command=Mutton_Nallighosh_Biryani)
 
Mutton_Nallighosh_Biryani.grid(row=3,column=0,sticky=W) Mutton_Juicy_Biryani=Checkbutton(biryanisFrame,text="Mutton Juicy Biryani- 469",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var14,command=Mutton_Juicy_Biryani) Mutton_Juicy_Biryani.grid(row=4,column=0,sticky=W) Fish_Biryani=Checkbutton(biryanisFrame,text="Fish Biryani- 510",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var15,command=Fish_Biryani) Fish_Biryani.grid(row=5,column=0,sticky=W) Prawn_Biryani=Checkbutton(biryanisFrame,text="Prawn Biryani- 470",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var16,command=Prawn_Biryani) Prawn_Biryani.grid(row=6,column=0,sticky=W)
Veg_Pulao=Checkbutton(biryanisFrame,text="Veg Pulao- 220",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var17,command=Veg_Pulao) Veg_Pulao.grid(row=7,column=0,sticky=W) Panner_Biryani=Checkbutton(biryanisFrame,text="Panner Biryani- 250",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var18,command=Panner_Biryani) Panner_Biryani.grid(row=8,column=0,sticky=W)


#entry fields for biryani textChicken_Dum_Biryani=Entry(biryanisFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_C hicken_Dum_Biryani)
textChicken_Dum_Biryani.grid(row=0,column=1) textChicken_Frypiece_Biryani=Entry(biryanisFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable= e_Chicken_Frypiece_Biryani)
textChicken_Frypiece_Biryani.grid(row=1,column=1) textChicken_Biryani_Spl=Entry(biryanisFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Ch icken_Biryani_spl)
textChicken_Biryani_Spl.grid(row=2,column=1) textMutton_Nallighosh_Biryani=Entry(biryanisFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Mutton_Nallighosh_Biryani) textMutton_Nallighosh_Biryani.grid(row=3,column=1)

textMutton_Juicy_Biryani=Entry(biryanisFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_M utton_Juicy_Biryani)
textMutton_Juicy_Biryani.grid(row=4,column=1) textFish_Biryani=Entry(biryanisFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Fish_Birya ni)
textFish_Biryani.grid(row=5,column=1) textPrawn_Biryani=Entry(biryanisFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Prawn_Bi ryani)
textPrawn_Biryani.grid(row=6,column=1) textVeg_Pulao=Entry(biryanisFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Veg_Pulao) textVeg_Pulao.grid(row=7,column=1) textPanner_Biryani=Entry(biryanisFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Panner_ Biryani)
textPanner_Biryani.grid(row=8,column=1)





#Startersframe Chicken_Mangolia=Checkbutton(startersFrame,text="Chicken Mangolia-
210",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var19,command=Chicken_Mangolia) Chicken_Mangolia.grid(row=0,column=0,sticky=W) Chicken_Manchuria=Checkbutton(startersFrame,text="Chicken Manchuria- 189",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var20,command=Chicken_Manchuria) Chicken_Manchuria.grid(row=1,column=0,sticky=W) Chicken_Drumsticks=Checkbutton(startersFrame,text="Chicken Drumsticks- 210",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var21,command=Chicken_Drumsticks)
 
Chicken_Drumsticks.grid(row=2,column=0,sticky=W) Chicken_Kabab=Checkbutton(startersFrame,text="Chicken Kabab- 240",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var22,command=Chicken_Kabab) Chicken_Kabab.grid(row=3,column=0,sticky=W) Egg_Manchuria=Checkbutton(startersFrame,text="Egg Manchuria- 199",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var23,command=Egg_Manchuria) Egg_Manchuria.grid(row=4,column=0,sticky=W) Veg_Manchuria=Checkbutton(startersFrame,text="Veg Manchuria- 170",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var24,command=Veg_Manchuria) Veg_Manchuria.grid(row=5,column=0,sticky=W) Fried_Mushroom=Checkbutton(startersFrame,text="Fried Mushroom- 170",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var25,command=Fried_Mushroom) Fried_Mushroom.grid(row=6,column=0,sticky=W) Baby_Corn=Checkbutton(startersFrame,text="Baby Corn- 190",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var26,command=Baby_Corn) Baby_Corn.grid(row=7,column=0,sticky=W) Panner_Tikka=Checkbutton(startersFrame,text="Panner Tikka- 199",font=("arial",8,"bold"),onvalue=1,offvalue=0,variable=var27,command=Panner_Tikka) Panner_Tikka.grid(row=8,column=0,sticky=W)



#entry fields for starters


textChicken_Mangolia=Entry(startersFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Chick en_Mangolia)
textChicken_Mangolia.grid(row=0,column=1) textChicken_Manchuria=Entry(startersFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Chic ken_Manchuria)
textChicken_Manchuria.grid(row=1,column=1) textChicken_Drumsticks=Entry(startersFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Chic ken_Drumsticks)
textChicken_Drumsticks.grid(row=2,column=1) textChicken_kabab=Entry(startersFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Chicken_ kabab)
textChicken_kabab.grid(row=3,column=1) textEgg_Manchuria=Entry(startersFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Egg_Man churia)
textEgg_Manchuria.grid(row=4,column=1) textVeg_Manchuria=Entry(startersFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Veg_Ma nchuria)
textVeg_Manchuria.grid(row=5,column=1) textFried_Mushroom=Entry(startersFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Fried_ Mushroom)
textFried_Mushroom.grid(row=6,column=1) textBabyCorn=Entry(startersFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_BabyCorn) 
textBabyCorn.grid(row=7,column=1) textPanner_Tikka=Entry(startersFrame,font=("arial",12,"bold"),bd=7,width=6,state=DISABLED,textvariable=e_Panner_Tik ka)
textPanner_Tikka.grid(row=8,column=1)



#costlabels and entry fields

labelcostofMaincourse=Label(costFrame,text="Cost of Maincourse",font=("arial",16,"bold"),bg="light yellow")
 
labelcostofMaincourse.grid(row=0,column=0)


textCostofMaincourse=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=costofMainc oursevar)
textCostofMaincourse.grid(row=0,column=1,padx=41)

labelcostofBiryani=Label(costFrame,text="Cost of Biryani",font=("arial",16,"bold"),bg="light yellow") labelcostofBiryani.grid(row=1,column=0)

textCostofBiryani=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=costofBiryanivar) 
textCostofBiryani.grid(row=1,column=1,padx=41)

labelcostofStarters=Label(costFrame,text="Cost of Starters",font=("arial",16,"bold"),bg="light yellow") 
labelcostofStarters.grid(row=2,column=0)

textCostofStarters=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=costofStartersvar)

textCostofStarters.grid(row=2,column=1,padx=41)



labelSubtotal=Label(costFrame,text="Sub total ",font=("arial",16,"bold"),bg="light yellow") labelSubtotal.grid(row=0,column=2)


textCostofSubtotal=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=costofSubtotalva r)
textCostofSubtotal.grid(row=0,column=3,padx=41)

labelServicetax=Label(costFrame,text="Service Tax",font=("arial",16,"bold"),bg="light yellow") labelServicetax.grid(row=1,column=2)


textCostofServicetax=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=costofServicet axvar)
textCostofServicetax.grid(row=1,column=3,padx=41)

labelTotalcost=Label(costFrame,text="Total Cost",font=("arial",16,"bold"),bg="light yellow") labelTotalcost.grid(row=2,column=2)

textTotalcost=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=costofTotalcostvar) textTotalcost.grid(row=2,column=3,padx=41)



#buttons


buttonTotal=Button(buttonFrame,text="Total",font=("arial",14,"bold"),command=totalcost) buttonTotal.grid(row=0,column=0)
 
buttonReceipt=Button(buttonFrame,text="Receipt",font=("arial",14,"bold"),command=receipt) buttonReceipt.grid(row=0,column=1) buttonSave=Button(buttonFrame,text="Save",font=("arial",14,"bold"),command=save) buttonSave.grid(row=0,column=2) buttonSend=Button(buttonFrame,text="Send",font=("arial",14,"bold"),command=send) buttonSend.grid(row=0,column=3) buttonReset=Button(buttonFrame,text="Reset",font=("arial",14,"bold"),command=reset) buttonReset.grid(row=0,column=4)

#textarea for receipt


textReciept=Text(recieptFrame,font=("arial",12,"bold"),width=42,height=14) textReciept.grid(row=0,column=0)



#calculator operator=''
def buttonClick(numbers): global operator operator=operator+numbers calculatorField.delete(0,END)
calculatorField.insert(END,operator)

def clear(): global operator operator=''
calculatorField.delete(0,END)


def answer(): global operator
result=str(eval(operator)) calculatorField.delete(0,END) calculatorField.insert(0,result) operator=''

calculatorField=Entry(calculatorFrame,font=("arial",16,"bold"),width=32) calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text="7",font=("arial",16,"bold"),width=7,bg="yellow",command=lambda:buttonClick("7"))

button7.grid(row=1,column=0) button8=Button(calculatorFrame,text="8",font=("arial",16,"bold"),width=7,bg="yellow",command=lambda:buttonClick("8"))

button8.grid(row=1,column=1) button9=Button(calculatorFrame,text="9",font=("arial",16,"bold"),width=7,bg="yellow",command=lambda:buttonClick("9"))

button9.grid(row=1,column=2) buttonPlus=Button(calculatorFrame,text="+",font=("arial",16,"bold"),width=4,bg="yellow",command=lambda:buttonClick( "+"))
buttonPlus.grid(row=1,column=3) button4=Button(calculatorFrame,text="4",font=("arial",16,"bold"),width=7,bg="yellow",command=lambda:buttonClick("4"))

button4.grid(row=2,column=0)
 
button5=Button(calculatorFrame,text="5",font=("arial",16,"bold"),width=7,bg="yellow",command=lambda:buttonClick("5"))

button5.grid(row=2,column=1) button6=Button(calculatorFrame,text="6",font=("arial",16,"bold"),width=7,bg="yellow",command=lambda:buttonClick("6"))

button6.grid(row=2,column=2) buttonMinus=Button(calculatorFrame,text="-",font=("arial",16,"bold"),width=4,bg="yellow",command=lambda:buttonClick("-")) buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text="1",font=("arial",16,"bold"),width=7,bg="yellow",command=lambda:buttonClick("1"))

button1.grid(row=3,column=0) button2=Button(calculatorFrame,text="2",font=("arial",16,"bold"),width=7,bg="yellow",command=lambda:buttonClick("2"))

button2.grid(row=3,column=1) button3=Button(calculatorFrame,text="3",font=("arial",16,"bold"),width=7,bg="yellow",command=lambda:buttonClick("3"))

button3.grid(row=3,column=2) buttonMult=Button(calculatorFrame,text="",font=("arial",16,"bold"),width=4,bg="yellow",command=lambda:buttonClick(" "))
buttonMult.grid(row=3,column=3) buttonAns=Button(calculatorFrame,text="Ans",font=("arial",16,"bold"),width=7,bg="yellow",command=answer) buttonAns.grid(row=4,column=0) buttonClear=Button(calculatorFrame,text="Clear",font=("arial",16,"bold"),width=7,bg="yellow",command=clear) buttonClear.grid(row=4,column=1) button0=Button(calculatorFrame,text="0",font=("arial",16,"bold"),width=7,bg="yellow",command=lambda:buttonClick("0"))

button0.grid(row=4,column=2) buttonDiv=Button(calculatorFrame,text="/",font=("arial",16,"bold"),width=4,bg="yellow",command=lambda:buttonClick("/ "))
buttonDiv.grid(row=4,column=3) root.mainloop()
