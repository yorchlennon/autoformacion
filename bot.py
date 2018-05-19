# -*- coding: utf-8 -*-
import telebot 
import random
bot = telebot.TeleBot('538628418:AAFjQ3IGb0c2neSjAWO8xb5e0n1w1l2NN28')

@bot.message_handler(commands=['saluda'])
def saluda(mensaje):
     id_chat= mensaje.chat.id #El id del chat para saber el destino de la respuesta que va a enviar el bot
     username= message.username
     bot.send_message( id_chat, 'Que pasa gente' + username) 
     
@bot.message_handler(commands=['planes'])
def planes(mensaje):
    plan =  ['¿Cuando vamos a la Warner que tengo 2x1?','Tengo barbacoa en el Chaparral','Ya no propongo mas planecillos','¿Está Ovi?','Estoy en Salou']
    aleatorio = random.randrange(0,len(plan),1)
    id_chat= mensaje.chat.id 
    bot.send_message( id_chat, plan[aleatorio])   
     
@bot.message_handler(commands=['selfie'])
def selfie(mensaje):
    id_chat = mensaje.chat.id
    bot.send_message( id_chat, 'ratata.jpg')
    bot.send_message( id_chat, '..')
    bot.send_message( id_chat, 'No tengo el archivo, ahora estoy alojado en el pc de Jorge')
  # bot.send_photo(id_chat, photo=open('rattata.jpg', 'rb'))

@bot.message_handler(commands=['echo'])
def echo(mensaje, repito):
     bot.send_message( id_chat, repito)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logger.error(e)
        time.sleep(15)
