from pygame import*
import random
def showEndWindow(window, message):
    clock = time.Clock()
    run = True
    font.init()
    text = font.Font(None, 70).render(message, True, (255, 255, 255))
    while run:
        # обробка подій
        for e in event.get():
            if e.type == QUIT:
                quit()

        #рендер
        window.blit(text, (120, 100))
        display.update()
        clock.tick(60)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__()
        self.speed = speed
        self.player_image = transform.scale(image.load(player_image), (size_w, size_h))
        self.rect = self.player_image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.player_image, (self.rect.x, self.rect.y))

class Hero(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed

class HeroT(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed*2
        if self.rect.x >= 500:   
            self.speed *= -1


window = display.set_mode((500, 300))
clock = time.Clock()
background = transform.scale(image.load("Galaxy.jpg"), (500, 300))
hero = Hero("hero.png", 50, 100, 2, 10, 50)
heroT = HeroT("hero.png", 450, 100, 2, 10, 50)
ball = Ball("asteroid.png", 225, 125, 2, 50, 50) 
while True:
    #обробка подій
    for e in event.get():
        if e.type == QUIT:
            quit()
    
    if ball.rect.colliderect(hero.rect):
        pass

    if ball.rect.x >= 500:
        showEndWindow(window, "Ти програв!")
    if ball.rect.x <= 0:
        showEndWindow(window, "Ти програв!")
    
    if ball.rect.y >= 300:
        ball.speed *= -1
    if ball.rect.y <= 0:
        ball.speed *= -1

    if heroT.rect.colliderect(ball.rect):
        ball.speed *= -1
    if hero.rect.colliderect(ball.rect):
        ball.speed *= -1
        #if not ball_collide:
        #    if random.randint(0, 1) == 0:
        #        ball.rect.y *= 1
        #    else:
        #        ball.rect.y *= -1
    # оновлення обєктів
    hero.update()
    heroT.update()
    ball.update()
    # відмалювати
    window.blit(background, (0, 0))
    hero.draw(window)
    heroT.draw(window)
    ball.draw(window)
    display.update()
    clock.tick(60)