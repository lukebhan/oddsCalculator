import numpy as np

def calculatePayout(stake, odds):
    if odds < 0:
        return stake*100/odds*-1 + stake
    else:
        return stake*odds/100+stake

print("Welcome to the FreeBet Calculator!")
print("This calculator allows you to quickly calculate the hedge bet for a freebet")
print("Please provide your freebet size, odds for the bet and odds for the hedge bet")
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
hedge = input("Please provide the odds for your hedge bet: ")
try:
    type(hedge) is int
except: 
    raise TypeError("Invalid Input for Hedging. Please give a Integer.")
hedge = int(hedge)
if hedge >= 0:
    hedgeProb = 1+hedge/100
else:
    hedgeProb = 1+100/(hedge*-1)
val = np.around((calculatePayout(int(stake), int(odds))-float(stake))/(hedgeProb), 2)
print("You need ", val, " for your hedge bet!")
print("You will spend a total of", val, "for a payout of",np.around(calculatePayout(val, hedge), 4), "with a profit of", np.around(calculatePayout(val, hedge)-val, 4))
