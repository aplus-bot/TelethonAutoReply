import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# LOAD CONFIG
from Combined_Bot import API_ID, API_HASH

if __name__ == "__main__":
    print("--- Session String Generator ---")
    print(f"Using API_ID: {API_ID}")
    
    # Initialize client to generate string
    with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        print("\n👇 COPY THE STRING BELOW AND PASTE IT INTO RENDER ENVIRONMENT VARIABLES 👇\n")
        print(client.session.save())
        print("\n👆 COPY THE STRING ABOVE 👆\n")
        print("Variable Name: SESSION_STRING")