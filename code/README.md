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

Dit algoritme werkt met alle 6 netlists, met een relatief hoge kost.
Met gebruik van het genetisch algoritme om de netlist te sorteren, of de random layer methode, kan de kost verlaagd worden.

### A* algoritme (a_star.py)

A* is een algorimte dat altijd het kortste pad tussen twee punten vindt. 

A* werkt zonder toevoegingen alleen met netlist 1.
Met gebruik van het genetisch algoritme en/of de random layer methode werkt A* met alle 6 netlists, en met een lagere kost dan het greedy algoritme.


### Genetisch algoritme (genetic.py)

We maken willekeurige volgorden van onze netlist aan en selecteren zo de volgorden die een zo laag mogelijke totale kost hebben met A*, door meerdere generaties.


### shared_functions.py

Dit bestand bevat functies die gebruikt worden door meerdere algoritmes in verschillende files. 



