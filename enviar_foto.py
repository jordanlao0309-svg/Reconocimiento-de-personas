import telebot

TOKEN = "8290331427:AAE4YhjNtZHXIP0ZQ4fcFWji76xaAhCZx64"
CHAT_ID = "8269065510"
bot = telebot.TeleBot(TOKEN)

with open("alerta.jpg", "rb") as photo:
    bot.send_photo(CHAT_ID, photo, caption="Prueba de foto manual")
print("📤 Foto enviada")
