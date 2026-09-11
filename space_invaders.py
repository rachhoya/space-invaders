import pygame
pygame.init()

WIDTH=900
HEIGHT=500
spaceship_width=55
spaceship_height=40
screen=pygame.display.set_mode((WIDTH,HEIGHT))

space=pygame.image.load("sky2.png")
space=pygame.transform.scale(space,(WIDTH,HEIGHT))

spaceship=pygame.image.load("yellow_spaceship.png")
yellow_spaceship=pygame.transform.rotate(pygame.transform.scale(spaceship,(spaceship_width,spaceship_height)),90)

spaceship2=pygame.image.load("red_spaceship.png")
red_spaceship=pygame.transform.rotate(pygame.transform.scale(spaceship2,(spaceship_width,spaceship_height)),270)

border=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
vel=5

def draw_window(red,yellow):
    screen.blit(space,(0,0))
    screen.blit(yellow_spaceship,(yellow.x,yellow.y))
    screen.blit(red_spaceship,(red.x,red.y))
    pygame.draw.rect(screen,"white",border)
    pygame.display.update()

def yellow_handle_movement(key_pressed,yellow):
    if key_pressed[pygame.K_a]:
        yellow.x-=vel
    if key_pressed[pygame.K_d]:
            yellow.x+=vel
    if key_pressed[pygame.K_w]:
            yellow.y-=vel
    if key_pressed[pygame.K.s]:
            yellow.y+=vel

def red_handle_movement(key_pressed,red):
    if key_pressed[pygame.K_LEFT]:
        red.x-=vel
    if key_pressed[pygame.K_RIGHT]:
            red.x+=vel
    if key_pressed[pygame.K_UP]:
            red.y-=vel
    if key_pressed[pygame.K.DOWN]:
            red.y+=vel
    
    








def main():
    red=pygame.Rect(700,300,spaceship_width,spaceship_height)
    yellow=pygame.Rect(700,300,spaceship_width,spaceship_height)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    key_pressed=pygame.key.get_pressed()
    draw_window(red,yellow)



    pygame.display.update()

main()