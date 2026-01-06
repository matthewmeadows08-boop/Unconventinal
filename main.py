####import modules###
import tkinter as TK #import Tkinter
import background as BG #import background file
from PIL import ImageTk, Image #import pillow for images
import os as system

#import variables from background.py
PanelX = BG.panelX
PanelY = BG.panelY
PanelZ = BG.panelZ


###create window###
root = TK.Tk() #name Tkinter as root
root.title("GameEngine") #name the window
root.iconbitmap("Images/AppIcon/favicon.ico") #set icon of window 
root.attributes('-fullscreen', True) #set fullscreen
root.minsize(600, 400) #set minimum window size


###set background image###
bg_image = Image.open(BG.image_path)
photo = ImageTk.PhotoImage(bg_image)

background_label = TK.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = photo 

#set foreground text
foreground_label = TK.Label(root, text= ("PanelX:", PanelX,"//", "panelY:", PanelY,"//", "PanelZ:", PanelZ), font=("Helvetica", 16), bg="#88cffa") 
foreground_label.place(relx=0.5, rely=0.1, anchor=TK.CENTER)


###define functions###
def enter_fullscreen(event):
    root.attributes('-fullscreen', True)

def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

def printdebug(event):
    # Print debug information to console
    print(" ")
    print("---DEBUG INFO---")
    print("PanelX:", PanelX)
    print("PanelY:", PanelY)
    print("PanelZ:", PanelZ)
    print("Image Path:", BG.get_image_path(PanelX, PanelY, PanelZ))

def loadsprites(x, y, z):
    # Load sprites based on current panel coordinates
    global PanelX, PanelY, PanelZ
    PanelX, PanelY, PanelZ = x, y, z
    if PanelX == 1 and PanelY == 1 and PanelZ == 1:
        print("Load sprites for panel (1, 1, 1)")
    elif PanelX == 2 and PanelY == 2 and PanelZ == 2:
        print("Load sprites for panel (2, 2, 2)")
    elif PanelX == 3 and PanelY == 3 and PanelZ == 3:
        print("Load sprites for panel (3, 3, 3)")
    else:
        print("No sprites to load for panel (", PanelX, ",", PanelY, ",", PanelZ, ")")
    pass

def clear_sprites():
    # Clear all currently loaded sprites
    print("Clearing all sprites from the screen.")
    pass

def change_background(x, y, z):
    # Change background image based on new X, Y, Z coordinates."
    global PanelX, PanelY, PanelZ, photo, bg_image
    PanelX, PanelY, PanelZ = x, y, z
    new_image_path = BG.get_image_path(x, y, z)
    bg_image = Image.open(new_image_path)
    photo = ImageTk.PhotoImage(bg_image)
    background_label.config(image=photo)
    background_label.image = photo
    printdebug()
    clear_sprites()
    loadsprites()

def on_window_resize(event):
    # Resize background image to fit new window size
    global photo
    if bg_image:
        resized_image = bg_image.resize((event.width, event.height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(resized_image)
        background_label.config(image=photo)
        background_label.image = photo
        print("Window resized to:", event.width,"x",event.height)


###bind events###
root.bind('<Configure>', on_window_resize)
root.bind('f', enter_fullscreen)
root.bind('<Escape>', exit_fullscreen) #bind escape key to exit fullscreen
root.bind('d', printdebug) #bind D key to debug


root.mainloop() #create Loop

