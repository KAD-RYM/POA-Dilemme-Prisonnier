import random
from moteur import TournamentGenerationnel
from strategies import AllD, RandomStrat, TitForTat, Tester, Joss, Pavlov, Pairman

if __name__ == "__main__":
    random.seed(42)

    strategies_classes = [AllD, RandomStrat, TitForTat, Tester, Joss, Pavlov, Pairman]

    w = 0.999
    nb_generations = 10
    nb_parties = 5

    tournoi_gen = TournamentGenerationnel(strategies_classes, nb_generations=nb_generations, nb_parties=nb_parties, w=w)
    historique = tournoi_gen.run_evolution()

    print("==================================================")
    print("  ÉVOLUTION INTERGÉNÉRATIONNELLE (Horizon Inconnu)")
    print("==================================================")
    for gen, data in enumerate(historique):
        print(f"Génération {gen + 1} (Durée moyenne des parties : {data['moyenne_tours']:.1f} tours) :")
        for nom, proportion in sorted(data['repartition'].items(), key=lambda x: x[1], reverse=True):
            print(f"  - {nom} : {proportion * 100:.2f}%")
        print("-" * 50)