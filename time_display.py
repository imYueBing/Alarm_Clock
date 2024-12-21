import pygame
import time

def display_time():
    """
    使用 pygame 显示当前时间
    """
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("현재 시간")  # 显示窗口标题
    font = pygame.font.Font(None, 74)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        current_time = time.strftime("%H:%M:%S")
        text = font.render(current_time, True, (255, 255, 255))
        screen.blit(text, (100, 80))

        pygame.display.flip()
        clock.tick(1)

    pygame.quit()
