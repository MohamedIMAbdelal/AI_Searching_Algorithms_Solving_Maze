from pyamaze import maze,agent,textLabel , COLOR #here we call the library pyamaze to use clas maze , agent , textlabel , COLOR
from queue import PriorityQueue # we call Query datastructure to use priroty queue here
from timeit import timeit
def h(cell1,cell2): # we define a heuristic function here to calculate the h(n) in manhatin distance
    x1,y1=cell1 # we say X1 , Y1 = coordinates of cell1 , like cell1 = (2,3) then X1 = 2 , Y1 = 3 
    x2,y2=cell2
    return abs(x2-x1) + abs(y2-y1) # eventually we calculate the distance by substracing X1 from X2 in currCell from GoalCell in X , Y Coordinates then sum them



def aStar(m): # we define aStar func to calculate path
    start=(m.rows,m.cols) # initalize start value by saying x = num of rows , y = num of cols 
    g_score={cell:float('inf') for cell in m.grid} # initialize g_score value for every cell in maze by 'inf'
    g_score[start]=0 # initalize g_score of start only by zero because we count from it
    goal_cell = (1,1) # we define here goal to use later in code
    f_score={cell:float('inf') for cell in m.grid} # initialize 'inf' value for every cell in f func but not start cell
    f_score[start]=h(start , goal_cell) # here the value be value of heuristic func only because g(n) = 0

    list_queue = PriorityQueue() # we initalize a priorty queue by name of list_queue
    list_queue.put((f_score[start],start))# we use tuples to store a value for each cell by f(n) and tuples dont change only read
    aPath={}#initalize path empty dictionary
    while (list_queue):#loop on queue and if true continue , false end
        currCell=list_queue.get()[1] # we intialize currCell by cell (6 , (3,3)) , we need (3,3)
        if currCell == goal_cell:# if currCell = goalCell then break
            break
        for d in 'ESNW':#loop on the four directions but here the order wont matter because we use f(n)
            if m.maze_map[currCell][d]==True:#here we check for true values in every direction to switch on it later like ['E' : 1 , 'S' : 0 , 'N' : 1 , 'W' : 0] , here we only use east and north because have true values
                if d=='E':#if direction has true value on east then nextCell (x,y+1) means dont change rows but add another column to the currCell (row , col + 1)
                    NextCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    NextCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    NextCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    NextCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(NextCell,goal_cell)

                if temp_f_score < f_score[NextCell]:
                    g_score[NextCell]= temp_g_score
                    f_score[NextCell]= temp_f_score
                    list_queue.put((f_score[NextCell],NextCell))
                    aPath[NextCell]=currCell
    fwdPath = {}#initialize fwdpath that stores final shortest path generated from apath
    while goal_cell != start:#here we traverse from goalCell towards startCell so we can only store the shortest path needed
        fwdPath[aPath[goal_cell]] = goal_cell#in apath we were trying to connect start cell with nextcell and so on until reach goalCell but here we try to connect nextCell to goalCell from goalCell itself 
        goal_cell = aPath[goal_cell]
    return fwdPath

if __name__=='__main__': #block is a common Python idiom used to check whether the Python script is being run as the main program or if it is being imported as a module into another script.
    myMaze=maze(50,70)
    myMaze.CreateMaze(loadMaze = 'maze--2024-01-28--10-18-00.csv')
    path=aStar(myMaze)
    
    a=agent(myMaze,color=COLOR.cyan,filled=True,footprints=True)
    myMaze.tracePath({a:path} , delay = 50)
    l=textLabel(myMaze,'A Star Path Length',len(path)+1)

    t1=timeit(stmt='aStar(myMaze)',number=10,globals=globals())
    textLabel(myMaze,'A-Star Time',round(t1,5))

    myMaze.run()