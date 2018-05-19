# -*- coding: utf-8 -*-
import telebot 
import requests
bot = telebot.TeleBot('593925092:AAENICMP76F9pQhfuOy1U92QNK0srb6FVvI')

@bot.message_handler(content_types=['text'])
def localizame(mensaje):
  id_chat= mensaje.chat.id
  bot.send_message(id_chat, mensaje)
 
# api-endpoint
URL = "http://maps.googleapis.com/maps/api/geocode/json"
 
# location given here
location = "Babel Sistemas de Informacion Madrid"
 
# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}
 
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
 
# extracting data in json format
data = r.json()
 
 
# extracting latitude, longitude and formatted address 
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']
 
# printing the output
#print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#      %(latitude, longitude,formatted_address))

bot.polling()
#while True:
#    try:
#        bot.polling(none_stop=True)
#    except Exception as e:
#        logger.error(e)
#        time.sleep(15)
