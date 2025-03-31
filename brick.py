import turtle
from typing import Union


def distance(t1: turtle.Turtle, t2: turtle.Turtle) -> float:
    """
    Calculate the distance between two turtle objects.

    :param t1: The first turtle object.
    :param t2: The second turtle object.

    :return: The distance between the two turtle objects as a float.
    """
    return ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5


class Brick:
    """
    Represents a brick in the game. Handles its appearance and collisions with the ball.
    """
    def __init__(self, x: float, y: float, color: str) -> None:
        """
        Initializes a brick with a specific position, color, and size.

        :param x: The x-coordinate of the brick's starting position.
        :param y: The y-coordinate of the brick's starting position.
        :param color: The color of the brick.
        """
        self.brick: turtle.Turtle = turtle.Turtle()
        self.brick.shape("square")
        self.brick.color(color)
        self.brick.shapesize(stretch_wid=1, stretch_len=2)
        self.brick.penup()
        self.brick.goto(x, y)


    def hit_ball(self, ball: "Ball") -> bool:
        """
        Checks if the ball has collided with this brick.

        :param ball: The ball object to check for a collision.
        :return: True if the ball has collided with the brick, otherwise False.
        """
        return distance(self.brick, ball.ball) < 25


    def destroy(self) -> None:
        """
        Moves the brick off-screen, effectively destroying it when the ball collides with it.
        """
        self.brick.goto(1000, 1000)
