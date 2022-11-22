import pygame


class BaseScreen:
    """Base class for all game screens"""

    def __init__(self, window, current_selection):
        # window surface
        self.window = window
        # By default, there is no next screen (= game quits)
        self.next_screen = False
        self.kill_count = 0
        self.time = 0
        self.current_selection = current_selection


    def run(self):
        """
        This is the main method of the class.
        It manages the event loop, and:
        * ticks the clock at 60 FPS
        * calls `update` and `draw`
        * calls `manage_event` for each event received
        * quits the game if the quit button is clicked, or the Escape key is pressed
        """

        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            # Tick the clock
            clock.tick(60)
            # Do whatever is needed to update the screen objects
            self.update()
            # Draw the objects on the screen
            self.draw()
            # Update the display
            pygame.display.update()
            # manage the enemies from game.py
            self.manage_enemies()

            #Manage time
            self.time = int(pygame.time.get_ticks() / 1000)

            # Event loop
            for event in pygame.event.get():
                # Quit the game
                if event.type == pygame.QUIT:
                    self.running = False
                    self.next_screen = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.next_screen = False

                # Call the manage_event method
                self.manage_event(event)

                

    @property
    def rect(self):
        """Useful property to check for boundaries and dimensions"""

        return self.window.get_rect()

    def draw(self):
        """Child classes should override this method"""

        print("You should override the DRAW method in your class...")

    def update(self):
        """Child classes should override this method"""

        print("You should override the UPDATE method in your class...")

    def manage_event(self, event):
        pass

    def manage_enemies(self):
        pass