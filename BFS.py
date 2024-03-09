from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit
def BFS(m):
    start=(m.rows,m.cols)
    frontier=[start]
    explored=[start]
    bfsPath={}
    while (frontier):
        currCell=frontier.pop(0)
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
    fwdPath={}
    goal_cell = (1,1)
    while goal_cell != start:
        fwdPath[bfsPath[goal_cell]] = goal_cell
        goal_cell = bfsPath[goal_cell]
    return fwdPath

if __name__=='__main__':
    myMaze = maze(50,70)
    myMaze.CreateMaze(loadMaze = 'maze--2024-01-28--10-18-00.csv')
    path=BFS(myMaze)

    a=agent(myMaze,color = COLOR.cyan,footprints=True,filled=True)
    myMaze.tracePath({a:path} , delay = 50)
    l=textLabel(myMaze,'BFS Path',len(path)+1)

    t1=timeit(stmt='BFS(myMaze)',number=10,globals=globals())
    textLabel(myMaze,'BFS Time',round(t1,5))

    myMaze.run()