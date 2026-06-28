import random, pygame, time, schedule, sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Library Game")
pygame.display.set_icon(pygame.image.load("assets/images/icon.jpg"))
clock = pygame.time.Clock()

tot_buku = 9
books_inhand = 0
total_books_collected = 0
running = True
warna = "black"
screen.fill(warna)
text_font = pygame.font.SysFont(None, 36)
text_small = pygame.font.SysFont(None, 24)

class rak_sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/shelf.jpg")
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.x = 1280-400
        self.rect.y = 720-400

class buku_sprite_yellow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/buku_kuning.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

    def randomize_position(self):
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

class buku_sprite_green(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/buku_hijau.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

    def randomize_position(self):
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

class buku_sprite_white(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/buku_putih.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

    def state(self, floor, held, shelf):
        if held:
            def update(self):
                self.rect
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

class kokomi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("assets/images/icon.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def update(self): #Movement of the player
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
rak = rak_sprite()  
player_sprites = pygame.sprite.GroupSingle(Kokomi)
object_sprites = pygame.sprite.Group()
book_in_hand = pygame.sprite.Group()
for i in range(tot_buku//3):
    buku_banyak = buku_sprite_yellow()
    object_sprites.add(buku_banyak)
for i in range(tot_buku//3):
    buku_banyak = buku_sprite_green()
    object_sprites.add(buku_banyak)
for i in range(tot_buku//3):
    buku_banyak = buku_sprite_white()
    object_sprites.add(buku_banyak)
rak_sprites = pygame.sprite.GroupSingle(rak)

text_surface = text_font.render("Collect the books!", True, (255, 255, 255))
text_total = text_font.render(f"Total books collected: 0/{tot_buku}", True, (255, 255, 255))
text_inventory = text_font.render(f"Inventory: {books_inhand}/3", True, ("white"))
text_pickup = text_small.render("Press [E] to pick up the book", True, ("white"))

def draw_everything():
    screen.fill(warna)
    rak_sprites.draw(screen)
    object_sprites.draw(screen)
    player_sprites.draw(screen)
    screen.blit(text_surface, (10, 10))
    screen.blit(text_inventory, (10, 720 - text_total.get_height()-10 - text_inventory.get_height() - 10))
    screen.blit(text_total, (10, 720 - text_total.get_height()-10))

text_total = text_font.render(f"Total books collected: {total_books_collected}/{tot_buku}", True, (255, 255, 255))

while running: 
    player_sprites.update()
    object_sprites.update()
    draw_everything()

    current_time_ms = pygame.time.get_ticks()

    if len(object_sprites) == 0:
        text_surface = text_font.render("You've collected all the books!, Put it on the shelf!", True, (255, 255, 255))

    collision_book = pygame.sprite.spritecollide(Kokomi, object_sprites, False)
    if collision_book:
        for book in collision_book:
            if len(book_in_hand) < 3:
                text_pickup = text_small.render("Press [E] to pick up the book", True, ("white"))
                screen.blit(text_pickup, (book.rect.x + 50 - text_pickup.get_width()/2, book.rect.y - 15 - text_pickup.get_height()))
                if pygame.key.get_pressed()[pygame.K_e]:
                    object_sprites.remove(book)
                    book_in_hand.add(book)
                    text_inventory = text_font.render(f"Inventory: {len(book_in_hand)}/3", True, ("white"))
            else:
                text_pickup = text_small.render("Your inventory is full", True, ("white"))
                screen.blit(text_pickup, (book.rect.x + 50 - text_pickup.get_width()/2, book.rect.y - 15 - text_pickup.get_height()))

    collision_rak = pygame.sprite.spritecollide(Kokomi, rak_sprites, False)
    if collision_rak:
        if len(book_in_hand) > 0:
            text_rak = text_font.render("Press [SPACE] to place the book on the shelf", True, (255, 255, 255))
            for rak in collision_rak:    
                screen.blit(text_rak, (1280-text_rak.get_width()-10, 720-400-text_rak.get_height()-10))
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                for i in range(len(book_in_hand)):
                    for book in book_in_hand:
                        total_books_collected+=1
                        book_in_hand.remove(book)
                text_total = text_font.render(f"Total books collected: {total_books_collected}/{tot_buku}", True, (255, 255, 255))
                text_inventory = text_font.render(f"Inventory: {len(book_in_hand)}/3", True, ("white"))      
        else:
            if total_books_collected == tot_buku:
                text_surface = text_font.render("Congratulations! You've placed all the books on the shelf!", True, (255, 255, 255))
            else:
                text_rak = text_font.render("There are no books to place on the shelf!", True, (255, 255, 255))
                screen.blit(text_rak, (1280-text_rak.get_width() - 10, 720-400-text_rak.get_height()-10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()