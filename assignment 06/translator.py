import os
import time
WORDS = []
################################### SHOW MENU  ####################################################
def show_menu():
    print("\n \n welcome to translator  :)\n")
    print("1-add new word :\n")
    print("2-translation english 2 persian :\n")
    print("3-translation persian 2 english :\n")
    print("4-exit :\n")
##################################### LOAD DATA FROM FILE  ##################################################
def load_data_from_file():
    if os.path.exists("words_bank.txt"):
        f= open('words_bank.txt','r')
        big_text=f.read()
        lines = big_text.split('\n')
        for i in range(0,len(lines)- 1,2):
            my_dict={'english':lines[i],'persian':lines[i+1]}
            WORDS.append(my_dict)
        f.close()
    else:
        print("\n File 'words_bank.txt' vojod nadarad \n")
        exit()
########################################   ADD WORD IN DICTIONARY  ###############################################
def add():
    english = input('lotfan kalame English khod ra vared konid : ')
    for word in WORDS:
        if word['english'] == english:
            print("\nkalame vared shode daron dictionary mojod mibashad")
            break
    else:
        persian = input('lotfan kalame farsi khod ra vared konid : ')
        new_dict = {'english':english,'persian':persian}
        WORDS.append(new_dict)
        print("\n kalame mored nazar be dictionary ezafe shod ")
        f= open('words_bank.txt','w')
        for i in range(len(WORDS)):
            f.write(WORDS[i]['english']+'\n')
            if i == len(WORDS) - 1:
                f.write(WORDS[i]['persian'])
            else:
                f.write(WORDS[i]['persian']+'\n')
        f.close()
    print("\n kalame vared shode dar dictionary save shod \n ")
########################################  ENGLISH TO PERSIAN  ###############################################    
def translate_english_2_persian():
    print('\n motarjem English be Persian \n')
    user_text =input(' lotfan jomle khod ra vared konid :')
    user_jomalat =user_text.split('.')
    output_text=""
    for jomle in user_jomalat:
        user_words = jomle.split(' ')
        s = ''
        for user_word in user_words:
            for word in WORDS:
                if user_word == word['english']:
                    s +=word['persian']+" "
                    break
            else :
                s+=user_word+' '
        output_text += s + '. '
    print('\n tarjome farsi matn shoma  :\n'+ output_text)   
##########################################  PERSIAN TO ENGLISH   #############################################
def translate_persian_2_english():
    print('\n motarjem Persian be  English  \n')
    user_text =input(' lotfan jomle khod ra vared konid :')
    user_jomalat =user_text.split('.')
    output_text=""
    for jomle in user_jomalat:
        user_words = jomle.split(' ')
        s = ''
        for user_word in user_words:
            for word in WORDS:
                if user_word == word['persian']:
                    s +=word['english']+" "
                    break
            else :
                s+=user_word+' '
        output_text += s + '. '
    print("\n tarjome farsi matn shoma  :\n"+ output_text)   
##################################### MAIN    ##################################################
load_data_from_file()
while True :
    show_menu()
    choise=int(input("lotfan amaliat mored nazar ra entekhab konid :"))
    if choise == 1 :
        add()
    elif choise == 2 :
        translate_english_2_persian()
    elif choise == 3 :
        translate_persian_2_english()
    elif choise == 4 :
        print("goodbye :)\n\n")
        time.sleep(5)    
        os.system("cls")     
        exit()