from pyamaze import maze , agent , COLOR , textLabel
start = 20 
end = 20
m=maze(start,end)
m.CreateMaze(x = start / 2 , y = end / 2 , pattern = None , loopPercent= 0 , theme = 'dark')
a = agent(m , x = start , y = end , shape = 'arrow' ,goal=None, filled = True , footprints= True , color= 'red')
b = agent(m,filled = True , footprints= True)
c = agent(m , x = 1, y = 1 , footprints=True , color="black")
# print(m.grid)
# print(m.maze_map)
print(m.path)
# m.markCells=[(5,5),(5,6),(5,7),(4,5),(2,1),(6,5),(20,20)]
# m.markCells = m.path # we try to equal marked cells with pathcells
# path2 = [(5,4),(5,2),(4,3),(3,3)]
# path3 = "SSWWNNEE"
m.tracePath({a:m.path},delay=100 , showMarked=True)
# m.tracePath({b:path2 , c:path3},delay=500 )
l1 = textLabel(m , "Number of Rows",m.rows)
l2 = textLabel(m , "Number of Cols",m.cols)
l3 = textLabel(m , "Number of steps",len(m.path))
# def count_steps():
#     return len(markCells)
# l4 = textLabel(m , "Number of steps",count_steps)


# m.run()