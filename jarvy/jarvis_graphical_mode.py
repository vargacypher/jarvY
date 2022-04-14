import speech_recognition as sr
from gtts import gTTS
import os
from preferredsoundplayer import *
import datetime
import pywhatkit as kit
import time
import subprocess as sp

#apt install mpv, flac, cmatrix
#pip pipwin 
# pipwin pyaudio

#Função para ouvir e reconhecer a fala

def listen():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:

        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        print("Diga alguma coisa: ")
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
        frase=""
        
        try:
        #Passa a variável para o algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio,language='pt-BR')

            print("Você disse: " + frase)       
        
        except:

            print("Não entendi Mestre")

    return frase

#while True:
 #   ouvir_microfone()


def respond(output):
    num = 0
    print(output)
    num += 1
    response = gTTS(text=output, lang='pt')
    file = str(num)+".mp3"
    response.save(file)
    soundplay(file,True)
    os.remove(file)

if __name__=='__main__':
    respond("Olá Mestre, eu sou JarvYY sua personal assistant")
    respond("Como posso lhe ajudar?")
    
    while True:
        text = listen().lower()
        
        if text==0:
            continue
        
        elif 'ok'in text:
            respond("Olá")
            text = listen().lower()        
        
        else:
            continue
        
        if 'horas' in text:
            time = datetime.datetime.now().strftime("%H:%M")
            respond("São "+time)
            
        elif 'dormir' in text:
            respond("Adeus baby S2")
            os.system("lxterminal -e 'bash kill.sh; bash killall -TERM python'") 
            break
        
        elif 'youtube' in text:
            respond("O que deseja ouvir?")
            query = listen().lower()
            kit.playonyt(query)
            
        elif 'google' in text:
            respond("O que quer saber?")
            query = listen().lower()
            if 'nada' in query:
                continue
            kit.search(query)
            respond("Buscando")
            
        elif 'cmd' in text:
            os.system("lxterminal")
        
        elif 'matrix' in text:
            os.system("lxterminal -e 'cmatrix'")
            
        #todo
        elif 'meu mix' in text:
            respond("carregando")
            #Todo Implement sleep dyamic
            os.system("lxterminal -e 'bash /home/pi/Desktop/playlist.sh;sleep 5h'") 

        elif 'nuclear' in text:
            respond("Comando")
            query = listen().lower()
            if 'nada' in query:
                continue
            respond("Executando")
            os.system(f"lxterminal -e '{query}; bash'")
            #sp.run(query,shell=True)
            respond('Feito')
            
        else:
            respond("O idiota que me programou ainda não adicionou esta função")
