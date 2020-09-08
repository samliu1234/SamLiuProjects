import tkinter as tk
from tkinter import *
import time
import math
import simpleaudio as sa
import pickle

root = tk.Tk()
# if you change the height, change the y-intercept as well
canvas = tk.Canvas(root, width=545, height=600, bg="#B9BFA5")
canvas.pack()


# reset function
def reset():
    file = open("/Users/SamRoo/PycharmProjects/OOPPractice/Minigolf/Minigolf High Scores", "wb")
    pickle.dump([], file)
    file.close()


highscore = pickle.load(open("/Users/SamRoo/PycharmProjects/OOPPractice/Minigolf/Minigolf High "
                                                 "Scores", "rb"))


# variables spanning across the entire game
class Game:
    def __init__(self):
        self.game = "homescreen"
        self.total_turn = 0
        self.turn = 0
        
        
g = Game()


# make global t variable (for turn)
t = None


class Homescreen:
    def __init__(self):
        self.image = PhotoImage(file="/Users/SamRoo/PycharmProjects/OOPPractice/Minigolf/loading screen.gif")
        self.credits_image = PhotoImage(file="/Users/SamRoo/PycharmProjects/OOPPractice/Minigolf/credits.gif")
        self.background = canvas.create_image(275, 300, image=self.image, anchor="center")
        self.credits = None
        canvas.bind_all("<Button-1>", self.touch)

    # when the user clicks, this function will check if the user clicks "start", "credits", or "quit"
    def touch(self, event):
        if g.game == "homescreen":
            x = root.winfo_pointerx()
            y = root.winfo_pointery() - 50
            if 240 <= x <= 310:
                if 440 <= y <= 465:
                    # start game
                    g.game = "game1"
                    canvas.delete(self.background)
                    global t
                    t = Turn()
                elif 480 <= y <= 505:
                    # credits screen
                    self.credits = canvas.create_image(275, 300, image=self.credits_image, anchor="center")
                elif 520 <= y <= 545:
                    # quit game
                    root.destroy()
            elif 50 <= x <= 105:
                if 30 <= y <= 55:
                    if self.credits is not None:
                        canvas.delete(self.credits)


h = Homescreen()


class Green:
    def __init__(self, x1, y1, x2, y2):
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill="#2EC330", outline="#2EC330")


class Rectangular_Wall:
    def __init__(self, x1, y1, x2, y2, block):
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="")
        self.block = block


class Circular_Wall:
    def __init__(self, x1, y1, x2, y2, bool):
        self.id = canvas.create_oval(x1, y1, x2, y2, fill="white", outline="")
        self.radius = abs((x2 - x1) / 2)
        self.speed_up = bool


class Polygonal_Wall:
    def __init__(self, *args):
        self.coords = []
        for arg in args:
            self.coords.append(arg)
        self.id = canvas.create_polygon(self.coords, fill="white", outline="")


class Speed_Up:
    def __init__(self, x1, y1, x2, y2, direction):
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill="#228B22", outline="")
        self.direction = direction


class Hole:
    def __init__(self, x1, y1, x2, y2):
        self.id = canvas.create_oval(x1, y1, x2, y2, fill="black")


class Water:
    def __init__(self, x1, y1, x2, y2):
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill="#8DEEEE", outline="#8DEEEE")


# class that creates the three maps
class Map:
    def __init__(self):
        # boolean that ensures the maps are only created once
        self.bool = False

        # arrows image
        self.arrows_image = PhotoImage(file="/Users/SamRoo/PycharmProjects/OOPPractice/Minigolf/arrows.gif")

        # initialize elements of the first map
        self.green1_map1 = None
        self.green2_map1 = None
        self.greens_map1 = []

        self.outerwall1_map1 = None
        self.outerwall2_map1 = None
        self.outerwall3_map1 = None
        self.outerwall4_map1 = None
        self.outerwall5_map1 = None
        self.outerwall6_map1 = None
        self.outerwall7_map1 = None
        self.outerwall8_map1 = None
        self.outerwalls_map1 = []

        self.circle_map1 = None

        self.triangle1_map1 = None
        self.triangle2_map1 = None

        self.hole_map1 = None
        self.ball_map1 = None

        # initialize elements of the second map
        self.green1_map2 = None
        self.green2_map2 = None
        self.green3_map2 = None
        self.green4_map2 = None
        self.green5_map2 = None
        self.greens_map2 = []

        self.outerwall1_map2 = None
        self.outerwall2_map2 = None
        self.outerwall3_map2 = None
        self.outerwall4_map2 = None
        self.outerwall5_map2 = None
        self.outerwall6_map2 = None
        self.outerwalls_map2 = []

        self.circle_map2 = None
        self.arrows_map2 = None

        self.triangle1_map2 = None
        self.triangle2_map2 = None
        self.rectangle_map2 = None
        self.windmill_circle_map2 = None
        self.windmill_rectangle1_map2 = None
        self.windmill_rectangle2_map2 = None
        self.polygons_map2 = []

        self.ramp_map2 = None
        self.triangle_coords_map2 = None
        self.triangle_map2 = None

        self.hole_map2 = None
        self.water_map2 = None
        self.ball_map2 = False

        # initialize elements of the third map
        self.green_map3 = None

        self.outerwall1_map3 = None
        self.outerwall2_map3 = None
        self.outerwall3_map3 = None
        self.outerwall4_map3 = None
        self.outerwalls_map3 = []

        self.circle1_map3 = None
        self.circle2_map3 = None

        self.triangle1_map3 = None
        self.triangle2_map3 = None

        self.ramp1_map3 = None
        self.triangle1_coords_map3 = []
        self.ramp2_map3 = None
        self.triangle2_coords_map3 = []
        self.ramp3_map3 = None
        self.triangle3_coords_map3 = []
        self.ramp4_map3 = None
        self.triangle4_coords_map3 = []
        self.ramp5_map3 = None
        self.triangle5_coords_map3 = []
        self.ramps_map3 = []

        self.river1_map3 = None
        self.river2_map3 = None
        self.river3_map3 = None
        self.rivers_map3 = []

        self.hole_map3 = None
        self.ball_map3 = None

    def game(self):
        if g.game == "game1" and self.bool is False:
            # green
            self.green1_map1 = Green(50, 275, 300, 550)
            self.green2_map1 = Green(250, 50, 500, 325)
            self.greens_map1 = [self.green1_map1, self.green2_map1]

            # outer walls
            self.outerwall1_map1 = Rectangular_Wall(42, 267, 50, 558, "right")
            self.outerwall2_map1 = Rectangular_Wall(42, 550, 308, 558, "up")
            self.outerwall3_map1 = Rectangular_Wall(300, 325, 308, 558, "left")
            self.outerwall4_map1 = Rectangular_Wall(300, 325, 508, 333, "up")
            self.outerwall5_map1 = Rectangular_Wall(500, 42, 508, 333, "left")
            self.outerwall6_map1 = Rectangular_Wall(242, 42, 508, 50, "down")
            self.outerwall7_map1 = Rectangular_Wall(242, 42, 250, 275, "right")
            self.outerwall8_map1 = Rectangular_Wall(42, 267, 250, 275, "down")
            self.outerwalls_map1 = [self.outerwall1_map1, self.outerwall2_map1, self.outerwall3_map1,
                                    self.outerwall4_map1, self.outerwall5_map1, self.outerwall6_map1,
                                    self.outerwall7_map1, self.outerwall8_map1]

            # circular wall
            self.circle_map1 = Circular_Wall(170, 300, 220, 350, False)

            # triangles
            self.triangle1_map1 = Polygonal_Wall(310, 220, 340, 160, 365, 245)
            self.triangle2_map1 = Polygonal_Wall(185, 425, 250, 450, 220, 470)

            # hole, ball
            self.hole_map1 = Hole(455, 80, 470, 95)
            self.ball_map1 = Ball(80, 510, 90, 520)

            # change boolean
            self.bool = True

        elif g.game == "game2" and self.bool is False:
            # green
            self.green1_map2 = Green(50, 50, 100, 550)
            self.green2_map2 = Green(100, 50, 400, 200)
            self.green3_map2 = Green(100, 400, 400, 550)
            self.green4_map2 = Green(250, 200, 400, 400)
            self.green5_map2 = Green(400, 50, 500, 200)
            self.greens_map2 = [self.green1_map2, self.green2_map2, self.green3_map2, self.green4_map2,
                                self.green5_map2]

            # outer walls
            self.outerwall1_map2 = Rectangular_Wall(42, 42, 50, 558, "right")
            self.outerwall2_map2 = Rectangular_Wall(42, 550, 408, 558, "up")
            self.outerwall3_map2 = Rectangular_Wall(400, 200, 408, 558, "left")
            self.outerwall4_map2 = Rectangular_Wall(400, 200, 508, 208, "up")
            self.outerwall5_map2 = Rectangular_Wall(500, 42, 508, 208, "left")
            self.outerwall6_map2 = Rectangular_Wall(42, 42, 508, 50, "down")
            self.outerwalls_map2 = [self.outerwall1_map2, self.outerwall2_map2, self.outerwall3_map2,
                                    self.outerwall4_map2, self.outerwall5_map2, self.outerwall6_map2]

            # bouncy wall
            self.circle_map2 = Circular_Wall(335, 330, 385, 380, True)
            self.arrows_map2 = canvas.create_image(360, 355, image=self.arrows_image, anchor="center")

            # triangles and rectangles
            self.triangle1_map2 = Polygonal_Wall(90, 455, 140, 435, 155, 490)
            self.triangle2_map2 = Polygonal_Wall(305, 510, 330, 425, 355, 470)
            self.rectangle_map2 = Polygonal_Wall(270, 234, 275, 230, 345, 290, 340, 294)

            # windmill
            self.windmill_circle_map2 = Circular_Wall(152, 112, 173, 133, False)
            # top right -> left bottom
            self.windmill_rectangle1_map2 = Polygonal_Wall(202.5 - 2.5, 82.5 - 2.5, 202.5 + 2.5, 82.5 + 2.5,
                                                           122.5 + 2.5, 162.5 + 2.5, 122.5 - 2.5, 162.5 - 2)
            # top left -> bottom right
            self.windmill_rectangle2_map2 = Polygonal_Wall(122.5 - 2.5, 82.5 + 2.5, 122.5 + 2.5, 82.5 - 2.5,
                                                           202.5 + 2.5, 162.5 - 2.5, 202.5 - 2.5, 162.5 + 2.5)
            canvas.create_oval(159, 119, 166, 126, fill="#2EC330", outline="#2EC330")
            self.polygons_map2 = [self.triangle1_map2, self.triangle2_map2, self.rectangle_map2,
                                  self.windmill_circle_map2, self.windmill_rectangle1_map2,
                                  self.windmill_rectangle2_map2]

            # ramp
            self.ramp_map2 = Speed_Up(300, 50, 400, 200, "left")
            self.triangle_coords_map2 = [350 + 5 * math.sqrt(3), 115, 350 + 5 * math.sqrt(3), 135,
                                         350 - 5 * math.sqrt(3), 125]
            self.triangle_map2 = canvas.create_polygon(self.triangle_coords_map2, fill="white", outline="")

            # hole, water, ball
            self.hole_map2 = Hole(442.5, 115, 457.5, 130)
            self.water_map2 = Water(100, 200, 250, 400)
            self.ball_map2 = Ball(80, 510, 90, 520)

            # change boolean
            self.bool = True

        elif g.game == "game3" and self.bool is False:
            # green
            self.green_map3 = Green(50, 35, 500, 565)

            # outer walls
            self.outerwall1_map3 = Rectangular_Wall(42, 27, 50, 573, "right")
            self.outerwall2_map3 = Rectangular_Wall(42, 565, 508, 573, "up")
            self.outerwall3_map3 = Rectangular_Wall(500, 27, 508, 573, "left")
            self.outerwall4_map3 = Rectangular_Wall(42, 27, 508, 35, "down")
            self.outerwalls_map3 = [self.outerwall1_map3, self.outerwall2_map3, self.outerwall3_map3,
                                    self.outerwall4_map3]

            # bouncy walls
            self.circle1_map3 = Circular_Wall(80, 360, 120, 400, True)
            canvas.create_image(100, 380, image=self.arrows_image, anchor="center")
            self.circle2_map3 = Circular_Wall(428, 400, 468, 440, True)
            canvas.create_image(448, 420, image=self.arrows_image, anchor="center")

            # triangles
            self.triangle1_map3 = Polygonal_Wall(58, 180, 75, 140, 90, 200)
            self.triangle2_map3 = Polygonal_Wall(450, 240, 490, 255, 475, 280)

            # ramps
            self.ramp1_map3 = Speed_Up(165, 110, 385, 171, "down")
            self.triangle1_coords_map3 = [275 - 10, 140.5 - 5 * math.sqrt(3), 275 + 10, 140.5 - 5 * math.sqrt(3), 275,
                         140.5 + 5 * math.sqrt(3)]
            canvas.create_polygon(self.triangle1_coords_map3, fill="white", outline="")
            self.ramp2_map3 = Speed_Up(165, 232, 385, 293, "down")
            self.triangle2_coords_map3 = [275 - 10, 262.5 - 5 * math.sqrt(3), 275 + 10, 262.5 - 5 * math.sqrt(3), 275,
                         262.5 + 5 * math.sqrt(3)]
            canvas.create_polygon(self.triangle2_coords_map3, fill="white", outline="")
            self.ramp3_map3 = Speed_Up(165, 354, 385, 415, "down")
            self.triangle3_coords_map3 = [275 - 10, 384.5 - 5 * math.sqrt(3), 275 + 10, 384.5 - 5 * math.sqrt(3), 275,
                         384.5 + 5 * math.sqrt(3)]
            canvas.create_polygon(self.triangle3_coords_map3, fill="white", outline="")
            self.ramp4_map3 = Speed_Up(150, 520, 250, 555, "left")
            self.triangle4_coords_map3 = [200 + 3.75 * math.sqrt(3), 537.5 - 7.5, 200 + 3.75 * math.sqrt(3), 537.5 + 7.5,
                         200 - 3.75 *
                         math.sqrt(3), 537.5]
            canvas.create_polygon(self.triangle4_coords_map3, fill="white", outline="")
            self.ramp5_map3 = Speed_Up(300, 520, 400, 555, "right")
            self.triangle5_coords_map3 = [350 - 3.75 * math.sqrt(3), 537.5 - 7.5, 350 - 3.75 * math.sqrt(3), 537.5 + 7.5,
                         350 + 3.75 *
                         math.sqrt(3), 537.5]
            canvas.create_polygon(self.triangle5_coords_map3, fill="white", outline="")
            self.ramps_map3 = [self.ramp1_map3, self.ramp2_map3, self.ramp3_map3, self.ramp4_map3, self.ramp5_map3]

            # water
            self.river1_map3 = Water(130, 110, 165, 475)
            self.river2_map3 = Water(385, 110, 420, 475)
            self.river3_map3 = Water(130, 475, 420, 510)
            self.rivers_map3 = [self.river1_map3, self.river2_map3, self.river3_map3]

            # hole, ball
            self.hole_map3 = Hole(267.5, 530, 282.5, 545)
            self.ball_map3 = Ball(270, 440, 280, 450)

            # change boolean
            self.bool = True


m = Map()


class Circles:
    def __init__(self):
        self.circles_list = []
        self.xincrement = 0
        self.yincrement = 0
        self.angle = 0
        self.timer = math.pow(10, 10)

    # "s" represents starting, "e" represents ending
    def create_circles(self, sx, sy, ex, ey):
        # say sx = 300, ex = 370
        # self.xincrement = 10
        self.xincrement = (ex - sx) / 7
        self.yincrement = (ey - sy) / 7
        # if the increment is larger than 30, cap it at 30
        if math.sqrt(math.pow(self.xincrement, 2) + math.pow(self.yincrement, 2)) > 30:
            if self.xincrement != 0:
                self.angle = math.atan(-self.yincrement / self.xincrement)
                # quadrant 1 and 4 are fine, angles in quadrants 2 and 3 need to be adjusted
                if self.xincrement < 0:
                    self.angle += math.pi
            else:
                if self.yincrement > 0:
                    # technically, if yincrement > 0, self.angle = pi/2
                    # however, since we have -math.sin, we set self.angle = -pi/2 instead
                    self.angle = -math.pi / 2
                else:
                    self.angle = math.pi / 2
            self.xincrement = 30 * math.cos(self.angle)
            self.yincrement = 30 * -math.sin(self.angle)
        for x in range(0, 8):
            c = canvas.create_oval(sx + self.xincrement * x - 2.5, sy + self.yincrement * x - 2.5, sx + self.xincrement
                                   * x + 2.5, sy + self.yincrement * x + 2.5, fill="white", outline="")
            self.circles_list.append(c)


Circles = Circles()


class Ball:
    def __init__(self, x1, y1, x2, y2):
        self.id = canvas.create_oval(x1, y1, x2, y2, fill="white", outline="")
        # x and y centres of the ball
        self.x = (x1 + x2) / 2
        self.y = (y1 + y2) / 2
        self.tempx = (x1 + x2) / 2
        self.tempy = (y1 + y2) / 2
        # x and y speeds of the ball
        self.xspeed = 0
        self.yspeed = 0
        # slope and y-intercept of wall
        self.m = 0
        self.b = 0
        # angles
        self.angle_of_impact = 0
        self.angle_of_incidence = 0
        self.angle_of_reflection = 0
        # movement timer
        self.timer = math.pow(10, 10)
        # pull and release variables
        self.is_clicked = False
        self.angle = 0
        # variable tracking whether ball is on a slope
        self.slope = False
        # water variables
        self.water_timer = math.pow(10, 10)
        self.water_boolean = False
        # hole variables
        self.win_timer = math.pow(10, 10)
        self.win_timer2 = math.pow(10, 10)
        self.restart_timer = math.pow(10, 10)
        self.win_boolean = False
        self.win_boolean2 = False
        self.win_boolean3 = False
        self.win_background = None
        self.win_text = None
        self.ticks = 0
        # variable indicating whether the ball is moving
        self.moving = False
        # variables dealing with which speed-up
        self.z = 0
        self.z_var = 0
        # bind the pull and release features
        canvas.bind_all("<Button-1>", self.pull)
        canvas.bind_all("<ButtonRelease-1>", self.stop_pulling)

    # this function controls the boolean that allows for the measuring to occur
    def pull(self, event):
        if self.moving is False and self.water_boolean is False:
            self.is_clicked = True

    # the trajectory showed by the circles is threefold the amount pulled back
    def measure(self):
        # preliminarily delete the existing circles
        if Circles.circles_list.__len__() != 0:
            for item in Circles.circles_list:
                canvas.delete(item)
        posx = root.winfo_pointerx()
        # since the navigation bar at the top counts as coordinates, subtract 50
        posy = root.winfo_pointery() - 50
        # if self.x = 300 and posx is 340, xforward becomes -120
        finishingx = 3 * (self.x - posx) + self.x
        finishingy = 3 * (self.y - posy) + self.y
        Circles.create_circles(self.x, self.y, finishingx, finishingy)

    def stop_pulling(self, event):
        # delete the circles
        if Circles.circles_list.__len__() != 0:
            for item in Circles.circles_list:
                canvas.delete(item)

        if self.moving is False and self.is_clicked is True:
            # increment turns
            g.turn += 1
            g.total_turn += 1
            # obtain the x and y coordinates at the point where the golfer releases the mouse
            posx = root.winfo_pointerx()
            posy = root.winfo_pointery() - 50
            # change boolean
            self.is_clicked = False

            # this part of the function deals with the movement of the ball
            self.xspeed = (self.x - posx) / 10
            self.yspeed = (self.y - posy) / 10
            # the speed can't be greater than 6, so cap it at such
            if math.sqrt(math.pow(self.xspeed, 2) + math.pow(self.yspeed, 2)) > 6:
                # we need a separate case for when xspeed = 0 because we cannot have a denominator of 0
                if self.xspeed != 0:
                    self.angle = math.atan(-self.yspeed / self.xspeed)
                    # quadrant 1 and 4 are fine, the angles in quadrants 2 and 3 need to be corrected
                    if self.xspeed < 0:
                        self.angle += math.pi
                else:
                    if self.yspeed > 0:
                        # technically, if yspeed > 0, self.angle = pi/2
                        # however, since we have -math.sin, we set self.angle = -pi/2 instead
                        self.angle = -math.pi / 2
                    else:
                        self.angle = math.pi / 2
                self.xspeed = 6 * math.cos(self.angle)
                self.yspeed = 6 * -math.sin(self.angle)
            self.timer = time.time()
            self.tempx = self.x
            self.tempy = self.y

    def ball_movement(self):
        if g.game == "game1":
            for item in m.outerwalls_map1:
                if item.block == "right" or item.block == "left":
                    self.vertical(item)
                else:
                    self.horizontal(item)
            self.positive_top(m.triangle1_map1.id, 1, 3)
            self.negative_top(m.triangle1_map1.id, 3, 5)
            self.negative_bottom(m.triangle1_map1.id, 1, 5)
            self.negative_top(m.triangle2_map1.id, 1, 3)
            self.positive_bottom(m.triangle2_map1.id, 3, 5)
            self.negative_bottom(m.triangle2_map1.id, 1, 5)
            self.touch_circle(m.circle_map1)
        elif g.game == "game2":
            for item in m.outerwalls_map2:
                if item.block == "right" or item.block == "left":
                    self.vertical(item)
                else:
                    self.horizontal(item)
            self.positive_top(m.triangle1_map2.id, 1, 3)
            self.negative_top(m.triangle1_map2.id, 3, 5)
            self.negative_bottom(m.triangle1_map2.id, 1, 5)
            self.positive_top(m.triangle2_map2.id, 1, 3)
            self.negative_top(m.triangle2_map2.id, 3, 5)
            self.positive_bottom(m.triangle2_map2.id, 1, 5)
            self.touch_circle(m.circle_map2)
            self.positive_top(m.rectangle_map2.id, 1, 3)
            self.negative_top(m.rectangle_map2.id, 3, 5)
            self.positive_bottom(m.rectangle_map2.id, 5, 7)
            self.negative_bottom(m.rectangle_map2.id, 1, 7)
            self.touch_circle(m.windmill_circle_map2)
            self.negative_top(m.windmill_rectangle1_map2.id, 1, 3)
            self.positive_bottom(m.windmill_rectangle1_map2.id, 3, 5)
            self.negative_bottom(m.windmill_rectangle1_map2.id, 5, 7)
            self.positive_top(m.windmill_rectangle1_map2.id, 1, 7)
            self.positive_top(m.windmill_rectangle2_map2.id, 1, 3)
            self.negative_top(m.windmill_rectangle2_map2.id, 3, 5)
            self.positive_bottom(m.windmill_rectangle2_map2.id, 5, 7)
            self.negative_bottom(m.windmill_rectangle2_map2 .id, 1, 7)
            self.touch_speedup(m.ramp_map2)
        else:
            for item in m.outerwalls_map3:
                if item.block == "right" or item.block == "left":
                    self.vertical(item)
                else:
                    self.horizontal(item)
            self.positive_top(m.triangle1_map3.id, 1, 3)
            self.negative_top(m.triangle1_map3.id, 3, 5)
            self.negative_bottom(m.triangle1_map3.id, 1, 5)
            self.negative_top(m.triangle2_map3.id, 1, 3)
            self.positive_bottom(m.triangle2_map3.id, 3, 5)
            self.negative_bottom(m.triangle2_map3.id, 1, 5)
            self.touch_circle(m.circle1_map3)
            self.touch_circle(m.circle2_map3)
            for self.z in range(0, m.ramps_map3.__len__()):
                self.touch_speedup(m.ramps_map3[self.z])

        if time.time() - self.timer >= 0.01:
            if self.slope is not True:
                # deceleration algorithm
                speed = abs(math.pow(self.xspeed, 2) + math.pow(self.yspeed, 2))
                if speed >= 5:
                    self.xspeed *= 0.99
                    self.yspeed *= 0.99
                elif speed >= 4:
                    self.xspeed *= 0.98
                    self.yspeed *= 0.98
                elif speed > 3:
                    self.xspeed *= 0.975
                    self.yspeed *= 0.975
                elif speed > 2:
                    self.xspeed *= 0.972
                    self.yspeed *= 0.972
                else:
                    self.xspeed *= 0.97
                    self.yspeed *= 0.97

            self.moving = True

            if abs(self.xspeed) < 0.01 and abs(self.yspeed) < 0.01:
                self.timer = math.pow(10, 10)
                self.moving = False
                self.xspeed = 0
                self.yspeed = 0
            # move the ball
            canvas.move(self.id, self.xspeed, self.yspeed)
            # reset the timer
            self.timer = time.time()
            # update the x and y pos based on the speeds
            self.x += self.xspeed
            self.y += self.yspeed

    # deals with the case where the wall has a positive slope, and reflects off the bottom
    def positive_bottom(self, obj, y1, y2):
        pos = canvas.coords(obj)
        # obtain the slope and y-intercept of the wall. Note that the origin (0, 0) is at the bottom left
        self.m = (pos[y2] - pos[y1]) / (pos[y2 - 1] - pos[y1 - 1])
        self.b = 600 - (pos[y2] - self.m * pos[y2 - 1])
        self.m = -self.m
        # the slope angle is the angle from horizontal
        slope_angle = math.atan(abs(self.m))
        for i in range(-18, 18):
            # obtain the y coordinate of the ball (relative to the top)
            ycoor = self.y + 5 * math.sin(math.radians(10 * i))
            xcoor_wall = ((600 - ycoor) - self.b) / self.m
            xcoor = self.x + 5 * math.cos(math.radians(10 * i))
            # if the ball is to the left of the wall
            # check the x-coordinate and y-coordinate of the ball is in the range of the wall
            if -8 <= xcoor - xcoor_wall <= 0 and min(pos[y1], pos[y2]) <= self.y + 5 and max(pos[y1], pos[y2]) >= \
                    self.y - 5 and min(pos[y1 - 1], pos[y2 - 1]) <= self.x + 5 and max(pos[y1 - 1], pos[y2 - 1]) >= \
                    self.x - 5:
                if self.xspeed != 0:
                    self.angle_of_impact = math.atan(-self.yspeed / self.xspeed)
                else:
                    self.angle_of_impact = self.denominator(True)
                if self.xspeed > 0:
                    self.angle_of_impact -= math.pi
                halves = slope_angle - self.angle_of_impact
                # top half
                if 0 <= halves <= math.pi / 2:
                    if self.xspeed != 0:
                        angle = math.atan(abs(self.yspeed) / abs(self.xspeed))
                    else:
                        angle = self.denominator(True)
                    # moving up
                    if self.yspeed < 0:
                        self.angle_of_incidence = slope_angle + angle
                    else:
                        self.angle_of_incidence = slope_angle - angle
                    self.angle_of_reflection = math.pi + slope_angle + self.angle_of_incidence
                # bottom half
                else:
                    if self.xspeed != 0:
                        angle = math.atan(abs(self.xspeed) / abs(self.yspeed))
                    else:
                        angle = self.denominator(False)
                    # moving right
                    if self.xspeed > 0:
                        self.angle_of_incidence = math.pi / 2 - slope_angle - angle
                    else:
                        self.angle_of_incidence = math.pi / 2 - slope_angle + angle
                    self.angle_of_reflection = slope_angle - self.angle_of_incidence
                current_speed = math.sqrt(math.pow(abs(self.xspeed), 2) + math.pow(abs(self.yspeed), 2))
                self.xspeed = current_speed * math.cos(self.angle_of_reflection)
                self.yspeed = -current_speed * math.sin(self.angle_of_reflection)
                return

    # deals with the case where the ball has a positive slope, and reflects off the top
    def positive_top(self, obj, y1, y2):
        pos = canvas.coords(obj)
        self.m = (pos[y2] - pos[y1]) / (pos[y2 - 1] - pos[y1 - 1])
        self.b = 600 - (pos[y2] - self.m * pos[y2 - 1])
        self.m = -self.m
        slope_angle = math.atan(abs(self.m))
        for i in range(-18, 18):
            ycoor = self.y + 5 * math.sin(math.radians(10 * i))
            xcoor_wall = ((600 - ycoor) - self.b) / self.m
            xcoor = self.x + 5 * math.cos(math.radians(10 * i))
            if 0 <= xcoor - xcoor_wall <= 8 and min(pos[y1], pos[y2]) <= self.y + 5 and max(pos[y1], pos[y2]) >= \
                    self.y - 5 and min(pos[y1 - 1], pos[y2 - 1]) <= self.x + 5 and max(pos[y1 - 1], pos[y2 - 1]) >= \
                    self.x - 5:
                if self.xspeed != 0:
                    self.angle_of_impact = math.atan(-self.yspeed / self.xspeed)
                else:
                    self.angle_of_impact = self.denominator(True)
                if self.xspeed > 0:
                    self.angle_of_impact += math.pi
                halves = math.pi + slope_angle - self.angle_of_impact
                # bottom half
                if 0 <= halves <= math.pi / 2:
                    if self.xspeed != 0:
                        angle = math.atan(abs(self.yspeed) / abs(self.xspeed))
                    else:
                        angle = self.denominator(True)
                    # moving down
                    if self.yspeed > 0:
                        self.angle_of_incidence = slope_angle + angle
                    else:
                        self.angle_of_incidence = slope_angle - angle
                    self.angle_of_reflection = slope_angle + self.angle_of_incidence
                # top half
                else:
                    if self.xspeed != 0:
                        angle = math.atan(abs(self.xspeed) / abs(self.yspeed))
                    else:
                        angle = self.denominator(False)
                    # moving left
                    if self.xspeed < 0:
                        self.angle_of_incidence = math.pi / 2 - slope_angle - angle
                    else:
                        self.angle_of_incidence = math.pi / 2 - slope_angle + angle
                    self.angle_of_reflection = math.pi + slope_angle - self.angle_of_incidence
                current_speed = math.sqrt(math.pow(abs(self.xspeed), 2) + math.pow(abs(self.yspeed), 2))
                self.xspeed = current_speed * math.cos(self.angle_of_reflection)
                self.yspeed = -current_speed * math.sin(self.angle_of_reflection)
                return

    # deals with the case where the ball has a negative slope, and reflects off the bottom
    def negative_bottom(self, obj, y1, y2):
        pos = canvas.coords(obj)
        self.m = (pos[y2] - pos[y1]) / (pos[y2 - 1] - pos[y1 - 1])
        self.b = 600 - (pos[y2] - self.m * pos[y2 - 1])
        self.m = -self.m
        # the slope angle is the angle that the wall makes with the horizontal (going left b/c of absolute value)
        slope_angle = math.atan(abs(self.m))
        for i in range(-18, 18):
            ycoor = self.y + 5 * math.sin(math.radians(10 * i))
            xcoor_wall = ((600 - ycoor) - self.b) / self.m
            xcoor = self.x + 5 * math.cos(math.radians(10 * i))
            if 0 <= xcoor - xcoor_wall <= 8 and min(pos[y1], pos[y2]) <= self.y + 5 and max(pos[y1], pos[y2]) >= \
                    self.y - 5 and min(pos[y1 - 1], pos[y2 - 1]) <= self.x + 5 and max(pos[y1 - 1], pos[y2 - 1]) >= \
                    self.x - 5:
                if self.xspeed != 0:
                    self.angle_of_impact = math.atan(-self.yspeed / self.xspeed)
                else:
                    self.angle_of_impact = self.denominator(True)
                if self.xspeed > 0:
                    self.angle_of_impact += math.pi
                else:
                    self.angle_of_impact += 2 * math.pi
                halves = 2 * math.pi - slope_angle - self.angle_of_impact
                # bottom half
                if 0 <= halves <= math.pi / 2:
                    if self.xspeed != 0:
                        angle = math.atan(abs(self.xspeed) / abs(self.yspeed))
                    else:
                        angle = self.denominator(False)
                    # moving right
                    if self.xspeed > 0:
                        self.angle_of_incidence = math.pi / 2 - slope_angle + angle
                    else:
                        self.angle_of_incidence = math.pi / 2 - slope_angle - angle
                    self.angle_of_reflection = math.pi - slope_angle + self.angle_of_incidence
                # top half
                else:
                    if self.xspeed != 0:
                        angle = math.atan(abs(self.yspeed) / abs(self.xspeed))
                    else:
                        angle = self.denominator(True)
                    # moving down
                    if self.yspeed > 0:
                        self.angle_of_incidence = slope_angle - angle
                    else:
                        self.angle_of_incidence = slope_angle + angle
                    self.angle_of_reflection = 2 * math.pi - slope_angle - self.angle_of_incidence
                current_speed = math.sqrt(math.pow(abs(self.xspeed), 2) + math.pow(abs(self.yspeed), 2))
                self.xspeed = current_speed * math.cos(self.angle_of_reflection)
                self.yspeed = -current_speed * math.sin(self.angle_of_reflection)
                return

    # deals with the case where the ball has a negative slope, and reflects off the top
    def negative_top(self, obj, y1, y2):
        pos = canvas.coords(obj)
        self.m = (pos[y2] - pos[y1]) / (pos[y2 - 1] - pos[y1 - 1])
        self.b = 600 - (pos[y2] - self.m * pos[y2 - 1])
        self.m = -self.m
        # the slope angle is the angle that the wall makes with the horizontal (going left b/c of absolute value)
        slope_angle = math.atan(abs(self.m))
        for i in range(-18, 18):
            ycoor = self.y + 5 * math.sin(math.radians(10 * i))
            xcoor_wall = ((600 - ycoor) - self.b) / self.m
            xcoor = self.x + 5 * math.cos(math.radians(10 * i))
            if -8 <= xcoor - xcoor_wall <= 0 and min(pos[y1], pos[y2]) <= self.y + 5 and max(pos[y1], pos[y2]) >= \
                    self.y - 5 and min(pos[y1 - 1], pos[y2 - 1]) <= self.x + 5 and max(pos[y1 - 1], pos[y2 - 1]) >= \
                    self.x - 5:
                if self.xspeed != 0:
                    self.angle_of_impact = math.atan(-self.yspeed / self.xspeed)
                else:
                    self.angle_of_impact = self.denominator(True)
                if self.xspeed > 0:
                    self.angle_of_impact += math.pi
                halves = math.pi - slope_angle - self.angle_of_impact
                # top half
                if 0 <= halves <= math.pi / 2:
                    if self.xspeed != 0:
                        angle = math.atan(abs(self.xspeed) / abs(self.yspeed))
                    else:
                        angle = self.denominator(False)
                    # moving right
                    if self.xspeed > 0:
                        self.angle_of_incidence = math.pi / 2 - slope_angle - angle
                    else:
                        self.angle_of_incidence = math.pi / 2 - slope_angle + angle
                    self.angle_of_reflection = -slope_angle + self.angle_of_incidence
                # bottom half
                else:
                    if self.xspeed != 0:
                        angle = math.atan(abs(self.yspeed) / abs(self.xspeed))
                    else:
                        angle = self.denominator(True)
                    # moving down
                    if self.yspeed > 0:
                        self.angle_of_incidence = slope_angle + angle
                    else:
                        self.angle_of_incidence = slope_angle - angle
                    self.angle_of_reflection = math.pi - slope_angle - self.angle_of_incidence
                current_speed = math.sqrt(math.pow(abs(self.xspeed), 2) + math.pow(abs(self.yspeed), 2))
                self.xspeed = current_speed * math.cos(self.angle_of_reflection)
                self.yspeed = -current_speed * math.sin(self.angle_of_reflection)
                return

    # deals with the case where the denominator is 0
    def denominator(self, x):
        if x is True:
            if self.yspeed > 0:
                return 3 * math.pi / 2
            else:
                return math.pi / 2
        else:
            if self.xspeed > 0:
                return 0
            else:
                return math.pi

    # deals with the case where the ball hits a horizontal wall
    def horizontal(self, obj):
        pos = canvas.coords(obj.id)
        if (obj.block == "down" and -6 <= (self.y - 5) - pos[3] <= 0) or (obj.block == "up" and 0 <= (self.y + 5) -
                                                                          pos[1] <= 6):
            if min(pos[0], pos[2]) <= self.x <= max(pos[0], pos[2]):
                self.yspeed = -self.yspeed

    # deals with the case where the ball hits a vertical wall
    def vertical(self, obj):
        pos = canvas.coords(obj.id)
        if (obj.block == "right" and -6 <= (self.x - 5) - pos[2] <= 0) or (
                obj.block == "left" and 0 <= (self.x + 5) -
                pos[0] <= 6):
            if min(pos[1], pos[3]) <= self.y <= max(pos[1], pos[3]):
                self.xspeed = -self.xspeed

    def touch_circle(self, obj):
        pos = canvas.coords(obj.id)
        # the algorithm for determining if two circles touch works as follows
        # first, determine the centres of both circles
        # check that the distance between the centres if less than (overlapping) or equal (tangent) to the sum of the
        # radii
        centrex = (pos[0] + pos[2]) / 2
        centrey = (pos[1] + pos[3]) / 2
        distance = math.sqrt(math.pow(centrex - self.x, 2) + math.pow(centrey - self.y, 2))
        if distance <= 5 + obj.radius:
            # we calculate the angle created by the line between the point of impact and the centre of the circle
            # we then add 90 degrees to obtain the angle of the tangent line
            # then, the calculations are the same as the line calculations
            slope_angle = math.atan(abs((self.x - centrex) / (self.y - centrey)))
            # positive bottom = bottom right
            if self.x > centrex and self.y > centrey:
                self.angle_of_impact = math.atan(-self.yspeed / self.xspeed)
                if self.xspeed > 0:
                    self.angle_of_impact -= math.pi
                halves = slope_angle - self.angle_of_impact
                # top half
                if 0 <= halves <= math.pi / 2:
                    angle = math.atan(abs(self.yspeed) / abs(self.xspeed))
                    # moving down
                    if self.yspeed < 0:
                        self.angle_of_incidence = slope_angle + angle
                    else:
                        self.angle_of_incidence = slope_angle - angle
                    self.angle_of_reflection = math.pi + slope_angle + self.angle_of_incidence
                # bottom half
                else:
                    angle = math.atan(abs(self.xspeed) / abs(self.yspeed))
                    # moving right
                    if self.xspeed > 0:
                        self.angle_of_incidence = math.pi / 2 - slope_angle - angle
                    else:
                        self.angle_of_incidence = math.pi / 2 - slope_angle + angle
                    self.angle_of_reflection = slope_angle - self.angle_of_incidence
            # positive top = top left
            elif self.x < centrex and self.y < centrey:
                self.angle_of_impact = math.atan(-self.yspeed / self.xspeed)
                if self.xspeed > 0:
                    self.angle_of_impact += math.pi
                halves = math.pi + slope_angle - self.angle_of_impact
                # bottom half
                if 0 <= halves <= math.pi / 2:
                    angle = math.atan(abs(self.yspeed) / abs(self.xspeed))
                    # moving down
                    if self.yspeed > 0:
                        self.angle_of_incidence = slope_angle + angle
                    else:
                        self.angle_of_incidence = slope_angle - angle
                    self.angle_of_reflection = slope_angle + self.angle_of_incidence
                # top half
                else:
                    angle = math.atan(abs(self.xspeed) / abs(self.yspeed))
                    # moving left
                    if self.xspeed < 0:
                        self.angle_of_incidence = math.pi / 2 - slope_angle - angle
                    else:
                        self.angle_of_incidence = math.pi / 2 - slope_angle + angle
                    self.angle_of_reflection = math.pi + slope_angle - self.angle_of_incidence
            # negative bottom = bottom left
            elif self.x < centrex and self.y > centrey:
                self.angle_of_impact = math.atan(-self.yspeed / self.xspeed)
                if self.xspeed > 0:
                    self.angle_of_impact += math.pi
                else:
                    self.angle_of_impact += 2 * math.pi
                halves = 2 * math.pi - slope_angle - self.angle_of_impact
                # bottom half
                if 0 <= halves <= math.pi / 2:
                    angle = math.atan(abs(self.xspeed) / abs(self.yspeed))
                    # moving right
                    if self.xspeed > 0:
                        self.angle_of_incidence = math.pi / 2 - slope_angle - angle
                    else:
                        self.angle_of_incidence = math.pi / 2 - slope_angle + angle
                    self.angle_of_reflection = math.pi - slope_angle + self.angle_of_incidence
                # top half
                else:
                    angle = math.atan(abs(self.yspeed) / abs(self.xspeed))
                    # moving down
                    if self.yspeed > 0:
                        self.angle_of_incidence = slope_angle - angle
                    else:
                        self.angle_of_incidence = slope_angle + angle
                    self.angle_of_reflection = 2 * math.pi - slope_angle - self.angle_of_incidence
            # negative top = top right
            else:
                self.angle_of_impact = math.atan(-self.yspeed / self.xspeed)
                if self.xspeed > 0:
                    self.angle_of_impact += math.pi
                halves = math.pi - slope_angle - self.angle_of_impact
                # top half
                if 0 <= halves <= math.pi / 2:
                    angle = math.atan(abs(self.xspeed) / abs(self.yspeed))
                    # moving right
                    if self.xspeed > 0:
                        self.angle_of_incidence = math.pi / 2 - slope_angle - angle
                    else:
                        self.angle_of_incidence = math.pi / 2 - slope_angle + angle
                    self.angle_of_reflection = -slope_angle + self.angle_of_incidence
                # bottom half
                else:
                    angle = math.atan(abs(self.yspeed) / abs(self.xspeed))
                    # moving down
                    if self.yspeed > 0:
                        self.angle_of_incidence = slope_angle + angle
                    else:
                        self.angle_of_incidence = slope_angle - angle
                    self.angle_of_reflection = math.pi - slope_angle - self.angle_of_incidence
            current_speed = math.sqrt(math.pow(abs(self.xspeed), 2) + math.pow(abs(self.yspeed), 2))
            if obj.speed_up is True:
                current_speed = 5
            self.xspeed = current_speed * math.cos(self.angle_of_reflection)
            self.yspeed = -current_speed * math.sin(self.angle_of_reflection)
            return

    def touch_speedup(self, obj):
        pos = canvas.coords(obj.id)
        if self.x + 5 >= pos[0] and self.x - 5 <= pos[2] and self.y + 5 >= pos[1] and self.y - 5 <= pos[3]:
            self.slope = True
            if obj.direction == "down":
                if self.yspeed <= 5.95:
                    self.yspeed += 0.05
            elif obj.direction == "up":
                if self.yspeed >= -5.95:
                    self.yspeed -= 0.05
            elif obj.direction == "right":
                if self.xspeed <= 5.95:
                    self.xspeed += 0.05
            else:
                if self.xspeed >= -5.95:
                    self.xspeed -= 0.05
            self.z_var = self.z
        elif self.z == self.z_var:
            self.slope = False

    def touch_water(self):
        if g.game == "game2":
            pos = canvas.coords(m.water_map2.id)
            if pos[0] <= self.x <= pos[2] and pos[1] <= self.y <= pos[3] and self.water_boolean is False:
                self.water_timer = time.time()
                canvas.itemconfig(self.id, state="hidden")
                self.water_boolean = True
                self.timer = math.pow(10, 10)

            if time.time() - self.water_timer >= 1:
                canvas.itemconfig(self.id, state="normal")
                g.turn += 2
                g.total_turn += 2
                canvas.move(self.id, self.tempx - self.x, self.tempy - self.y)
                self.x = self.tempx
                self.y = self.tempy
                self.water_timer = math.pow(10, 10)
                self.water_boolean = False
                self.moving = False
        elif g.game == "game3":
            for item in m.rivers_map3:
                pos = canvas.coords(item.id)
                if pos[0] <= self.x <= pos[2] and pos[1] <= self.y <= pos[3] and self.water_boolean is False:
                    self.water_timer = time.time()
                    canvas.itemconfig(self.id, state="hidden")
                    self.water_boolean = True
                    self.timer = math.pow(10, 10)

                if time.time() - self.water_timer >= 1:
                    canvas.itemconfig(self.id, state="normal")
                    g.turn += 2
                    g.total_turn += 2
                    canvas.move(self.id, self.tempx - self.x, self.tempy - self.y)
                    self.x = self.tempx
                    self.y = self.tempy
                    self.water_timer = math.pow(10, 10)
                    self.water_boolean = False
                    self.moving = False

    def touch_hole(self):
        if g.game == "game1":
            pos_hole = canvas.coords(m.hole_map1.id)
        elif g.game == "game2":
            pos_hole = canvas.coords(m.hole_map2.id)
        else:
            pos_hole = canvas.coords(m.hole_map3.id)
        centrex = (pos_hole[0] + pos_hole[2]) / 2
        centrey = (pos_hole[1] + pos_hole[3]) / 2
        if 0 <= abs(centrex - self.x) <= 7.5 and 0 <= abs(centrey - self.y) <= 7.5:
            if self.win_boolean is False:
                self.ticks = 1
                canvas.move(self.id, (centrex - self.x) / 20, (centrey - self.y) / 20)
                self.win_boolean = True
                self.win_timer = time.time()
            if time.time() - self.win_timer >= 0.01 and self.ticks < 20:
                canvas.move(self.id, (centrex - self.x) / 20, (centrey - self.y) / 20)
                self.win_timer = time.time()
                self.ticks += 1
            if time.time() - self.win_timer >= 0.5 and self.ticks == 20 and self.win_boolean2 is False:
                self.win_background = canvas.create_rectangle(-5, -5, 555, 605, fill="white")
                if g.game == "game1":
                    if g.turn == 1:
                        self.text = "Hole in One!"
                    elif g.turn == 2:
                        self.text = "Birdie!"
                    elif g.turn == 3:
                        self.text = "Par"
                    elif g.turn == 4:
                        self.text = "Bogey"
                    elif g.turn == 5:
                        self.text = "Double Bogey"
                    elif g.turn == 6:
                        self.text = "Triple Bogey"
                    else:
                        self.text = f'+{g.turn - 3}'
                elif g.game == "game2":
                    if g.turn == 1:
                        self.text = "Hole in One!"
                    elif g.turn == 2:
                        self.text = "Eagle!"
                    elif g.turn == 3:
                        self.text = "Birdie!"
                    elif g.turn == 4:
                        self.text = "Par"
                    elif g.turn == 5:
                        self.text = "Bogey"
                    elif g.turn == 6:
                        self.text = "Double Bogey"
                    elif g.turn == 7:
                        self.text = "Triple Bogey"
                    else:
                        self.text = f'+{g.turn - 4}'
                else:
                    if g.turn == 1:
                        self.text = "Hole in One!"
                    elif 2 <= g.turn <= 3:
                        self.text = f'+{g.turn - 6}'
                    elif g.turn == 4:
                        self.text = "Eagle!"
                    elif g.turn == 5:
                        self.text = "Birdie!"
                    elif g.turn == 6:
                        self.text = "Par"
                    elif g.turn == 7:
                        self.text = "Bogey"
                    elif g.turn == 8:
                        self.text = "Double Bogey"
                    elif g.turn == 9:
                        self.text = "Triple Bogey"
                    else:
                        self.text = f'+{g.turn - 6}'
                self.win_text = canvas.create_text(275, 300, font=("Gotham", 30), text=self.text)
                self.win_boolean2 = True
                self.win_timer2 = time.time()

            if time.time() - self.win_timer2 >= 3:
                if g.game == "game1":
                    # delete game 1
                    g.game = "game2"
                    canvas.delete(self.win_text)
                    canvas.delete(self.win_background)
                    for item in m.greens_map1:
                        canvas.delete(item.id)
                    for item in m.outerwalls_map1:
                        canvas.delete(item.id)
                    canvas.delete(m.circle_map1)
                    canvas.delete(m.triangle1_map1)
                    canvas.delete(m.triangle2_map1)
                    canvas.delete(m.hole_map1.id)
                    canvas.delete(m.ball_map1.id)
                    self.timer = math.pow(10, 10)
                    self.water_timer = math.pow(10, 10)
                    self.water_boolean = False
                    self.win_timer = math.pow(10, 10)
                    self.win_timer2 = math.pow(10, 10)
                    self.win_boolean = False
                    self.win_boolean2 = False
                    m.bool = False
                    g.turn = 0
                elif g.game == "game2":
                    # delete game 2
                    g.game = "game3"
                    canvas.delete(self.win_text)
                    canvas.delete(self.win_background)
                    for item in m.greens_map2:
                        canvas.delete(item.id)
                    for item in m.outerwalls_map2:
                        canvas.delete(item.id)
                    canvas.delete(m.circle_map2.id)
                    canvas.delete(m.arrows_image)
                    for item in m.polygons_map2:
                        canvas.delete(item.id)
                    canvas.delete(m.ramp_map2.id)
                    canvas.delete(m.triangle_map2)
                    canvas.delete(m.hole_map2.id)
                    canvas.delete(m.water_map2.id)
                    canvas.delete(m.ball_map2.id)
                    canvas.delete(m.ball_map2)
                    self.timer = math.pow(10, 10)
                    self.water_timer = math.pow(10, 10)
                    self.water_boolean = False
                    self.win_timer = math.pow(10, 10)
                    self.win_timer2 = math.pow(10, 10)
                    self.win_boolean = False
                    self.win_boolean2 = False
                    m.bool = False
                    g.turn = 0
                else:
                    if self.win_boolean3 is False:
                        self.win_background = canvas.create_rectangle(-5, -5, 555, 605, fill="white")
                        if g.total_turn > 13:
                            text = "+"
                        else:
                            text = ""
                        self.win_text = canvas.create_text(275, 275, font=("Gotham", 30), text=f'Total Score: {text}{g.total_turn - 13}')
                        # obtain the array of highscores
                        highscore = pickle.load(open("/Users/SamRoo/PycharmProjects/OOPPractice/Minigolf/Minigolf High "
                                                     "Scores", "rb"))
                        # append the current score
                        highscore.append(g.total_turn - 13)
                        # store the file as a variable
                        file = open("/Users/SamRoo/PycharmProjects/OOPPractice/Minigolf/Minigolf High Scores", "wb")
                        # place high score in the file
                        pickle.dump(sorted(highscore), file)
                        position = sorted(highscore).index(g.total_turn - 13) + 1
                        canvas.create_text(275, 325, font=("Gotham", 30), text=f'All-Time Position: {position}')
                        self.win_boolean3 = True
                        file.close()

                        self.restart_timer = time.time()

        if time.time() - self.restart_timer > 5:
            # restart the game
            canvas.create_rectangle(-5, -5, 555, 605, fill="#B9BFA5", outline="#B9BFA5")
            global h
            h = Homescreen()
            g.game = "homescreen"
            m.bool = False
            g.turn = 0
            g.total_turn = 0


class Turn:
    def __init__(self):
        self.text = canvas.create_text(275, 14, font=("Gotham", 15), text="Stroke: " + str(g.turn),
                                       fill="white")

# turn object is created when the user presses "play"


bool = False


wave_obj = sa.WaveObject.from_wave_file('/Users/SamRoo/PycharmProjects/OOPPractice/Minigolf/Minigolf Music.wav')
wave_obj.play()


while True:
    canvas.update()
    canvas.update_idletasks()
    time.sleep(0.01)
    m.game()
    if g.game != "homescreen":
        b = ""
        if g.game == "game1":
            b = m.ball_map1
        elif g.game == "game2":
            b = m.ball_map2
        else:
            b = m.ball_map3
        # function shows the trajectory of the ball
        # when the mouse is clicked, this function begins
        # when the mouse is released, the release function is called, which stops the pull function
        if b.is_clicked is True:
            b.measure()
        if b.win_boolean is False:
            b.ball_movement()
        b.touch_water()
        b.touch_hole()
        canvas.itemconfig(t.text, text=f'Stroke: {g.turn}')