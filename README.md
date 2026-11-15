# Projet : Simulation du Dilemme du Prisonnier Itéré 

Projet réalisé dans le cadre du module de Programmation Orientée Objet / Systèmes Multi-Agents (Master 1 IASD). 

Ce projet implémente en Python orienté objet une simulation complète des tournois d'Axelrod basés sur le **Dilemme du Prisonnier Itéré**, incluant des stratégies classiques, des extensions tel que horizon inconnu pour ne pas connaître la fin réelle du tournois et des dynamiques évolutionnistes avec une sélection intergénérationnelle.

---

## Structure du Projet

```text
.
├── strategies.py      # Implémentation des classes de stratégies (All-D, Tit-For-Tat, etc.)
├── moteur.py          # Moteurs de match et de tournoi (Classique, Horizon Inconnu, Générationnel)
└── main.py            # Script principal interactif pour lancer les simulations
```

## Prérequis

- **Python 3.8** ou supérieur.
- Aucune bibliothèque externe n'est requise (le projet utilise uniquement les modules natifs de Python comme `random`).

---

## Utilisation

Le projet dispose d'un **script principal interactif** `main.py` qui permet de tester l'ensemble des fonctionnalités et des étapes du projet via un menu textuel sur le terminal.

Pour lancer le simulateur, exécutez la commande suivante dans ton terminal :

```bash
python3 main.py
```

Il suffit de suivre les instructions affichées dans le terminal pour tester les différentes stratégies et modes de jeu. 
Le menu interactif propose 3 grands modes :

1. Duel entre deux stratégies : Permet d'affronter directement deux stratégies au choix en choisissant soit un nombre de tours fixe, soit un horizon inconnu w.
2. Tournoi complet : Fait s'affronter l'ensemble de la population de stratégies (les 7 profils : All-D, Random, Tit-For-Tat, Tester, Joss, Pavlov, Pairman) avec un choix de durée de tours fixe, soit un horizon inconnu w.
3. Sélection Intergénérationnelle : Simule l'évolution de la population sur plusieurs générations où la proportion de chaque stratégie en fonction de ses scores cumulés.

## Stratégies Implémentées

- All-D : Trahit systématiquement.
- Random : Joue Coopérer ou Trahir de manière aléatoire (50/50).
- Tit-For-Tat : Coopère au premier tour, puis imite le dernier coup de l'adversaire.
- Tester : Trahit au premier tour, puis alterne selon la réaction de l'adversaire.
- Joss : Joue comme Tit-For-Tat mais trahit sournoisement de temps en temps.
- Pavlov : Répète son action si elle a rapporté gros, change sinon.
- Pairman : Analyse le comportement global de l'adversaire sur l'historique long pour ajuster sa coopération.

## Étapes du Projet couvertes

- Étape 1/2 : Tournois fermés et élargis sur un nombre de tours fixe (ex : 200 tours).
- Étape 3.1 : Introduction de l'Horizon Inconnu via une probabilité de continuation w.
- Étape 3.2 : Implémentation de la Sélection Intergénérationnelle pour observer le développement des stratégies sur le long terme.