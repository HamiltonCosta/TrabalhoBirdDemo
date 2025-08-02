import pygame
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 700
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bird - Demo')

# Fontes
font = pygame.font.SysFont('Bauhaus 93', 60)
footer_font = pygame.font.SysFont('Arial', 20)

# Cores
white = (255, 255, 255)

# Variáveis do jogo
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
menu = True
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

# Imagens
bg = pygame.image.load('assets/img/bg.png')
ground_img = pygame.image.load('assets/img/ground.png')
button_img = pygame.image.load('assets/img/restart.png')
message_img = pygame.image.load('assets/img/message.png')

# Sons
point_sound = pygame.mixer.Sound('assets/sons/point.wav')
hit_sound  = pygame.mixer.Sound('assets/sons/hit.wav')
wing_sound = pygame.mixer.Sound('assets/sons/wing.wav')

# Funções
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height / 2)
    return 0

# Classes
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images  = [pygame.image.load(f'assets/img/bird{num}.png') for num in range(1, 4)]
        self.index   = 0
        self.counter = 0
        self.image   = self.images[self.index]
        self.rect    = self.image.get_rect(center=(x, y))
        self.vel     = 0
        self.clicked = False

    def update(self):
        if flying:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if not game_over:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.vel = -10
                wing_sound.play()
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            self.counter += 1
            if self.counter > 5:
                self.counter = 0
                self.index = (self.index + 1) % len(self.images)

            img = self.images[self.index]
            self.image = pygame.transform.rotate(img, self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        super().__init__()
        self.image = pygame.image.load('assets/img/pipe.png')
        self.rect  = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - pipe_gap // 2]
        if position == -1:
            self.rect.topleft = [x, y + pipe_gap // 2]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect  = self.image.get_rect(topleft=(x, y))

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

# Grupos
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flappy = Bird(100, int(screen_height / 2))
bird_group.add(flappy)

# Botão de restart
button_x = screen_width // 2 - 50
button_y = screen_height - 150
restart_button = Button(button_x, button_y, button_img)

# Loop principal
run = True
while run:
    clock.tick(fps)

    # Menu
    if menu:
        screen.blit(bg, (0, 0))
        text_surface = font.render('FlyBird', True, white)
        draw_text('FlyBird', font, white, screen_width // 2 - text_surface.get_width() // 2, 200)
        screen.blit(message_img, (screen_width // 2 - message_img.get_width() // 2, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu = False
                flying = False
                game_over = False
                score = reset_game()

        # Direitos autorais no menu
        footer_text = 'Hamilton Costa Gonçalves Junior RU:4742586'
        footer_surface = footer_font.render(footer_text, True, white)
        screen.blit(footer_surface, ((screen_width - footer_surface.get_width()) // 2, screen_height - 30))

        pygame.display.update()
        continue

    # Fundo
    screen.blit(bg, (0, 0))

    # Sprites
    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)
    screen.blit(ground_img, (ground_scroll, 768))

    # Pontuação
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
           and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
           and not pass_pipe:
            pass_pipe = True
        if pass_pipe:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                point_sound.play()
                pass_pipe = False

    draw_text(str(score), font, white, int(screen_width / 2), 20)

    # Colisões
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        if not game_over:
            hit_sound.play()
        game_over = True

    if flappy.rect.bottom >= 768:
        if not game_over:
            hit_sound.play()
        game_over = True
        flying = False

    # Geração de canos
    if not game_over and flying:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(screen_width, screen_height // 2 + pipe_height, -1)
            top_pipe = Pipe(screen_width, screen_height // 2 + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

        pipe_group.update()

    # Botão restart
    if game_over:
        if restart_button.draw():
            game_over = False
            score = reset_game()

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not flying and not game_over:
            flying = True

    # Direitos autorais (rodapé)
    footer_text = 'Hamilton Costa Gonçalves Junior RU:4742586'
    footer_surface = footer_font.render(footer_text, True, white)
    screen.blit(footer_surface, ((screen_width - footer_surface.get_width()) // 2, screen_height - 30))

    pygame.display.update()

pygame.quit()
