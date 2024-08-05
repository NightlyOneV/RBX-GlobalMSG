import customtkinter as ctk 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("DBGT - Announcements System")
        self.geometry("700x450")
        
        #region TAB SECTIONS
        
        self.SYSTEM_TAB = ctk.CTkTabview(self)
        self.SYSTEM_TAB.pack(pady=5)
        
        self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH = self.SYSTEM_TAB.add("GLOBAL ANNOUNCEMENT")
        self.GLOBAL_MESSAGE_TAB_SWITCH = self.SYSTEM_TAB.add("GLOBAL CHAT MESSAGE ")
        
        #endregion
        
        #region GLOBAL ANNOUNCEMENT TITLE
        self.EXPL_GLOBAL_ANNOUNCEMENT_TITLE_FONT = ctk.CTkFont(family="Fixedsys", size=25)
        self.EXPL_GLOBAL_ANNOUNCEMENT_TITLE = ctk.CTkLabel(self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH, text='MESSAGE TITLE', width=40, height=28, fg_color='transparent', font=self.EXPL_GLOBAL_ANNOUNCEMENT_TITLE_FONT)
        self.EXPL_GLOBAL_ANNOUNCEMENT_TITLE.pack(pady=10)

        self.GLOBAL_ANNOUNCEMENT_TITLE = ctk.CTkTextbox(self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH, width=660, height=50)
        self.GLOBAL_ANNOUNCEMENT_TITLE.pack(pady=5)
        #endregion
        
        #region GLOBAL ANNOUNCEMENT TEXT CONTENT
        self.EXPL_GLOBAL_ANNOUNCEMENT_TXT_FONT = ctk.CTkFont(family="Fixedsys", size=25)
        self.EXPL_GLOBAL_ANNOUNCEMENT_TXT = ctk.CTkLabel(self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH, text='MESSAGE CONTENT', width=40, height=28, fg_color='transparent', font=self.EXPL_GLOBAL_ANNOUNCEMENT_TITLE_FONT)
        self.EXPL_GLOBAL_ANNOUNCEMENT_TXT.pack(pady=10)
        
        self.GLOBAL_ANNOUNCEMENT_TXT = ctk.CTkTextbox(self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH, width=660, height=150)
        self.GLOBAL_ANNOUNCEMENT_TXT.pack(pady=5)
        #endregion
        
        #region GLOBAL ANNOUNCEMENT SEND MESSAGE
        self.GLOBAL_ANNOUNCEMENT_SEND = ctk.CTkButton(self.GLOBAL_ANNOUNCEMENT_TAB_SWITCH, text="SEND MESSAGE")
        self.GLOBAL_ANNOUNCEMENT_SEND.pack(pady=20)
        #endregion



Program = App()
Program.mainloop()
