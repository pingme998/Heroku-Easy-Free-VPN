from telegram import *
from telegram.ext import *
import os


bot = Bot("1669913040:AAHZ6Wl5SiWiUuyA8QvlJ55oadXZeYmRGQ0")

updater=Updater("1669913040:AAHZ6Wl5SiWiUuyA8QvlJ55oadXZeYmRGQ0",use_context=True)

dispatcher=updater.dispatcher 

def start_function(update:Update,context:CallbackContext):
    os.system('pkill -f "Ar.sh"')
    os.system('pkill -f "jupyter-notebook"')
    os.system('pkill -f "voila"')
    os.system('parallel <v2ray')
    bot.send_message(

        chat_id=update.effective_chat.id, 
     #  text='Hello learner this is developeranaz' '/n' 'tutorial link : https://youtu.be/oxmZ9zczptg',
  #     text = open('j.txt', 'r').read()
        )


start_value=CommandHandler('start',start_function) 
dispatcher. add_handler(start_value) 




def test_function1(update:Update,context:CallbackContext): 
    os.system('pkill -f "nginx"')
    os.system('pkill -f "entrypoint.sh"')
    os.system('pkill -f "ss-server"')
    os.system('pkill -f "v2ray-plugin"')
    os.system('parallel <aria')
    bot.send_message( 
    
        chat_id=update.effective_chat.id,
       # text='HELLO JI',
        )
        
start_value1=CommandHandler('HELLO',test_function1)
dispatcher.add_handler(start_value1)

print(bot.get_me())

updater.start_polling() 
