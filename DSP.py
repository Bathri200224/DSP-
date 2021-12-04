import random
import itertools
import threading
import time
import sys

done = False

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
global lst
lst=[]
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    lst.append(root.data)
    inorder(root.right)
    return lst


def preorder(root):
    if root is None:
        return
    lst.append(root.data)
    preorder(root.left)
    preorder(root.right)
    return lst


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    lst.append(root.data)
    postorder(root.right)
    return lst

def GenerateMineSweeperMap(n, k):
    arr = [[0 for row in range(n)] for column in range(n)]
    for num in range(k):
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        arr[y][x] = 'X'
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-1):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1 # center right
        if (x >=1 and x <= n-1) and (y >= 0 and y <= n-1):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1 # center left
        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1 # top left
 
        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1 # top right
        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1 # top center
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1 # bottom right
        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1 # bottom left
        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1 # bottom center
    return arr
def GeneratePlayerMap(n):
    arr = [['-' for row in range(n)] for column in range(n)]
    return arr
def DisplayMap(map):
    for row in map:
        print(" ".join(str(cell) for cell in row))
        print("")
def CheckWon(map):
    for row in map:
        for cell in row:
            if cell == '-':
                return False
    return True

def CheckContinueGame(score):
    print("Your score: ", score)
    isContinue = input("Do you want to try again? (y/n) :")
    if isContinue == 'n':
        return False
    return True
def Game():
    GameStatus = True
    while GameStatus:
        difficulty = input("Select your difficulty (b, i, h):")
        if difficulty.lower() == 'b':
            n = 5
            k = 3
        elif difficulty.lower() == 'i':
            n = 6
            k = 8
        else:
            n = 8
            k = 20
 
        minesweeper_map = GenerateMineSweeperMap(n, k)
        player_map = GeneratePlayerMap(n)
        score = 0
        while True:
            if CheckWon(player_map) == False:
                print("Enter your cell you want to open :")
                x = input("X (1 to 5) :")
                y = input("Y (1 to 5) :")
                x = int(x) - 1 # 0 based indexing
                y = int(y) - 1 # 0 based indexing
                if (minesweeper_map[y][x] == 'X'):
                    print("Game Over!")
                    DisplayMap(minesweeper_map)
                    GameStatus = CheckContinueGame(score)
                    break
                else:
                    player_map[y][x] = minesweeper_map[y][x]
                    DisplayMap(player_map)
                    score += 1
 
            else:
                DisplayMap(player_map)
                print("You have Won!")
                GameStatus = CheckContinueGame(score)
                break
#creating a recursive function  
def tower_of_hanoi(disks, source, auxiliary, target):
    global count #using global scope the count is assigned a value anywhere within the function’s body
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))
        count=count+1#moves getting incremented 
        return  
    #function call itself-recursion  
    tower_of_hanoi(disks - 1, source, target, auxiliary)
    count=count+1
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))
    tower_of_hanoi(disks - 1, auxiliary, source, target)


if __name__ == '__main__':
    print("We welcome you to play our iteration of the game minesweeper:)")
    print("Please choose your difficulty level; b:beginner i:intermediate  h:hard")
    print("In the grid there are some bombs placed randomly; the most places you navigate without encountering a bomg you get a point.")
    print("If the number 0 shows up in a cell, it means that particular cell is touching zero bombs")
    print("If the number 1 shows up in a cell, it means that particular cell is touching one bomb")
    print("If the number 2 shows up in a cell, it means that particular cell is touching two bombs")
    print("All the best and good luck!")
    try:
        Game()
    except KeyboardInterrupt:
        print('\nEnd of Game. Bye Bye!')
    
    print("\n\nWelcome to play the game Tower of Hanoi")
    print("We can solve a problem in tower of hanoi using stack concept from data structure,")
    print("We know that the basic rule of stack is last in first out,using this rule the problem can be solved easily.") 
    name=input("Enter your name:")
    count=0 #when no moves are done at the beginning 
    disks=int(input("Enter the number of disks:"))

    print("Enter the no.of moves that you think to bring the disks from source rod to target rod,") 
    moves=int(input("enter the number of moves:"))
    print("THE STEPS TO BRING THE DISKS FROM SOURCE ROD TO TARGET ROD ARE:")
    #We are referring source as A,auxiliary as B,and target as C
    tower_of_hanoi(disks, 'A', 'B', 'C')#Calling the function
    print("RESULT:-")
    if(moves!=count):
        print("YOU HAVE FAILED!!KINDLY REATTEND BY UNDERSTANDING THE CONCEPT")
    else:
        print("YOU HAVE SUCCESSFULLY UNDERSTOOD THE CONCEPT!!")
        print("YOU HAVE PASSED THE GAME!!")
        print("CONGRATULATIONS!!",name,"YOU GOT 500 POINTS")
        points=500
        print("THE WINNER IS",name),
        

    print("\n\nHello",name,", welcome to DSP olympics's Tree traversal game:)")
    print("You will be asked to choose what type of traversal you would like to perform")
    print("Then enter the values of the respective nodes")
    print("Finally enter your answer and the system will evaluate your answer and tell you the result")
    root=Node(input("\nENTER NODE 1:"))
    root.left=Node(input("ENTER NODE 2:"))
    root.right=Node(input("ENTER NODE 3:"))
    root.left.left=Node(input("ENTER NODE 4:"))
    root.right.left=Node(input("ENTER NODE 5:"))
    root.right.right=Node(input("ENTER NODE 6:"))


print("\nWHICH TRAVERSAL DO YOU SEEK?")
print("ENTER 1 FOR INORDER")
print("ENTER 2 FOR PREORDER")
print("ENTER 3 FOR POSTORDER")

opt=int(input())
    

if(opt==1):
    print("Inorder rules are as follows:")
    print("\nIn this traversal method, the left subtree is visited first, then the root and later the right sub-tree.") 
    print("We should always remember that every node may represent a subtree itself.")
    print("If a binary tree is traversed in-order, the output will produce sorted key values in an ascending order.")
    print("\nEnter your answer for the question")
    inord = input('Input in-order traversal: ').split()
    print(inord)
    result=inorder(root)
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rVERIFYING WITH OUR SATELLITE SERVERS ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r   ')

    t = threading.Thread(target=animate)
    t.start()

    time.sleep(5)
    done = True
    print("\n")
    print(result)
    if(result!=inord):
        print("WASTED")
        print("TRY AGAIN")
    else:
        print("SUCCESS")
        print("YOU HAVE SUCCESSFULLY UNDERSTOOD THE CONCEPT OF TREE TRAVERSAL")
        print("CONGRATULATIONS",name,"YOU HAVE EARNED 500 POINTS")
        points=points+500
        print("YOUR TOTAL POINTS IS NOW",points)
        print("IT WAS FUN TO HAVE YOU PLAY WITH US,GOODBYE AND WE HOPE YOU HAVE A GREAT DAY:)")
        print("CIAO AMIGO")

elif(opt==2):
    print("preorder rules are as follows:")
    print("\nIn this traversal method, the root node is visited first, then the left subtree and finally the right subtree.")
    print("\nEnter your answer")
    preord = input('Input in-order traversal: ').split()
    print(preord)
    result=preorder(root)
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rVERIFYING WITH OUR SATELLITE SERVERS ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r   ')

    t = threading.Thread(target=animate)
    t.start()

    time.sleep(5)
    done = True
    print(result)
    if(result!=preord):
        print("WASTED")
        print("TRY AGAIN")
    else:
        print("SUCCESS")
        print("YOU HAVE SUCCESSFULLY UNDERSTOOD THE CONCEPT OF TREE TRAVERSAL")
        print("CONGRATULATIONS",name,"YOU HAVE EARNED 500 POINTS")
        points=points+500
        print("YOUR TOTAL POINTS IS NOW",points)
        print("IT WAS FUN TO HAVE YOU PLAY WITH US,GOODBYE AND WE HOPE YOU HAVE A GREAT DAY:)")
        print("CIAO AMIGO")
        


elif(opt==3):
    print("postorder rules are as follows:")
    print("\nIn this traversal method, the root node is visited last, hence the name.")
    print("First we traverse the left subtree, then the right subtree and finally the root node.")
    print("\nEnter your answer")
    postord = input('Input in-order traversal: ').split()
    print(postord)
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rVERIFYING WITH OUR SATELLITE SERVERS ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r  ')
    
    t = threading.Thread(target=animate)
    t.start()

    time.sleep(5)
    done = True
    result=postorder(root)
    print(result)
    if(result!=postord):
        print("WASTED")
        print("TRY AGAIN")
    else:
        print("SUCCESS")
        print("YOU HAVE SUCCESSFULLY UNDERSTOOD THE CONCEPT OF TREE TRAVERSAL")
        print("CONGRATULATIONS",name,"YOU HAVE EARNED 500 POINTS")
        points=points+500
        print("YOUR TOTAL POINTS IS NOW",points)
        print("IT WAS FUN TO HAVE YOU PLAY WITH US,GOODBYE AND WE HOPE YOU HAVE A GREAT DAY:)")
        print("CIAO AMIGO")
        
else:
    print("YOU HAVE SELECTED A WRONG OPTION PLEASE TRY AGAIN")
    
print("                                                      END CREDITS:                                                 ")
print("                                              A A.B.B STUDIOS PRODUCTION                                          ")
print("                                                     DSP OLYMPICS                                                 ")
