import json
import telebot

TOKEN = "8290331427:AAE4YhjNtZHXIP0ZQ4fcFWji76xaAhCZx64"
bot = telebot.TeleBot(TOKEN)

# Archivo JSON para guardar datos
ARCHIVO_JSON = "datos.json"

# Función para guardar datos en JSON
def guardar_dato(dato):
    try:
        with open(ARCHIVO_JSON, "w") as archivo:
            json.dump({"dato": dato}, archivo)
    except Exception as e:
        print(f"Error guardando dato: {e}")

# Función para leer datos de JSON
def leer_dato():
    try:
        with open(ARCHIVO_JSON, "r") as archivo:
            datos = json.load(archivo)
        return datos.get("dato", "No hay datos guardados.")
    except FileNotFoundError:
        return "No hay datos guardados aún."

# -------------------------------
# COMANDOS DEL BOT
# -------------------------------

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "¡Hola! Soy tu bot 🤖. Usa /guardar para guardar texto y /ver para verlo.")

@bot.message_handler(commands=["guardar"])
def guardar(message):
    texto = message.text.replace("/guardar", "").strip()
    if texto:
        guardar_dato(texto)
        bot.reply_to(message, f"✅ Guardado: {texto}")
    else:
        bot.reply_to(message, "❌ Debes escribir algo después de /guardar.")

@bot.message_handler(commands=["ver"])
def ver(message):
    dato = leer_dato()
    bot.reply_to(message, f"📦 Tu dato: {dato}")

# 🔹 Comando /hola
@bot.message_handler(commands=["hola"])
def hola(message):
    bot.reply_to(message, "¡Hola! 👋 Espero que tengas un gran día.")

# 🔹 Comando /saludo
@bot.message_handler(commands=["saludo"])
def saludo(message):
    bot.reply_to(message, f"¡Saludos, {message.from_user.first_name}! 😎")

# 🔹 Comando /alerta
@bot.message_handler(commands=["alerta"])
def alerta(message):
    bot.reply_to(message, "🚨 ALERTA: Se ha detectado una situación especial.")

# 🔹 Comando /foto
@bot.message_handler(commands=["foto"])
def foto(message):
    bot.send_message(message.chat.id, "📷 Aquí tienes una foto de prueba.")
    bot.send_photo(message.chat.id, "https://i.imgur.com/ExdKOOz.png")

# 🔹 Comando /detectar
@bot.message_handler(commands=["detectar"])
def detectar(message):
    bot.reply_to(message, "🔍 Sistema de detección activado (simulado).")

# -------------------------------
# INICIAR BOT
# -------------------------------
def main():
    print("🚀 Bot en marcha...")
    bot.polling()

if __name__ == "__main__":
    main()

