import customtkinter as ctk 
import requests 
from CTkColorPicker import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#region API KEY
API_KEY = ""
#endregion



class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("DBGT - Announcements System")
        self.geometry("700x450")
        self.resizable(False, False)

        self.HEADER_COLOR = "#FFFFFF"
        self.CONTENT_COLOR = "#FFFFFF"

        #region TAB SECTIONS
        
        self.SYSTEM_TAB = ctk.CTkTabview(self)
        self.SYSTEM_TAB.pack(pady=5)
        
        self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH = self.SYSTEM_TAB.add("GLOBAL ANNOUNCEMENT")
        self.GLOBAL_MESSAGE_TAB_SWITCH = self.SYSTEM_TAB.add("GLOBAL CHAT MESSAGE ")
        
        #endregion
        
        #region GLOBAL ANNOUNCEMENT CONTENTS
        
        #region GLOBAL ANNOUNCEMENT TITLE

        self.EXPL_GLOBAL_ANNOUNCEMENT_TITLE_FONT = ctk.CTkFont(family="Fixedsys", size=25)
        self.EXPL_GLOBAL_ANNOUNCEMENT_TITLE = ctk.CTkLabel(self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH, text='MESSAGE HEADER', width=40, height=28, fg_color='transparent', font=self.EXPL_GLOBAL_ANNOUNCEMENT_TITLE_FONT)
        self.EXPL_GLOBAL_ANNOUNCEMENT_TITLE.pack(pady=5)

        self.GLOBAL_ANNOUNCEMENT_TITLE = ctk.CTkTextbox(self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH, width=660, height=26)
        self.GLOBAL_ANNOUNCEMENT_TITLE.pack(pady=5)

        #endregion
        
        #region GLOBAL ANNOUNCEMENT TEXT CONTENT

        self.EXPL_GLOBAL_ANNOUNCEMENT_TXT_FONT = ctk.CTkFont(family="Fixedsys", size=25)
        self.EXPL_GLOBAL_ANNOUNCEMENT_TXT = ctk.CTkLabel(self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH, text='MESSAGE CONTENT', width=40, height=28, fg_color='transparent', font=self.EXPL_GLOBAL_ANNOUNCEMENT_TITLE_FONT)
        self.EXPL_GLOBAL_ANNOUNCEMENT_TXT.pack(pady=5)
        
        self.GLOBAL_ANNOUNCEMENT_TXT = ctk.CTkTextbox(self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH, width=660, height=100)
        self.GLOBAL_ANNOUNCEMENT_TXT.pack(pady=5)

        #endregion
        
        #region GLOBAL ANNOUNCEMENT SEND MESSAGE
        self.GLOBAL_ANNOUNCEMENT_HEADER_COLOR = ctk.CTkButton(self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH, width = 200, height=50, text="SELECT HEADER COLOR", command=lambda: self.ASK_U_COLOR)
        self.GLOBAL_ANNOUNCEMENT_HEADER_COLOR.pack(pady=5)

        self.GLOBAL_ANNOUNCEMENT_SEND = ctk.CTkButton(self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH,width = 150, height = 50, text="SEND MESSAGE", command=self.GLOBAL_ANNOUNCEMENT_EVENT, fg_color='red', hover_color='dark red')
        self.GLOBAL_ANNOUNCEMENT_SEND.pack(pady=5)
        
        #endregion
       
        #endregion

        #region GLOBAL MESSAGE CONTENTS

        #region GLOBAL MESSAGE TITLE

        self.EXPL_GLOBAL_MESSAGE_TITLE = ctk.CTkLabel(self.GLOBAL_MESSAGE_TAB_SWITCH, text='MESSAGE NAME', width=40, height=28, fg_color="transparent", font=self.EXPL_GLOBAL_ANNOUNCEMENT_TITLE_FONT)
        self.EXPL_GLOBAL_MESSAGE_TITLE.pack(pady=5)

        self.GLOBAL_MESSAGE_TITLE = ctk.CTkTextbox(self.GLOBAL_MESSAGE_TAB_SWITCH, width=660, height=26)
        self.GLOBAL_MESSAGE_TITLE.pack(pady=5)

        #endregion

        #region GLOBAL MESSAGE TEXT CONTENT
        
        self.EXPL_GLOBAL_MESSAGE_TXT = ctk.CTkLabel(self.GLOBAL_MESSAGE_TAB_SWITCH, text='MESSAGE CONTENT', width=40, height=28, fg_color="transparent", font=self.EXPL_GLOBAL_ANNOUNCEMENT_TITLE_FONT)
        self.EXPL_GLOBAL_MESSAGE_TXT.pack(pady=5)

        self.GLOBAL_MESSAGE_TXT = ctk.CTkTextbox(self.GLOBAL_MESSAGE_TAB_SWITCH, width=660, height=100)
        self.GLOBAL_MESSAGE_TXT.pack(pady=5)

        #endregion

        #region GLOBAL MESSAGE BUTTONS 
        
        self.GLOBAL_MESSAGE_COLOR_PICKER = ctk.CTkButton(self.GLOBAL_MESSAGE_TAB_SWITCH, width = 200, height=50, text="SELECT CHAT COLOR", command=self.ASK_U_COLOR("Msg"))
        self.GLOBAL_MESSAGE_COLOR_PICKER.pack(padx=0, pady=5)

        self.GLOBAL_MESSAGE_SEND = ctk.CTkButton(self.GLOBAL_MESSAGE_TAB_SWITCH, width = 200, height = 50, text="SEND MESSAGE", command=self.GLOBAL_MESSAGE_EVENT, fg_color='red', hover_color='dark red')
        self.GLOBAL_MESSAGE_SEND.pack(padx=0,pady=5)

        #endregion

        #endregion

    def ASK_U_COLOR(self, whatType):
        print(whatType)
        pickingColor = AskColor()
        color = pickingColor.get()
        
        match whatType:
            case "Header":
                self.HEADER_COLOR = color
                self.APPLY_COLOR("Announce")
            case "Content":
                self.CONTENT_COLOR = color
                self.APPLY_COLOR("Announce")
            case "Msg":
                self.MSG_COLOR = color
                self.APPLY_COLOR("Msg")

      

    def APPLY_COLOR(self, whatType ):
        match whatType:
            case "Msg":
                self.EXPL_GLOBAL_MESSAGE_TXT.configure(text_color=self.MSG_COLOR)
            case "Announce":
                self.EXPL_GLOBAL_ANNOUNCEMENT_TITLE.configure(text_color=self.HEADER_COLOR)
                self.EXPL_GLOBAL_ANNOUNCEMENT_TXT.configure(text_color=self.CONTENT_COLOR)

    def ERROR_WARNING(self, errorCode, errorReason):
        ERROR_WINDOW = ctk.CTkToplevel(self)
        ERROR_WINDOW.title("ERROR")
        ERROR_WINDOW.geometry = "300x200"
        ERROR_WINDOW.resizable(False, False)
        ERROR_WINDOW.focus()

        ERROR_LABEL = ctk.CTkLabel(ERROR_WINDOW, width=250, height=150, text=f"ERROR {errorCode} | {errorReason}")
        ERROR_LABEL.pack(pady=5)

    def FIRE_MESSAGING_SERVICE(self, HEADER, CONTENT, TYPE):
        if TYPE == "GA":
            
            POST_MESSAGING_SERVICE_API = "https://apis.roblox.com/messaging-service/v1/universes/6312078066/topics/GLOBALANNOUNCE"
            POST_MESSAGE = {'message':f"{HEADER}ç{CONTENT}"}
            POST_HEADERS = {'x-api-key':API_KEY, 'Content-Type': 'application/json'}    
            
            reqStatus = requests.post(POST_MESSAGING_SERVICE_API, json=POST_MESSAGE, headers=POST_HEADERS)
            
            if reqStatus.status_code == 200:
                print("Message Sent!")
            else:
                self.ERROR_WARNING(reqStatus.status_code, reqStatus.reason)
            
        else:
            
            POST_MESSAGING_SERVICE_API = "https://apis.roblox.com/messaging-service/v1/universes/6312078066/topics/GLOBALMESSAGE"
            POST_MESSAGE = {'message':f"{HEADER}ç{CONTENT}"}
            POST_HEADERS = {'x-api-key':API_KEY, 'Content-Type': 'application/json'}    
            
            reqStatus = requests.post(POST_MESSAGING_SERVICE_API, json=POST_MESSAGE, headers=POST_HEADERS)
            
            if reqStatus.status_code == 200:
                print("Message Sent!")
            else:
                self.ERROR_WARNING(reqStatus.status_code)


    def GLOBAL_ANNOUNCEMENT_EVENT(self):
        TITLE_text = self.GLOBAL_ANNOUNCEMENT_TITLE.get("0.0", "end")
        MSG_text = self.GLOBAL_ANNOUNCEMENT_TXT.get("0.0", "end")

        self.FIRE_MESSAGING_SERVICE(TITLE_text, MSG_text, "GA")
        
    def GLOBAL_MESSAGE_EVENT(self):
        TITLE_text = self.GLOBAL_MESSAGE_TITLE.get("0.0", "end")
        MSG_Text = self.GLOBAL_MESSAGE_TXT.get("0.0", "end")

        self.FIRE_MESSAGING_SERVICE(TITLE_text, MSG_Text, "GM")

Program = App()
Program.mainloop()
