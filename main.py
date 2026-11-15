import random
from strategies import AllD, RandomStrat, TitForTat, Tester, Joss, Pavlov, Pairman
from moteur import Match, MatchHorizonInconnu, Tournament, TournamentHorizonInconnu, TournamentGenerationnel

STRATEGIES_MAP = {
    "all-d": AllD,
    "random": RandomStrat,
    "tit-for-tat": TitForTat,
    "tester": Tester,
    "joss": Joss,
    "pavlov": Pavlov,
    "pairman": Pairman
}

def afficher_menu_strategies():
    print("\n--- Stratégies disponibles ---")
    for nom in STRATEGIES_MAP.keys():
        print(f" - {nom}")

def main():
    random.seed(42)
    
    print("==================================================")
    print("      SIMULATEUR DILEMME DU PRISONNIER      ")
    print("==================================================")

    print("1. Duel entre deux stratégies")
    print("2. Tournoi complet entre toutes les stratégies")
    print("3. Sélection intergénérationnelle")
    print("4. Quitter")
    
    choix_mode = input("\nChoisissez le mode (1, 2, 3 ou 4) : ").strip().lower()
    
    if choix_mode == "4":
        return

    if choix_mode == "1":
        afficher_menu_strategies()
        
        while True:
            nom1 = input("1ère stratégie : ").strip().lower()
            if nom1 in STRATEGIES_MAP: break
            print("Nom de stratégie invalide. Réessayez.")

        while True:
            nom2 = input("2ème stratégie : ").strip().lower()
            if nom2 in STRATEGIES_MAP: break
            print("Nom de stratégie invalide. Réessayez.")

        strat1 = STRATEGIES_MAP[nom1]()
        strat2 = STRATEGIES_MAP[nom2]()

        while True:
            type_horizon = input("Choisissez un type de partie : (1: Nombre de tours fixes | 2: Horizon inconnu) : ").strip()
            if type_horizon in ["1", "2"]: break
            print("Entrez 1 ou 2.")

        if type_horizon == "1":
            nb_rounds = int(input("Veuillez entrer le nombre de tours (ex: 200) : "))
            s1, s2 = Match(strat1, strat2, nb_rounds).play()
            print(f"\n--- Résultat Duel ({nb_rounds} tours) ---")
            print(f"{strat1.name} : {s1} pts | {strat2.name} : {s2} pts")
        else:
            w = float(input("Veuillez entrer la probabilité w (ex: 0.95) : "))
            s1, s2, nb_tours = MatchHorizonInconnu(strat1, strat2, w).play()
            print(f"\n--- Résultat Duel (Horizon w={w}, arrêté à {nb_tours} tours) ---")
            print(f"{strat1.name} : {s1} pts | {strat2.name} : {s2} pts")

    elif choix_mode == "2":
        population_classes = [AllD, RandomStrat, TitForTat, Tester, Joss, Pavlov, Pairman]
        
        while True:
            type_h = input("Choisissez un type de partie : (1: Nombre de tours fixes | 2: Horizon inconnu) : ").strip()
            if type_h in ["1", "2"]: break
            print("Entrez 1 ou 2.")

        if type_h == "1":
            nb_rounds = int(input("Veuillez entrer le nombre de tours (ex: 200) : "))
            tournoi = Tournament([sc() for sc in population_classes], nb_parties=5, nb_rounds=nb_rounds)
            classement = tournoi.run()
            print(f"\n--- CLASSEMENT : TOURNOI CLASSIQUE ({nb_rounds} tours) ---")
            for rang, (nom, score) in enumerate(classement, 1):
                print(f"{rang}. {nom} : {score} points")
        else:
            w = float(input("Veuillez entrer la probabilité w (ex: 0.95) : "))
            tournoi = TournamentHorizonInconnu([sc() for sc in population_classes], nb_parties=5, w=w)
            classement, moyenne_tours = tournoi.run()
            print(f"\n--- CLASSEMENT : HORIZON INCONNU (w={w}, moy: {moyenne_tours:.1f} tours) ---")
            for rang, (nom, score) in enumerate(classement, 1):
                print(f"{rang}. {nom} : {score} points")

    elif choix_mode == "3":
        population_classes = [AllD, RandomStrat, TitForTat, Tester, Joss, Pavlov, Pairman]
        
        while True:
            type_h = input("Choisissez un type de partie : (1: Nombre de tours fixes | 2: Horizon inconnu) : ").strip()
            if type_h in ["1", "2"]: break
            print("Entrez 1 ou 2.")

        if type_h == "1":
            nb_rounds = int(input("Veuillez entrer le nombre de tours (ex: 200) : "))
            nb_gen = int(input("Veuillez entrer le nombre de générations (ex: 10) : "))
            
            tournoi_gen = TournamentGenerationnel(population_classes, nb_generations=nb_gen, nb_parties=5, nb_rounds=nb_rounds)
            historique = tournoi_gen.run_evolution()
        else:
            w = float(input("Veuillez entrer la probabilité w (ex: 0.95) : "))
            nb_gen = int(input("Veuillez entrer le nombre de générations (ex: 10) : "))
            
            tournoi_gen = TournamentGenerationnel(population_classes, nb_generations=nb_gen, nb_parties=5, w=w)
            historique = tournoi_gen.run_evolution()
            
        print(f"\n--- ÉVOLUTION INTERGÉNÉRATIONNELLE ({nb_gen} génaration) ---")
        for gen, data in enumerate(historique):
            print(f"Génération {gen + 1} (Durée moy. : {data['moyenne_tours']:.1f} tours) :")
            for nom, proportion in sorted(data['repartition'].items(), key=lambda x: x[1], reverse=True):
                print(f"  - {nom} : {proportion * 100:.2f}%")
            print("-" * 40)
    else:
        print("Option invalide.")

if __name__ == "__main__":
    main()