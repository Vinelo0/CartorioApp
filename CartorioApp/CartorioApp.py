import webbrowser
import kivy
from kivy.app import App
import traceback
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen

class Tela (ScreenManager):
    pass

class main (App):
    def build(self):
        try:
            return Tela()
        except Exception as e:
            with open("log.txt", "a") as log_file:
                log_file.write("Erro: " + str(e) + "\n")
                traceback.print_exc(file=log_file)
    
    
    def Link(self,contato):
         webbrowser.open("https://discordapp.com/channels/@me/vinelo2/")
            
    def Forms(self,ctt):
        webbrowser.open("https://forms.gle/jvDVPxmobeGiAndY9")
             
    def rename(self,name,color,formato):
        rename = "/rename "
        cor=""
        formatacao=""
        if color != 0 or formato != 0:
            if color == 1:
                cor = "&0"
            elif color == 2:
                cor = "&9"
            elif color == 3:
                cor = "&a"
            elif color == 4:
                cor ="&c"
            elif color == 5:
                cor="&e"
            elif color == 6:
                cor="&d"
            elif color == 7:
                cor ="&5"
            elif color == 8:
                cor = "&b"
            elif color ==9:
                cor = "&6"
            elif color == 10:
                cor = "&7"
            elif color == 11:
                cor ="&1"
            elif color ==12:
                cor="&4"
            elif color == 13:
                cor = "&2"
            elif color == 14:
                cor ="&8"
            elif color == 15:
                cor="&3"
                
            if formato == 1:
                formatacao ="&l"
            elif formato == 2:
                formatacao = "&o"
            
            resultado = rename + cor + formatacao + name
            self.root.ids.renomeado.text = resultado  
        else:
            resultado = rename + name
            self.root.ids.renomeado.text = resultado 
main().run()