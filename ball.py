import turtle


class Ball:
    """
    Class to initialize the ball in the game. Handles movement, ricochet, and paddle and brick interaction.
    """

    def __init__(self) -> None:
        """
        Initializes the ball object, its shape, color, speed, and starting position.
        """
        self.ball: turtle.Turtle = turtle.Turtle()
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.penup()
        self.ball.goto(0, -230)
        self.dx: float = 2
        self.dy: float = 2


    def move(self) -> None:
        """
        Moves the ball by the velocity of dx and dy.
        Will bounce off of bricks, paddle, and screen edges.
        """
        self.ball.setx(self.ball.xcor() + self.dx)
        self.ball.sety(self.ball.ycor() + self.dy)

        if self.ball.xcor() > 290 or self.ball.xcor() < -290:
            self.dx *= -1
        if self.ball.ycor() > 290:
            self.dy *= -1


    def bounce_y(self) -> None:
        """
        Reverses ball direction when hitting anything.
        """
        self.dy *= -1


    def reset_position(self) -> None:
        """
        Resets the ball to its starting position after missing contact with the paddle.
        """
        self.ball.goto(0, -230)
        self.dy *= -1


    def ycor(self) -> float:
        """
        Gets the current y-coordinate of the ball.

        :return: The y-coordinate of the ball as a float.
        """
        return self.ball.ycor()


    def xcor(self) -> float:
        """
        Gets the current x-coordinate of the ball.

        :return: The x-coordinate of the ball as a float.
        """
        return self.ball.xcor()
