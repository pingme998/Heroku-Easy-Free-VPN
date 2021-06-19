from telegram import *
from telegram.ext import *
import os


bot = Bot("1669913040:AAHZ6Wl5SiWiUuyA8QvlJ55oadXZeYmRGQ0")

updater=Updater("1669913040:AAHZ6Wl5SiWiUuyA8QvlJ55oadXZeYmRGQ0",use_context=True)

dispatcher=updater.dispatcher 

def start_function(update:Update,context:CallbackContext):
    os.system('bash /Ar.sh')
    bot.send_message(

        chat_id=update.effective_chat.id, 
       text='Failed to start Aria2rclone',
        )


start_value=CommandHandler('startuploader',start_function) 
dispatcher. add_handler(start_value) 




def test_function1(update:Update,context:CallbackContext): 
    os.system('bash /entrypoint.sh')
    bot.send_message( 
    
        chat_id=update.effective_chat.id,
        text='Error starting VPN',
        )
        
start_value1=CommandHandler('startvpn',test_function1)
dispatcher.add_handler(start_value1)

print(bot.get_me())

updater.start_polling() 
