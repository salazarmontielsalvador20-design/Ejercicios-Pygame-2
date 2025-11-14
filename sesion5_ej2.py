import pygame, sys
pygame.init()
ANCHO,ALTO=400,300
pantalla=pygame.display.set_mode((ANCHO,ALTO))
clock=pygame.time.Clock()
sheet=pygame.image.load("personaje_spritesheet_64x64.png").convert_alpha()
frames=[sheet.subsurface((i*64,0,64,64)) for i in range(4)]
idx=0;timer=0
running=True
while running:
    dt=clock.tick(60); timer+=dt
    if timer>=120: timer=0; idx=(idx+1)%4
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT: running=False
    pantalla.fill((40,90,120)); pantalla.blit(frames[idx],(168,118))
    pygame.display.flip()
pygame.quit(); sys.exit()
