import random
from moteur import Tournament
from strategies import AllD, RandomStrat, TitForTat, Tester, Joss

if __name__ == "__main__":
    random.seed(42)

    population = [
        AllD(),
        RandomStrat(),
        TitForTat(),
        Tester(),
        Joss()
    ]

    nb_parties = 5
    nb_rounds = 200

    tournoi = Tournament(population, nb_parties=nb_parties, nb_rounds=nb_rounds)
    classement = tournoi.run()

    print("==========================================")
    print("  CLASSEMENT DU TOURNOI DE BASE (200 tours) ")
    print("==========================================")
    for rang, (nom, score) in enumerate(classement, 1):
        print(f"{rang}. {nom} : {score} points")
    print("==========================================")