import pygame, sys
pygame.init()
ANCHO,ALTO=600,400
pantalla=pygame.display.set_mode((ANCHO,ALTO))
clock=pygame.time.Clock()
a=pygame.Rect(100,150,80,80)
b=pygame.Rect(300,150,80,80)
running=True
while running:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT: running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: a.x-=4
    if keys[pygame.K_RIGHT]: a.x+=4
    color=(255,0,0) if a.colliderect(b) else (0,255,0)
    pantalla.fill((30,30,30))
    pygame.draw.rect(pantalla,color,a)
    pygame.draw.rect(pantalla,(0,0,255),b)
    pygame.display.flip(); clock.tick(60)
pygame.quit(); sys.exit()
