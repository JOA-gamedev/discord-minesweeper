import random

gridl=8
bombs=5
colormode = False

grid=[]
for c in range(gridl):
    grid.append([])
    for u in range(gridl):
        grid[c].append(0)

b=0
while b < bombs:
    x=random.randrange(0,gridl)
    y=random.randrange(0,gridl)
    if(not grid[x][y]<0):
        grid[x][y]=-1*bombs-1
        b=b+1

for a in range(gridl):
    for b in range(gridl):
        if(grid[a][b]<0):
            if(a+1<gridl):
                grid[a+1][b]=grid[a+1][b]+1
            if(a-1>-1):
                grid[a-1][b]=grid[a-1][b]+1
            if(b+1<gridl):
                grid[a][b+1]=grid[a][b+1]+1
            if(b-1>-1):
                grid[a][b-1]=grid[a][b-1]+1
            if(a+1<gridl and b+1<gridl):
                grid[a+1][b+1]=grid[a+1][b+1]+1
            if(a-1>-1 and b-1>-1):
                grid[a-1][b-1]=grid[a-1][b-1]+1
            if(a+1<gridl and b-1>-1):
                grid[a+1][b-1]=grid[a+1][b-1]+1
            if(a-1>-1 and b+1<gridl):
                grid[a-1][b+1]=grid[a-1][b+1]+1

minesweeper = ""
for yg in grid:
    for xg in yg:
        if(xg>-1 and xg<11):
            if(colormode):
                if(xg==0):
                    minesweeper += "||🟩||"
                if(xg==1):
                    minesweeper += "||🟨||"
                if(xg==2):
                    minesweeper += "||🟧||"
                if(xg==3):
                    minesweeper += "||🟥||"
                if(xg==4):
                    minesweeper += "||🟦||"
                if(xg==5):
                    minesweeper += "||🟪||"
                if(xg==6):
                    minesweeper += "||🟫||"
                if(xg==7):
                    minesweeper += "||⬛||"
                if(xg==8):
                    minesweeper += "||⬜||"
            else:
                minesweeper += "||"+str(xg) + "⃣"+"||"
        else:
            minesweeper += "||💥||"
    minesweeper += "\n"

print(minesweeper)
print("there are", bombs, "bombs")
print(gridl, "x", gridl, "grid")
print("colormode is", colormode)
print("made by JOACHIM")
