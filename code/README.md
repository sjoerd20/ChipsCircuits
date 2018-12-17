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

### algorithms/

We gebruiken twee pathfinding algoritmes: greedy en A*.
Beide algoritmen zijn deterministisch, maar deze lopen vast bij grotere netlists, omdat een gate bijvoorbeeld geen buren meer heeft.

Hiervoor hebben we oplossingen:
* Het gebruik van een genetisch algoritme om de netlist te sorteren
* Het gebruik van een heuristiek om te voorkomen buren in te sluiten
