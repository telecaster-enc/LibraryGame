import random, pygame, time, schedule, sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Library Game")
pygame.display.set_icon(pygame.image.load("assets/icon.jpg"))
clock = pygame.time.Clock()

running = True
warna = "black"
screen.fill(warna)
text_font = pygame.font.SysFont(None, 36)
text_surface = text_font.render("Collect the books!", True, (255, 255, 255))
text_total = text_font.render("Total books collected: 0/4", True, (255, 255, 255))

class rak_sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/shelf.jpg")
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.x = 1280-400
        self.rect.y = 720-400

class buku_sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/buku.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

    def randomize_position(self):
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

class buku_sprite2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/buku.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

    def randomize_position(self):
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

class buku_sprite3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/buku.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

    def randomize_position(self):
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

class buku_sprite4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/buku.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

    def randomize_position(self):
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

class kokomi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/icon.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += 10
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= 10
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += 10
            #self.rect = self.image.get_rect()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= 10
            #self.rect = self.image_flipped.get_rect()

Kokomi = kokomi()
buku1 = buku_sprite()
buku2 = buku_sprite2()
buku3 = buku_sprite3()
buku4 = buku_sprite4()
rak = rak_sprite()  
player_sprites = pygame.sprite.GroupSingle(Kokomi)
object_sprites = pygame.sprite.Group()
object_sprites.add(buku1)
object_sprites.add(buku2)
object_sprites.add(buku3)
object_sprites.add(buku4)
rak_sprites = pygame.sprite.GroupSingle(rak)

def draw_everything():
    screen.fill(warna)
    rak_sprites.draw(screen)
    object_sprites.draw(screen)
    player_sprites.draw(screen)
    screen.blit(text_surface, (720/2 - text_surface.get_width()/2, 10))
    screen.blit(text_total, (10, 620))

def show_text():
    text_surface = text_font.render("You collected a book!", True, (255, 255, 255))
    screen.blit(text_surface, (720/2 - text_surface.get_width()/2, 50))
    pygame.display.flip()

# Initialize the total books collected
total_books_collected = 0
text_total = text_font.render(f"Total books collected: {total_books_collected}/4", True, (255, 255, 255))

while running: 
    player_sprites.update()
    object_sprites.update()
    draw_everything()

    if len(object_sprites) == 0:
        text_surface = text_font.render("You've collected all the books!, Put it on the shelf!", True, (255, 255, 255))

    collision_book = pygame.sprite.spritecollide(Kokomi, object_sprites, True)
    if collision_book:
        show_text()
        total_books_collected += 1
        text_total = text_font.render(f"Total books collected: {total_books_collected}/4", True, (255, 255, 255))

    collision_rak = pygame.sprite.spritecollide(Kokomi, rak_sprites, False)
    if collision_rak:
        if len(object_sprites) == 0:
            text_rak = text_font.render("Press [SPACE] to place the book on the shelf", True, (255, 255, 255))
            screen.blit(text_rak, (720/2 - text_rak.get_width()/2, 100))
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                text_rak = text_font.render("You placed the book on the shelf!, You Won!", True, (255, 255, 255))
                screen.blit(text_rak, (720/2 - text_rak.get_width()/2, 150))
                pygame.display.flip()
                time.sleep(2)
                running = False
        else:
            text_rak = text_font.render("You need to collect all the books first!", True, (255, 255, 255))
            screen.blit(text_rak, (720/2 - text_rak.get_width()/2, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()