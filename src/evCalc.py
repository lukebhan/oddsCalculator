import numpy as np

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

print("Welcome to the Positive EV Calculator!")
print("Please provide your stake, odds, and the current market odds!")
stake = input("Please provide your stake in dollars: ")
try:
    type(stake) is float or type(stake) is int
except:
    raise TypeError("Invalid Input for stake. Please give a number.")
odds = input("Please provide your bets odds with a - indicating a minus: ")
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

calculateEV(float(stake), int(odds), int(market1), int(market2), 1, True)
