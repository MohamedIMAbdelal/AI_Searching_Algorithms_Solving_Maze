from Dijkstra import dijkstra
from A_STAR_Demo import aStar
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit


###########################
## Combined Comparison ##
if __name__=='__main__':
    myMaze=maze(50,70)
    myMaze.CreateMaze(loadMaze = 'maze--2024-01-28--10-18-00.csv')
    # myMaze.CreateMaze()
    searchPath,aPath,fwdPath=aStar(myMaze)
    fwddijkPath,visitedNodes,dijkPath,dijkSearch=dijkstra(myMaze)

    l=textLabel(myMaze,'A-Star Path Length',len(fwdPath)+1)
    l=textLabel(myMaze,'dijkstra Path Length',len(fwddijkPath)+1)
    # l=textLabel(myMaze,'A-Star Search Length',len(searchPath)+1)
    # l=textLabel(myMaze,'dijkstra Search Length',len(dijkSearch)+1)

    a=agent(myMaze,footprints=True,color=COLOR.cyan,filled=True)#astar
    b=agent(myMaze,footprints=True,color=COLOR.yellow,filled=True)#dijkstra

    myMaze.tracePath({a:fwdPath},delay=100)
    myMaze.tracePath({b:fwddijkPath},delay=100)

    t1=timeit(stmt='aStar(myMaze)',number=10,globals=globals())
    t2=timeit(stmt='dijkstra(myMaze)',number=10,globals=globals())

    textLabel(myMaze,'A-Star Time',round(t1,5))
    textLabel(myMaze,'dijkstra Time',round(t2,5))


    myMaze.run()