# Игра на Pygame, чтобы начать надо нажать пробел тогда всё отресуется, выход на крестик не работает(
import pygame
from pygame import *
from random import randint
import pygame
import keyboard
# Инициализируем pygame
pygame.init()
# Создание экрана
window = display.set_mode((700, 500))
# Название
display.set_caption('Слоты')
# Загрузка и изменение размеров изображений # Можете изменить здесь 13 14 15 строки banan.png просто вот так написать
bg_image = transform.scale(image.load('background.jpg'), (700, 500))
bidon_image = transform.scale(image.load('monky.png'), (100, 100))
banan_image = transform.scale(image.load('banan.jpg'), (100, 100))
klubnika_image = transform.scale(image.load('klubnika.jpg'), (100, 100))
# Параметры нашего текста
font = pygame.font.SysFont(None, 72)
# Функция обработки самой игры
def spin():
    # Рандомные значения переменных
    x = randint(1, 3)
    y = randint(1, 3)
    z = randint(1, 3)
    # Отрисовка при разных значениях
    if x == 1:
        window.blit(bidon_image, (135, 230))
    elif x == 2:
        window.blit(banan_image, (135, 230))
    elif x == 3:
        window.blit(klubnika_image, (135, 230))
    if y == 1:
        window.blit(bidon_image, (295, 230))
    elif y == 2:
        window.blit(banan_image, (295, 230))
    elif y == 3:
        window.blit(klubnika_image, (295, 230))
    if z == 1:
        window.blit(bidon_image, (470, 230))
    elif z == 2:
        window.blit(banan_image, (470, 230))
    elif z == 3:
        window.blit(klubnika_image, (470, 230))
    # Проверяем выйграл или нет
    if x == y and x == z:
        # Отрисовываем текст
        text = font.render('Ты выйграл', True, (23, 237, 51))
    else:
        text = font.render('Проиграл', True, (213, 35, 57))
    # Отрисовываем текст на экране
    window.blit(text, (215, 5))
    # Задержка
    pygame.time.wait(300)
# Главный цикл игры
running = True
while running:
    # Отрисовываем фон
    window.blit(bg_image, (0, 0))
    # Обрабатываем закрытие приложения
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Ждем нажатия пробела
    while not keyboard.is_pressed('space'):
        pygame.time.wait(5)
    spin()
    # Обновляем экран
    pygame.display.update()
# Включаем библиотеку keyboard
keyboard.wait()
pygame.quit()