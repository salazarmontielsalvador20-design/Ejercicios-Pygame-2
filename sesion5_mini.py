import pygame, sys, math
pygame.init()
ANCHO,ALTO=800,600
pantalla=pygame.display.set_mode((ANCHO,ALTO))
clock=pygame.time.Clock()
nave=pygame.image.load("nave.png").convert_alpha()
x,y=400,300; angle=0
running=True
while running:
    dt=clock.tick(60)/1000
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT: running=False
    mx,my=pygame.mouse.get_pos(); dx,dy=mx-x,my-y
    angle=-math.degrees(math.atan2(dy,dx))-90
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        x+=math.cos(math.radians(-angle-90))*200*dt
        y+=-math.sin(math.radians(-angle-90))*200*dt
    pantalla.fill((0,0,30))
    rot=pygame.transform.rotate(nave,angle)
    pantalla.blit(rot,rot.get_rect(center=(x,y)))
    pygame.display.flip()
pygame.quit(); sys.exit()
