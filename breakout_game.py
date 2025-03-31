"""
What is it:
A replica of the Breakout game. Using a paddle, bounce a ball to destroy blocks.

How to run:
Run the programme. Use the left and right arrow keys to move the paddle and intercept the ball.

Documentation:
https://docs.python.org/3/library/turtle.html

Made by:
Jacob Fairhurst
"""

import turtle
from typing import List
from brick import Brick
from ball import Ball
from paddle import Paddle


class BreakoutGame:
    """
    Handles the main game logic, including screen initialization, paddle movement, ball physics, and brick-breaking mechanics.
    """
    def __init__(self) -> None:
        """
        Initializes the game with screen setup, paddle, ball, bricks, and game loop.
        """
        self.screen: turtle.Screen = turtle.Screen()
        self.screen.title("Breakout")
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

        self.paddle: Paddle = Paddle()
        self.ball: Ball = Ball()
        self.bricks: List[Brick] = self.create_bricks()

        self.screen.listen()
        self.screen.onkey(self.paddle.move_left, "Left")
        self.screen.onkey(self.paddle.move_right, "Right")

        self.run_game()


    def create_bricks(self) -> List[Brick]:
        """
        Creates and returns a list of Brick objects arranged in rows with different colors.

        :return: A list of Brick objects representing the game's brick wall.
        """
        bricks: List[Brick] = []
        colors: List[str] = ["red", "orange", "yellow", "green", "blue"]
        for i in range(5):
            for n in range(-250, 300, 50):
                brick = Brick(n, 200 - (i * 25), colors[i])
                bricks.append(brick)
        return bricks


    def run_game(self) -> None:
        """
        Starts the game loop, continuously updating the screen, moving the ball, and checking for collisions.
        """
        while True:
            self.screen.update()
            self.ball.move()
            self.check_collisions()


    def check_collisions(self) -> None:
        """
        Checks for collisions between the ball and paddle or bricks.
        The ball bounces off the paddle and destroys bricks upon impact.
        """
        if self.paddle.hit_ball(self.ball):
            self.ball.bounce_y()

        for brick in self.bricks:
            if brick.hit_ball(self.ball):
                self.bricks.remove(brick)
                brick.destroy()
                self.ball.bounce_y()
                break

        if self.ball.ycor() < -290:
            self.ball.reset_position()


if __name__ == "__main__":
    BreakoutGame()
    turtle.mainloop()
