import pygame

pygame.init()

S_WIDTH = 800
S_HEIGHT = 600
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("Humans running from AI")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

square_size = 50

move_speed = 10
auto_speed = 20

font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

def reset_game():
   x_human = S_WIDTH // 2
   y_human = S_HEIGHT // 2
   speed_x_human = 0
   speed_y_human = 0

   x_auto = S_WIDTH // 4
   y_auto = S_HEIGHT // 2
   x_auto1 = S_WIDTH // 3
   y_auto1 = S_HEIGHT // 2
   speed_x_auto = auto_speed
   speed_y_auto = auto_speed
   speed_x_auto1 = -auto_speed
   speed_y_auto1 = -auto_speed

   start_ticks = pygame.time.get_ticks()

   return x_human, y_human, speed_x_human, speed_y_human, x_auto, y_auto, speed_x_auto, speed_y_auto, x_auto1, y_auto1, speed_x_auto1, speed_y_auto1, start_ticks

x_human, y_human, speed_x_human, speed_y_human, x_auto, y_auto, speed_x_auto, speed_y_auto, x_auto1, y_auto1, speed_x_auto1, speed_y_auto1, start_ticks = reset_game()

running = True
clock = pygame.time.Clock()

while running:
   for e in pygame.event.get():
      if e.type == pygame.QUIT:
         running = False
      elif e.type == pygame.KEYDOWN:
         if e.key == pygame.K_UP:
            speed_y_human = -move_speed
         elif e.key == pygame.K_DOWN:
            speed_y_human = move_speed
         elif e.key == pygame.K_LEFT:
            speed_x_human = -move_speed
         elif e.key == pygame.K_RIGHT:
            speed_x_human = move_speed
      elif e.type == pygame.KEYUP:
         if e.key in (pygame.K_LEFT, pygame.K_RIGHT):
            speed_x_human = 0
         if e.key in (pygame.K_UP, pygame.K_DOWN):
            speed_y_human = 0

   x_human += speed_x_human
   y_human += speed_y_human

   if x_human < 0:
      x_human = 0
   elif x_human + square_size > S_WIDTH:
      x_human = S_WIDTH - square_size
   elif y_human < 0:
      y_human = 0
   elif y_human + square_size > S_HEIGHT:
      y_human = S_HEIGHT - square_size

   x_auto += speed_x_auto
   y_auto += speed_y_auto

   x_auto1 += speed_x_auto1
   y_auto1 += speed_y_auto1

   if x_auto < 0 or x_auto + square_size > S_WIDTH:
      speed_x_auto = -speed_x_auto
   if y_auto < 0 or y_auto + square_size > S_HEIGHT:
      speed_y_auto = -speed_y_auto

   if x_auto1 < 0 or x_auto1 + square_size > S_WIDTH:
      speed_x_auto1 = -speed_x_auto1
   if y_auto1 < 0 or y_auto1 + square_size > S_HEIGHT:
      speed_y_auto1 = -speed_y_auto1

   if (x_human < x_auto + square_size and x_human + square_size > x_auto and y_human < y_auto + square_size and y_human + square_size > y_auto) or (x_human < x_auto1 + square_size and x_human + square_size > x_auto1 and y_human < y_auto1 + square_size and y_human + square_size > y_auto1):
      screen.fill(WHITE)
      text = font.render("Game Over", True, BLACK)
      text_rect = text.get_rect(center=(S_WIDTH // 2, S_HEIGHT // 2 - 50))
      screen.blit(text, text_rect)

      survial_time = (pygame.time.get_ticks() - start_ticks) / 1000
      
      time_text = font.render("Survival Time: " + str(round(survial_time)) + " seconds", True, BLACK)
      time_rect = text.get_rect(center=(S_WIDTH // 2, S_HEIGHT // 2 - 30))
      time_rect = time_text.get_rect(center=(S_WIDTH // 2, S_HEIGHT // 2 + 20))
      screen.blit(time_text, time_rect)

      pygame.display.update()
      pygame.time.wait(3000)

      x_human, y_human, speed_x_human, speed_y_human, x_auto, y_auto, speed_x_auto, speed_y_auto, x_auto1, y_auto1, speed_x_auto1, speed_y_auto1, start_ticks = reset_game()
      continue

   screen.fill(WHITE)

   pygame.draw.rect(screen, RED, (x_human, y_human, square_size, square_size))

   pygame.draw.rect(screen, BLUE, (x_auto, y_auto, square_size, square_size))

   pygame.draw.rect(screen, BLACK, (x_auto1, y_auto1, square_size, square_size))

   pygame.display.update()

   clock.tick(30)

pygame.quit()
