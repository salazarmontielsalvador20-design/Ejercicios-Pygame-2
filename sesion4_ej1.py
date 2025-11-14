# sesion4_ej1.py
import pygame, sys
pygame.init()
ANCHO,ALTO = 800,600
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Sesión4 - Rebote con velocidad variable")
clock = pygame.time.Clock()
x,y = 100,100
vx,vy = 4,3
radio = 20
running=True
while running:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            running=False
    x += vx
    y += vy
    # bounce
    if x-radio <=0 or x+radio >= ANCHO:
        vx = -vx
        vx += 0.1 if vx>0 else -0.1
    if y-radio <=0 or y+radio >= ALTO:
        vy = -vy
        vy += 0.1 if vy>0 else -0.1
    pantalla.fill((30,30,30))
    pygame.draw.circle(pantalla,(200,60,60),(int(x),int(y)),radio)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
