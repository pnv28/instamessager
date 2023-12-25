from instagrapi import Client
client = Client()
client.login(username='the_pnv28', password='may8,rat')
print(f"Succesfully logged in")

def sendDailyHomie():
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

sendDailyHomie()