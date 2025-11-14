import pygame, sys, random

# --- 1. Inicialización ---
pygame.init()
ANCHO, ALTO = 800, 600 # Un tamaño de ventana razonable
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesion 6 - Ejercicio 2: Recolector")
clock = pygame.time.Clock()

# --- 2. Colores ---
BG_COLOR = (10, 20, 40)      # Azul oscuro
PLAYER_COLOR = (255, 255, 0) # Amarillo (como en tu código)
ITEM_COLOR = (255, 255, 255) # Círculo blanco

# --- 3. Entidades del Juego ---

# Jugador (Rectángulo)
# Sigue las 4 flechas
player_rect = pygame.Rect(50, 50, 40, 40) # Mismo tamaño que tu código
player_speed = 5

# Objeto a recolectar (Círculo)
ITEM_RADIUS = 15
# Usamos un Rect para la posición y colisión
# Lo posicionamos lejos del jugador al inicio
item_rect = pygame.Rect(
    random.randint(ANCHO // 2, ANCHO - 50), # Lejos del jugador
    random.randint(50, ALTO - 50),
    ITEM_RADIUS * 2,
    ITEM_RADIUS * 2
)

# --- 4. Estado del Juego ---
score = 0
font = pygame.font.SysFont(None, 40) # Fuente más grande
running = True

# --- Bucle Principal del Juego ---
while running:

    # --- 5. Manejo de Eventos ---
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    # --- 6. Control del Jugador (4 direcciones) ---
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

    # Colisión: Jugador vs Círculo
    if player_rect.colliderect(item_rect):
        score += 1
        
        # SOLUCIÓN AL BUG:
        # Mover el círculo a una nueva posición aleatoria
        # Dejamos un margen de 50px con los bordes
        item_rect.center = (
            random.randint(50, ANCHO - 50), 
            random.randint(50, ALTO - 50)
        )
        
        # Anti-bucle: Si reaparece encima del jugador, moverlo de nuevo
        # (Esto es una seguridad extra, aunque es poco probable)
        if player_rect.colliderect(item_rect):
             item_rect.center = (ANCHO // 2, ALTO // 2) # Mover al centro


    # --- 8. Dibujado (Render) ---
    
    # Fondo
    pantalla.fill(BG_COLOR)

    # Dibujar jugador (Rectángulo)
    pygame.draw.rect(pantalla, PLAYER_COLOR, player_rect)

    # Dibujar item (Círculo)
    pygame.draw.circle(pantalla, ITEM_COLOR, item_rect.center, ITEM_RADIUS)

    # Dibujar marcador
    score_text = font.render(f"Puntos: {score}", True, (255, 255, 255))
    pantalla.blit(score_text, (10, 10))

    # --- 9. Actualizar Pantalla ---
    pygame.display.flip()
    clock.tick(60) # 60 FPS

# --- Salir ---
pygame.quit()
sys.exit()