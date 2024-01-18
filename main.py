import random
import sqlite3

import pygame
import sys
import pygame_menu

pygame.init()
go = False
white_figure = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_figure = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
black_queen = pygame.image.load('images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (50, 50))
black_king = pygame.image.load('images/black king.png')
black_king = pygame.transform.scale(black_king, (50, 50))
black_rook = pygame.image.load('images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (50, 50))
black_bishop = pygame.image.load('images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (50, 50))
black_knight = pygame.image.load('images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (50, 50))
black_pawn = pygame.image.load('images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (50, 50))
white_king = pygame.image.load('images/white king.png')
white_king = pygame.transform.scale(white_king, (50, 50))
white_rook = pygame.image.load('images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (50, 50))
white_bishop = pygame.image.load('images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (50, 50))
white_knight = pygame.image.load('images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (50, 50))
white_pawn = pygame.image.load('images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (45, 45))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
w, h = 0, 0
size = width, height = 1200, 650
screen = pygame.display.set_mode(size)
left = 10
top = 10
cell_size = 30
user_name, user_password = '', ''
user_white_score = 0
user_black_score = 0
num_level = 1


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.cell_d = []  # [[], [], [], [], [], [], []]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            if y % 2 == 0:
                for x in range(self.width):
                    if x % 2 == 0:
                        pygame.draw.rect(screen, pygame.Color(162, 95, 42), (
                            x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                            self.cell_size))
                    else:
                        pygame.draw.rect(screen, pygame.Color(214, 148, 94), (
                            x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                            self.cell_size))
            else:
                for x in range(self.width):
                    if x % 2 == 1:
                        pygame.draw.rect(screen, pygame.Color(162, 95, 42), (
                            x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                            self.cell_size))
                    else:
                        pygame.draw.rect(screen, pygame.Color(214, 148, 94), (
                            x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                            self.cell_size))
        pygame.draw.rect(screen, pygame.Color(162, 95, 42), (self.left, self.top,
                                                             self.cell_size * 8, self.cell_size * 8), 1)

    def on_click(self, cell_coords):
        print(cell_coords)

    def get_cell(self, mouse_pos):
        if self.left <= mouse_pos[1] < self.left + self.height * self.cell_size and self.top <= mouse_pos[
            0] < self.top + self.width * self.cell_size:
            self.cell_d.append(
                (int((mouse_pos[1] - self.left) / self.cell_size), int((mouse_pos[0] - self.top) / self.cell_size)))
            print(self.cell_d)
            return self.cell_d
        else:
            return None

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell != None:
            self.on_click(cell)
        if cell == None:
            print(cell)


class White_Pawn(pygame.sprite.Sprite):
    def __init__(self, i):
        pygame.sprite.Sprite.__init__(self)
        self.image = white_pawn
        self.rect = self.image.get_rect()
        self.i = i
        index = piece_list.index(white_figure[self.i])
        self.rect = (white_locations[self.i][0] * 70 + 20, white_locations[self.i][1] * 70 + 20)

    def update(self):
        self.rect = pygame.Rect(list(self.rect) + [45, 45])
        self.rect.move_ip((700, 700))


class Black_Pawn(pygame.sprite.Sprite):
    def __init__(self, i):
        pygame.sprite.Sprite.__init__(self)
        self.image = black_pawn
        self.rect = self.image.get_rect()
        self.i = i
        self.rect = (black_locations[self.i][0] * 70 + 20, black_locations[self.i][1] * 70 + 20)

    def update(self):
        self.rect = pygame.Rect(list(self.rect) + [45, 45])
        self.rect.move_ip((700, 700))


class White_Rook(pygame.sprite.Sprite):
    def __init__(self, i):
        pygame.sprite.Sprite.__init__(self)
        self.image = white_rook
        self.rect = self.image.get_rect()
        self.i = i
        index = piece_list.index(white_figure[self.i])
        self.rect = (white_locations[self.i][0] * 70 + 20, white_locations[self.i][1] * 70 + 20)

    def update(self):
        self.rect = pygame.Rect(list(self.rect) + [45, 45])
        self.rect.move_ip((700, 700))


class Black_Rook(pygame.sprite.Sprite):
    def __init__(self, i):
        pygame.sprite.Sprite.__init__(self)
        self.image = black_rook
        self.rect = self.image.get_rect()
        self.i = i
        self.rect = (black_locations[self.i][0] * 70 + 20, black_locations[self.i][1] * 70 + 20)

    def update(self):
        self.rect = pygame.Rect(list(self.rect) + [45, 45])
        self.rect.move_ip((700, 700))


def list_board():
    b = []
    x, y = 10, 10
    k = 70
    for i in range(8):
        b.append([])
        for j in range(8):
            b[i].append((x, y, x + k, y + k))
            x += k
        y += k
        x = 10
    return b


def pieces_board():
    global num_level
    p_b = []
    for i in range(8):
        p_b.append([])
        for j in range(8):
            if i == 1:
                p_b[i].append('wp')
            elif i == 6:
                p_b[i].append('bp')
            elif num_level == 2:
                if i == 0 and (j == 0 or j == 7):
                    p_b[i].append('wr')
                elif i == 7 and (j == 0 or j == 7):
                    p_b[i].append('br')
                else:
                    p_b[i].append('')
            else:
                p_b[i].append('')
    return p_b


def add_figure(all_s, white_s, black_s):
    if num_level == 2:
        rook = White_Rook(0)
        all_s.add(rook)
        white_s.add(rook)
        all_s.change_layer(rook, 1)
        all_s.move_to_front(rook)
        rook = White_Rook(7)
        all_s.add(rook)
        white_s.add(rook)
        all_s.change_layer(rook, 1)
        all_s.move_to_front(rook)
        rook = Black_Rook(0)
        black_s.add(rook)
        all_s.add(rook)
        all_s.change_layer(rook, 1)
        all_s.move_to_front(rook)
        rook = Black_Rook(7)
        black_s.add(rook)
        all_s.add(rook)
        all_s.change_layer(rook, 1)
        all_s.move_to_front(rook)
    for i in range(8):
        pawn = White_Pawn(i + 8)
        all_s.add(pawn)
        white_s.add(pawn)
        all_s.change_layer(pawn, 1)
        all_s.move_to_front(pawn)
    for i in range(8):
        pawn = Black_Pawn(i + 8)
        all_s.add(pawn)
        black_s.add(pawn)
        all_s.change_layer(pawn, 1)
        all_s.move_to_front(pawn)
    return all_sprites, white_s, black_s


def first_window():
    global all_sprites, sp, b, go
    running = True
    num_btn = 0
    all_sprites = pygame.sprite.LayeredUpdates()
    white_sprite = pygame.sprite.Group()
    black_sprite = pygame.sprite.Group()
    all_sprites, white_sprite, black_sprite = add_figure(all_sprites, white_sprite, black_sprite)
    pieces_b = pieces_board()
    piece_move = {}
    last_color = 'wp'
    last_kill_color = ''
    score_white = 0
    score_black = 0
    font = pygame.font.Font(None, 30)
    main_text = ["Следующий ход:", "Счёт белых:", "Счёт чёрных:"]
    inf_text = ["- Вы можете съесть (Вашу фигуру могут съесть)", "- если Вы туда пойдете, фигуру могут съесть",
                "- безопасный ход"]
    text_list = ["белые", "чёрные", "Белая фигура съедена", "Черная фигура съедена"]
    text_line = text_list[0]
    sp = ''
    while running:
        screen.fill((153, 153, 153))
        board = Board(8, 8)
        board.set_view(10, 10, 70)
        board.render(screen)
        all_sprites.draw(screen)
        text_coord = -10
        pygame.draw.circle(screen, "red", (620,
                                           text_coord + 40), 15)
        pygame.draw.circle(screen, "orange", (620,
                                              text_coord + 80), 15)
        pygame.draw.circle(screen, "green", (620,
                                             text_coord + 120), 15)
        text_coord = -20
        for line in inf_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 40
            intro_rect.top = text_coord
            intro_rect.left = 650
            screen.blit(string_rendered, intro_rect)
        if piece_move != {}:
            for i in piece_move[0]:
                # pygame.draw.rect(screen, "green", (i[1] * 70 + 10,
                #                                   i[0] * 70 + 10, 70, 70), 5)
                pygame.draw.circle(screen, "green", (i[1] * 70 + 45,
                                                     i[0] * 70 + 45), 5)
            for i in piece_move[1]:
                pygame.draw.rect(screen, "red", (i[1] * 70 + 10,
                                                 i[0] * 70 + 10, 70, 70), 5)
            for i in piece_move[2]:
                pygame.draw.rect(screen, "orange", (i[1] * 70 + 10,
                                                    i[0] * 70 + 10, 70, 70), 5)
        text_coord = 120
        string_rendered = font.render(last_kill_color, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.left = 600
        intro_rect.top = text_coord + 120
        screen.blit(string_rendered, intro_rect)
        if text_line == 'белые':
            pygame.draw.circle(screen, "white", (820,
                                                 text_coord + 40), 20)
        else:
            pygame.draw.circle(screen, "black", (820,
                                                 text_coord + 40), 20)
        string_rendered = font.render(str(score_white), 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.left = 740
        intro_rect.top = text_coord + 60
        screen.blit(string_rendered, intro_rect)
        string_rendered = font.render(str(score_black), 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.left = 750
        intro_rect.top = text_coord + 90
        screen.blit(string_rendered, intro_rect)
        for line in main_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 30
            intro_rect.top = text_coord
            intro_rect.left = 600
            screen.blit(string_rendered, intro_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_kill_color = ''
                num_btn += 1
                b = list_board()
                for sprite in all_sprites:
                    rect = pygame.Rect(list(sprite.rect) + [45, 45])
                    if rect.collidepoint(event.pos):
                        if num_btn % 2 == 1:
                            global go
                            go = False
                            if text_line == 'белые' and sprite in white_sprite:
                                sp = sprite
                                go = True
                            elif text_line == 'чёрные' and sprite in black_sprite:
                                sp = sprite
                                go = True
                            if go and type(sp) != str:
                                for i in range(8):
                                    for j in range(8):
                                        if (b[i][j][0] <= sp.rect[0] <= b[i][j][2]) and (
                                                b[i][j][1] <= sp.rect[1] <= b[i][j][3]):
                                            sprite_old_pos = (i, j)
                                            piece_move = moves(sprite_old_pos, pieces_b)
                                            last_color = pieces_b[i][j]
                if num_btn % 2 == 0 and go:
                    sprite_old_pos = (0, 0)
                    for i in range(8):
                        for j in range(8):
                            if (b[i][j][0] <= sp.rect[0] <= b[i][j][2]) and (
                                    b[i][j][1] <= sp.rect[1] <= b[i][j][3]):
                                sprite_old_pos = (i, j)
                                piece_move = moves(sprite_old_pos, pieces_b)
                    for i in range(8):
                        for j in range(8):
                            if (b[i][j][0] <= event.pos[0] <= b[i][j][2]) and (
                                    b[i][j][1] <= event.pos[1] <= b[i][j][3]):
                                if (i, j) in piece_move[1]:
                                    if last_color in ['wp', 'wr']:
                                        text_line = text_list[1]
                                        last_kill_color = text_list[3]
                                        if pieces_b[i][j] == 'br':
                                            score_white += 5
                                        else:
                                            score_white += 1
                                    if last_color in ['bp', 'br']:
                                        text_line = text_list[0]
                                        last_kill_color = text_list[2]
                                        if pieces_b[i][j] == 'wr':
                                            score_black += 5
                                        else:
                                            score_black += 1
                                    sp.rect = (b[i][j][0] + 10, b[i][j][1] + 10)
                                    pieces_b[i][j] = pieces_b[sprite_old_pos[0]][sprite_old_pos[1]]
                                    pieces_b[sprite_old_pos[0]][sprite_old_pos[1]] = ''
                                    for sprite in all_sprites:
                                        sp_rect = pygame.Rect(list(sp.rect) + [45, 45])
                                        sprite_rect = pygame.Rect(list(sprite.rect) + [45, 45])
                                        if sp != sprite and sp_rect.colliderect(sprite_rect):
                                            sprite.update()
                                            sprite.kill()
                                elif (i, j) in piece_move[0]:
                                    if last_color in ['wp', 'wr']:
                                        text_line = text_list[1]
                                    elif last_color in ['bp', 'br']:
                                        text_line = text_list[0]
                                    sp.rect = (b[i][j][0] + 10, b[i][j][1] + 10)
                                    pieces_b[i][j] = pieces_b[sprite_old_pos[0]][sprite_old_pos[1]]
                                    pieces_b[sprite_old_pos[0]][sprite_old_pos[1]] = ''
                                elif (i, j) in piece_move[2]:
                                    if last_color in ['wp', 'wr']:
                                        text_line = text_list[1]
                                    elif last_color in ['bp', 'br']:
                                        text_line = text_list[0]
                                    sp.rect = (b[i][j][0] + 10, b[i][j][1] + 10)
                                    pieces_b[i][j] = pieces_b[sprite_old_pos[0]][sprite_old_pos[1]]
                                    pieces_b[sprite_old_pos[0]][sprite_old_pos[1]] = ''
                    for i in range(8):
                        for j in range(8):
                            if (pieces_b[i][j] == 'bp' and i == 0) or (pieces_b[i][j] == 'wp' and i == 7):
                                running = False
                    w_in_s = 0
                    b_in_s = 0
                    for i in range(8):
                        for j in range(8):
                            if pieces_b[i][j] in ['wp', 'wr']:
                                w_in_s += 1
                            if pieces_b[i][j] in ['bp', 'br']:
                                b_in_s += 1
                    if w_in_s == 0 or b_in_s == 0:
                        running = False
                    piece_move = {}
            all_sprites.draw(screen)
            pygame.display.flip()
    update_var_into_bd(user_name, score_white, score_black)
    start_the_game()
    if num_level == 1:
        win_window()
    last_window()


surface = pygame.display.set_mode((1200, 650))
FPS = 50
clock = pygame.time.Clock()


def moves(koor, board):
    kx, ky = koor[0], koor[1]
    m = {0: [], 1: [], 2: []}  # 0 - просто ход, 1 - возможность съесть 2 - опасный ход
    if board[kx][ky] == 'wp':  # белая пешка
        if kx <= 6 and ky <= 6 and board[kx + 1][ky + 1] in ['bp', 'br']:  # диагональ вправо
            m[1].append((kx + 1, ky + 1))
        if kx <= 6 and ky >= 1 and board[kx + 1][ky - 1] in ['bp', 'br']:  # диагональ влево
            m[1].append((kx + 1, ky - 1))
        if kx == 1:  # начальная позиция
            if board[kx + 1][ky] == '':  # ход на клетку
                # опасно / безопасно
                if (ky <= 6 and board[kx + 2][ky + 1] in ['bp', 'br']) or (ky >= 1 and
                                                                           board[kx + 2][ky - 1] in ['bp', 'br']):
                    m[2].append((kx + 1, ky))
                else:
                    m[0].append((kx + 1, ky))
            if board[kx + 2][ky] == '':  # ход на 2 клетки
                # опасно / безопасно
                if ((ky <= 6 and board[kx + 3][ky + 1] in ['bp', 'br']) or
                        (ky >= 1 and board[kx + 3][ky - 1] in ['bp', 'br'])):
                    m[2].append((kx + 2, ky))
                else:
                    m[0].append((kx + 2, ky))
        else:  # ход в любом месте
            if board[kx + 1][ky] == '':
                # опасно / безопасно
                if ((ky <= 6 and kx <= 5 and board[kx + 2][ky + 1] in ['bp', 'br']) or
                        (ky >= 1 and kx <= 5 and board[kx + 2][ky - 1] in ['bp', 'br'])):
                    m[2].append((kx + 1, ky))
                else:
                    m[0].append((kx + 1, ky))
    if board[kx][ky] == 'bp':  # черная пешка
        if kx >= 1 and board[kx - 1][ky - 1] in ['wp', 'wr']:  # диагональ влево
            m[1].append((kx - 1, ky - 1))
        if kx >= 1 and ky <= 6 and board[kx - 1][ky + 1] in ['wp', 'wr']:  # дианональ вправо
            m[1].append((kx - 1, ky + 1))
        if kx == 6:  # начальная позиция
            if board[kx - 1][ky] == '':  # ход на клетку
                # опасно / безопасно
                if (ky <= 6 and board[kx - 2][ky + 1] in ['wp', 'wr']) or (ky >= 1 and
                                                                           board[kx - 2][ky - 1] in ['wp', 'wr']):
                    m[2].append((kx - 1, ky))
                else:
                    m[0].append((kx - 1, ky))
            if board[kx - 2][ky] == '':  # ход на 2 клетки
                # опасно / безопасно
                if (ky <= 6 and board[kx - 3][ky + 1] in ['wp', 'wr']) or (ky >= 1 and
                                                                           board[kx - 3][ky - 1] in ['wp', 'wr']):
                    m[2].append((kx - 2, ky))
                else:
                    m[0].append((kx - 2, ky))
        else:
            if board[kx - 1][ky] == '':  # любой ход
                # опасно / безопасно
                if (ky <= 6 and board[kx - 2][ky + 1] in ['wp', 'wr']) or (ky >= 1 and
                                                                           board[kx - 2][ky - 1] in ['wp', 'wr']):
                    m[2].append((kx - 1, ky))
                else:
                    m[0].append((kx - 1, ky))
    if board[kx][ky] == 'wr':  # белая ладья
        min_k, max_k = -1, 9
        for i in range(8):
            if board[i][ky] != '':
                if i < kx:
                    min_k = i
                elif i > kx:
                    max_k = min(max_k, i)
        if max_k == 9:
            max_k = 7
        if min_k == -1:
            min_k = 0
        for i in range(min_k, max_k + 1):
            if board[i][ky] in ['bp', 'br']:
                m[1].append((i, ky))
            elif board[i][ky] == '':
                m[0].append((i, ky))
        min_k, max_k = -1, 9
        for i in range(8):
            if board[kx][i] != '':
                if i < ky:
                    min_k = i
                elif i > ky:
                    max_k = min(max_k, i)
        if max_k == 9:
            max_k = 7
        if min_k == -1:
            min_k = 0
        for i in range(min_k, max_k + 1):
            if board[kx][i] in ['bp', 'br']:
                m[1].append((kx, i))
            elif board[kx][i] == '':
                m[0].append((kx, i))
    if board[kx][ky] == 'br':  # чёрная ладья
        min_k, max_k = -1, 9
        for i in range(8):
            if board[i][ky] != '':
                if i < kx:
                    min_k = i
                elif i > kx:
                    max_k = min(max_k, i)
        if max_k == 9:
            max_k = 7
        if min_k == -1:
            min_k = 0
        for i in range(min_k, max_k + 1):
            if board[i][ky] in ['wp', 'wr']:
                m[1].append((i, ky))
            elif board[i][ky] == '':
                m[0].append((i, ky))
        min_k, max_k = -1, 9
        for i in range(8):
            if board[kx][i] != '':
                if i < ky:
                    min_k = i
                elif i > ky:
                    max_k = min(max_k, i)
        if max_k == 9:
            max_k = 7
        if min_k == -1:
            min_k = 0
        for i in range(min_k, max_k + 1):
            if board[kx][i] in ['wp', 'wr']:
                m[1].append((kx, i))
            elif board[kx][i] == '':
                m[0].append((kx, i))
    return m


def terminate():
    pygame.quit()
    sys.exit()


def start_screen_1():
    intro_text = ["Пешечный бой", "Здравствуйте, " + user_name,
                  f"Ваш последний счёт: белые - {user_white_score}; черные - {user_black_score}",
                  "Правила игры",
                  "Для того чтобы сходить:",
                  "1) нажмите на фигуру",
                  "2) нажмите на клетку, куда хотите сходить",
                  "• Пешка ходит только на 1 клетку вперёд", "• Пешка ест только по диагонали",
                  "• Если пешка ещё не ходила, она может сходить на 2 или 1 клетку", "",
                  "Кто первый дойдет до края - победил", "", "", "", "Для продолжения нажмите на экран"]

    screen.fill((200, 200, 200))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                first_window()
        pygame.display.flip()
        clock.tick(FPS)


def start_screen_2():
    global num_level
    num_level = 2
    intro_text = ["Охота на пешки", "Здравствуйте, " + user_name,
                  f"Ваш последний счёт: белые - {user_white_score}; черные - {user_black_score}",
                  "Правила игры",
                  "Для того чтобы сходить:",
                  "1) нажмите на фигуру",
                  "2) нажмите на клетку, куда хотите сходить",
                  "• Пешка ходит только на 1 клетку вперёд", "• Пешка ест только по диагонали",
                  "• Если пешка ещё не ходила, она может сходить на 2 или 1 клетку", "",
                  "", "• Ладья ходит по вертикали и горизонтали",
                  "• Ладья ходит на любое количество клеток, если на пути нет припятствий",
                  "Кто первый дойдет до края - победил", "", "Для продолжения нажмите на экран"]

    screen.fill((200, 200, 200))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                first_window()
        pygame.display.flip()
        clock.tick(FPS)


star_sprites = pygame.sprite.Group()
screen_rect = (0, 0, width, height)


class Particle(pygame.sprite.Sprite):
    fire = [pygame.image.load("images\star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(star_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = 1

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    particle_count = 20
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


def last_window():
    global star_sprites
    intro_text = ["Поздравляем!", "Вы прошли все уровни :)",
                  "",
                  "Спасибо за игру!"]

    count = 0
    while True:
        count += 1
        screen.fill((200, 200, 200))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                terminate()
        if count % 10 == 0:
            create_particles((400 + ((count // 10) % 6) * 100, 0))
            create_particles((1000 - ((count // 10) % 6) * 100, 0))
        star_sprites.update()
        screen.fill((0, 0, 0))
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        star_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def win_window():
    global star_sprites
    intro_text = ["Поздравляем!", "Вы прошли уровень 1 :)",
                  "",
                  "Продолжайте в том же духе", "Нажмите на экран)"]

    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    run = True
    count = 0
    while run:
        count += 1
        screen.fill((200, 200, 200))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                run = False

        if count % 10 == 0:
            rn = random.randint(400, 1000)
            rn1 = random.randint(0, 100)
            create_particles((rn, rn1))
        star_sprites.update()
        screen.fill((0, 0, 0))
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        star_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(40)
    start_screen_2()


def update_var_into_bd(name, sc_w, sc_b):
    new_list = (sc_w, sc_b, name)
    sqlite_connection = sqlite3.connect("game_bd.sqlite")
    cursor = sqlite_connection.cursor()
    sqlite_update_query = """Update user set score_w = ?, score_b = ? where name = ?"""
    if user_name != '' and user_password != '':
        cursor.execute(sqlite_update_query, new_list)
    sqlite_connection.commit()
    cursor.close()


def insert_var_into_bd(name, password, sc_w, sc_b):
    sqlite_connection = sqlite3.connect("game_bd.sqlite")
    cursor = sqlite_connection.cursor()
    sqlite_insert_with_param = """INSERT INTO User
                              (name, password, score_w, score_b)
                              VALUES (?, ?, ?, ?);"""

    data_tuple = (name, password, sc_w, sc_b)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    sqlite_connection.commit()
    cursor.close()


replay_name = 0


def start_the_game():
    global user_name, user_password, replay_name, user_white_score, user_black_score
    user_name = name_input.get_value()
    user_password = passord_input.get_value()
    in_user = 0
    con = sqlite3.connect("game_bd.sqlite")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM User""").fetchall()
    for elem in result:
        if elem[0] == user_name and elem[1] == user_password:
            user_white_score = elem[2]
            user_black_score = elem[3]
            in_user = 1
        elif elem[0] == user_name and elem[1] != user_password:
            in_user = 1
    if in_user == 0:
        cur.close()
        insert_var_into_bd(user_name, user_password, 0, 0)


menu = pygame_menu.Menu('Добро пожаловать в шахматы   (UwU)', 1200, 650)
name_input = menu.add.text_input('Имя: ')
passord_input = menu.add.text_input('Пароль: ')
menu.add.button('Сохранить', start_the_game, font_color='green')
menu.add.button('Уровень 1', start_screen_1)
menu.add.button('Уровень 2', start_screen_2)
menu.add.button('Выход', pygame_menu.events.EXIT)
menu.mainloop(surface)
