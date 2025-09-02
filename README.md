# 🚨 Detección de Personas con Cámara IP y Bot de Telegram

Este proyecto permite **detectar personas en tiempo real** utilizando la cámara de tu **celular** como fuente de video (con la app [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam)) y enviar **alertas con fotos a Telegram** mediante un bot.

---

## 📌 Requisitos

- **Python 3.7+**
- Librerías necesarias:
  - `opencv-python`
  - `pyTelegramBotAPI`
- **Cuenta de Telegram** y un **bot** creado en [@BotFather](https://t.me/BotFather)
- Aplicación **IP Webcam** instalada en tu celular (Android)

---

## ⚙️ Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/jordanlao0309-svg/Reconocimiento-de-personas.git
cd Reconocimiento-de-personas
# Bot de Telegram para Detección de Personas con Cámara IP

## 3. Crear el Bot de Telegram
1. Abre Telegram y busca el bot `@BotFather`.
2. Escribe `/start`.
3. Escribe `/newbot`.
4. Ingresa un nombre para tu bot (ejemplo: BotDeteccionPersonas).
5. Ingresa un nombre de usuario único (debe terminar en `bot`, ejemplo: `DeteccionPersonas_bot`).
6. Copia el **token** que te dará BotFather (lo usarás en el código).

## 4. Crear y Activar un Entorno Virtual

Para mantener las dependencias organizadas:

python -m venv venv


Activar el entorno:

En Windows (PowerShell):

.\venv\Scripts\activate


En Linux/Mac:

source venv/bin/activate

## 5. Instalar las Librerías Necesarias

Ejecuta:

pip install opencv-python pyTelegramBotAPI

## 6. Configurar el Código

Edita el archivo detectar_personas.py y coloca:

Tu TOKEN de Telegram.

Tu CHAT_ID (puedes obtenerlo desde @userinfobot).

La IP de tu cámara (ejemplo: http://10.203.175.139:8080/video).

## 7. Ejecutar el Script

Con el entorno virtual activado:

python detectar_personas.py

## 8. Funcionamiento

El script abrirá un flujo de video desde tu celular (con la app IP Webcam).

Si detecta una persona, enviará una foto con alerta a tu chat de Telegram.

Presiona q para cerrar la ventana de video.

## 9. Notas Adicionales

IP Webcam: Debes instalar esta app en tu celular y conectarte a la misma red WiFi que la PC.

La URL para el stream es http://<ip-del-celular>:8080/video.

Para mantenerlo funcionando en la empresa, puedes instalarlo en una PC dedicada y dejarlo ejecutándose.

