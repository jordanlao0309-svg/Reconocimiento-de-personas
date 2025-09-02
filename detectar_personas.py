import cv2
import telebot
import time

# 🔑 Pon tu token del bot de Telegram
TOKEN = "8290331427:AAE4YhjNtZHXIP0ZQ4fcFWji76xaAhCZx64"
CHAT_ID = "8269065510"  # Tu chat ID de Telegram
bot = telebot.TeleBot(TOKEN)

# Modelo de detección de personas
person_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# URL del stream de IP Webcam (usa /video para video en vivo)
url = "http://10.203.175.139:8080/video"

cap = cv2.VideoCapture(url)
last_sent = 0  # Para evitar enviar muchas fotos seguidas

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    persons = person_cascade.detectMultiScale(gray, 1.1, 4)

    if len(persons) > 0:
        print("🚨 Persona detectada")
        cv2.imwrite("alerta.jpg", frame)

        # Enviar a Telegram cada 10 segundos máximo
        if time.time() - last_sent > 10:
            with open("alerta.jpg", "rb") as photo:
                bot.send_photo(CHAT_ID, photo, caption="🚨 Persona detectada por la cámara")
            last_sent = time.time()

    for (x, y, w, h) in persons:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Detección de Personas", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

