import pygame, sys, random
pygame.init()
ANCHO,ALTO=640,480
pantalla=pygame.display.set_mode((ANCHO,ALTO))
clock=pygame.time.Clock()
item=pygame.image.load("bola.png").convert_alpha()
player=pygame.Rect(50,50,40,40)
goal=item.get_rect(topleft=(200,200))
font=pygame.font.SysFont(None,32); score=0
running=True
while running:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT: running=False
    k=pygame.key.get_pressed()
    if k[pygame.K_LEFT]: player.x-=4
    if k[pygame.K_RIGHT]: player.x+=4
    if k[pygame.K_UP]: player.y-=4
    if k[pygame.K_DOWN]: player.y+=4
    if player.colliderect(goal):
        score+=1
        goal.topleft=(random.randint(0,600), random.randint(0,440))
    pantalla.fill((10,20,40))
    pantalla.blit(item,goal)
    pygame.draw.rect(pantalla,(255,255,0),player)
    pantalla.blit(font.render(f"Puntos: {score}",1,(255,255,255)),(10,10))
    pygame.display.flip(); clock.tick(60)
pygame.quit(); sys.exit()
