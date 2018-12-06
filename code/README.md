# Code

## In deze map

### classChip.py

Dit bestand bevat 3 classes: Node, Path, Chip.

* Node:
    * Representeert een kruising op een Manhattan grid
    * Bevat coordinaten en gegevens of de node bezet of een gate is.
* Path
    * Representeert een pad tussen 2 punten
    * Bevat alle nodes in een pad en de bijbehorende net
* Chip
    * Representeert de chip
    * Bevat alle nodes van de chip

### load_data.py

Dit bestand laad de gegeven netlists.

### visualization.py

Dit bestand bevat de code voor alle visualizaties van het probleem en de oplossingen. Er zijn twee soortn evaluaties beschikbaar: een 2D plot per laag van de chip en een 3D representatie van de volledige chip. 

## Algorithms

We gebruiken twee pathfinding algoritmes: greedy en A*.
Beide algoritmen zijn deterministisch, maar deze lopen vast bij grotere netlists, omdat een gate bijvoorbeeld geen buren meer heeft.

Hiervoor hebben we twee oplossingen, die beiden een niet-deterministische oplossing verkrijgen:
* Het gebruik van een genetisch algoritme om de netlist te sorteren, zodat A* wél werkt
* Elke net eerst naar een willekeurige laag van de chip te sturen, om de dichtheid van nets te verminderen

### Greedy algoritme (greedy.py)

Een algoritme dat direct van gate naar gate probeert te gaan, en simpelweg omhoog of omlaag gaat als het niet verder kan op dezelfde laag. 

Dit algoritme werkt met alle 6 netlists, met relatief hoge kosten.

### A* algoritme (a_star.py)

A* is een algorimte dat altijd het kortste pad tussen twee punten vindt. 

A* selecteert een pad die f(n) = g(n) + h(n) minimalizeert, waarbij n het volgende punt in de pad is, g(n) de kost van het pad tot n is, en h(n) de heuristiek is die de kost schat van n tot het doel.

A* werkt zonder toevoegingen alleen met netlist 1.
Met gebruik van het genetisch algoritme en/of de random layer methode werkt A* met alle 6 netlists, en met een lagere kost dan het greedy algoritme.

### Genetisch algoritme (genetic.py)

We maken willekeurige volgorden van onze netlist aan en selecteren zo de volgorden die zo laag mogelijke totale kosten hebben met A*, door meerdere generaties. Elke generatie nemen we dan de beste volgorden (die de laagste kosten hebben met A*) en maken we kinderen uit paren van deze generatie door willekeurig steeds een net uit een van beide ouders over te nemen (als deze er al in zit pakken we een andere). Deze kinderen worden dan de nieuwe generatie en we herhalen het proces.

### shared_functions.py

Dit bestand bevat functies die gebruikt worden door meerdere algoritmes in verschillende files. 



