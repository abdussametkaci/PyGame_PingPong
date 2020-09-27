import pygame
BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):

    # This class represents a paddle. It derives from the "Sprite" class in Pygame.
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveUp(self, pixel):

        self.rect.y = self.rect.y - pixel

        #Check that you are not going too far (off the screen - top of the screen)
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixel):

        self.rect.y = self.rect.y + pixel

        #Check that you are not going too far (off the screen - bottom of the screen)
        if self.rect.y > 400:
            self.rect.y = 400

