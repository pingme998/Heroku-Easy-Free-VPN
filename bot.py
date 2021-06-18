from telegram import *
from telegram.ext import *


bot = Bot("1669913040:AAHZ6Wl5SiWiUuyA8QvlJ55oadXZeYmRGQ0")

updater=Updater("1669913040:AAHZ6Wl5SiWiUuyA8QvlJ55oadXZeYmRGQ0",use_context=True)

dispatcher=updater.dispatcher 

def start_function(update:Update,context:CallbackContext): 
    bot.send_message(

        chat_id=update.effective_chat.id, 
        text='Hello learner this is developeranaz' '/n' 'tutorial link : https://youtu.be/oxmZ9zczptg',
        #text3='wffff',
        ! rclone serve http CLOUDNAME:
        )


start_value=CommandHandler('start',start_function) 
dispatcher. add_handler(start_value) 




def test_function1(update:Update,context:CallbackContext): 
    bot.send_message( 
    
        chat_id=update.effective_chat.id,
        text='HELLO JI',
        )
        
start_value1=CommandHandler('HELLO',test_function1)
dispatcher.add_handler(start_value1)

print(bot.get_me())

updater.start_polling() 
