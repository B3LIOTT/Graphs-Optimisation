# Motivation
Voir ```Synthèse.pdf``` pour plus de détails sur la motivation de ce projet.

# Uitlisation
Pour lancer une résolution sur un graphe:
```python main.py <exercice> <alg type> <filename>```

Exercices: 1=Shortest path, 2=Traveling salesman
Alg types:
- Exercice 1: 1=CPLEX, 2=A*
- Exercice 2: 1=CPLEX, 2=Brute force

Info: Le fichier de graphe pour le probleme du plus court chemin doit etre dans le dossier 'graphes', ou dans 'graphes2' pour le Voyageur de Commerce.

# Format des données
Plus court chemin:
Le tableau contient uniquement des valeurs entières dans {0, 3} selon les règles suivantes : 
- un 1 représente une case qui peut être parcourue,
- un 0 une case associée à un obstacle.
- Les valeurs 2 et 3 sont particulières et représentent respectivement le départ et l’arrivée, qui peuvent se trouver n’importe où dans le réseau.

Voyageur de Commerce:
La première ligne contient le nombre de sommets du graphe et le nombre d’arêtes, séparés par un espace.
On a ensuite autant de lignes qu’il y a d’arêtes, avec sur chaque ligne les numéros des deux sommets incidents à l’arête et le coût de cette arête, avec un espace entre chaque valeur.
Les sommets sont numérotés à partir de 0.
Le graphe doit être complet.


