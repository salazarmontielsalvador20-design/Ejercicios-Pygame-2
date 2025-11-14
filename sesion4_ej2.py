# sesion4_ej2.py
import pygame, sys
pygame.init()
ANCHO,ALTO = 600,400
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Sesión4 - Pulsación")
clock = pygame.time.Clock()
radio = 20
creciendo = True
running=True
while running:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            running=False
    if creciendo:
        radio += 0.5
        if radio >= 50:
            creciendo = False
    else:
        radio -= 0.5
        if radio <= 20:
            creciendo = True
    pantalla.fill((40,40,80))
    pygame.draw.circle(pantalla,(100,200,255),(ANCHO//2,ALTO//2),int(radio))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
