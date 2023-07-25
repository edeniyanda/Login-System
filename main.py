from tkinter import *
from PIL import Image, ImageTk




APP_WIDTH = 1000
APP_HEIGHT = 600

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
sign_in_frame = Frame(root, width=450, height= 500, background="green")
sign_in_frame.place(x = 470, y = 70)

Label(sign_in_frame, text= "Sign In", font=("Arial", 20, "bold"), bg="white", fg= "cornflowerblue").place(x = 200, y = 30)

username = Entry(sign_in_frame, width=30, border=0 )
username.place(x= 20, y = 100, )
username.insert(0, "Username/email")

root.mainloop()