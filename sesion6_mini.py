import pygame,sys,random,math
pygame.init()
ANCHO,ALTO=800,600
pantalla=pygame.display.set_mode((ANCHO,ALTO))
clock=pygame.time.Clock()
nave=pygame.image.load("nave.png").convert_alpha()
item=pygame.transform.scale(pygame.image.load("bola.png").convert_alpha(),(32,32))
obs=pygame.transform.scale(pygame.image.load("obstaculo.png").convert_alpha(),(80,80))
x,y=200,300; angle=0
items=[pygame.Rect(random.randint(50,750),random.randint(50,550),32,32) for _ in range(5)]
obstacles=[[random.randint(800,1200),random.randint(0,520),random.randint(2,5)] for _ in range(4)]
score=0; font=pygame.font.SysFont(None,32)
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
    player_rect=pygame.Rect(int(x)-20,int(y)-20,40,40)
    for it in items[:]:
        if player_rect.colliderect(it):
            score+=1; items.remove(it)
            items.append(pygame.Rect(random.randint(50,750),random.randint(50,550),32,32))
    for ob in obstacles:
        ob[0]-=ob[2]
        if ob[0]<-80:
            ob[0]=random.randint(800,1200); ob[1]=random.randint(0,520)
        if player_rect.colliderect(pygame.Rect(ob[0],ob[1],80,80)):
            score=0; x,y=200,300
    pantalla.fill((5,5,25))
    for it in items: pantalla.blit(item,it)
    for ob in obstacles: pantalla.blit(obs,(ob[0],ob[1]))
    rot=pygame.transform.rotate(nave,angle)
    pantalla.blit(rot,(x-rot.get_width()//2,y-rot.get_height()//2))
    pantalla.blit(font.render(f"Puntos: {score}",1,(255,255,255)),(10,10))
    pygame.display.flip()
pygame.quit(); sys.exit()
