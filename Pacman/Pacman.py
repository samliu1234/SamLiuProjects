import tkinter as tk
from tkinter import *
import time
import math
import random
import simpleaudio as sa
import pickle

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=640, bg="#181818")
canvas.pack()


# reset function
def reset():
    pickle.dump(0, open("High Scores", "wb"))


# tile class
class Tile:
    def __init__(self, x1, y1, x2, y2):
        self.tile = canvas.create_rectangle(x1, y1, x2, y2, fill="#282828", outline="#282828")


# creates tiles when x and y are even
for x in range(0, 15):
    for y in range(0, 15):
        if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
            Tile(x * 40, y * 40, x * 40 + 40, y * 40 + 40)


# wall class
class Wall:
    def __init__(self, x1, y1, x2, y2):
        self.wall = canvas.create_rectangle(x1, y1, x2, y2, fill="#000080", outline="#000080")


# side walls
TopWall = Wall(15, 15, 585, 25)
LeftWall = Wall(15, 15, 25, 585)
BotWall = Wall(15, 575, 585, 585)
RightWall = Wall(575, 15, 585, 585)

# non-side walls
Wall1 = Wall(95, 25, 105, 105)
Wall2 = Wall(495, 25, 505, 105)
Wall3 = Wall(175, 95, 425, 105)
Wall4 = Wall(95, 495, 105, 585)
Wall5 = Wall(495, 495, 505, 585)
Wall6 = Wall(175, 495, 425, 505)
Wall7 = Wall(95, 175, 105, 265)
Wall8 = Wall(95, 335, 105, 425)
Wall9 = Wall(95, 175, 265, 185)
Wall10 = Wall(95, 415, 265, 425)
Wall11 = Wall(335, 175, 505, 185)
Wall12 = Wall(495, 175, 505, 265)
Wall13 = Wall(335, 415, 505, 425)
Wall14 = Wall(495, 335, 505, 425)
Wall15 = Wall(175, 255, 185, 345)
Wall16 = Wall(415, 255, 425, 345)
Wall17 = Wall(175, 335, 425, 345)
Wall18 = Wall(175, 255, 425, 265)

# place all the walls into a list to be accessed later
walls = [Wall1, Wall2, Wall3, Wall4, Wall5, Wall6, Wall7, Wall8, Wall9, Wall10, Wall11, Wall12, Wall13, Wall14, Wall15,
         Wall16, Wall17, Wall18]


# coin class
class Coin:
    def __init__(self, x1, y1, x2, y2):
        self.coin = canvas.create_oval(x1, y1, x2, y2, fill="yellow", outline="yellow")
        self.coords = [x1, y1, x2, y2]


# coin dictionary to store coin objects
coins = {
}

# individual coins
for x in range(1, 7):
    coins[x] = Coin(55, 15 + 40 * x, 65, 25 + 40 * x)
for x in range(7, 13):
    coins[x] = Coin(55, 15 + 40 * (x + 1), 65, 25 + 40 * (x + 1))
for x in range(13, 19):
    coins[x] = Coin(535, 15 + 40 * (x - 12), 545, 25 + 40 * (x - 12))
for x in range(19, 25):
    coins[x] = Coin(535, 15 + 40 * (x - 11), 545, 25 + 40 * (x - 11))
for x in range(25, 34):
    coins[x] = Coin(95 + 40 * (x - 24), 535, 105 + 40 * (x - 24), 545)
for x in range(34, 38):
    coins[x] = Coin(95 + 40 * (x - 33), 55, 105 + 40 * (x - 33), 65)
for x in range(39, 43):
    coins[x] = Coin(95 + 40 * (x - 33), 55, 105 + 40 * (x - 33), 65)
for x in range(43, 54):
    coins[x] = Coin(55 + 40 * (x - 43), 135, 65 + 40 * (x - 43), 145)
for x in range(54, 65):
    coins[x] = Coin(55 + 40 * (x - 53), 455, 65 + 40 * (x - 53), 465)
for x in range(65, 74):
    coins[x] = Coin(95 + 40 * (x - 64), 215, 105 + 40 * (x - 64), 225)
for x in range(74, 83):
    coins[x] = Coin(95 + 40 * (x - 73), 375, 105 + 40 * (x - 73), 385)
for x in range(83, 86):
    coins[x] = Coin(135, 215 + 40 * (x - 82), 145, 225 + 40 * (x - 82))
for x in range(86, 89):
    coins[x] = Coin(455, 215 + 40 * (x - 85), 465, 225 + 40 * (x - 85))
coins[89] = Coin(135, 95, 145, 105)
coins[90] = Coin(455, 95, 465, 105)
coins[91] = Coin(135, 495, 145, 505)
coins[92] = Coin(455, 495, 465, 505)
coins[93] = Coin(295, 175, 305, 185)
coins[94] = Coin(295, 415, 305, 425)
coins[95] = Coin(95, 295, 105, 305)
coins[96] = Coin(495, 295, 505, 305)
coins[97] = Coin(495, 135, 505, 145)


# powerup class
class Powerup():
    def __init__(self, x1, y1, x2, y2):
        self.powerup = canvas.create_oval(x1, y1, x2, y2, fill="red", outline="red")
        self.coords = [x1, y1, x2, y2]


# two individual powerups
Powerup1 = Powerup(55, 295, 65, 305)
Powerup2 = Powerup(535, 295, 545, 305)

# load individual powerups into a list
powerups = [Powerup1, Powerup2]


# cherry class
class Cherry:
    def __init__(self):
        self.image = PhotoImage(file="/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/cherry.gif")
        self.cherry = canvas.create_image(285, 45, image=self.image, anchor=NW)
        self.exists = True


# create cherry object
Cherry = Cherry()


# pacman class
class Pacman:
    def __init__(self):
        # import right, left, up, down, and closed images of pacman, ready to be used
        self.image_right = PhotoImage(file="/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/right.gif")
        self.image_left = PhotoImage(file="/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/left.gif")
        self.image_up = PhotoImage(file="/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/up.gif")
        self.image_down = PhotoImage(file="/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/down.gif")
        self.image_closed = PhotoImage(file="/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/closed.gif")
        # initialize pacman to face right
        self.pacman = canvas.create_image(280, 360, image=self.image_right, anchor=NW)
        # determines if pacman can move left, right, up, or down
        # initially, pacman is allowed to move in any direction
        self.can_left = True
        self.can_right = True
        self.can_up = True
        self.can_down = True
        # timer that controls pacman opening and closing its mouth
        self.timer = time.time()
        # timer for the cherry
        self.cherry_timer = time.time()
        # list of deleted coins, so the coins are eliminated from the code once obtained
        self.deleted = []
        # variable indicating whether pacman's mouth is currently opened or closed, initialized to be closed
        self.is_closed = False
        # indicates pacman's current direction
        # allows program to know which direction to set pacman to be facing once mouth opens again
        self.direction = "right"
        # boolean controlling music
        # dictionary converting the direction to the corresponding image
        self.directions = {
            "right": self.image_right,
            "left": self.image_left,
            "up": self.image_up,
            "down": self.image_down
        }
        # boolean indicating whether cherry's bonus is activated
        self.bonus = False
        # if the user goes on the cherry, a point should only be added once, create boolean to ensure that
        self.has_added = False
        # list storing deleted powerups once they're used
        self.deletedpowerups = []
        # binds keys to movement
        canvas.bind_all("<KeyPress-Left>", self.move_left)
        canvas.bind_all("<KeyPress-Right>", self.move_right)
        canvas.bind_all("<KeyPress-Up>", self.move_up)
        canvas.bind_all("<KeyPress-Down>", self.move_down)

    # method that's always running
    def always_run(self):
        # if the cherry bonus is active
        if time.time() - self.cherry_timer <= 10 and self.bonus is True:
            self.bonus = True
        else:
            self.bonus = False

    # method controlling pacman switching from open to close
    def switch_pacman(self):
        # if pacman's mouth is not closed
        if self.is_closed is False:
            if time.time() - self.timer >= 0.15:
                self.is_closed = True
                canvas.itemconfig(self.pacman, image=self.image_closed)
                self.timer = time.time()
        # if pacman's mouth is closed
        else:
            if time.time() - self.timer >= 0.15:
                self.is_closed = False
                canvas.itemconfig(self.pacman, image=self.directions[self.direction])
                self.timer = time.time()

    # move left if allowed
    def move_left(self, event):
        if self.can_left is True:
            canvas.move(self.pacman, -10, 0)
            self.direction = "left"

    # move right if allowed
    def move_right(self, event):
        if self.can_right is True:
            canvas.move(self.pacman, 10, 0)
            self.direction = "right"

    # move up if allowed
    def move_up(self, event):
        if self.can_up is True:
            canvas.move(self.pacman, 0, -10)
            self.direction = "up"

    # move down if allowed
    def move_down(self, event):
        if self.can_down is True:
            canvas.move(self.pacman, 0, 10)
            self.direction = "down"

    # if a wall is below pacman
    def touch_down(self):
        # coordinates of pacman
        pos = canvas.coords(self.pacman)
        pos_right = pos[0] + 50
        pos_down = pos[1] + 50
        # check every wall
        for x in range(0, 18):
            # coordinates of the specific wall being checked
            posx = canvas.coords(walls[x].wall)
            # non-border walls
            if pos_right >= posx[0] and pos[0] <= posx[2] and 0 <= pos_down - posx[1] <= 5:
                self.can_down = False
                break
            # lower border wall
            if pos_down >= 575:
                self.can_down = False
                break
            # if self.can_down is true after the for loop, that means it didn't break
            # This confirms that pacman can move
            self.can_down = True

    # if a wall is above pacman
    def touch_up(self):
        pos = canvas.coords(self.pacman)
        pos_right = pos[0] + 50
        for x in range(0, 18):
            posx = canvas.coords(walls[x].wall)
            if pos_right >= posx[0] and pos[0] <= posx[2] and 0 <= posx[3] - pos[1] <= 5:
                self.can_up = False
                return
            if pos[1] <= 25:
                self.can_up = False
                return
            self.can_up = True

    # if a wall is to the left of pacman
    def touch_left(self):
        pos = canvas.coords(self.pacman)
        pos_down = pos[1] + 50
        for x in range(0, 18):
            posx = canvas.coords(walls[x].wall)
            if pos_down >= posx[1] and pos[1] <= posx[3] and 0 <= posx[2] - pos[0] <= 5:
                self.can_left = False
                return
            if pos[0] <= 25:
                self.can_left = False
                return
            self.can_left = True

    # if a wall is to the right of pacman
    def touch_right(self):
        pos = canvas.coords(self.pacman)
        pos_down = pos[1] + 50
        pos_right = pos[0] + 50
        for x in range(0, 18):
            posx = canvas.coords(walls[x].wall)
            if pos_down >= posx[1] and pos[1] <= posx[3] and 0 <= pos_right - posx[0] <= 5:
                self.can_right = False
                return
            if pos_right >= 575:
                self.can_right = False
                return
            self.can_right = True

    # if pacman touches a coin
    def touch_coin(self):
        # coordinates of pacman
        pos = canvas.coords(self.pacman)
        # x and y centres of pacman
        pos_centre_x = pos[0] + 25
        pos_centre_y = pos[1] + 25
        # goes through all 98 coins
        for x in range(1, 98):
            # if coin isn't already deleted
            if not self.deleted.__contains__(x):
                if x != 38:
                    # coordinates of coin
                    pos_coin = coins[x].coords
                    # if the pacman touches the coin, delete the coin and append it to the deleted list
                    if pos_coin[0] - 25 <= pos_centre_x <= pos_coin[2] + 25:
                        if pos_coin[1] - 25 <= pos_centre_y <= pos_coin[3] + 25:
                            canvas.delete(coins[x].coin)
                            self.deleted.append(x)
                            # if the cherry bonus is active, add 2 to the score
                            if self.bonus is True:
                                Score.score += 3
                            # otherwise, add 1
                            else:
                                Score.score += 1

    # if pacman touches a powerup
    def touch_powerup(self):
        # coordinates of pacman
        pos = canvas.coords(self.pacman)
        # x and y centres
        pos_centre_x = pos[0] + 25
        pos_centre_y = pos[1] + 25
        # goes through both powerups
        for x in range(0, 2):
            # if the powerup hasn't been used already
            if not self.deletedpowerups.__contains__(x):
                # coordinates of powerup
                pos_powerup = powerups[x].coords
                # if pacman touches the powerup, delete the powerup and append to the deleted list
                # also, set the scared properties to be true
                if pos_powerup[0] - 25 <= pos_centre_x <= pos_powerup[2] + 25:
                    if pos_powerup[1] - 25 <= pos_centre_y <= pos_powerup[3] + 25:
                        canvas.delete(powerups[x].powerup)
                        self.deletedpowerups.append(x)
                        blue_ghost.is_scared = True
                        pink_ghost.is_scared = True
                        # if the cherry bonus is active, add 2 to the score
                        if self.bonus is True:
                            Score.score += 3
                        # otherwise, add 1
                        else:
                            Score.score += 1

    # if pacman touches the cherry
    def touch_cherry(self):
        # if the cherry exists
        if Cherry.exists is True:
            # coordinates of cherry
            pos_cherry = canvas.coords(Cherry.cherry)
            posx_cherry = pos_cherry[0] + 25
            posy_cherry = pos_cherry[1] + 25
            # coordinates of pacman
            pos = canvas.coords(self.pacman)
            posx_pacman = pos[0] + 25
            posy_pacman = pos[1] + 25
            # if pacman touches the powerup
            if posx_cherry - 25 <= posx_pacman <= posx_cherry + 25:
                if posy_cherry - 25 <= posy_pacman <= posy_cherry + 25:
                    # add point if a point hasn't already been aded
                    if self.has_added is False:
                        Score.score += 1
                        self.has_added = True
                    self.bonus = True
                    canvas.delete(Cherry.cherry)
                    Cherry.exists = False
                    # start timer
                    self.cherry_timer = time.time()

    # checks win condition
    def win_con(self):
        # if all 97 coins have been deleted (eaten)
        if self.deleted.__len__() == 96:
            canvas.create_rectangle(0, 0, 600, 600, fill="white", outline="white")
            canvas.create_text(300, 300, font=("Comic Sans MS", 30), text="You've won!")


# create pacman object
Pacman = Pacman()


# ghost class
class Ghost:
    def __init__(self, xpos, ypos, image, od):
        # import images so they're ready to be used
        self.blue_ghost = PhotoImage(file="/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/blue_ghost.gif")
        self.pink_ghost = PhotoImage(file="/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/pink_ghost.gif")
        self.scared_ghost = PhotoImage(file="/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/scared_ghost.gif")
        self.eyes = PhotoImage(file="/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/eyes.gif")
        # set the image (which really is the colour) parameter to a variable
        self.colour = image
        # dictionary converting the colour to its corresponding image
        self.ghost_dict = {
            "b": self.blue_ghost,
            "p": self.pink_ghost,
        }
        # create ghost itself
        self.ghost = canvas.create_image(xpos, ypos, image=self.ghost_dict[self.colour], anchor=NW)
        # storing original direction parameter (od) under variable
        self.original_direction = od
        # create timer variables for future use
        self.timer = time.time()
        self.timer2 = time.time()
        self.timer3 = time.time()
        self.timer4 = time.time()
        self.timer5 = time.time()
        self.timer6 = time.time()
        # this allows time.time() - self.timer7 to initialize as negative
        self.timer7 = 1 * math.pow(1000, 100)
        self.timer8 = time.time()
        # create tick variables for future use
        self.ticks = 0
        self.ticks2 = 0
        # boolean variables for future use
        self.first = True
        self.has_paused = False
        self.game_started = False
        self.boolean = False
        self.is_scared = False
        self.is_retreating = False
        # initializes variables that will determine the ghost's distance from pacman
        self.left_distance = 0
        self.right_distance = 0
        self.up_distance = 0
        self.down_distance = 0
        # variable indicating whether the ghost has flashed or not
        self.has_flashed = False
        # initializes self.square, the variable determine which square the ghost is on
        # differs depending on which ghost it is
        if self.original_direction == "right":
            self.square = 82
        else:
            self.square = 84
        # list determinning if the wall is already occupied
        self.occupied = []
        for z in range(1, 16):
            self.occupied.append(z)
        for z in range(1, 14):
            self.occupied.append(1 + 15 * z)
        for z in range(1, 14):
            self.occupied.append(15 * (z + 1))
        for z in range(211, 226):
            self.occupied.append(z)
        self.occupied.append(18)
        self.occupied.append(28)
        self.occupied.append(33)
        self.occupied.append(43)
        for z in range(35, 42):
            self.occupied.append(z)
        for z in range(63, 74):
            self.occupied.append(z)
        self.occupied.remove(68)
        self.occupied.append(78)
        self.occupied.append(88)
        self.occupied.append(93)
        self.occupied.append(103)
        for z in range(95, 102):
            self.occupied.append(z)
        self.occupied.append(110)
        self.occupied.append(116)
        self.occupied.append(123)
        self.occupied.append(133)
        for z in range(125, 132):
            self.occupied.append(z)
        self.occupied.append(138)
        self.occupied.append(148)
        for z in range(153, 164):
            self.occupied.append(z)
        self.occupied.remove(158)
        for z in range(183, 194):
            self.occupied.append(z)
        self.occupied.remove(184)
        self.occupied.remove(192)
        self.occupied.append(198)
        self.occupied.append(208)

    # function that adds the walls after the ghosts have left them at the start of the game
    def add_wall(self):
        # configure the wall to be invisible
        canvas.itemconfig(Wall18.wall, fill="", outline="")
        # wait for one second, then set the ticks to be 1 and start the timer
        if time.time() - self.timer >= 1 and self.has_paused is False:
            self.ticks = 1
            self.timer2 = time.time()
            self.has_paused = True

        # every 0.1 seconds, for 1.6 seconds, move the ghost five units up and increment the ticks
        if time.time() - self.timer2 >= 0.1 and self.ticks <= 16 and self.has_paused is True:
            self.ticks += 1
            canvas.move(self.ghost, 0, -5)
            self.timer2 = time.time()

        # once 3 seconds have passed (the ghosts finished moving after 2.6 seconds), make the wall opaque
        if time.time() - self.timer >= 3:
            canvas.itemconfig(Wall18.wall, fill="#000080")
            self.game_started = True

    # function that's always running, used to cause movement to be gradual (pauses between movement)
    def always_run(self):
        # if ghost isn't scared or retreating, every 0.4 seconds, move
        if time.time() - self.timer3 >= 0.4 and self.is_scared is False and self.is_retreating is False:
            self.move()
            # reset timer for next cycle
            self.timer3 = time.time()

        # if ghost is scared and function hasn't been run yet
        # configuration and timer resets should only occur once. Once function has been run, change boolean to true
        if self.is_scared is True and self.boolean is False:
            canvas.itemconfig(self.ghost, image=self.scared_ghost)
            self.timer4 = time.time()
            self.timer5 = time.time()
            self.timer7 = time.time()
            self.boolean = True

        # if the ghost is scared and not retreating, run code every 0.5 seconds
        if time.time() - self.timer4 >= 0.5 and self.is_scared is True and self.is_retreating is False:
            self.scared()
            self.timer4 = time.time()

        # after seven seconds, alert the user that the ghosts will change form
        if time.time() - self.timer5 >= 6 and time.time() - self.timer7 >= 0.3 and self.is_scared is True and self.is_retreating is False:
            self.flash()
            self.has_flashed = not self.has_flashed
            self.timer7 = time.time()

        # after ten seconds, the ghosts aren't scared anymore
        # reset the boolean variable
        if time.time() - self.timer5 >= 8:
            self.is_scared = False
            self.boolean = False
            canvas.itemconfig(self.ghost, image=self.ghost_dict[self.colour])

        # if the ghosts are retreating, make them move every 0.1 seconds
        if time.time() - self.timer6 >= 0.1 and self.is_retreating is True:
            self.retreating()
            self.timer6 = time.time()

    # function that returns array of possible directions
    def get_directions(self) -> []:
        # initially, all the directions are possible
        possib = ["up", "down", "left", "right"]
        # the ghost can't move the direction it came from (in most scenarios), so remove that direction
        if possib.__contains__(self.original_direction) and self.square != 17 and self.square != 29 and self.square\
                != 209 and self.square != 197:
            possib.remove(self.original_direction)
        # if the ghost is below a wall, remove the possibility of up
        if possib.__contains__("up"):
            if self.occupied.__contains__(self.square - 15):
                possib.remove("up")
        # if the ghost above a wall, remove the possibility of going down
        if possib.__contains__("down"):
            if self.occupied.__contains__(self.square + 15):
                possib.remove("down")
        # if the ghost is to the right of a wall, remove the possibility of going left
        if possib.__contains__("left"):
            if self.occupied.__contains__(self.square - 1):
                possib.remove("left")
        # if the ghost is to the left of wall, remove the possibility of going right
        if possib.__contains__("right"):
            if self.occupied.__contains__(self.square + 1):
                possib.remove("right")
        # return the set of possible directions
        return possib

    # if there is only one possibility
    def len_one(self, array):
        possib = array
        if possib[0] == "left":
            self.move_left()
        elif possib[0] == "right":
            self.move_right()
        elif possib[0] == "up":
            self.move_up()
        else:
            self.move_down()

    # function controlling movement of ghosts
    def move(self):
        # get possibility list
        possib = self.get_directions()
        # if game has started
        if self.game_started is True:
            # if there is only one possibility, call function
            if possib.__len__() == 1:
                self.len_one(possib)
            # if there's more than one possibility
            else:
                # get coordinates of ghost
                pos_ghost = canvas.coords(self.ghost)
                # get x and y centres of ghost
                ghost_xcentre = pos_ghost[0] + 25
                ghost_ycentre = pos_ghost[1] + 25
                # get coordinates of pacman
                pos_pacman = canvas.coords(Pacman.pacman)
                # get x and y centres of pacman
                pacman_xcentre = pos_pacman[0] + 25
                pacman_ycentre = pos_pacman[1] + 25
                # array of distances between ghost and pacman
                array = []
                # if down is a possibility, calculate the ghost's hypothetical distance from pacman if it moves down
                if possib.__contains__("down"):
                    self.down_distance = math.sqrt(math.pow(pacman_xcentre - ghost_xcentre, 2) + math.pow\
                        (pacman_ycentre - (ghost_ycentre + 25), 2))
                    array.append(self.down_distance)
                # if left is a possibility, calculate the ghost's hypothetical distance from pacman if it moves left
                if possib.__contains__("left"):
                    self.left_distance = math.sqrt(math.pow(pacman_xcentre - (ghost_xcentre - 25), 2) + math.pow\
                        (pacman_ycentre - ghost_ycentre, 2))
                    array.append(self.left_distance)
                # if up is a possibility, calculate the ghost's hypothetical distance from pacman if it moves up
                if possib.__contains__("up"):
                    self.up_distance = math.sqrt(math.pow(pacman_xcentre - ghost_xcentre, 2) + math.pow\
                        (pacman_ycentre - (ghost_ycentre - 25), 2))
                    array.append(self.up_distance)
                # if right is a possibility, calculate the ghost's hypothetical distance from pacman if it moves right
                if possib.__contains__("right"):
                    self.right_distance = math.sqrt(math.pow(pacman_xcentre - (ghost_xcentre + 25), 2) + math.pow\
                        (pacman_ycentre - ghost_ycentre, 2))
                    array.append(self.right_distance)
                # obtain the last distance and perform the appropriate function
                chosen = min(array)
                if chosen == self.left_distance:
                    self.move_left()
                elif chosen == self.right_distance:
                    self.move_right()
                elif chosen == self.up_distance:
                    self.move_up()
                else:
                    self.move_down()

    # function controlling movement of ghost when it's scared
    def scared(self):
        # get possibility list
        possib = self.get_directions()
        # if there is only one possibility, call function
        if possib.__len__() == 1:
            self.len_one(possib)
        # if there is more than one possibility, randomly determine which direction it goes
        else:
            # continues to generate random numbers until one of the conditions is met
            while True:
                # random integer between 0 and 3
                rand = random.randrange(0, 4)
                if rand == 0 and possib.__contains__("left"):
                    self.move_left()
                    break
                elif rand == 1 and possib.__contains__("up"):
                    self.move_up()
                    break
                elif rand == 2 and possib.__contains__("right"):
                    self.move_right()
                    break
                elif rand == 3 and possib.__contains__("down"):
                    self.move_down()
                    break

    # function that causes ghosts to flash
    def flash(self):
        # if the ghost has not flashed (in its scared form), temporarily configure image to be normal
        if self.has_flashed is False:
            if self.colour == "b":
                canvas.itemconfig(self.ghost, image=self.blue_ghost)
            else:
                canvas.itemconfig(self.ghost, image=self.pink_ghost)
        # if the ghost has flashed, temporarily configure image to be scared
        else:
            canvas.itemconfig(self.ghost, image=self.scared_ghost)

    # retreating function
    def retreating(self):
        # the first time the ghost moves when it begins retreating, it is allowed to move backwards
        # it only wants the fastest rout back to its starting position
        if self.first is True:
            self.original_direction = "none"
            self.first = False
        # get possibilities
        possib = self.get_directions()
        # if there's only one possibility
        if possib.__len__() == 1:
            self.len_one(possib)
        # if there's more than one possibility
        else:
            # initialize xcentre variable
            xcentre = 0
            # customize xcentre based on the ghost
            if self.colour == "b":
                xcentre = 260
            if self.colour == "p":
                xcentre = 340
            # initialize the ycentre variable
            ycentre = 220
            # coordinates of ghost
            pos_ghost = canvas.coords(self.ghost)
            # x and y centres of ghost
            ghost_xcentre = pos_ghost[0] + 25
            ghost_ycentre = pos_ghost[1] + 25
            # array of possible directions
            array = []
            # instead of the target being selected to be pacman like it usually is, the target is its starting position
            if possib.__contains__("down"):
                self.down_distance = math.sqrt(math.pow(xcentre - ghost_xcentre, 2) + math.pow(ycentre - (ghost_ycentre + 25), 2))
                array.append(self.down_distance)
            if possib.__contains__("left"):
                self.left_distance = math.sqrt(math.pow(xcentre - (ghost_xcentre - 25), 2) + math.pow(ycentre - ghost_ycentre, 2))
                array.append(self.left_distance)
            if possib.__contains__("up"):
                self.up_distance = math.sqrt(math.pow(xcentre - ghost_xcentre, 2) + math.pow(ycentre - (ghost_ycentre - 25), 2))
                array.append(self.up_distance)
            if possib.__contains__("right"):
                self.right_distance = math.sqrt(math.pow(xcentre - (ghost_xcentre + 25), 2) + math.pow(ycentre - ghost_ycentre, 2))
                array.append(self.right_distance)
            # get the direction that leads to the shortest distance to its starting position
            chosen = min(array)
            # run the appropriate function
            if chosen == self.left_distance:
                self.move_left()
            elif chosen == self.right_distance:
                self.move_right()
            elif chosen == self.up_distance:
                self.move_up()
            else:
                self.move_down()
        # if the ghost reaches its starting position, it isn't scared or retreating anymore, reconfigure properties
        if self.colour == "b" and self.square == 82 or self.colour == "p" and self.square == 84:
            self.is_retreating = False
            self.is_scared = False
            self.boolean = False
            canvas.itemconfig(self.ghost, image=self.ghost_dict[self.colour])
            self.timer3 = time.time()

    # move ghost left, change square position, set original direction
    def move_left(self):
        canvas.move(self.ghost, -40, 0)
        self.square -= 1
        self.original_direction = "right"

    # move ghost right, change square position, set original direction
    def move_right(self):
        canvas.move(self.ghost, 40, 0)
        self.square += 1
        self.original_direction = "left"

    # move ghost up, change square position, set original direction
    def move_up(self):
        canvas.move(self.ghost, 0, -40)
        self.square -= 15
        self.original_direction = "down"

    # move ghost down, change square position, set original direction
    def move_down(self):
        canvas.move(self.ghost, 0, 40)
        self.square += 15
        self.original_direction = "up"

    # function when the ghost touches pacman (lose OR ghost retreats)
    def lose_check(self):
        # if the ghost isn't retreating, run the function
        # if the ghost is retreating, nothing should be done
        if self.is_retreating is False:
            # coordinates of ghost
            pos = canvas.coords(self.ghost)
            # centres of ghost
            posx_centre = pos[0] + 25
            posy_centre = pos[1] + 25
            # coordinates of pacman
            pos_pac = canvas.coords(Pacman.pacman)
            # centres of pacman
            posx_pac_centre = pos_pac[0] + 25
            posy_pac_centre = pos_pac[1] + 25
            # if pacman is touching the ghost:
            if -25 <= posx_centre - posx_pac_centre <= 25:
                if -25 <= posy_centre - posy_pac_centre <= 25:
                    # if the ghost is not scared, the player loses
                    if self.is_scared is False:
                        canvas.create_rectangle(0, 0, 600, 650, fill="white", outline="white")
                        canvas.create_text(300, 300, font=("Comic Sans MS", 30), text="Game over")
                        canvas.create_text(300, 350, font=("Comic Sans MS", 20), text="Score: " + str(Score.score))
                        # takes pacman far away from the map so the user can't get any points after losing
                        canvas.move(Pacman.pacman, -1000, -1000)
                        # retrieve the current high score value
                        # rb indicates opening
                        highscore = pickle.load(open("/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/High Scores", "rb"))
                        # if current score is greater than previous high score
                        if Score.score >= highscore:
                            # open high score file
                            # wb indicates closing
                            load = open("/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/High Scores", "wb")
                            # place high score in the file
                            pickle.dump(Score.score, load)
                            # close file
                            load.close()
                            # update to new high score
                            highscore = pickle.load(open("/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/High Scores", "rb"))
                        # print high score
                        canvas.create_text(300, 400, font=("Comic Sans MS", 20), text="High Score: "+str(highscore))
                        # stop all music
                        sa.stop_all()
                    else:
                        # otherwise, the ghost retreats
                        canvas.itemconfig(self.ghost, image=self.eyes)
                        self.is_retreating = True
                        # increment the score by 30
                        Score.score += 30


# create ghost objects
blue_ghost = Ghost(235, 275, "b", "right")
pink_ghost = Ghost(315, 275, "p", "left")


# score class
class Score:
    def __init__(self):
        self.background = canvas.create_rectangle(0, 600, 600, 640, fill="#000080", outline="#000080")
        # score is equal to the number of coins eaten
        self.score = 0
        self.score_text = canvas.create_text(300, 617, font=("Comic Sans MS", 15), fill="white", text="Score: " +
                                                                                                      str(self.score))

    # update score
    def update_score(self):
        canvas.itemconfig(self.score_text, text="Score: " + str(self.score))


# create score object
Score = Score()


# indicator class
class Indicator:
    def __init__(self):
        self.timer = math.pow(1000, 100)
        self.has_started = False
        self.is_cherry = False
        self.text = ""
        self.colour = ""
        self.rectangle = canvas.create_rectangle(0, 600, 600, 640, fill="red", outline="red")
        self.text = canvas.create_text(300, 617, font=("Comic Sans MS", 15), fill="white", text="Cherry bonus! 3x score!")
        # hide rectangle and text
        canvas.itemconfigure(self.rectangle, state="hidden")
        canvas.itemconfigure(self.text, state="hidden")

    # method that always runs
    def always_run(self):
        # if the cherry bonus is true, start the timer
        # self.has_started is set to True so this method only runs once
        if Pacman.bonus is True and self.has_started is False:
            self.timer = time.time()
            self.has_started = True

        # if the cherry bonus is active
        if Pacman.bonus is True:
            # for one seconds, display the text, then make it disappear
            if 0 <= time.time() - self.timer <= 1:
                if self.is_cherry is False:
                    canvas.itemconfigure(self.rectangle, state="normal")
                    canvas.itemconfigure(self.text, state="normal")
                else:
                    canvas.itemconfigure(self.rectangle, state="hidden")
                    canvas.itemconfigure(self.text, state="hidden")
            # once one second has passed, reset the timer and change the cherry boolean
            else:
                self.timer = time.time()
                self.is_cherry = not self.is_cherry


# create indicator object
Indicator = Indicator()

musiccount = time.time()-61

while True:
    if time.time() - musiccount >= 61:
        wave_obj = sa.WaveObject.from_wave_file("/Users/SamRoo/PycharmProjects/OOPPractice/Pacman/PacMan Music.wav")
        wave_obj.play()
        musiccount = time.time()
    canvas.update()
    canvas.update_idletasks()
    Pacman.always_run()
    Pacman.switch_pacman()
    Pacman.touch_down()
    Pacman.touch_up()
    Pacman.touch_left()
    Pacman.touch_right()
    Pacman.touch_coin()
    Pacman.touch_powerup()
    Pacman.touch_cherry()
    Pacman.win_con()
    blue_ghost.add_wall()
    blue_ghost.always_run()
    blue_ghost.lose_check()
    pink_ghost.add_wall()
    pink_ghost.always_run()
    pink_ghost.lose_check()
    Score.update_score()
    Indicator.always_run()
    time.sleep(0.01)
