import random
from tkinter import *

class Dungeon(object):
    def __init__(self, RoomWidth, RoomHeight):
        self.RoomWidth = RoomWidth
        self.RoomHeight = RoomHeight
    def Resolution(self):
        return "resolution: %s,%s" % (self.RoomWidth, self.RoomHeight)

class Window(object):
    def Create(width, height):
        WindowWidth = width
        WindowHeight = height
        BackGround = 'Khaki'
        _Window = Canvas(width = WindowWidth, height = WindowHeight, bg = BackGround)
        _Window.pack()
        return _Window

if __name__ == "__main__":
    width = 600
    height = 600
    WorkSpace = Window.Create(width,height)

    
    Room = []
    for num in range(random.randint(10, 50)):
        Room.append(num)
        Room[num] = Dungeon(random.randint(5,50), random.randint(5,50))
        print("Room #%s, %s"% (num, Room[num].Resolution()))
        WorkSpace.create_rectangle(width/2-Room[num].RoomWidth, height/2-Room[num].RoomHeight,
                                   width/2+Room[num].RoomWidth, height/2+Room[num].RoomHeight,
                                   outline = 'Blue')
