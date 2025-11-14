import pygame, sys
pygame.init()
ANCHO,ALTO = 800,600
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Sesion5 Ej1 - Escalado")
clock = pygame.time.Clock()
img = pygame.image.load("nave.png").convert_alpha()
scale=1.0
running=True
while running:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT: running=False
        elif ev.type==pygame.KEYDOWN:
            if ev.key in (pygame.K_PLUS, pygame.K_EQUALS): scale+=0.1
            elif ev.key in (pygame.K_MINUS, pygame.K_UNDERSCORE): scale=max(0.1, scale-0.1)
    pantalla.fill((20,20,20))
    w,h=int(img.get_width()*scale), int(img.get_height()*scale)
    pantalla.blit(pygame.transform.scale(img,(w,h)), (ANCHO//2-w//2, ALTO//2-h//2))
    pygame.display.flip(); clock.tick(60)
pygame.quit(); sys.exit()
