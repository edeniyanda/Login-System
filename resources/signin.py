from tkinter import *
from PIL import Image, ImageTk
def signin():
    # Import necessary modules

    # Constants for the application window size
    APP_WIDTH = 1000
    APP_HEIGHT = 600

    # Font type used in the application
    font_type = "Open Sans"

    # Initialize the root window
    root = Tk()

    # Get the screen width and height to center the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    alignstr = f'{APP_WIDTH}x{APP_HEIGHT}+{(screen_width - APP_WIDTH) // 2}+{(screen_height - APP_HEIGHT) // 2}'

    # Configure the root window properties
    root.geometry(alignstr)  # Set the window dimensions and position
    root.resizable(0, 0)     # Disable window resizing
    root.title("QuantumTone-Login")      # Set the title of the window
    root.configure(background="white")  # Set the background color of the window

    # Load and display the Sign In image on the window
    picture_img = PhotoImage(file="assets/images/login.png")
    picture_label = Label(root, image=picture_img)
    picture_label.place(x=30, y=80)

    # Create the Sign In frame
    sign_in_frame = Frame(root, width=450, height=500, background="white")
    sign_in_frame.place(x=470, y=70)

    # Label displaying "Sign In" in the Sign In frame
    Label(sign_in_frame, text="Sign In", font=(font_type, 20, "bold"), bg="white", fg="cornflowerblue").place(x=200, y=30)

    # Username/Email Entry with placeholder text and event handlers
    def on_username_input(e):
        name = username.get()
        if len(name) == 0 or name == "Enter your Username or Email":
            username.delete(0, "end")

    def on_username_output(e):
        name = username.get()
        if name == "":
            username.insert(0, "Enter your Username or Email")

    # Create the Username/Email Entry widget
    username = Entry(sign_in_frame, width=30, border=0, font=(font_type, 11), fg="#8B8B7D")
    username.place(x=20, y=100)
    username.insert(0, "Enter your Username or Email")
    username.bind("<FocusIn>", on_username_input)
    username.bind("<FocusOut>", on_username_output)

    # Separator line for Username/Email Entry
    Frame(sign_in_frame, width=500, height=2, bg="cornflowerblue").place(x=15, y=130)

    # Password Entry with placeholder text and event handlers
    def on_password_input(e):
        code = password.get()
        if (len(code) == 0) or (code == "Enter your Password"):
            password.delete(0, "end")
        password.config(show="*")

    def on_password_output(e):
        code = password.get()
        if code == "":
            
            password.insert(0, "Enter your Password")

    # Create the Password Entry widget
    password = Entry(sign_in_frame, width=30, border=0, font=(font_type, 11), fg="#8B8B7D")
    password.place(x=20, y=170)
    password.insert(0, "Enter your Password")
    password.bind("<FocusIn>", on_password_input)
    password.bind("<FocusOut>", on_password_output)

    # Password state widget and functionality
    def password_state():
        if btn_password_state.current_image == view_state_img:
            btn_password_state["image"] = hide_state_img
            btn_password_state.current_image = hide_state_img
            password.config(show="")
            
        else:
            btn_password_state["image"] = view_state_img
            password.config(show="*")
            btn_password_state.current_image = view_state_img
        
    view_image = Image.open("assets/images/view.png")
    view_state_img = ImageTk.PhotoImage(view_image)

    hide_image = Image.open("assets/images/hide.png")
    hide_state_img = ImageTk.PhotoImage(hide_image)

    btn_password_state = Button(sign_in_frame, image=view_state_img, width=20, bg="white", border=0, command = password_state)
    btn_password_state.current_image = view_state_img 
    btn_password_state.place(x=420, y=170)


    # Separator line for Password Entry
    Frame(sign_in_frame, width=500, height=2, bg="cornflowerblue").place(x=15, y=200)

    # Sign In button
    btn_sign_in = Button(sign_in_frame, width=65, text="Sign In", bg="cornflowerblue", fg="white", border=0, pady=6, cursor="hand2")
    btn_sign_in.place(x=15, y=240)

    # Label and button for the Sign Up option
    Label(sign_in_frame, text="Already have an account?", fg="black", bg="white", font=("Open Sans", 10)).place(x=100, y=280)
    sign_up_btn = Button(sign_in_frame, text="Sign Up", bg="white", fg="cornflowerblue", border=0, font=(font_type, 10), cursor="hand2")
    sign_up_btn.place(x=260, y=280)

    # Start the main event loop of the application
    root.mainloop()

