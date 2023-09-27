from discordrp import Presence
import time

client_id = "1063742854125592586"  # Replace this with your own client id

with Presence(client_id) as presence:
    print("Connected")
    presence.set(
        {
            "state": "In Game",
            "details": "Summoner's Rift",
            "timestamps": {"start": int(time.time())},
        }
    )
    print("Presence updated")

    while True:
        time.sleep(15)