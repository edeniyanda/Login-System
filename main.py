from tkinter import *
from PIL import Image, ImageTk


APP_WIDTH = 1000
APP_HEIGHT = 600
font_type = "Open Sans"
root = Tk()

screen_width =root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
alignstr = f'{APP_WIDTH}x{APP_HEIGHT}+{(screen_width - APP_WIDTH) // 2}+{(screen_height - APP_HEIGHT) // 2}'
root.geometry(alignstr)
root.resizable(0,0)
root.title("Login")
root.configure(background="white")


# Load Sign in Image 
picture_img = PhotoImage(file="assets/images/login.png")

picture_label = Label(root, image=picture_img)
picture_label.place(x= 30, y = 80)

# Create Sign Frame
sign_in_frame = Frame(root, width=450, height= 500, background="white")
sign_in_frame.place(x = 470, y = 70)

Label(sign_in_frame, text= "Sign In", font=(font_type, 20, "bold"), bg="white", fg= "cornflowerblue").place(x = 200, y = 30)


# Username/ Email Entry
def on_input(e):
    name = username.get()
    if len(name) == 0 or name == "Enter your Username or Email":
        username.delete(0, "end")

def on_output(e):
    name = username.get()
    if name == "":
        username.insert(0, "Enter your Username or Email")
        
username = Entry(sign_in_frame, width=30, border=0, font=(font_type, 11), fg = "#8B8B7D")
username.place(x= 20, y = 100, )
username.insert(0, "Enter your Username or Email")
username.bind("<FocusIn>", on_input)
username.bind("<FocusOut>", on_output)

Frame(sign_in_frame, width = 500, height = 2, bg="cornflowerblue").place(x = 15, y = 130)


# Password Entry
def on_input(e):
    code = password.get()
    if (len(code) == 0) or (code == "Enter your Password"):
        password.delete(0, "end")
    password.config(show="*")
    
def on_output(e):
    code = password.get()
    if code == "":
        password.config(show="")
        password.insert(0, "Enter your Password")
password = Entry(sign_in_frame, width=30, border=0, font=(font_type, 11), fg = "#8B8B7D")
password.place(x= 20, y = 170, )
password.insert(0, "Enter your Password")
password.bind("<FocusIn>", on_input)
password.bind("<FocusOut>", on_output)


Frame(sign_in_frame, width = 500, height = 2, bg="cornflowerblue").place(x = 15, y = 200)


# Sign In button
btn_sign_in = Button(sign_in_frame, width=65, text = "Sign In", bg = "cornflowerblue", fg = "white", border=0, pady=6, cursor="hand2")
btn_sign_in.place(x= 15, y = 240)


# Have any account
Label(sign_in_frame, text="Already have an account?", fg="black", bg="white",font=("Open Sans", 10) ).place(x = 100, y = 280)
sign_up_btn = Button(sign_in_frame, text = "Sign Up", bg = "white", fg = "cornflowerblue", border=0, font=(font_type, 10), cursor = "hand2")
sign_up_btn.place(x = 260, y = 280)


root.mainloop()