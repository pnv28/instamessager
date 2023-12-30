import tkinter as tk
import tkinter.ttk as tkk
from instagrapi import Client
import time

root = tk.Tk()
root.title("Insta Messager")
root.geometry("800x600")

try:
    loggedinLabel = tk.Label(text="Establishing connection to Instagram")
    loggedinLabel.pack()
    client = Client()
    client.login(username='the_pnv28', password='may8,rat')
    print(f"Succesfully logged in")
    loggedinLabel = tk.Label(text="Succesfully Established connection to Instagram", fg="green")
    loggedinLabel.pack()
except:
    loggedinLabel= tk.Label(text="Connection Failed\nClosing in 5 seconds", fg="red")
    loggedinLabel.pack()
    time.sleep(5)
    root.destroy()
    exit()


def sendDailyHomie():
    print("Option to send Message to Homies has been Selected")
    print("Getting USER ID")
    shubi_id = client.user_id_from_username('lazy_kedia')
    ans_id = client.user_id_from_username('anshulagarwal7838')
    esh_id = client.user_id_from_username('eshaan_bh')
    print(f"User IDs obtains\nShubi:{shubi_id}\nAns: {ans_id}\nEsh: {esh_id}")
    print("Attempting to send DM")
    try:
        client.direct_send("https://www.instagram.com/p/C0H6udbOH2d/?igsh=eHBvdGhneTA4b2No", [int(shubi_id)])
    except:
        print("DM Succesfully sent to Shubi")
    try:
        client.direct_send("https://www.instagram.com/p/C0H6udbOH2d/?igsh=eHBvdGhneTA4b2No", [int(esh_id)])
    except:
        print("DM Succesfully sent to Anshul")
    try:
        client.direct_send("https://www.instagram.com/p/C0H6udbOH2d/?igsh=eHBvdGhneTA4b2No", [int(ans_id)])
    except:
        print("DM Successfully sent to Eshaan")
    successLabel = tk.Label(text="Message Succesfully Sent to Homies", fg="green")
    successLabel.pack()

def sendMessage():
    username = sendUsernameEntry.get()
    message = sendEntry.get()
    print("Option to send Message to a specified user has been selected")
    user_id = client.user_id_from_username(username)
    print(f"User ID of the {username} is {user_id}")
    try:
        client.direct_send(message, [int(user_id)])
    except:
        print(f"Succesfully sent message to {username}")
        successLabel = tk.Label(text=f"Successfully sent Message to {username}", fg="green")

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

root.mainloop()
