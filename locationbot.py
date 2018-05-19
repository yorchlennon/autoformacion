# -*- coding: utf-8 -*-
import telebot 
import requests
bot = telebot.TeleBot('593925092:AAENICMP76F9pQhfuOy1U92QNK0srb6FVvI')

@bot.message_handler(content_types=['text'])
def handle_text(mensaje):
  id_chat= mensaje.chat.id
  bot.send_message(id_chat, mensaje.message.text)
 

bot.polling()
#while True:
#    try:
#        bot.polling(none_stop=True)
#    except Exception as e:
#        logger.error(e)
#        time.sleep(15)
