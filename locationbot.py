# -*- coding: utf-8 -*-
import telebot 
import requests
import logging
bot = telebot.TeleBot('593925092:AAENICMP76F9pQhfuOy1U92QNK0srb6FVvI')

@bot.message_handler(content_types=['text'])
def handle_text(mensaje):
  id_chat= mensaje.chat.id
  location = mensaje.text
  URL = "http://maps.googleapis.com/maps/api/geocode/json"
  PARAMS = {'address':location}
  r = requests.get(url = URL, params = PARAMS)
  # extracting data in json format
  data = r.json()
  # extracting latitude, longitude and formatted address 
  #of the first matching location
  latitude = data['results'][0]['geometry']['location']['lat']
  longitude = data['results'][0]['geometry']['location']['lng']
  formatted_address = data['results'][0]['formatted_address']
  #printing the output
  localizacion ="Direccion:%s\nLatitud:%s\nLongitud:%s" %(formatted_address,latitude, longitude)
  bot.send_message(id_chat, localizacion)
 

bot.polling()
#while True:
#    try:
#        bot.polling(none_stop=True)
#    except Exception as e:
#        logger.error(e)
#        time.sleep(15)
