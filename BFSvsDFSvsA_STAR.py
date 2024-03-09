from BFS_Demo import BFS
from A_STAR_Demo import aStar
from DFS_Demo import DFS
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

###########################
## Comparison One by One ##

# First Run this for BFS:
# m=maze(20,30)
# m.CreateMaze(loadMaze='mazeComparison1.csv')
# bSearch,bfsPath,fwdPath=BFS(m)


# l=textLabel(m,'BFS Path Length',len(fwdPath)+1)
# l=textLabel(m,'BFS Search Length',len(bSearch)+1)


# a=agent(m,footprints=True,color=COLOR.blue,filled=True)
# b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
# c=agent(m,footprints=True,color=COLOR.red)
# m.tracePath({a:bSearch},delay=50)
# m.tracePath({b:bfsPath},delay=100)
# m.tracePath({c:fwdPath},delay=100)

# m.run()


# Then run this for A-Star
# m=maze(20,30)
# m.CreateMaze(loadMaze='mazeComparison1.csv')
# aSearch,aPath,fwdPath=aStar(m)

# l=textLabel(m,'A-Star Path Length',len(fwdPath)+1)
# l=textLabel(m,'A-Star Search Length',len(aSearch)+1)

# a=agent(m,footprints=True,color=COLOR.blue,filled=True)
# b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
# c=agent(m,footprints=True,color=COLOR.red)
# m.tracePath({a:aSearch},delay=50)
# m.tracePath({b:aPath},delay=100)

# m.tracePath({c:fwdPath},delay=100)


# m.run()




###########################
## Combined Comparison ##
if __name__=='__main__':
    myMaze=maze(50,70)
    myMaze.CreateMaze(loadMaze = 'maze--2024-01-28--10-18-00.csv')
    # myMaze.CreateMaze()
    searchPath,aPath,fwdPath=aStar(myMaze)
    bSearch,bfsPath,fwdBFSPath=BFS(myMaze)
    dSeacrh,dfsPath,fwdDFSPath = DFS(myMaze)


    l=textLabel(myMaze,'A-Star Path Length',len(fwdPath)+1)
    l=textLabel(myMaze,'BFS Path Length',len(fwdBFSPath)+1)
    l=textLabel(myMaze,'DFS Path Length',len(fwdDFSPath)+1)

    # l=textLabel(myMaze,'A-Star Search Length',len(searchPath)+1)
    # l=textLabel(myMaze,'BFS Search Length',len(bSearch)+1)
    # l=textLabel(myMaze,'DFS Search Length',len(dSeacrh)+1)


    a=agent(myMaze,footprints=True,color=COLOR.cyan,filled=True)#bfs
    b=agent(myMaze,footprints=True,color=COLOR.yellow,filled=True)#astar
    c= agent(myMaze,footprints=True,color=COLOR.red,filled=True)#dfs

    myMaze.tracePath({b:fwdPath},delay=50)#astar
    myMaze.tracePath({a:fwdBFSPath},delay=50)#bfs
    myMaze.tracePath({c:fwdDFSPath},delay=50)#dfs

    t1=timeit(stmt='aStar(myMaze)',number=10,globals=globals())
    t2=timeit(stmt='BFS(myMaze)',number=10,globals=globals())
    t3 = timeit(stmt='DFS(myMaze)',number=10,globals=globals())

    textLabel(myMaze,'A-Star Time',round(t1,5))
    textLabel(myMaze,'BFS Time',round(t2,5))
    textLabel(myMaze,'DFS Time',round(t3,5))

    myMaze.run()