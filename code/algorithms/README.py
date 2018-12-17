### Greedy algoritme (greedy.py)

Een algoritme dat direct van gate naar gate probeert te gaan, en simpelweg omhoog of omlaag gaat als het niet verder kan op dezelfde laag. 

### A* algoritme (a_star.py)

A* is een algorimte dat altijd het kortste pad tussen twee punten vindt. 

A* selecteert een pad die f(n) = g(n) + h(n) minimalizeert, waarbij n het volgende punt in de pad is, g(n) de kost van het pad tot n is, en h(n) de heuristiek is die de kost schat van n tot het doel.

### Genetisch algoritme (genetic.py)

We maken willekeurige volgorden van onze netlist aan en selecteren zo de volgorden die zo laag mogelijke totale kosten hebben met A*, door meerdere generaties. Elke generatie nemen we dan de beste volgorden (die de laagste kosten hebben met A*) en maken we kinderen uit paren van deze generatie door willekeurig steeds een net uit een van beide ouders over te nemen (als deze er al in zit pakken we een andere). Deze kinderen worden dan de nieuwe generatie en we herhalen het proces.

### shared_functions.py

Dit bestand bevat functies die gebruikt worden door meerdere algoritmes in verschillende files. 
