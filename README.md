<h1> Sportbetter Calculation Toolkit</h1>

<h2> Parlay Calculator </h2>

This is a quick parlay calculator that considers some of the common promos offered. It is used to identify profitable bets and promos from various sportsbooks. 
Currently, the calculator supports the following:

<ul>
  <li>Single Expected Value Calculator</li>
  <li>Parlay Expected Value Calculator Up to Any Number of Legs</li>
  <ul> Promos Supported:
    <li>Parlay Insurance where if a single leg loses, your money is returned
    </li>
    <li> Parlays where a free bet is awarded no matter win or lose. The user just adds the value of the free bet. </li>
    <li> Parlays where a free bet is only awarded in the case of a loss. </li>
  </ul>
</ul> 

<h3>Usage</h3>
For usage, one must run the program by typing:
```python parlayPromo.py```
This calculator was tested and verified using Python 3.8. 
From here, one can chose to either work with the command line interface or can chose to load a file. If one choses to load a file, make sure that file is in the directory of the calculator. (Move the examples.txt file into the source directory as an example)
There are a series of example files. Any future files must follow this exact format. "#" can be used for commented lines to keep track of legs. 

<h2>Positive EV Calculator </h2>
This calculator provides the expected value of a bet and its odds with respect to a true market evaluation. It removes the vig and is fully CLI based

<h3>Usage</h3>
For usage, one must run the program:
``` python evCalc.py ```
This calculator was tested and verified using Python 3.8. Follow the command line prompts to perform the calculation.


<h2>Freebet Calculator</h2>
This calculator provides the amount to hedge a free bet according to some given odds. It also will calculate the total payout and profit of hedging your freebet!

<h3>Usage</h3>
For usage, one must run the program:
``` python freeBetCalc.py ```
This calculator was tested and verified using Python 3.8. Follow the command line prompts to perform the calculation.

<h2>Arbitrage Calculator</h2>
This calculator provides the amount to hedge a arbitrage according to some given odds. It also will calculate the total payout and profit of hedging your arb!

<h3>Usage</h3>
For usage, one must run the program:
``` python arbCalc.py ```
This calculator was tested and verified using Python 3.8. Follow the command line prompts to perform the calculation.


<h2>Documentation</h2>
All documentation is stored in the docs setion. Please see this for a full explanation of all the math and methods in this program. 

<h2>Contributing</h2>
Contributions to add new promos are certainly welcomed. Please just make a pull request. 
