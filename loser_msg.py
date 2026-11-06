from tkinter import *
from tkinter import ttk

color_winner = ""

def Losee():
    losee = Tk()
    losee.title("Turtle Race")
    play_again = {"yes": False}

    def choose(again):
        play_again["yes"] = again
        losee.quit()

    losee.protocol("WM_DELETE_WINDOW", lambda: choose(False))

    loser_mgs = ttk.Frame(losee, padding=10)
    loser_mgs.pack(pady=30)

    window_width = 400
    window_height = 250

    # Get the screen width and height
    screen_width = losee.winfo_screenwidth()
    screen_height = losee.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2


    # Set the window geometry to center it
    losee.geometry(f"{window_width}x{window_height}+{x}+{y}")
    print_msg = f"Pouts...not this time!!!\n\nThe {color_winner.capitalize()} turtle is the winner."
    ttk.Label(loser_mgs, text=print_msg, font=("Helvetica", 16), foreground="black", justify="center").grid(column=0, row=0)
    ttk.Label(loser_mgs, text="Play again?", font=("Helvetica", 14)).grid(column=0, row=1, pady=(18, 8))
    buttons = ttk.Frame(loser_mgs)
    buttons.grid(column=0, row=2)
    ttk.Button(buttons, text="Yes", command=lambda: choose(True)).grid(column=0, row=0, padx=8)
    ttk.Button(buttons, text="No", command=lambda: choose(False)).grid(column=1, row=0, padx=8)
    losee.mainloop()
    losee.destroy()
    return play_again["yes"]

if __name__ == "__main__":
    Losee()

