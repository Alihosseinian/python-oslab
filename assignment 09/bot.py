from os import error
import telebot
import random
import qrcode
import datetime
import gtts
from gtts import gTTS
import khayyam

## Username : @alihosseinian_bot
bot = telebot.TeleBot("2107910319:AAFKbQ7rmsjDOwI64QmZgZsgw-MwWj9X6m4")

############################################    #HELP      ############################################################

@bot.message_handler(commands=['start'])
def hello(message):
    bot.reply_to(message, "خوش آمدین" + message.from_user.first_name)

############################################    #GAME      #############################################################
random_number=0
test=None
def generate_random_number():
    global random_number
    random_number = random.randint(1, 10)

@bot.message_handler(commands=['game'])
def game_function(message):
    global test
    test = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = telebot.types.KeyboardButton('new game')
    test.add(itembtn1)
    generate_random_number()
    txt = bot.send_message(message.chat.id, ' عددی به صورت رندوم بین 1-10 انتخاب شده ، حدس شما چیست ؟')
    bot.register_next_step_handler(txt, game)

def game(txt):
   
    if txt.text == 'new game':
        generate_random_number()
        txt=bot.send_message(txt.chat.id, 'بازی جدیدی شروع شد و یک عدد جدید انتخاب شد ')        
        game_function(txt)

    elif int(txt.text) < random_number:
        txt = bot.send_message(txt.chat.id, '⬆️برو بالاتر',reply_markup=test)
        bot.register_next_step_handler(txt, game)

    elif int(txt.text) > random_number:
        txt = bot.send_message(txt.chat.id, '⬇️بیا پایین تر',reply_markup=test)
        bot.register_next_step_handler(txt, game)

    elif int(txt.text) == random_number:
        txt = bot.send_message(txt.chat.id, 'درست حدس زدی باریییکلااا👏👍',reply_markup=test )


#########################################   #AGE    ######################################################################

@bot.message_handler(commands=['age'])
def age_function(message):
    age = bot.send_message(message.chat.id, 'تاریخ تولدتو به هجری شمسی به صورت 1379/8/9 وارد کن')
    bot.register_next_step_handler(age, calcute_age)

def calcute_age(message):
    try:
        date = message.text.split("/")
        difrence = str(khayyam.JalaliDatetime.now() - khayyam.JalaliDatetime(date[0], date[1], date[2]))
        difrence = difrence.split(' ')
        year = int(difrence[0])//365
        day= int(difrence[0])%365
        
        bot.send_message(message.chat.id, "شما هم اکنون "+str(year)+"سال"+str(day)+"روز ، سن دارید \n")
    except:
        age = bot.send_message(message.chat.id,'لطفا با فرمت گفته شده متن را وارد کنید')
        bot.register_next_step_handler(age, calcute_age)

############################################    #CONVERT TEXT TO VOICE     ##############################################

@bot.message_handler(commands=['voice'])
def voice_generat_function(message):
   txt = bot.send_message(message.chat.id,'iam black board : لطفا یک جمله انگلیسی به صورت روبرو وارد کنید')
   bot.register_next_step_handler(txt, convert_text_to_voice)

def convert_text_to_voice(message):
    try:
        my_text = message.text
        language = 'en'
        my_object = gtts.gTTS(text=my_text, lang=language, slow=False)
        my_object.save("my_object.mp3")
        voice = open('my_object.mp3', 'rb')
        bot.send_voice(message.chat.id, voice)
    except:
        txt = bot.send_message(message.chat.id,'لطفا با فرمت گفته شده متن را وارد کنید')
        bot.register_next_step_handler(txt, convert_text_to_voice)

###########################################     #FIND MAX NUMBER    ####################################################

@bot.message_handler(commands=['max'])
def find_max_function(message):
    array = bot.send_message(message.chat.id, 'لطفا آرایه از اعداد به صورت : 1,2,3,4 وارد کنید')
    bot.register_next_step_handler(array, find_max_number)

def find_max_number(message):
    try:
        numbers = list(map(int, message.text.split(',')))
        max_number =max(numbers)
        bot.send_message(message.chat.id, "بزرگترین عدد :" + str(max_number) + "است"+"\n")
    except:
        array = bot.send_message(message.chat.id,'لطفا با فرمت گفته شده اعداد را وارد کنید')
        bot.register_next_step_handler(array, find_max_function)     

###############################################  #FIND ARG MAX NUMBER    ###############################################

@bot.message_handler(commands=['argmax'])
def find_arg_max_function(message):
    array = bot.send_message(message.chat.id, 'لطفا آرایه از اعداد به صورت :1,2,3,4 ، وارد کنید')
    bot.register_next_step_handler(array, find_index_max)

def find_index_max (message):
        try:
            numbers = list(map(int, message.text.split(',')))
            arg_max_number = numbers.index(max(numbers)) + 1
            bot.send_message(message.chat.id, "اندیس بزرگترین عدد : " + str(arg_max_number) + " است"+"\n")
        except:
            array = bot.send_message(message.chat.id,'لطفا با فرمت گفته شده اعداد را وارد کنید')
            bot.register_next_step_handler(array, find_arg_max_function)       

################################################  #CONVERT TEXT TO QRCODE  ############################################

@bot.message_handler(commands=['qrcode'])
def qrcode_generat_function(message):
    txt = bot.send_message(message.chat.id, 'لطفا نوشته خود را وارد کنید ')
    bot.register_next_step_handler(txt, qrcode_generator)
def qrcode_generator(message):
    
    picture = qrcode.make(message)
    picture.save('QrCode.png')
    qr_picture = open('QrCode.png', 'rb')
    bot.send_photo(message.chat.id, qr_picture)
   
##################################################     #HELP   ########################################################

@bot.message_handler(commands=['help'])
def help_function(message):
    bot.reply_to(message,""""
    /start : مقدمتان گلباران😂
    /game :بازی حدس عدد اجرا می شود 🎲🎮
    /age : تبدیل تاریخ تولد به سال و روز 📅
    /voice : تبدیل جمله انگلیسی به وویس🎼🎵
    /max : یافتن بزرگترین عدد ♍️ 
    /argmax : یافتن اندیس بزرگترین عدد Ⓜ️
    /qrcode : تبدیل متن به بارکد  
    /help : نمایش منو 
    """ )

#################################################################################################################               
bot.infinity_polling()