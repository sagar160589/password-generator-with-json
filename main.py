from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def find_password():
    website = entry_website.get().capitalize()
    web_flag = False
    #Load data json
    if website != '':
        try:
            with open("data.json", mode="r") as data:
                data_dict = json.load(data)
            for data in data_dict:
                if data == website:
                    web_flag = True
                    messagebox.showinfo(title=website, message=f"Email: {data_dict[data]['email']} \n Password: {data_dict[data]['password']}")
            if not web_flag:
                    messagebox.showinfo(title=website, message="No details exists for the mentioned website")
        except FileNotFoundError:
            print("No data file found")
    else:
        messagebox.showerror(message="Please enter the website name to search")


def generate_password():
    entry_pwd.delete(0,END)
    password_list =[]
    letter_list = [choice(letters) for char in range(randint(8,10))]
    number_lst = [choice(numbers) for number in range(randint(2,4))]
    symbol_list = [choice(symbols) for symbol in range(randint(2,4))]
    password_list = letter_list + number_lst + symbol_list
    shuffle(password_list)
    final_pwd = "".join(password_list)
    entry_pwd.insert(0, final_pwd)
    pyperclip.copy(final_pwd)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    website = entry_website.get()
    email = entry_email.get()
    pwd = entry_pwd.get()

    #Nested dictionary for json
    new_data = {website.capitalize():{
        "email": email,
        "password": pwd
    }}

    if len(website) == 0 or len(pwd) == 0:
        empty_data = messagebox.showerror(title="Oops", message="Fields cannot be left empty before saving!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the entries entered Email: {email} and Password: {pwd}. Are these correct to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as data:
                    curr_data = json.load(data)
            except FileNotFoundError:
                print("File not found error. Creating new file")
                with open("data.json", mode="w") as data:
                    json.dump(new_data, data, indent=4 )
            else:
                curr_data.update(new_data)
                with open("data.json", mode="w") as data:
                    json.dump(curr_data, data, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_pwd.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
#creating a window

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
#window.minsize(width=300, height=300)


#create a canvas for password logo

canvas = Canvas()
canvas.config(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image)
canvas.grid(column=1, row=0)

# create labels & buttons & entries

label_website = Label()
label_website.config(text="Website:")
label_website.grid(row=1, column=0)

entry_website = Entry(width=33)
entry_website.grid(row=1, column=1)
entry_website.focus()

search_button = Button()
search_button.config(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

label_email = Label()
label_email.config(text="Email/Username:")
label_email.grid(row=2, column=0)
entry_email = Entry(width=52)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0,"sagarpt89@gmail.com")

label_pwd = Label()
label_pwd.config(text="Password:")
label_pwd.grid(row=3, column=0)
entry_pwd = Entry(width=33)
entry_pwd.grid(row=3, column=1)

pwd_button = Button()
pwd_button.config(text="Generate Password", command=generate_password)
pwd_button.grid(row=3, column=2)

add_button = Button()
add_button.config(text="Add", width=44, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)






window.mainloop()


