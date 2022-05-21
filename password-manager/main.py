from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def search_website():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            searched_website = website_entry.get()
            email = data[searched_website]["email"]
            password = data[searched_website]["password"]
            messagebox.showinfo(title=searched_website, message=f"Email: {email}\nPassword:{password}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for the website exists")


def add_clicked():
    with open("passwords.txt", "a") as file:
        if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
            messagebox.showinfo(title="Empty Entry Detected", message="Please don't leave any of the fields empty!")
        else:
            is_ok = messagebox.askyesno(title="Details Enter", message=f"These are the details entered:"
                                                                       f"\nWebsite: {website_entry.get()}"
                                                                       f"\nEmail: {email_entry.get()}"
                                                                       f"\nPassword:{password_entry.get()}"
                                                                       f"\nIs it okay to save?")
            if is_ok:
                new_data = {
                    website_entry.get(): {
                        "email": email_entry.get(),
                        "password": password_entry.get()
                    }
                }
                try:
                    with open("data.json", "r") as data_file:
                        data = json.load(data_file)
                        data.update(new_data)
                except FileNotFoundError:
                    with open("data.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    with open("data.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)
                finally:
                    website_entry.delete(0, 'end')
                    email_entry.delete(0, 'end')
                    password_entry.delete(0, 'end')
                # file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")


window = Tk()
window.title("Password Manager")
window.config(padx=55, pady=55)

canvas = Canvas(width="200", height="200")
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, stick="W")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="W")

add = Button(text="Add", width=36, command=add_clicked)
add.grid(column=1, row=4, columnspan=2)

generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3)

search = Button(text="Search", width=10, command=search_website)
search.grid(column=2, row=1)

window.mainloop()
