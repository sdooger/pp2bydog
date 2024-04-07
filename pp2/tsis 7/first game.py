import pygame
from time import localtime as now 
pygame.init()
minute = second = 0

def get_time():
    global minute, second
    minute, second = now().tm_min, now().tm_sec
get_time()

screen_h = 650
screen_w = 900
win = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Микки Часы')


img_main = pygame.image.load(r'C:\Users\user\Desktop\pp2\clock.png')
img_main = pygame.transform.scale(img_main, (screen_w, screen_h))
img_left = pygame.image.load(r'C:\Users\user\Desktop\pp2\small-arrow.png')
img_left = pygame.transform.scale(img_left, (30, screen_h))
img_right = pygame.image.load(r'C:\Users\user\Desktop\pp2\big-arrow.png')
img_right = pygame.transform.scale(img_right, (45, screen_h))

def print_img_by_degree(image, degree): # поворачивает картину на заданное количество градусов
    image = pygame.transform.rotate(image, degree) # поворачивет картину можно сказать обновляя изображение 
    rect = image.get_rect() # для определения положения и размеров изображения
    rect.center = win.get_rect().center # чтобы было в центре
    win.blit(image, rect) # чтобы имаге было на поверхности по данным характеристикам



def play_tick():
    music = pygame.mixer.music.load(r'C:\Users\user\Desktop\pp2\music.mp3')
    pygame.mixer.music.play()

play_tick()

clock = pygame.time.Clock()
run = 1

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
    win.blit(img_main, (0, 0))
    get_time()
    if not pygame.mixer.music.get_busy(): 
        play_tick()
    print_img_by_degree(img_left, -second*6 - (0.9 if second>30 else +1.2)) # плавное перемещение при переходе через 30 секунд
    print_img_by_degree(img_right, -minute * 6 - 0) 
    
    
    pygame.display.update()
    clock.tick(60)