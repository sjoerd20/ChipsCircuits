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

### greedy algoritme (greedy.py)

Deterministisch algoritme 

### A* algoritme (a_star.py)

A* is een deterministisch algoritme. Dit algorimte vindt altijd het kortste pad tussen twee punten. 

Omdat A* in dit programma wordt gecombineerd met het niet-deterministische genetische algoritme, zijn de berekende oplossingen niet-deterministisch


### genetic heuristiek (genetic.py)

Dit is een niet-deterministisch algoritme


### shared_functions.py

Dit bestand bevat functies die gebruikt worden door meerdere algoritmes in verschillende files. 



