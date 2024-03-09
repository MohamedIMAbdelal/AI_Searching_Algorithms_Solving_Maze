from pyamaze import maze , agent , COLOR , textLabel
start = 5 
end = 5
myMaze=maze(start,end)
myMaze.CreateMaze(x = 1,y = 3,loopPercent = 100 , loadMaze = 'maze--2024-01-28--11-40-24.csv')
a = agent(myMaze,x = 4,y = 3, filled = True , footprints= True , color= 'cyan')
# b = agent(m,filled = True , footprints= True)
# c = agent(m , x = 1, y = 1 , footprints=True , color="black")


myMaze.tracePath({a:myMaze.path},delay=500)

l1 = textLabel(myMaze , "Path Length",len(myMaze.path)+1)

myMaze.run()