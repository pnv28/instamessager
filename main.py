import tkinter as tk
import tkinter.ttk as tkk
from instagrapi import Client
import time

# Getting Stuff
from config import username, password, homies, messageForHomies, DailyHomieMessage


root = tk.Tk()
root.title("Insta Messager by pnv28")
root.geometry("800x600")

def goodExit():
    root.destroy()
    exit()


root.protocol("WM_DELETE_WINDOW", goodExit)
print("Tool made by pnv28")


try:
    loggedinLabel = tk.Label(text="Establishing connection to Instagram")
    loggedinLabel.pack()
    client = Client()
    client.login(username=username, password=password)
    print(f"Succesfully logged in")
    loggedinLabel = tk.Label(text="Succesfully Established connection to Instagram", fg="green")
    loggedinLabel.pack()
except:
    loggedinLabel= tk.Label(text="Connection Failed\nClosing in 5 seconds", fg="red")
    loggedinLabel.pack()
    print("Could Not Connect to Instagram | Program Quitting in 5 seconds\nMake Sure the Login Credentials are valid")
    time.sleep(5)
    root.destroy()
    exit()

def sendDailyHomie():
    print("Option to send Daily Message to Homie Selected")
    try:
        for i in homies:
            try:
                client.direct_send(DailyHomieMessage, [int(client.user_id_from_username(i))])
            except:
                print(f"Message One Sent to {i}")
    except:
        print("An Error Occured Program Quitting in 5 Seconds")
        errorLabel = tk.Label(text="An Error Occured Quitting in 5 Seconds", fg="red")
        errorLabel.pack()
        time.sleep(5)
        root.destroy()
        exit()
    successLabel = tk.Label(text="Message Succesfully Sent to Homies", fg="green")
    successLabel.pack()

def sendMessage():
    username = sendUsernameEntry.get()
    message = sendEntry.get()
    print("Option to send Message to a specified user has been selected")
    try:
        client.direct_send(message, [int(client.user_id_from_username(username))])
    except:
        print(f"Succesfully sent message to {username}")
        successLabel = tk.Label(text=f"Successfully sent Message to {username}", fg="green")

def spamMessage():
    username = spamUsernameEntry.get()
    message = spamMessageEntry.get()
    spamCount = spamNumberEntry.get()
    print("Option to Spam messages has Been Selected")
    userId = client.user_id_from_username(username)
    try:
        for i in range(int(spamCount)):
            try:
                message = message + spamCount
                client.direct_send(message, [int(userId)])
            except:
                print(f"Message {i} Sent")
    except:
        print("An Error Occured Program Quitting in 5 Seconds")
        errorLabel = tk.Label(text="An Error Occured Quitting in 5 Seconds", fg="red")
        errorLabel.pack()
        time.sleep(5)
        root.destroy()
        exit()
    print(f"Spamming {username} Successfull")

sendDailyHomieButton = tk.Button(text="Send DailyHomieMessage to the Homies", command=sendDailyHomie)
sendDailyHomieButton.pack()

sendLabel = tk.Label(text="\n\n\nDo You Wish to send message to anyone else ??")
sendLabel.pack()
sendEntry = tk.Entry()
sendEntry.pack()
sendEntry.insert(1, "Insert Message Here")
sendUsernameEntry = tk.Entry()
sendUsernameEntry.pack()
sendUsernameEntry.insert(1, "Insert Username of the User")
sendButton = tk.Button(text="Send the Above Message", command=sendMessage)
sendButton.pack()

spamLabel = tk.Label(text="\n\n\nSpamming is not Advisable but it is Sure Fun\nBelow is a Simple Insta Spamming Tool")
spamLabel.pack()
spamUsernameEntry = tk.Entry()
spamUsernameEntry.pack()
spamUsernameEntry.insert(1, "Username")
spamMessageEntry = tk.Entry()
spamMessageEntry.pack()
spamMessageEntry.insert(1, "Message")
spamNumberEntry = tk.Entry()
spamNumberEntry.pack()
spamNumberEntry.insert(1, "No. of Mesages")
spamButton = tk.Button(text="Click Here to Initiate Spam", command=spamMessage)
spamButton.pack()
creditsLabel = tk.Label(text="Tool made by pnv28", fg="blue")
creditsLabel.pack()

closeButton = tk.Button(text="Close Application | Do Not Use the Close button from System Menu Bar", command=exit)
closeButton.pack()

root.mainloop()