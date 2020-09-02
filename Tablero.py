import pygame
from pygame.locals import *
import random


class tablero():
    def __init__(self, square_size):
        self.square_size = square_size
        self.numbers = []
        for i in range(9):
            self.numbers.append([])
        for i in range(81):
            j = random.random()
            if j > 0:
                self.numbers[int(i/9)].append(random.randint(1, 9))
            else:
                self.numbers[int(i/9)].append(0)
        self.Check_rules()

    def draw(self, canvas, myfont):
        location = [-(self.square_size/2), (self.square_size/2)]
        for i in range(81):
            location[0] += self.square_size
            pygame.draw.rect(
                canvas, (255, 255, 255), (location[0], location[1], self.square_size, self.square_size), 1)
            if (i+1) % 9 == 0:
                location[0] = -(self.square_size/2)
                location[1] += self.square_size
        self.draw_numbers(canvas, myfont)

    def draw_numbers(self, canvas, myfont):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                if self.numbers[i][j] == 0:
                    continue
                text = myfont.render(
                    str(self.numbers[i][j]), True, (255, 255, 255))
                font_size = myfont.size(str(self.numbers[i][j]))
                x_pos = ((j*self.square_size) -
                         (font_size[0]/2)) + self.square_size
                y_pos = ((i*self.square_size) -
                         (font_size[1]/2)) + self.square_size
                canvas.blit(text, (x_pos, y_pos))

    def Check_rules(self):
        self.all_around = ((-1, -1), (0, -1), (1, -1), (-1, 0),
                      (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
        self.center_positions = ((1, 1), (4, 1), (7, 1), (1, 4),
                            (4, 4), (7, 4), (1, 7), (4, 7), (7, 7))
        # check same numbers on the 3x3 cubes
        for i in self.center_positions:
            self.Check_same_numbers(self.all_around, i)

        # Checks same numbers on horizontal lines
        nums = []
        for j in range(9):
            self.horizontal_positions = [(i, 0) for i in range(9)]
            self.Check_same_numbers(self.horizontal_positions, (0, j))
        # Check same numbers on vertical lines
        for j in range(9):
            self.veritical_positions = [(0, i) for i in range(9)]
            self.Check_same_numbers(self.veritical_positions, (j, 0))

    def Check_duplicates(self, a):
        appeared_nums = []
        for i in a:
            if i in appeared_nums:
                return True
            else:
                if i != 0:
                    appeared_nums.append(i)
        return False

    def Check_same_numbers(self, positions_to_check, starting_position):
        nums = []
        for j in positions_to_check:
            pos_x = starting_position[0] + j[0]
            pos_y = starting_position[1] + j[1]
            nums.append(self.numbers[pos_y][pos_x])
            duplicated = self.Check_duplicates(nums)
            if duplicated:
                nums.pop()
                self.numbers[pos_y][pos_x] = 0
        return set(nums)
        nums = []

    def Find_nearest_Center(self,position):
        posibilities = (1,0,-1)
        for i in self.center_positions:
            for j in posibilities:
                if j + position[0] ==  i[0]:
                    center_x = i[0]
                if j + position[1] == i[1]:
                    center_y = i[1]
        return (center_x,center_y)

    def solve_sudoku(self):
        for y_pos in range(len(self.numbers)):
            for x_pos in range(len(self.numbers[1])):
                if self.numbers[y_pos][x_pos] == 0:
                    posibilities = self.Find_posible_nums((x_pos,y_pos))
                    if len(posibilities) == 1:
                        posibilities = list(posibilities)
                        self.numbers[y_pos][x_pos] = posibilities[0]

    def Find_posible_nums(self,pos):
        x_pos = pos[0]
        y_pos = pos[1]
        posibilities = set([i+1 for i in range(9)])
        nearest_center = self.Find_nearest_Center((x_pos,y_pos))
        used_allaround_nums = self.Check_same_numbers(self.all_around,nearest_center)
        posibilities -= used_allaround_nums
        used_horizontal_nums = self.Check_same_numbers(self.horizontal_positions,(0,y_pos))
        posibilities -= used_horizontal_nums
        used_vertical_nums = self.Check_same_numbers(self.veritical_positions,(x_pos,0))
        posibilities -= used_vertical_nums

        return posibilities


            



                      




