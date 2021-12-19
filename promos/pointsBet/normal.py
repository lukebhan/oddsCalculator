import numpy as np
import matplotlib.pyplot as plt


def classifyPt(point, stake, hedge):
    # Assume we hedge the under line
    pt = int(point)
    # Add 21 point cap for example
    if pt > 10 or pt < -10:
        if pt > 0:
            pt = 10
        else:
            pt = -10
    if pt > 2:
        return (pt-2)*stake - hedge
    else: 
        return (pt-2)*stake + ((pt-2)*stake*-0.75) + (hedge*100/150+hedge)

def getEV(pointsList):
    cnt = 0
    for item in pointsList:
        cnt += item/10000
    return cnt

def winPtc(pointsList):
    cnt = 0
    for item in pointsList:
        if item > 0:
            cnt += 1
    return cnt / len(pointsList)
stake = 150
data = np.random.normal(0, 13, 10000)
ev = []
count = 0
hedgeList = np.linspace(0, 1000, 100)
evArr = []
winPtcArr=  []
stakeArr = []
for hedge in hedgeList:
    ev = []
    for val in data:
        ev.append(classifyPt(val, stake, hedge))
    winPtcArr.append(winPtc(ev))
    evArr.append(getEV(ev)/(stake+hedge))
    stakeArr.append(hedge)
print(max(winPtcArr))
plt.plot(stakeArr, winPtcArr, label="Win Percentage")
plt.plot(stakeArr, evArr, label="EV Percentage")
plt.xlabel("Hedge Amnt")
plt.ylabel("Expected Multiplied Money")
plt.legend()
plt.show()

