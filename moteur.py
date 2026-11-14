import random

class MatchHorizonInconnu:
    def __init__(self, strat1, strat2, w=0.95):
        self.strat1 = strat1
        self.strat2 = strat2
        self.w = w
        self.payoffs = {
            ('C', 'C'): (3, 3),
            ('C', 'D'): (0, 5),
            ('D', 'C'): (5, 0),
            ('D', 'D'): (2, 2)
        }

    def play(self):
        self.strat1.reset()
        self.strat2.reset()
        hist1, hist2 = [], []
        score1, score2 = 0, 0
        nb_tours = 0

        while True:
            a1 = self.strat1.get_action(hist1, hist2)
            a2 = self.strat2.get_action(hist2, hist1)

            g1, g2 = self.payoffs[(a1, a2)]
            score1 += g1
            score2 += g2

            hist1.append(a1)
            hist2.append(a2)
            nb_tours += 1

            if random.random() > self.w:
                break

        return score1, score2, nb_tours


class TournamentHorizonInconnu:
    def __init__(self, strategies, nb_parties=5, w=0.95):
        self.strategies = strategies
        self.nb_parties = nb_parties
        self.w = w
        self.scores = {s.name: 0 for s in strategies}
        self.total_tours_global = 0
        self.nb_matchs_global = 0

    def run(self):
        for i, s1 in enumerate(self.strategies):
            for j, s2 in enumerate(self.strategies):
                if i != j:
                    for _ in range(self.nb_parties):
                        s1_score, _, nb_tours = MatchHorizonInconnu(s1, s2, self.w).play()
                        self.scores[s1.name] += s1_score
                        self.total_tours_global += nb_tours
                        self.nb_matchs_global += 1
                        
        moyenne_tours = self.total_tours_global / self.nb_matchs_global
        return sorted(self.scores.items(), key=lambda x: x[1], reverse=True), moyenne_tours


class TournamentGenerationnel:
    def __init__(self, strategies_classes, nb_generations=10, nb_parties=5, w=0.95):
        self.strategies_classes = strategies_classes
        self.nb_generations = nb_generations
        self.nb_parties = nb_parties
        self.w = w
        
        self.population = {sc(): 1.0 / len(strategies_classes) for sc in strategies_classes}

    def run_evolution(self):
        historique_pop = []
        
        for gen in range(self.nb_generations):
            repartition_actuelle = {strat.name: prop for strat, prop in self.population.items()}
            
            strategies_actives = list(self.population.keys())
            scores = {s.name: 0.0 for s in strategies_actives}
            
            total_tours_gen = 0
            nb_matchs_gen = 0
            
            # Tournoi de la génération
            for i, s1 in enumerate(strategies_actives):
                for j, s2 in enumerate(strategies_actives):
                    if i != j:
                        total_s1 = 0
                        for _ in range(self.nb_parties):
                            s1_score, _, nb_tours = MatchHorizonInconnu(s1, s2, self.w).play()
                            total_s1 += s1_score
                            total_tours_gen += nb_tours
                            nb_matchs_gen += 1
                            
                        scores[s1.name] += total_s1 * self.population[s2]

            moyenne_tours_gen = total_tours_gen / nb_matchs_gen if nb_matchs_gen > 0 else 0
            
            historique_pop.append({
                "repartition": repartition_actuelle,
                "moyenne_tours": moyenne_tours_gen
            })

            somme_scores = sum(scores.values())
            if somme_scores == 0:
                break
                
            nouvelle_population = {}
            for strat in strategies_actives:
                nouvelle_part = scores[strat.name] / somme_scores
                if nouvelle_part > 0.0001:
                    nouvelle_population[strat] = nouvelle_part
            
            self.population = nouvelle_population

        return historique_pop