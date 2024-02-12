from tkinter import *
import requests
import json
from tkinter import messagebox
from tkinter import ttk

def msg(number,message):
        url="https://www.fast2sms.com/dev/bulkV2"
        parameters= {"authorization":"30HNakQ5zR8CTpUxXSG7Yyr1Kt2LlO6FoAMbeZ9cujqgD4VdshV6QFnsyg29EhcL1TKzpCMtrkYadJxX",
                                    "sender_id":"FSTSMS",
                                    "message":message,
                                    "language":"english",
                                    "route":"p",
                                    "numbers":number
                        }

        response=requests.get(url,params=parameters)
        dic=response.json()
        return dic.get('return')
    
def btn_click():
        num=txt_phoneNo.get()
        msg1=txt_msg.get()
        #print(num)
        #print(msg1)
        succes= msg(num,msg1)
        if succes == True:
            messagebox.showinfo("Send Sucees","Sucessfully sent ")
        else:
            messagebox.showerror("Show Error","Enter Valid phone No")


global txt_phoneNo,txt_msg
root=Tk()
root.title("Messages App")
root.geometry("1000x600+100+50")
root.resizable(False,False)

headingFrame1 = Frame(root,bg="blue",bd=5)
headingFrame1.place(x=0,y=0,height=60,width=1000)
headingLabel = Label(headingFrame1, text="Message Sender ", bg='pink', fg='black', font=("times new roman",30,"bold"))
headingLabel.place(x=0,y=0,height=50,width=989)
Frame_login=Frame(root,bg="light pink",bd=12)
Frame_login.place(x=180,y=100,height=450,width=620)

#title=Label(Frame_login,text="Messages ", font=("Impact",20,"bold"),fg="red",bg="white",justify='center').place(x=50,y=30)
PhoneNo=Label(Frame_login,text="To", font=("Goudy old style",12,"bold"),fg="black",bg="lightgrey").place(x=70,y=100)  
txt_phoneNo = Entry(Frame_login,width=7) # Entry 
txt_phoneNo.place(x=70,y=130,height=35,width=200)# adding to grid

Msg=Label(Frame_login,text="Enter message", font=("Goudy old style",12,"bold"),fg="black",bg="lightgrey").place(x=70,y=200)
txt_msg=Entry(Frame_login,font=("time new roman",12),bg="light blue")
txt_msg.place(x=70,y=230,width=280,height=80)

send_btn=Button(root,text="Send",fg="white",bg="red",font=("times new roman",12,"bold"),bd=5,command=btn_click).place(x=500,y=450,width=150,height=40)

quitBtn = Button(root,text="Quit",bg='grey', fg='black',command=root.destroy,font=("times new roman",16,"bold"))
quitBtn.place(x=820,y=530,height=40,width=130)
    
root.mainloop()

   