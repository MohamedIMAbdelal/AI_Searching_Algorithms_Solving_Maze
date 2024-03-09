from pyamaze import maze,agent,COLOR , textLabel
def DFS(m):
    start=(1,1)
    explored=[start]
    frontier=[start]
    dfsPath={}
    while (frontier):
        currCell=frontier.pop()
        if currCell==(m.rows,m.cols):
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
    fwdPath={}
    goal_cell=(m.rows,m.cols)
    while goal_cell != start:
        fwdPath[dfsPath[goal_cell]] = goal_cell
        goal_cell = dfsPath[goal_cell] 
    print(dfsPath)
    return fwdPath


if __name__=='__main__':
    m=maze(5,5)
    m.CreateMaze(x = m.rows , y = m.cols , loopPercent = 0 , loadMaze = 'Searching Algoritms/maze--2023-12-31--20-05-39.csv')
    path=DFS(m)
    a=agent(m,x = 1 , y = 1 ,shape= 'arrow' ,footprints=True , filled = True)
    m.tracePath({a:path})
    print(path)
    l=textLabel(m,'Length of Shortest Path',len(path)+1)
    m.run()