class Match:
    def __init__(self, strat1, strat2, nb_rounds=200):
        self.strat1 = strat1
        self.strat2 = strat2
        self.nb_rounds = nb_rounds
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

        for _ in range(self.nb_rounds):
            a1 = self.strat1.get_action(hist1, hist2)
            a2 = self.strat2.get_action(hist2, hist1)

            g1, g2 = self.payoffs[(a1, a2)]
            score1 += g1
            score2 += g2

            hist1.append(a1)
            hist2.append(a2)

        return score1, score2


class Tournament:
    def __init__(self, strategies, nb_parties=5, nb_rounds=200):
        self.strategies = strategies
        self.nb_parties = nb_parties
        self.nb_rounds = nb_rounds
        self.scores = {s.name: 0 for s in strategies}

    def run(self):
        for i, s1 in enumerate(self.strategies):
            for j, s2 in enumerate(self.strategies):
                if i != j: 
                    total_s1 = 0
                    for _ in range(self.nb_parties):
                        s1_score, _ = Match(s1, s2, self.nb_rounds).play()
                        total_s1 += s1_score
                    self.scores[s1.name] += total_s1
        
        return sorted(self.scores.items(), key=lambda x: x[1], reverse=True)