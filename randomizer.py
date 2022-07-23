from tkinter import *
import random

class main():
    secLevel = []

# password generator
def submit():
    password = entry.get()
    charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v''w', 'x', 'y', 'z', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '!', '@', '#', '$', '%']
    iconList = ['!', '@', '#', '$', '%']

# generator loop
    for char in main.secLevel:
        p = random.choice(iconList)
        p += password
        password = p
        password += str(random.randint(1, 9))
        password += random.choice(charList)
    text = StringVar()
    text.set(password)
    password += random.choice(iconList)

# result
    myEntry = Entry(window, bd=0,
                    font=("Arial", 12),
                    state="readonly",
                    textvariable=text)
    myEntry.pack()

# level of security
def order():
    if x.get() == 0:
        main.secLevel = [1]
    elif x.get() == 1:
        main.secLevel = [1, 2]
    elif x.get() == 2:
        main.secLevel = [1, 2, 3]
    elif x.get() == 3:
        main.secLevel = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    else:
        print("huh?")

# start window
window = Tk()
window.title("Password Generator")
label = Label(window, text="Type the keyword you'd like \nto make a password.", font=('Times New Roman', 18))
label.pack()

entry = Entry(window,
              font=('Times New Roman', 20),
              fg='black')
entry.pack(anchor=W)

submitButton = Button(window, text="Submit", command=submit)
submitButton.pack()

strengh = ['weak', 'mid', 'strong', 'extreme']
x = IntVar()
for index in range(len(strengh)):
    radiobutton = Radiobutton(window,
                              text=strengh[index],  # adds text to radio buttons
                              variable=x,  # groups radiobuttons together if they share the same variable
                              value=index,  # assigns each radiobutton a different value
                              padx=25,  # adds padding on x-axis
                              font=("Helvetica", 12, 'bold'),
                              # image = foodImages[index], #adds image to radiobutton
                              compound='left',  # adds image & text (left-side)
                              indicatoron=0,  # eliminate circle indicators
                              width=4,  # sets width of radio buttons
                              command=order  # set command of radiobutton to function
                              )
    radiobutton.pack(anchor=W)

window.mainloop()
