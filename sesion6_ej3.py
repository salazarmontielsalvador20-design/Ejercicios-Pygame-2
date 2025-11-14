import pygame, sys, random

# --- 1. Inicialización ---
pygame.init()
ANCHO, ALTO = 640, 480
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesion 6 - Ejercicio 3: Evitar Círculos")
clock = pygame.time.Clock()

# --- 2. Colores ---
# (R, G, B)
BG_COLOR = (10, 10, 10)       # Fondo casi negro
PLAYER_COLOR = (50, 200, 50)  # Verde
OBS_COLOR = (200, 50, 50)     # Rojo

# --- 3. Entidades del Juego ---

# Jugador (Rectángulo)
# Lo creamos como un objeto Rect de Pygame
player_rect = pygame.Rect(50, ALTO // 2 - 20, 40, 40)
player_speed = 5

# Lista de Obstáculos (Círculos)
# Guardaremos diccionarios para cada obstáculo
obstacles = []
NUM_OBSTACULOS = 8
OBSTACLE_RADIUS = 15

def crear_obstaculos():
    """Limpia y vuelve a crear todos los obstáculos a la derecha."""
    obstacles.clear()
    for _ in range(NUM_OBSTACULOS):
        # Usamos un Rect para guardar la posición y facilitar la colisión
        # Lo posicionamos fuera de la pantalla, a la derecha
        obs_rect = pygame.Rect(
            random.randint(ANCHO + 20, ANCHO + 400), # Pos X
            random.randint(0, ALTO - OBSTACLE_RADIUS * 2), # Pos Y
            OBSTACLE_RADIUS * 2, # Ancho
            OBSTACLE_RADIUS * 2  # Alto
        )
        obs_speed = random.randint(2, 7)
        obstacles.append({'rect': obs_rect, 'speed': obs_speed})

# Llenar la lista por primera vez
crear_obstaculos()

# --- 4. Estado del Juego ---
running = True
game_over = False
font = pygame.font.SysFont(None, 50)

# --- Bucle Principal del Juego ---
while running:

    # --- 5. Manejo de Eventos ---
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        # Reiniciar el juego si está en "Game Over"
        if ev.type == pygame.KEYDOWN and game_over:
            if ev.key == pygame.K_SPACE:
                player_rect.topleft = (50, ALTO // 2 - 20)
                crear_obstaculos()
                game_over = False

    # Si el juego ha terminado, no actualizar nada más
    if game_over:
        continue # Saltar el resto del bucle

    # --- 6. Control del Jugador (Solo Arriba y Abajo) ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Limitar al jugador dentro de la pantalla
    if player_rect.top < 0: player_rect.top = 0
    if player_rect.bottom > ALTO: player_rect.bottom = ALTO

    # --- 7. Lógica del Juego ---

    # Mover y revisar obstáculos
    for ob in obstacles:
        ob['rect'].x -= ob['speed'] # Mover a la izquierda

        # Si sale de pantalla, reciclarlo
        if ob['rect'].right < 0:
            ob['rect'].left = random.randint(ANCHO + 20, ANCHO + 200)
            ob['rect'].top = random.randint(0, ALTO - OBSTACLE_RADIUS * 2)
            ob['speed'] = random.randint(2, 7)

        # Colisión: Jugador vs Obstáculo
        # Usamos colliderect (colisión de rectángulos)
        # Es suficientemente bueno para este juego
        if player_rect.colliderect(ob['rect']):
            game_over = True # El juego termina

    # --- 8. Dibujado (Render) ---
    
    # Fondo
    pantalla.fill(BG_COLOR)

    # Dibujar jugador
    pygame.draw.rect(pantalla, PLAYER_COLOR, player_rect)

    # Dibujar obstáculos
    for ob in obstacles:
        # Dibujamos un círculo usando el CENTRO del rectángulo
        pygame.draw.circle(pantalla, OBS_COLOR, ob['rect'].center, OBSTACLE_RADIUS)

    # Si es Game Over, mostrar mensaje
    if game_over:
        texto = font.render("¡PERDISTE!", True, (255, 255, 255))
        texto_rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2 - 30))
        pantalla.blit(texto, texto_rect)
        
        texto2 = font.render("Pulsa ESPACIO", True, (200, 200, 200))
        texto_rect2 = texto2.get_rect(center=(ANCHO // 2, ALTO // 2 + 30))
        pantalla.blit(texto2, texto_rect2)

    # --- 9. Actualizar Pantalla ---
    pygame.display.flip()
    clock.tick(60) # 60 FPS

# --- Salir ---
pygame.quit()
sys.exit()