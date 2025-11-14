import pygame, sys, random

# --- 1. Inicialización ---
pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Recolector de Puntos (Simple)")
clock = pygame.time.Clock()

# --- 2. Cargar y Escalar Imágenes ---
# (Aquí solucionamos el problema de "imágenes gigantes")
try:
    # Ajusta los tamaños (ej. 50, 50) si se ven muy pequeños o grandes
    TAM_NAVE = (50, 50)
    TAM_BOLA = (30, 30)
    TAM_OBSTACULO = (60, 60)

    nave_img = pygame.transform.scale(pygame.image.load("nave.png").convert_alpha(), TAM_NAVE)
    bola_img = pygame.transform.scale(pygame.image.load("bola.png").convert_alpha(), TAM_BOLA)
    obs_img = pygame.transform.scale(pygame.image.load("obstaculo.png").convert_alpha(), TAM_OBSTACULO)

except pygame.error as e:
    print(f"Error al cargar/escalar una imagen: {e}")
    print("Asegúrate de que nave.png, bola.png y obstaculo.png estén en la carpeta.")
    sys.exit()

# --- 3. Entidades del Juego ---

# Jugador (Nave)
# Usamos .get_rect() DESPUÉS de escalar la imagen
player_rect = nave_img.get_rect(center=(100, ALTO // 2))
player_speed = 5

# Objeto a Recolectar (Bola)
# La posicionamos lejos del jugador al inicio
bola_rect = bola_img.get_rect(center=(random.randint(ANCHO // 2, ANCHO - 50), 
                                      random.randint(50, ALTO - 50)))

# Lista de Obstáculos
obstacles = []
NUM_OBSTACULOS = 5

def crear_obstaculos():
    """Vacía y rellena la lista de obstáculos, poniéndolos a la derecha."""
    obstacles.clear()
    for _ in range(NUM_OBSTACULOS):
        # Posición inicial: siempre a la derecha, fuera de la pantalla
        obs_rect = obs_img.get_rect(
            topleft=(random.randint(ANCHO + 50, ANCHO + 400), 
                     random.randint(0, ALTO - TAM_OBSTACULO[1]))
        )
        obs_speed = random.randint(2, 6)
        obstacles.append({'rect': obs_rect, 'speed': obs_speed})

# Creamos los obstáculos por primera vez
crear_obstaculos()

# --- 4. Estado del Juego ---
score = 0
font = pygame.font.SysFont(None, 40) # Fuente para el marcador
running = True

# --- Bucle Principal del Juego ---
while running:
    
    # --- 5. Manejo de Eventos ---
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    # --- 6. Control del Jugador ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Limitar al jugador dentro de la pantalla
    if player_rect.left < 0: player_rect.left = 0
    if player_rect.right > ANCHO: player_rect.right = ANCHO
    if player_rect.top < 0: player_rect.top = 0
    if player_rect.bottom > ALTO: player_rect.bottom = ALTO

    # --- 7. Lógica del Juego ---

    # Mover y revisar obstáculos
    for ob in obstacles:
        ob['rect'].x -= ob['speed'] # Mover a la izquierda
        
        # Si sale de pantalla, reciclarlo
        if ob['rect'].right < 0:
            ob['rect'].left = random.randint(ANCHO + 50, ANCHO + 200)
            ob['rect'].top = random.randint(0, ALTO - TAM_OBSTACULO[1])
            ob['speed'] = random.randint(2, 6)

        # Colisión: Jugador vs Obstáculo
        if player_rect.colliderect(ob['rect']):
            score = 0 # Reiniciar puntos
            player_rect.center = (100, ALTO // 2) # Reiniciar posición
            crear_obstaculos() # ¡Importante! Reiniciar todos los obstáculos
            break # Salir del bucle for, ya que chocamos

    # Colisión: Jugador vs Bola (recolectar)
    if player_rect.colliderect(bola_rect):
        score += 1
        # Reposicionar la bola (SOLUCIÓN AL BUG)
        # La movemos SIEMPRE a la mitad derecha de la pantalla
        bola_rect.center = (random.randint(ANCHO // 2, ANCHO - 50), 
                            random.randint(50, ALTO - 50))

    # --- 8. Dibujado (Render) ---
    
    # Fondo
    pantalla.fill((10, 20, 30)) # Azul oscuro espacial

    # Dibujar entidades
    pantalla.blit(nave_img, player_rect)
    pantalla.blit(bola_img, bola_rect)
    for ob in obstacles:
        pantalla.blit(obs_img, ob['rect'])

    # Dibujar marcador
    score_text = font.render(f"Puntos: {score}", True, (255, 255, 255))
    pantalla.blit(score_text, (10, 10))

    # --- 9. Actualizar Pantalla ---
    pygame.display.flip()
    clock.tick(60) # 60 FPS

# --- Salir ---
pygame.quit()
sys.exit()