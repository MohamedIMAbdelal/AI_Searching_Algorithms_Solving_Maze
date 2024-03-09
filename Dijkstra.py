from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit
def dijkstra(m):
    # if start is None:
    start=(m.rows,m.cols)

    # hurdles=[(i.position,i.cost) for i in h]

    unvisited = {n:float('inf') for n in m.grid}
    unvisited[start]=0
    searchPath = [start]
    visited={}
    revPath={} 
    while unvisited:
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]
        searchPath.append(currCell)
        if currCell==m._goal:
            break
        for d in 'EWNS':#direction does not matter here
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    NextCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    NextCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    NextCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    NextCell=(currCell[0]-1,currCell[1])
                if NextCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                # for hurdle in hurdles:
                #     if hurdle[0]==currCell:
                #         tempDist+=hurdle[1]

                if tempDist < unvisited[NextCell]:
                    unvisited[NextCell]=tempDist
                    revPath[NextCell]=currCell
        unvisited.pop(currCell)
    
    fwdPath={}
    cell=m._goal #= (1,1)
    while cell!=start:
        fwdPath[revPath[cell]]=cell #fwdpath[(1,2)] = (1,1)==> {(1,2) : (1,1)}
        cell=revPath[cell]
    
    return fwdPath,visited[m._goal],revPath,searchPath
            



if __name__=='__main__': #just to run the code in this file only while other files does not run simultoinsely
    myMaze=maze(50,70)
    myMaze.CreateMaze(loadMaze = 'maze--2024-01-28--10-18-00.csv')
    # myMaze.CreateMaze(loadMaze='dijkMaze.csv')

    # h1=agent(myMaze,4,4,color=COLOR.red)
    # h2=agent(myMaze,4,6,color=COLOR.red)
    # h3=agent(myMaze,4,1,color=COLOR.red)
    # h4=agent(myMaze,4,2,color=COLOR.red)
    # h5=agent(myMaze,4,3,color=COLOR.red)

    # h1.cost=100
    # h2.cost=100
    # h3.cost=100
    # h4.cost=100
    # h5.cost=100

    # path,c=dijstra(myMaze,h1,h2,h2,h3,h4,h5)
    path,c,d,f=dijkstra(myMaze)
    l=textLabel(myMaze,'dijkstra Path Length',len(path)+1)

    a=agent(myMaze,color=COLOR.cyan,filled=True,footprints=True)
    myMaze.tracePath({a:path} , delay = 50)

    t1=timeit(stmt='dijkstra(myMaze)',number=10,globals=globals())
    textLabel(myMaze,'dijkstra Time',round(t1,5))

    myMaze.run()