from pyamaze import maze,agent,COLOR , textLabel
from timeit import timeit
revPath = {}
def DFS(m):
    start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    while (frontier):
        currCell=frontier.pop()
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell]=currCell
    
    # revPath = {}
    revPath = dfsPath
    fwdPath={}
    goal_cell=(1,1)
    while goal_cell != start:
        fwdPath[dfsPath[goal_cell]] = goal_cell
        goal_cell = dfsPath[goal_cell]
    return fwdPath 


if __name__=='__main__':
    myMaze=maze(50,70)
    myMaze.CreateMaze(loadMaze = 'maze--2024-01-28--10-18-00.csv')
    path = DFS(myMaze)
    a = agent(myMaze,color = COLOR.cyan ,footprints=True , filled = True)
    
    myMaze.tracePath({a:path} , delay = 50)
    l=textLabel(myMaze,'DFS Path',len(path)+1)

    t1=timeit(stmt='DFS(myMaze)',number=10,globals=globals())
    textLabel(myMaze,'DFS Time',round(t1,5))

    myMaze.run()