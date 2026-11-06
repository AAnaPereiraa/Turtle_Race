from turtle import Turtle, Screen
import random
import winner_msg
import loser_msg

screen = Screen()
screen.title("Turtle Race")
# Center of the finish line. The default turtle shape points up in its
# polygon, so once it faces the line its nose is 16px ahead of its center.
finish_x = 350
turtle_nose = 16
finish_line = Turtle()
finish_line.penup()
finish_line.goto(finish_x, 300)
finish_line.right(90)
finish_line.pensize(5)
finish_line.pendown()
finish_line.forward(500)
finish_line.hideturtle()
racers_list = []

def racers(name, color, start_point):
    name = Turtle()
    name.shape("turtle")
    name.color(color)
    name.penup()
    name.goto(-400, start_point)
    racers_list.append([name, color, start_point])


def reset_racers():
    for racer in racers_list:
        turtle = racer[0]
        turtle.speed("fastest")
        turtle.goto(-400, racer[2])
        turtle.setheading(0)
        turtle.speed("slow")


def run():
    while True:
        player_choice = screen.textinput("Turtle Race", "Who is your winner? (Red, Blue, Yellow, Green or Black)")
        if player_choice is None:
            break

        # Nose meets the line here; the body stays behind it.
        touch_x = finish_x - turtle_nose
        winner = ""
        racing = True
        while racing:
            for racer in racers_list:
                turtle = racer[0]
                remaining = touch_x - turtle.xcor()
                step = random.randint(5, 21)
                if step >= remaining:
                    turtle.setx(touch_x)
                    winner = racer[1]
                    racing = False
                    break
                turtle.forward(step)

        winner_msg.color_winner = winner
        loser_msg.color_winner = winner
        if winner.lower() == player_choice.lower():
            play_again = winner_msg.Winn()
        else:
            play_again = loser_msg.Losee()

        if not play_again:
            break
        reset_racers()

    screen.bye()


def main():
    racers("red", "red", 0)
    racers("blue", "blue", 50)
    racers("yellow", "yellow", 100)
    racers("green", "green", 150)
    racers("black", "black", 200)
    run()


if __name__ == "__main__":
    main()






