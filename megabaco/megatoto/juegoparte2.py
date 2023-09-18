import pygame

x=50
y=50
Vel=5
pygame.init()
widht,height= 1280,720
screen = pygame.display.set_mode((widht,height))
clock = pygame.time.Clock()
pygame.display.set_caption("Juego 2")
running = True
sonic=pygame.image.load(r"C:\Users\BACO\Downloads\sonicsi.png")
medidas_sonic=pygame.transform.scale(sonic,(200,100))
dt = 0

screen.blit(medidas_sonic,(200,100))

while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        sonic.y -= Vel
    if keys[pygame.K_s]:
        sonic.y += Vel
    if keys[pygame.K_a]:
        sonic.x -= Vel
    if keys[pygame.K_d]:
        sonic.x += Vels

    
    pygame.display.flip()

   
    dt = clock.tick(60) / 1000

pygame.quit()