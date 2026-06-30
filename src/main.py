import random, pygame, time, schedule, sys, math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Library Game")
pygame.display.set_icon(pygame.image.load("assets/images/icon.jpg"))
clock = pygame.time.Clock()

running = True
warna = "grey"
screen.fill(warna)
floor_1 = pygame.image.load("assets/images/floor_1_grey.jpg")
floor_1 = pygame.transform.scale(floor_1, (1280,720))
floor_1_coll = pygame.image.load("assets/images/floor_1_alpha.jpg")
floor_1_coll = pygame.transform.scale(floor_1_coll, (1280,720))
text_font = pygame.font.SysFont(None, 36)
text_small = pygame.font.SysFont(None, 24)
tot_buku = 9
current_time = 0
books_inhand = 0
total_books_collected = 0 
num_slot = 0

class rak_sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/shelf.jpg")
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.x = 1280-400
        self.rect.y = 720-400

class shadow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/shadow.png").convert_alpha()
        self.rect = (0,0)

    def update(self):
        self.image = pygame.transform.scale(self.image, (80 - math.sin(current_time)*5, 30 - math.sin(current_time)*5))
    

class buku_sprite_yellow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/buku_kuning.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)

        self.shadow = pygame.draw.ellipse(screen,(0, 0, 0, 255), (self.rect.x, self.rect.y-150, 100,30))

        self.base_y= self.rect.y        
        self.held=False 
        self.slot = 0

        

    def update(self):
        if self.held:
            for Kokomi in player_sprites:
                self.rect.x=Kokomi.rect.x + (35*(self.slot-1))
                self.rect.y=Kokomi.rect.y-40
        else:
            self.rect.y=self.base_y+math.sin(current_time)*5

class buku_sprite_green(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/buku_hijau.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1180)
        self.rect.y = random.randint(0, 620)
        self.base_y= self.rect.y
        self.held=False 
        self.slot = 0

    def update(self):
        if self.held:
            for Kokomi in player_sprites:
                self.rect.x=Kokomi.rect.x + (35*(self.slot-1))
                self.rect.y=Kokomi.rect.y-40
        else:
            self.rect.y=self.base_y+math.sin(current_time)*5

class buku_sprite_white(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/buku_putih.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100,1280-400-100)
        self.rect.y = random.randint(0, 620)
        self.base_y= self.rect.y
        self.held=False 
        self.slot=0

    def update(self):
        if self.held:
            for Kokomi in player_sprites:
                self.rect.x=Kokomi.rect.x + (35*(self.slot-1))
                self.rect.y=Kokomi.rect.y-40
        else:
            self.rect.y=self.base_y+math.sin(current_time)*5

class kokomi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("assets/images/icon.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, True, False)
        self.turn_left = False
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300
        self.hitbox = pygame.draw.rect(screen, (0,0,0), (100,300, 100,100))


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if can_walk(self.rect.x, self.rect.y+10, "down"):
                self.rect.y += 10
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if can_walk(self.rect.x, self.rect.y-10, "up"):    
                self.rect.y -= 10
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if can_walk(self.rect.x+10, self.rect.y, "right"):
                self.rect.x += 10
            if self.turn_left:
                self.image = pygame.transform.flip(self.image, True, False)
                self.turn_left = False
            #self.rect = self.image.get_rect()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if can_walk(self.rect.x-10, self.rect.y, "left"):
                self.rect.x -= 10
            if not self.turn_left:
                self.image = pygame.transform.flip(self.image, True, False)
                self.turn_left = True
            #self.rect = self.image_flipped.get_rect()

Kokomi = kokomi()
rak = rak_sprite()  
player_sprites = pygame.sprite.GroupSingle(Kokomi)
object_sprites = pygame.sprite.Group()
shadow_sprites = pygame.sprite.Group()
book_in_hand = pygame.sprite.Group()
for i in range(tot_buku//3):
    buku_banyak = buku_sprite_yellow()
    object_sprites.add(buku_banyak)
    shade = shadow() 
    #shade.rect = (buku_banyak.rect.x+5, buku_banyak.rect.y+100)
    #shadow_sprites.add(shade)
for i in range(tot_buku//3):
    buku_banyak = buku_sprite_green()
    object_sprites.add(buku_banyak)
    shade = shadow() 
    #shade.rect = (buku_banyak.rect.x+5, buku_banyak.rect.y+100)
    #shadow_sprites.add(shade)
for i in range(tot_buku//3):
    buku_banyak = buku_sprite_white()
    object_sprites.add(buku_banyak)
    shade = shadow() 
    #shade.rect = (buku_banyak.rect.x+5, buku_banyak.rect.y+100)
    #shadow_sprites.add(shade)
rak_sprites = pygame.sprite.GroupSingle(rak)

text_surface = text_font.render("Collect the books!", True, ("black"))
text_total = text_font.render(f"Total books collected: 0/{tot_buku}", True, ("black"))
text_inventory = text_font.render(f"Inventory: {books_inhand}/3", True, ("black"))
text_pickup = text_small.render("Press [E] to pick up the book", True, ("black"))
text_total = text_font.render(f"Total books collected: {total_books_collected}/{tot_buku}", True, ("black"))

def draw_everything():
    screen.fill(warna)
    screen.blit(floor_1, (0,0)) 
    rak_sprites.draw(screen)
    #shadow_sprites.draw(screen)
    object_sprites.draw(screen)
    player_sprites.draw(screen)
    book_in_hand.draw(screen)
    player_sprites.update()
    #shadow_sprites.update()
    object_sprites.update()
    book_in_hand.update()
    screen.blit(text_surface, (10, 10))
    screen.blit(text_inventory, (10, 720 - text_total.get_height()-10 - text_inventory.get_height() - 10))
    screen.blit(text_total, (10, 720 - text_total.get_height()-10))

def can_walk(current_x, current_y, dir):
    try:
        if dir == "right":
            map_pixel = floor_1_coll.get_at((current_x+100,current_y))
            map_pixel2 = floor_1_coll.get_at((current_x+100,current_y+100))
        elif dir == "left":
            map_pixel = floor_1_coll.get_at((current_x,current_y))
            map_pixel2 = floor_1_coll.get_at((current_x,current_y+100))
        elif dir == "up":
            map_pixel = floor_1_coll.get_at((current_x,current_y))
            map_pixel2 = floor_1_coll.get_at((current_x+100,current_y))
        elif dir == "down":
            map_pixel = floor_1_coll.get_at((current_x,current_y+100))
            map_pixel2 = floor_1_coll.get_at((current_x+100,current_y+100))
    except IndexError:
        return False
    if map_pixel == (255, 255, 255) and map_pixel2 == (255, 255, 255):
        return True
    return False

while running: 
    draw_everything()
    current_time+=0.05

    collision_book = pygame.sprite.spritecollide(Kokomi, object_sprites, False)
    collision_shadow = pygame.sprite.spritecollide(Kokomi, shadow_sprites, False)
    if collision_book:
        for book in collision_book:
            if len(book_in_hand) < 3:
                text_pickup = text_small.render("Press [E] to pick up the book", True, ("black"))
                screen.blit(text_pickup, (book.rect.x + 50 - text_pickup.get_width()/2, book.rect.y - 15 - text_pickup.get_height()))
                if pygame.key.get_pressed()[pygame.K_e]:
                    object_sprites.remove(book)
                    for shadoww in collision_shadow:
                        shadow_sprites.remove(shadoww)
                    book_in_hand.add(book)
                    book.image = pygame.transform.scale(book.image,(30,30))
                    num_slot+= 1
                    book.slot = num_slot
                    book.held = True
                    text_inventory = text_font.render(f"Inventory: {len(book_in_hand)}/3", True, ("black"))
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
                        num_slot=0
                        book_in_hand.remove(book)
                text_total = text_font.render(f"Total books collected: {total_books_collected}/{tot_buku}", True, (255, 255, 255))
                text_inventory = text_font.render(f"Inventory: {len(book_in_hand)}/3", True, ("black"))      
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