import pygame
from breakout.screens import WelcomeScreen, GameScreen, GameOverScreen, Login



class Game:
    """Main class for the application"""

    def __init__(self):
        # Creates the window
        self.window = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('LoL Shoot')


    def run(self):
        """Main method, manages interaction between screens"""

        # These are the available screens
        screens = {
            "login": Login,
            "welcome": WelcomeScreen,
            "game": GameScreen,
            "game_over": GameOverScreen
        }

        # Start the loop
        running = True
        current_screen = "login"
        current_state = {}
        while running:
            print(current_state)
            # Obtain the screen class
            print(current_screen)
            screen_class = screens.get(current_screen)
            if not screen_class:
                raise RuntimeError(f"Screen {current_screen} not found!")

            # Create a new screen object, "connected" to the window
            screen = screen_class(self.window, current_state)
            print(screen_class)
            # Run the screen
            screen.run()

            # When the `run` method stops, we should have a `next_screen` setup
            if screen.next_screen is False:
                running = False
            # Switch to the next screen
            current_screen = screen.next_screen
            current_state = screen.state


if __name__ == "__main__":
    lolshoot = Game()
    lolshoot.run()
