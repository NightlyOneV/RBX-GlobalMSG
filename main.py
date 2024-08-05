import customtkinter as ctk 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("DBGT - Announcements System")
        self.geometry("700x350")
        self.resizable(False, False)

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
        self.GLOBAL_ANNOUNCEMENT_SEND = ctk.CTkButton(self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH,width = 660, height = 50, text="SEND MESSAGE", command=self.GLOBAL_ANNOUNCEMENT_EVENT)
        self.GLOBAL_ANNOUNCEMENT_SEND.pack(pady=10)
        
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

        #region GLOBAL MESSAGE SEND 
        
        self.GLOBAL_MESSAGE_SEND = ctk.CTkButton(self.GLOBAL_MESSAGE_TAB_SWITCH, width = 660, height = 50, text="SEND MESSAGE", command=self.GLOBAL_MESSAGE_EVENT)
        self.GLOBAL_MESSAGE_SEND.pack(pady=10)

        #endregion

        #endregion

    def GLOBAL_ANNOUNCEMENT_EVENT(self):
        TITLE_text = self.GLOBAL_ANNOUNCEMENT_TITLE.get("0.0", "end")
        MSG_text = self.GLOBAL_ANNOUNCEMENT_TXT.get("0.0", "end")

        print(TITLE_text)
        print(MSG_text)
        
    def GLOBAL_MESSAGE_EVENT(self):
        TITLE_text = self.GLOBAL_MESSAGE_TITLE.get("0.0", "end")
        MSG_Text = self.GLOBAL_MESSAGE_TXT.get("0.0", "end")

        print(TITLE_text)
        print(MSG_Text)

Program = App()
Program.mainloop()
