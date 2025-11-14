import pygame, sys
pygame.init()
ANCHO,ALTO=400,300
pantalla=pygame.display.set_mode((ANCHO,ALTO))
clock=pygame.time.Clock()

# --- CAMBIOS AQUÍ ---
# 1. Cargamos las 4 imágenes individuales que mencionaste
img_nave = pygame.image.load("nave.png").convert_alpha()
img_bola = pygame.image.load("bola.png").convert_alpha()
img_robot = pygame.image.load("robot.png").convert_alpha()
img_meteorito = pygame.image.load("meteorito.png").convert_alpha()

# 2. Las escalamos a un tamaño uniforme (64x64) y las guardamos en la lista 'frames'
size = (64, 64)
frames = [
    pygame.transform.scale(img_nave, size),
    pygame.transform.scale(img_bola, size),
    pygame.transform.scale(img_robot, size),
    pygame.transform.scale(img_meteorito, size)
]
# --- FIN DE LOS CAMBIOS ---

idx=0; timer=0
running=True
while running:
    dt=clock.tick(60)
    timer+=dt
    
    # 3. Ajustamos el timer a 100ms como pedía el ejercicio
    if timer >= 100: 
        timer = 0
        idx = (idx + 1) % 4 # % 4 porque hay 4 frames
        
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT: running=False
        
    pantalla.fill((40,90,120))
    # Centramos la imagen en la pantalla (168, 118)
    pantalla.blit(frames[idx],(168,118)) 
    pygame.display.flip()

pygame.quit(); sys.exit()