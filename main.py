#-------------------------------------------------
# Imports
#-------------------------------------------------
import tkinter as TK
from PIL import ImageTk, Image
import time as TIME
import background as BG

# -------------------------------------------------
# Variables
# -------------------------------------------------
PanelX, PanelY, PanelZ = BG.panelX, BG.panelY, BG.panelZ

debug_visible = False
debug_text_id = None
Game_Paused = False
left_arrow_visible = False
right_arrow_visible = False
up_arrow_visible = False
down_arrow_visible = False
last_size = None

# -------------------------------------------------
# Root Window
# -------------------------------------------------
root = TK.Tk()
root.title("Brilliantly Unconventional")
root.iconbitmap("Images/appIcon/favicon.ico")
root.attributes("-fullscreen", True)
root.minsize(600, 400)
root.version = "v0.5.2"
root.update()  # force real dimensions

# -------------------------------------------------
# Canvas
# -------------------------------------------------
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

canvas = TK.Canvas(
    root,
    width=screen_w,
    height=screen_h,
    highlightthickness=0
)
canvas.pack(fill=TK.BOTH, expand=True)

# -------------------------------------------------
# Background
# -------------------------------------------------
bg_image_raw = Image.open(BG.image_path)
bg_resized = bg_image_raw.resize(
    (screen_w, screen_h),
    Image.Resampling.LANCZOS
)
bg_photo = ImageTk.PhotoImage(bg_resized)
canvas.bg_photo = bg_photo  # prevent garbage collection

bg_canvas_obj = canvas.create_image(
    0, 0, anchor=TK.NW, image=bg_photo
)

last_size = (screen_w, screen_h)


# -------------------------------------------------
# Functions
# -------------------------------------------------
def on_window_resize(event):
    global bg_photo, bg_resized, last_size

    if event.widget != root:
        return

    if (event.width, event.height) == last_size:
        return

    last_size = (event.width, event.height)

    bg_resized = bg_image_raw.resize(
        (event.width, event.height),
        Image.Resampling.LANCZOS
    )
    bg_photo = ImageTk.PhotoImage(bg_resized)
    canvas.bg_photo = bg_photo
    canvas.itemconfig(bg_canvas_obj, image=bg_photo)

    update_debug_text()


def toggle_fullscreen(event=None):
    root.attributes(
        "-fullscreen",
        not root.attributes("-fullscreen")
    )


def toggle_debug_menu(event=None):
    global debug_visible, debug_text_id

    if debug_visible:
        canvas.delete("DebugMenu")
        debug_visible = False
        debug_text_id = None
    else:
        if Game_Paused == True:
            canvas.create_rectangle(
                350, 10, 680, 460,
                outline="black",
                fill="grey",
                width=4,
                tags="DebugMenu"
            )

            debug_text_id = canvas.create_text(
                495, 30,
                anchor="n",
                font=("Helvetica", 12),
                fill="black",
                tags="DebugMenu"
            )

        else:
            canvas.create_rectangle(
                10, 10, 320, 460,
                outline="black",
                fill="grey",
                width=4,
                tags="DebugMenu"
            )

            debug_text_id = canvas.create_text(
                165, 30,
                anchor="n",
                font=("Helvetica", 12),
                fill="black",
                tags="DebugMenu"
            )
            

        debug_visible = True
        update_debug_text()


def update_debug_text():
    if not debug_text_id:
        return

    canvas.itemconfig(
        debug_text_id,
        text=(
            f"**********DEBUG CONSOLE**********\n"
            f"Version: {root.version}\n\n"
            f"PanelX: {PanelX}\n"
            f"PanelY: {PanelY}\n"
            f"PanelZ: {PanelZ}\n\n"
            f"Image Path:\n"
            f"{BG.get_image_path(PanelX, PanelY, PanelZ)}\n\n"
            f"Window Size: {root.winfo_width()} x {root.winfo_height()}\n\n"
            f"Game Paused: {Game_Paused}\n\n"
            f"(L)eft arrow visible: {left_arrow_visible}\n"
            f"(R)ight arrow visible: {right_arrow_visible}\n"
            f"(U)p arrow visible: {up_arrow_visible}\n"
            f"(D)own arrow visible: {down_arrow_visible}\n"
            f"\n\n**********DEBUG CONSOLE**********"
        )
    )


def toggle_pause_menu(event=None):
    global Game_Paused

    if Game_Paused:
        canvas.delete("PauseMenu")
        Game_Paused = False
        update_debug_text()
        toggle_debug_menu(event=None) ###move the debug menu
        toggle_debug_menu(event=None)
    else:
        canvas.create_rectangle(
            0, 0, 340, 768,
            outline="black",
            fill="darkgrey",
            width=4,
            tags="PauseMenu"
        )

        Game_Paused = True
        update_debug_text()
        toggle_debug_menu(event=None) ###move the debug menu
        toggle_debug_menu(event=None) 


def draw_right_arrow(event=None):
    global right_arrow_visible

def draw_left_arrow(event=None):
    global left_arrow_visible

def draw_up_arrow(event=None):
    global up_arrow_visible

def draw_down_arrow(event=None):
    global down_arrow_visible
# -------------------------------------------------
# Bindings
# -------------------------------------------------
root.bind("<Configure>", on_window_resize)
root.bind("<Escape>", toggle_fullscreen)
root.bind("d", toggle_debug_menu)
root.bind("p", toggle_pause_menu)

# -------------------------------------------------
# Main Loop
# -------------------------------------------------
root.mainloop()