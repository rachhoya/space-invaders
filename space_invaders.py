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
fps=60
yellow_hit=pygame.USEREVENT+1
red_hit=pygame.USEREVENT+2
max_bullets=3
bullet_vel=7


def draw_window(red,yellow,red_bullets,yellow_bullets):
    screen.blit(space,(0,0))
    screen.blit(yellow_spaceship,(yellow.x,yellow.y))
    screen.blit(red_spaceship,(red.x,red.y))
    pygame.draw.rect(screen,"white",border)

    for i in red_bullets:
        pygame.draw.rect(screen,"red",i)

    for i in yellow_bullets:
        pygame.draw.rect(screen,"yellow",i)
    pygame.display.update()

def yellow_handle_movement(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x>0:
        yellow.x-=vel
    if key_pressed[pygame.K_d] and yellow.x+vel+yellow.width<border.x:
            yellow.x+=vel
    if key_pressed[pygame.K_w] and yellow.y-vel>0:
            yellow.y-=vel
    if key_pressed[pygame.K_s] and yellow.y+vel+yellow.height<HEIGHT-15:
            yellow.y+=vel

def red_handle_movement(key_pressed,red):
    if key_pressed[pygame.K_LEFT] and red.x-vel>border.x+border.width:
        red.x-=vel
    if key_pressed[pygame.K_RIGHT] and red.x+vel+red.width<WIDTH:
            red.x+=vel
    if key_pressed[pygame.K_UP] and red.y-vel>0:
            red.y-=vel
    if key_pressed[pygame.K_DOWN] and red.y+vel+red.height<HEIGHT-15:
            red.y+=vel

def handle_bullets(red_bullets,yellow_bullets,red,yellow):
    for i in red_bullets:
        i.x-=bullet_vel

    for i in yellow_bullets:
        i.x+=bullet_vel   
     

def main():
    red=pygame.Rect(700,300,spaceship_width,spaceship_height)
    yellow=pygame.Rect(200,300,spaceship_width,spaceship_height)

    red_bullets=[]
    yellow_bullets=[]

    red_health=10
    yellow_health=10

    clock=pygame.time.Clock()

    while True:
        clock.tick(fps)
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT:
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL and len(yellow_bullets)<max_bullets:
                    bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                    yellow_bullets.append(bullet)
                if event.key==pygame.K_RCTRL and len(red_bullets)<max_bullets:
                    bullet=pygame.Rect(red.x,red.y+red.height//2-2,10,5)
                    red_bullets.append(bullet)

                  
        key_pressed=pygame.key.get_pressed()
        draw_window(red,yellow,red_bullets,yellow_bullets)
        red_handle_movement(key_pressed,red)
        yellow_handle_movement(key_pressed,yellow)
        handle_bullets(red_bullets,yellow_bullets,red,yellow)

main()
