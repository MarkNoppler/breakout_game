import turtle


class Paddle:
    """
    Class for the player's paddle. Allows the paddle to move left and right using the corresponding arrow key.
    """
    def __init__(self) -> None:
        """
        Initializes the paddle object, its size, and starting position.
        """
        self.paddle: turtle.Turtle = turtle.Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(0, -250)


    def move_left(self) -> None:
        """
        Moves the paddle to the left by 70 pixels if it is within the play area.
        Higher values increase speed.

        :return: None
        """
        if self.paddle.xcor() > -250:
            self.paddle.setx(self.paddle.xcor() - 70)


    def move_right(self) -> None:
        """
        Moves the paddle to the right by 70 pixels if it is within the play area.
        Higher values increase speed.

        :return: None
        """
        if self.paddle.xcor() < 250:
            self.paddle.setx(self.paddle.xcor() + 70)


    def hit_ball(self, ball: "Ball") -> bool:
        """
        Checks if the paddle and ball have collided.

        :param ball: The ball object that collides with the paddle.
        :return: Boolean. True if the ball has made contact with the paddle, else False.
        """
        return ball.ycor() < -240 and self.paddle.xcor() - 50 < ball.xcor() < self.paddle.xcor() + 50
