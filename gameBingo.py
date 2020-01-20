# File: gameBingo.py
# the game of bingo
# 4x4 bingo board
# by: Rushnan Alam

from graphics import *    
from random import *

def main():
    row1, row2, row3, row4 = printIntro()
    windows = drawBoard(row1, row2, row3, row4)
    count_ = playGame(windows, row1, row2, row3, row4)
    printSummary(count_)
    

def printIntro():
    print("This is a game of Bingo!")
    print("In this game, a bingo is reached\nonly when all numbers in a horizontal row are crossed off.")
    print("The game coordinator will call numbers until a bingo is reached.")
    print("If a number called is on the board, click on it.")

    r1 = [randrange(1, 144), randrange(1, 144), randrange(1, 144), randrange(1, 144)]
    r2 = [randrange(1, 144), randrange(1, 144), randrange(1, 144), randrange(1, 144)]
    r3 = [randrange(1, 144), randrange(1, 144), randrange(1, 144), randrange(1, 144)]
    r4 = [randrange(1, 144), randrange(1, 144), randrange(1, 144), randrange(1, 144)]
    return r1, r2, r3, r4 
    
def drawBoard(row1, row2, row3, row4):
    win = GraphWin("Bingo Board", 325, 325)
    s1 = Rectangle(Point(20, 90), Point(90, 20))
    for i in range(4):
        x = s1.clone()
        x.move(70*(i), 0)
        x.draw(win)
    for i in range(4):
        x = s1.clone()
        x.move(70*(i), 70)
        x.draw(win)
    for i in range(4):
        x = s1.clone()
        x.move(70*(i), 140)
        x.draw(win)
    for i in range(4):
        x = s1.clone()
        x.move(70*(i), 210)
        x.draw(win)
    x = 55
    for i in range(4):
        x2 = 67*i
        Text(Point(x + x2, 55), row1[i]).draw(win)
    for i in range(4):
        x2 = 67*i
        Text(Point(x + x2, 122), row2[i]).draw(win)
    for i in range(4):
        x2 = 67*i
        Text(Point(x + x2, 189), row3[i]).draw(win)
    for i in range(4):
        x2 = 67*i
        Text(Point(x + x2, 256), row4[i]).draw(win)
    return win    
   
    
    
def playGame(windows, row1, row2, row3, row4):
    count = 0    
    number = randrange(1, 144)
    while row1 and row2 and row3 and row4: 
        number = randrange(1, 144)
        print("\nnumber called:", number)

        if number in row1: 
            print("CROSS OFF NUMBER!\n")
            row1.pop(row1.index(number))
            p = windows.getMouse()
            c = Circle(Point(p.getX(), p.getY()), 5)
            c.setFill("red")
            c.draw(windows)
        elif number in row2:
            print("CROSS OFF NUMBER!\n")
            row2.pop(row2.index(number))
            p = windows.getMouse()
            c = Circle(Point(p.getX(), p.getY()), 5)
            c.setFill("red")
            c.draw(windows)
            
        elif number in row3:
            print("CROSS OFF NUMBER!\n")
            row3.pop(row3.index(number))
            p = windows.getMouse()
            c = Circle(Point(p.getX(), p.getY()), 5)
            c.setFill("red")
            c.draw(windows)
            
        elif number in row4:
            print("CROSS OFF NUMBER!\n")
            row4.pop(row4.index(number))
            p = windows.getMouse()
            c = Circle(Point(p.getX(), p.getY()), 5)
            c.setFill("red")
            c.draw(windows)
            
        else:
            print("Number not on board.")
            print()
        count = count + 1

    t = Text(Point(162.5, 162.5), "BINGO! Click to close game board")
    t.setTextColor("yellow")
    t.setSize(15)
    t.setOutline("red")
    t.draw(windows)        
    windows.getMouse()
    windows.close()

    return count

def printSummary(count_):
    print("\n\nBINGO! You have successfully crossed off 1 row of numbers!!")
    print("It took", count_, "calls to win!")
        
    
if __name__ == "__main__":
    main()        
