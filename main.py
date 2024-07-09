import pgzrun
import random
WIDTH = 720
HEIGHT = 480
target1 = Actor("target_red1")
target1.x = WIDTH/2
target1.y = HEIGHT/2
target2 = Actor("duck_target_brown")
target2.right = WIDTH
target2.bottom = HEIGHT
target3 = Actor("duck_target_yellow")
target3.x = random.randint(0, WIDTH)
target3.y = random.randint(0, HEIGHT)
cursor = Actor("crosshair_outline_large")
rifle = Actor("rifle")
score = 0
def update():
    target1.x += random.randint(5, 10)
    target2.x += random.randint(1, 10)
    target3.x += random.randint(1, 15)
    if target1.left >= WIDTH:
        target1.right = 0
    if target2.left>= WIDTH:
        target2.right = 0
    if target3.left >= WIDTH:
        target3.right = 0
def on_mouse_move(pos):
    cursor.pos = pos
    rifle.left = pos[0]
    rifle.top = pos[1]
def on_mouse_down(pos):
    global score
    if cursor.colliderect(target1):
        target1.right = 0
        target1.y = random.randint(0, HEIGHT)
        score += 10
    elif cursor.colliderect(target2):
        target2.right = 0
        target2.y = random.randint(0, HEIGHT)
        score -= 5
    elif cursor.colliderect(target3):
        target3.right = 0
        target3.y = random.randint(0, HEIGHT)
        score -= 5
def draw():
    screen.clear()
    target1.draw()
    target2.draw()
    target3.draw()
    cursor.draw()
    rifle.draw()
    screen.draw.text(f"Score,{score}", (10, 10), fontsize=20, color="blue")
pgzrun.go()