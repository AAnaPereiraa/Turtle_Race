from tkinter import *
from tkinter import ttk

color_winner = ""

def Winn():
    winn = Tk()
    winn.title("Turtle Race")
    play_again = {"yes": False}

    def choose(again):
        play_again["yes"] = again
        winn.quit()

    winn.protocol("WM_DELETE_WINDOW", lambda: choose(False))

    winner_mgs = ttk.Frame(winn, padding=10)
    winner_mgs.pack(pady=30)

    window_width = 400
    window_height = 250

    # Get the screen width and height
    screen_width = winn.winfo_screenwidth()
    screen_height = winn.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2


    # Set the window geometry to center it
    winn.geometry(f"{window_width}x{window_height}+{x}+{y}")
    print_msg = f"**Congratulations**\n\nYour {color_winner.capitalize()} turtle is the winner."
    ttk.Label(winner_mgs, text=print_msg, font=("Helvetica", 16), foreground="black", justify="center").grid(column=0, row=0)
    ttk.Label(winner_mgs, text="Play again?", font=("Helvetica", 14)).grid(column=0, row=1, pady=(18, 8))
    buttons = ttk.Frame(winner_mgs)
    buttons.grid(column=0, row=2)
    ttk.Button(buttons, text="Yes", command=lambda: choose(True)).grid(column=0, row=0, padx=8)
    ttk.Button(buttons, text="No", command=lambda: choose(False)).grid(column=1, row=0, padx=8)
    winn.mainloop()
    winn.destroy()
    return play_again["yes"]


if __name__ == "__main__": 
    Winn()




