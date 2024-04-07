import pygame
import os

pygame.init()

screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption('Музыка')

music_files = [
    r'C:\Users\user\Desktop\pp2\music1.mp3',
    r'C:\Users\user\Desktop\pp2\music2.mp3',
    r'C:\Users\user\Desktop\pp2\music3.mp3',
    r'C:\Users\user\Desktop\pp2\music4.mp3'
]

pygame.mixer.init()

current_track = 0
playing = False

pygame.mixer.music.load(music_files[current_track])


def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    play_music()

def previous_track():
    global current_track
    current_track = (current_track -  1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    stop_music()
                    playing = False
                else:
                    play_music()
                    playing = True
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()

    pygame.display.flip()

pygame.quit()
