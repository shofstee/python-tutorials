import sys
import pygame


class Exercise:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Exercise 12.5")
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont(None, 48)
        self.tekst="<?>"

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key < 1100000:
                        print(chr(event.key))
                        self.tekst = "Character: " + str(chr(event.key))
                    else:
                        print(event.key)
                        self.tekst = "Control: " + str(event.key)

            self.screen.fill((230, 230, 230))

            image = self.font.render(self.tekst, True, (0, 0, 0), (230, 230, 230))
            rect = image.get_rect()
            rect.center = self.screen_rect.center
            self.screen.blit(image, rect)

            pygame.display.flip()


if __name__ == '__main__':
    ex = Exercise()
    ex.run()
