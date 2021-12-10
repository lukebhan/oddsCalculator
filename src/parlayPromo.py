import numpy as np

def convertAmericanToDecimal(odds):
    if odds > 0:
        return odds/100+1
    else:
        return 1-(100/(odds))

def convertDecimalToAmerican(odds):
    if odds > 2:
        return (odds-1)*100
    else:
        return (-100)/(odds-1)

# Calculates the implied odds of a market
def calculateImplied(market1):
    if market1 < 0:
        imp = market1*-1/(market1*-1+100)*100
    else:
        imp = 100/(market1+100)*100
    return imp / 100

# Calculates the true probability after removing vig. Returns the tuple (p1, p2, vig taken)
def calculateTrueProb(odds1, odds2):
    totalOdds = odds1 + odds2
    return odds1/totalOdds, odds2/totalOdds, totalOdds - 1

def calculatePayout(stake, odds):
    if odds < 0:
        return stake*100/odds*-1 + stake
    else:
        return stake*odds/100+stake

def calculateEV(stake, odds, market1, market2, marketToCompare, verbose=False):
    imp1 = calculateImplied(market1)
    imp2 = calculateImplied(market2)
    prob1, prob2, vig = calculateTrueProb(imp1, imp2)
    payout = calculatePayout(stake, odds)
    if marketToCompare == 1:
        ev = prob1*(payout-stake)-prob2*stake
    else:
        ev = prob2*(payout-stake)-prob1*stake
    if verbose:
        print("True Probabilities of Market 1 and Market 2")
        print("M1:", np.around(prob1, 4), "M2:", np.around(prob2, 4))
        print("The book is taking", np.around(vig*stake, 2), "dollars in vig(", np.around(vig, 4), " percent)")
        print("The expected value on a stake of", stake, "with payout of", payout, "is", np.around(ev, 4), "or", np.around(ev/stake, 4), "percent!")
    return ev, prob1

def readFile(f):
    line = f.readline()
    numLegs = None
    steak = None
    odds= None
    while numLegs is None or steak is None or odds is None:
        if line[0]== "#" or line[0] == "\n":
            line = f.readline()
            continue;
        else:
            if numLegs is None:
                numLegs = int(line)
            elif steak is None:
                steak = float(line)
            elif odds is None:
                odds = int(line)
            line = f.readline()
    parlayRes = []
    for i in range(numLegs):
        res, m1, m2 = readParlay(f)
        parlayRes.append([res, m1, m2])
    return numLegs, steak, odds, parlayRes

def readParlay(f):
    odds = None
    marketOdds1 = None
    marketOdds2 = None
    line = f.readline()
    while odds is None or marketOdds1 is None or marketOdds2 is None:
        if line[0]== "#" or line[0] == "\n":
            line = f.readline()
            continue;
        else:
            if odds is None:
                odds = int(line)
            elif marketOdds1 is None:
                marketOdds1 = int(line)
            elif marketOdds2 is None:
                marketOdds2 = int(line)
            line = f.readline()
    return odds, marketOdds1, marketOdds2

def readBonus(f):
    bonus = None
    freebet = None
    line = f.readline()
    while bonus is None:
        if line[0]== "#" or line[0] == "\n":
            line = f.readline()
            continue;
        else:
            bonus = int(line)
            line = f.readline()
    if bonus==3 or bonus==4:
        while freebet is None:
            if line[0]== "#" or line[0] == "\n":
                line = f.readline()
                continue;
            else:
                freebet = float(line)
        return bonus, freebet
    else:
        return bonus,None 

evValues = []
probArray = []


print("Welcome to the Parlay Calculator!")
print("Please provide your stake, odds, and the current market odds for item each parlay!\nThen, you will have the oppurtunity to chose from a set of supported promos.\n")

load = input("Odds can be loaded via file or via CLI, please give 0 for file or 1 for CLI ")
try:
    type(load) is int
except:
    raise TypeError("Invalid load option. Please give a integer")

if load == 1:
    numLegs = input("Please provide the number of legs: ")
    try:
        type(numLegs) is int
    except: 
        raise TypeError("Invalid number of legs. Please give a integer")

    stake = input("Please provide your stake in dollars: ")
    try:
        type(stake) is float or type(stake) is int
    except:
        raise TypeError("Invalid Input for stake. Please give a number.")
    obtainedOdds = input("Please provide leg total parlay odds with any profit bonuses and - indicating a minus: ")
    try:
        type(obtainedOdds) is int
    except: 
        raise TypeError("Invalid Input for Odds. Please give a Integer.")


    for i in range(int(numLegs)):
        odds = input("\nPlease provide leg " + str(i+1) + " odds with a - indicating a minus: ")
        try:
            type(odds) is int
        except: 
            raise TypeError("Invalid Input for Odds. Please give a Integer.")
        market1 = input("Please provide the market's odds for your bet: ")
        try:
            type(market1) is int
        except:
            raise TypeError("Invalid Input for Market Odds. Please give a Integer.")
        market2 = input("please provide the opposite side odd's for your bet: ")
        try:
            type(market2) is int
        except:
            raise TypeError("Invalid Input for Market Odds. Please give a Integer.")
        ev, prob = (calculateEV(1, int(odds), int(market1), int(market2), 1, False))
        evValues.append(ev)
        probArray.append(prob)

else: 
    fileName = input("Please give the input file name ")
    try:
        f = open(fileName, 'r')
    except:
        raise TypeError("Filename is invalid. Please check the spelling and that it is in the current directory")
    legs, stake, obtainedOdds, legValues = readFile(f)
    decOddsExpec =1
    decOddsExpecMarket = 1
    for i in range(legs): 
        ev, prob = calculateEV(1, int(legValues[i][0]), int(legValues[i][1]), int(legValues[i][2]), 1, False)
        evValues.append(ev)
        probArray.append(prob)
        decOddsExpec *= convertAmericanToDecimal(legValues[i][0])
        decOddsExpecMarket *= convertAmericanToDecimal(legValues[i][1])

print("\n")
for idx, item in enumerate(evValues):
    print("The expected value for leg " + str(idx+1) +" is", np.around(item, 4), "with win percentage", np.around(probArray[idx], 4))
probWin = np.prod(np.array(probArray))
payout = calculatePayout(stake, obtainedOdds)
print("The expected payout for a stake of", stake, "is", payout)
print("The win percentage is", probWin)
print("The no juice odds on your book should be given for parlay as", convertDecimalToAmerican(decOddsExpec-1))
print("The no juice market odds should be given for parlay as", convertDecimalToAmerican(decOddsExpecMarket-1))
print("The expected value for this parlay is", np.around((payout-stake)*probWin - stake*(1-probWin), 4), " for the steak or", np.around(((payout-stake)*probWin - stake*(1-probWin))/stake, 4), "percent")

print("\nCurrently Bonus Options:")
print("Option 1: No Promo")
print("Option 2: Parlay if only 1 leg misses, get money back")
print("Option 3: Parlay where you get a free bet no matter. In the case of a player, give the line. For example, get a free bet for najee harris rushing yards, just insert the over/under line for najee harris yards in this option.")
print("Option 4: Parlay where you get a free bet if loses. Same scenario as above just only pays bonus if we lose\n")
bonus = None
freebet = None

if load == 1:
    bonus = input("Please select a bonus option by providing the numer")
    try:
        type(bonus) is int
    except:
        raise TypeError("Bonus option is not valid. Please enter a integer")

    if bonus == 3 or bonus == 4:
        freebet = input("Please give the free bet value")
        try:
            type(freebet) is float
        except:
            raise TypeError("Free bet value is in valid")
else: 
    bonus, freebet = readBonus(f)


if bonus==1:
    print("Goodbye!")
elif bonus==2:
    # for bonus 2 we get the probability one leg misses. To do this, we need to iterate over each probability as following:
    probOneMisses = 0
    for i in range(len(probArray)):
        currentProb = 1
        for j in range(len(probArray)):
            #This is the leg that will miss
            if i == j:
                currentProb *= 1-probArray[j]
            else:
                currentProb *= probArray[j]
        probOneMisses += currentProb
    print("The probability that only one leg misses is", probOneMisses)
    print("The joint probability that either we win or one leg misses is", probOneMisses+probWin)
    print("With the insurance the expected value for this parlay is", np.around((payout-stake)*probWin - stake*(1-probWin-probOneMisses), 4), "or", np.around(((payout-stake)*probWin - stake*(1-probWin-probOneMisses))/stake, 4), "percent.")
elif bonus==3:
    print("With the free bet no matter win/lose the expected value for this parlay is", np.around(freebet*0.75+(payout-stake)*probWin - stake*(1-probWin), 4), "or", np.around((freebet*0.75+(payout-stake)*probWin - stake*(1-probWin))/stake, 4), "percent. For pessimism, we discount the bet to 0.75 its value.")
elif bonus==4:
    print("With the free bet if lose the expected value for this parlay is",np.around((payout-stake)*probWin - (freebet+stake)*(1-probWin), 4), "or", np.around(((payout-stake)*probWin - (stake+freebet)*(1-probWin))/stake, 4), "percent. For pessimism, we discount the bet to 0.75 its value.")





    

