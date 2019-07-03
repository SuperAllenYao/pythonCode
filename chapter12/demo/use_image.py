#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame
import pygame.color

# 不知道为什么, VScode老是提示 pygame的拼写错误
# 初始化pygame
pygame.init()

# 得到一个屏幕的对象
screen = pygame.display.set_mode((500, 500))

# 加载图片
ball = pygame.image.load('chapter12/demo/intro_ball.gif')
red = pygame.Color(255, 20, 20)

# 游戏的主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 更新状态
        # 画线
        pygame.draw.line(screen, red, (20, 20), (200, 200))
        # 画矩形
        # 绘制
    screen.blit(ball, (100, 100))
    pygame.display.flip()
