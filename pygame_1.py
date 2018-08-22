import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")
path="J://personal github//Game//"
walkRight = [pygame.image.load(path+'R1.png'), pygame.image.load(path+'R2.png'), pygame.image.load(path+'R3.png'), pygame.image.load(path+'R4.png'), pygame.image.load(path+'R5.png'), pygame.image.load(path+'R6.png'), pygame.image.load(path+'R7.png'), pygame.image.load(path+'R8.png'), pygame.image.load(path+'R9.png')]
walkLeft = [pygame.image.load(path+'L1.png'), pygame.image.load(path+'L2.png'), pygame.image.load(path+'L3.png'), pygame.image.load(path+'L4.png'), pygame.image.load(path+'L5.png'), pygame.image.load(path+'L6.png'), pygame.image.load(path+'L7.png'), pygame.image.load(path+'L8.png'), pygame.image.load(path+'L9.png')]
bg = pygame.image.load(path+'bg.jpg')
go=pygame.image.load(path+'game_over.jpg')
char = pygame.image.load(path+'standing.png')
clock = pygame.time.Clock()
score=0

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox=(self.x,self.y,29,52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                


class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load(path+'R1E.png'), pygame.image.load(path+'R2E.png'), pygame.image.load(path+'R3E.png'), pygame.image.load(path+'R4E.png'), pygame.image.load(path+'R5E.png'), pygame.image.load(path+'R6E.png'), pygame.image.load(path+'R7E.png'), pygame.image.load(path+'R8E.png'), pygame.image.load(path+'R9E.png'), pygame.image.load(path+'R10E.png'), pygame.image.load(path+'R11E.png')]
    walkLeft = [pygame.image.load(path+'L1E.png'), pygame.image.load(path+'L2E.png'), pygame.image.load(path+'L3E.png'), pygame.image.load(path+'L4E.png'), pygame.image.load(path+'L5E.png'), pygame.image.load(path+'L6E.png'), pygame.image.load(path+'L7E.png'), pygame.image.load(path+'L8E.png'), pygame.image.load(path+'L9E.png'), pygame.image.load(path+'L10E.png'), pygame.image.load(path+'L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.health = 10
        self.visible=True
        self.hitbox=(self.x,self.y,29,52)

    def draw(self, win):
        self.move()
        if self.visible :
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
                
            self.hitbox = (self.x + 19, self.y + 5, 32, 55)
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            
        print('hit')
        


def redrawGameWindow():
    win.blit(bg, (0,0))
    text=font.render('Score ' +str(score),1,(0,0,0))
    win.blit(text,(390,10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()


#mainloop
font= pygame.font.SysFont('comicsans',30)
man = player(200, 410, 64,64)
goblin = enemy(100, 410, 64, 64, 300)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                score+=10
                bullets.pop(bullets.index(bullet))
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()


