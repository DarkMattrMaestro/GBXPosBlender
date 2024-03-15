
import bpy, ctypes



def error_message(message: str):
    title = 'An error occured!'
    ctypes.windll.user32.MessageBoxW(0, message, title, 0)



def show_message_box(title = "Message Box", icon = 'INFO', lines=""):
    myLines = lines
    
    def draw(self, context):
        if (myLines == str(myLines)):
            self.layout.label(text=myLines)
        else:
            for n in myLines:
                self.layout.label(text=n)
            
    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)