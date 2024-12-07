import pygame

pygame.init()
pygame.display.set_caption("Pygame")
window = pygame.display.set_mode((800, 600))
x = 100
y = 0
x2 = 675
y2 = 0

def draw():
    global x, y, x2, y2
    window.fill((255, 255, 255))
    player1 = pygame.Rect(x, y, 25, 100)
    pygame.draw.rect(window, (0, 0, 0), player1)
    player2 = pygame.Rect(x2, y2, 25, 100)
    pygame.draw.rect(window, (0, 0, 0), player2)
    userinput = pygame.key.get_pressed()
    if userinput[pygame.K_w] and y > 0:
        y -= 10
    if userinput[pygame.K_s] and y < 500:
        y += 10
    if userinput[pygame.K_UP] and y2 > 0:
        y2 -= 10
    if userinput[pygame.K_DOWN] and y2 < 500:
        y2 += 10










run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()