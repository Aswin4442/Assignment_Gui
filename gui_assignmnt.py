from tkinter import*
user=Tk()
user.title("https://web.online calculator.com/device/")

entry=Entry(user,justify=CENTER,width=17,bg="grey14",fg="white",font=(("arial","26")))
entry.place(x=29,y=30)

bttn7=Button(user,text="7",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn7.place(x=40,y=80)

bttn8=Button(user,text="8",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn8.place(x=120,y=80)

bttn9=Button(user,text="9",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn9.place(x=200,y=80)

bttn_x=Button(user,text="*",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn_x.place(x=280,y=80)

bttn4=Button(user,text="4",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn4.place(x=40,y=177)

bttn5=Button(user,text="5",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn5.place(x=120,y=177)

bttn6=Button(user,text="6",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn6.place(x=200,y=177)

bttn_add=Button(user,text="+",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn_add.place(x=280,y=177)

bttn3=Button(user,text="3",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn3.place(x=200,y=274)

bttn2=Button(user,text="2",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn2.place(x=120,y=274)

bttn1=Button(user,text="1",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn1.place(x=40,y=274)

bttn0=Button(user,text="0",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn0.place(x=120,y=371)

bttnpoint=Button(user,text=".",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttnpoint.place(x=40,y=371)

bttnC=Button(user,text="C",bg="grey34",fg="orange red",activebackground="white",width=6,height=4,font="7")
bttnC.place(x=200,y=371)

bttn_sub=Button(user,text="-",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn_sub.place(x=280,y=274)

bttn_equal=Button(user,text="=",bg="grey34",fg="white",activebackground="white",width=6,height=4,font="7")
bttn_equal.place(x=280,y=371)


user.geometry("1000x850")
user.mainloop()





