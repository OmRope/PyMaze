from pymaze import maze,COLOR,agent
from agents import *

alogrithms = {1:'BFS',2:'DFS',3:'A star'}

def run_maze(x=10,y=10,loopPercent=0,algo='BFS',start=None,end=(1,1)):
    m=maze(x,y)
    m.CreateMaze(loopPercent=loopPercent,x=end[0],y=end[1])
    a=agent(m,footprints=True,filled=True,shape='arrow')
    if algo=='BFS':
        bSearch,bfsPath,fwdPath=BFS(m,start)
        if start==None:
            c=agent(m,end[0],end[1],footprints=True,color=COLOR.green,shape='square',filled=True,goal=(m.rows,m.cols))
            a=agent(m,footprints=True,color=COLOR.blue,shape='square',filled=True)
            b=agent(m,footprints=True,color=COLOR.red,shape='arrow',filled=False)
        else:
            a=agent(m,start[0],start[1],footprints=True,color=COLOR.blue,shape='square',filled=True)
            b=agent(m,start[0],start[1],footprints=True,color=COLOR.red,shape='arrow',filled=False)
            c=agent(m,end[0],end[1],footprints=True,color=COLOR.green,shape='square',filled=True,goal=(start[0],start[1]))

        m.tracePath({a:bSearch},delay=100)
        m.tracePath({c:bfsPath},delay=100)
        m.tracePath({b:fwdPath},delay=100)
        m.run()
    if algo=='DFS':
        dSearch,dfsPath,fwdPath=DFS(m,start)
        if start==None:
            c=agent(m,end[0],end[1],footprints=True,color=COLOR.green,shape='square',filled=True,goal=(m.rows,m.cols))
            a=agent(m,footprints=True,color=COLOR.blue,shape='square',filled=True)
            b=agent(m,footprints=True,color=COLOR.red,shape='arrow',filled=False)
        else:
            a=agent(m,start[0],start[1],footprints=True,color=COLOR.blue,shape='square',filled=True)
            b=agent(m,start[0],start[1],footprints=True,color=COLOR.red,shape='arrow',filled=False)
            c=agent(m,end[0],end[1],footprints=True,color=COLOR.green,shape='square',filled=True,goal=(start[0],start[1]))

        m.tracePath({a:dSearch},delay=100)
        m.tracePath({c:dfsPath},delay=100)
        m.tracePath({b:fwdPath},delay=100)

        m.run()

    if algo=='A star':
        aSearch,aPath,fwdPath=aStar(m,start)
        if start==None:
            c=agent(m,end[0],end[1],footprints=True,color=COLOR.green,shape='square',filled=True,goal=(m.rows,m.cols))
            a=agent(m,footprints=True,color=COLOR.blue,shape='square',filled=True)
            b=agent(m,footprints=True,color=COLOR.red,shape='arrow',filled=False)
        else:
            a=agent(m,start[0],start[1],footprints=True,color=COLOR.blue,shape='square',filled=True)
            b=agent(m,start[0],start[1],footprints=True,color=COLOR.red,shape='arrow',filled=False)
            c=agent(m,end[0],end[1],footprints=True,color=COLOR.green,shape='square',filled=True,goal=(start[0],start[1]))

        m.tracePath({a:aSearch},delay=100)
        m.tracePath({c:aPath},delay=100)
        m.tracePath({b:fwdPath},delay=100)

        m.run()

    if algo=='Dijkstra':
        dSearch,dPath,fwdPath=dijkstra(m,start)
        if start==None:
            c=agent(m,end[0],end[1],footprints=True,color=COLOR.green,shape='square',filled=True,goal=(m.rows,m.cols))
            a=agent(m,footprints=True,color=COLOR.blue,shape='square',filled=True)
            b=agent(m,footprints=True,color=COLOR.red,shape='arrow',filled=False)
        else:
            a=agent(m,start[0],start[1],footprints=True,color=COLOR.blue,shape='square',filled=True)
            b=agent(m,start[0],start[1],footprints=True,color=COLOR.red,shape='arrow',filled=False)
            c=agent(m,end[0],end[1],footprints=True,color=COLOR.green,shape='square',filled=True,goal=(start[0],start[1]))

        m.tracePath({a:dSearch},delay=100)
        m.tracePath({c:dPath},delay=100)
        m.tracePath({b:fwdPath},delay=100)

        m.run()

def compare_algo(x=10,y=10,loopPercent=0,aglo_1='BFS',algo_2='DFS',end=(1,1)):
    m=maze(x,y)
    m.CreateMaze(loopPercent=loopPercent,x=end[0],y=end[1])
    a=agent(m,footprints=True,filled=True,shape='arrow')

    searchPath,aPath,fwdPath=aStar(myMaze)
    bSearch,bfsPath,fwdBFSPath=BFS(myMaze)

    l=textLabel(myMaze,'A-Star Path Length',len(fwdPath)+1)
    l=textLabel(myMaze,'BFS Path Length',len(fwdBFSPath)+1)
    l=textLabel(myMaze,'A-Star Search Length',len(searchPath)+1)
    l=textLabel(myMaze,'BFS Search Length',len(bSearch)+1)

    a=agent(myMaze,footprints=True,color=COLOR.cyan,filled=True)
    b=agent(myMaze,footprints=True,color=COLOR.yellow)
    myMaze.tracePath({a:fwdBFSPath},delay=50)
    myMaze.tracePath({b:fwdPath},delay=50)

    t1=timeit(stmt='aStar(myMaze)',number=10,globals=globals())
    t2=timeit(stmt='BFS(myMaze)',number=10,globals=globals())

    textLabel(myMaze,'A-Star Time',t1)
    textLabel(myMaze,'BFS Time',t2)


    myMaze.run()
if __name__=='__main__':
    x=int(input("Enter Maze's rows: "))
    y=int(input("Enter Maze's cols: "))
    loop_per=int(input("Enter Loop percent(1-100):"))
    print("Do you want to give end coordinates\n1 : yes\n2 : No")
    choice = int(input())
    end=None
    if choice==1:
        x_cord=int(input(f"X cord (1-{x}): "))
        y_cord=int(input(f"Y cord (1-{y}): "))
        end=(x_cord,y_cord)
    else:
        end=(1,1)
    print("Do you want compare algorithms\n1 : yes\n2 : No")
    choice = int(input())
    if choice==1:
        print("Choose First Algorithm : ")
        for i,algo in alogrithms.items():
            print(f'{i} : {algo}')
        algo_1 = int(input("First Algorithm : "))
        algo_2 = int(input("Second Algorithm : "))
        compare_algo(x=x,y=y,loopPercent=loop_per,end=end,algo_1=algo_1,algo_2=algo_2)

    else:
        print("Choose from the following alogrithm to Complete the Maze")
        for i,algo in alogrithms.items():
            print(f'{i} : {algo}')
        choice = int(input())
            
        run_maze(x=x,y=y,loopPercent=loop_per,end=end,algo=alogrithms[choice])
    