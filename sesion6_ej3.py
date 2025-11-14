import pygame, sys, random
pygame.init()
ANCHO,ALTO=640,480
pantalla=pygame.display.set_mode((ANCHO,ALTO))
clock=pygame.time.Clock()
player=pygame.Rect(50,200,40,40)
obs_img=pygame.image.load("obstaculo.png").convert_alpha()
ow,oh=obs_img.get_width(),obs_img.get_height()
obstacles=[[random.randint(200,800),random.randint(0,400),random.randint(2,5)] for _ in range(4)]
running=True
while running:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT: running=False
    k=pygame.key.get_pressed()
    if k[pygame.K_UP]: player.y-=4
    if k[pygame.K_DOWN]: player.y+=4
    pantalla.fill((0,0,0))
    for ob in obstacles:
        ob[0]-=ob[2]
        if ob[0]<-ow:
            ob[0]=random.randint(640,900); ob[1]=random.randint(0,400)
        pantalla.blit(obs_img,(ob[0],ob[1]))
        if player.colliderect(pygame.Rect(ob[0],ob[1],ow,oh)):
            player.topleft=(50,200)
    pygame.draw.rect(pantalla,(0,200,50),player)
    pygame.display.flip(); clock.tick(60)
pygame.quit(); sys.exit()
