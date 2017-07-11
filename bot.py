#!/usr/bin/python3
#documentación que he seguido: http://www.akirasan.net/bots-de-telegram-mediante-python/
import telegram
from telegram.ext import Updater  
from telegram.ext import CommandHandler

#Ponemos el token generado con BothFather y declaramos nuestro bot y el gestor de actualizaciones
TOKEN = '410680215:AAEdOl7MhiYoCe7ZsaptD_UIwLqFgXjPIa0'
nwkbot = telegram.Bot(token=TOKEN)
nwkbot_updater = Updater(nwkbot.token)

#Definimos las funciones de los comandos
def start(bot=nwkbot, update=nwkbot_updater):
    bot.sendMessage(chat_id=update.message.chat_id, text="¡Hola soldado! Bienvenido a Netwekeend")

def info(bot=nwkbot, update=nwkbot_updater):
    bot.sendMessage(chat_id=update.message.chat_id, text="Este bot ha sido  creado por Rafael Aybar Segura (ras212). puedes colaborar aquí https://github.com/RafaelAybar/NWK-BOT")

#Habilitamos las funciones creadas en el gestor de comandos
start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)

#"Unimos" el gestor de comandos con el de actualizaciones
dispatcher = nwkbot_updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)

#Lanzamos el gestor de actualizaciones
nwkbot_updater.start_polling()
while True:
    pass