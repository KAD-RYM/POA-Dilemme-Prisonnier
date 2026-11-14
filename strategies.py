import random

class Strategy:
    def __init__(self, name):
        self.name = name
    
    def reset(self):
        """Réinitialise l'état interne de la stratégie entre deux matchs si nécessaire."""
        pass

    def get_action(self, my_history, opp_history):
        raise NotImplementedError


class AllD(Strategy):
    def __init__(self):
        super().__init__("ALL-D")
    
    def get_action(self, my_history, opp_history):
        return 'D'


class RandomStrat(Strategy):
    def __init__(self):
        super().__init__("RANDOM")
    
    def get_action(self, my_history, opp_history):
        return random.choice(['C', 'D'])


class TitForTat(Strategy):
    def __init__(self):
        super().__init__("TIT-FOR-TAT")
    
    def get_action(self, my_history, opp_history):
        if not opp_history:
            return 'C'
        return opp_history[-1]


class Tester(Strategy):
    def __init__(self):
        super().__init__("TESTER")
    
    def reset(self):
        pass

    def get_action(self, my_history, opp_history):
        t = len(my_history)
        if t == 0:
            return 'D'
        if opp_history[-1] == 'D' and t == 1:
            return opp_history[-1]
        sequence = ['C', 'C', 'D']
        return sequence[t % len(sequence)]


class Joss(Strategy):
    def __init__(self):
        super().__init__("JOSS")
        self.tft = TitForTat()
    
    def reset(self):
        self.tft.reset()

    def get_action(self, my_history, opp_history):
        action = self.tft.get_action(my_history, opp_history)
        if action == 'C' and random.random() < 0.10:
            return 'D'
        return action

class Pavlov(Strategy):
    def __init__(self):
        super().__init__("PAVLOV")
        self.last_my_action = 'C'
        self.last_opp_action = 'C'

    def reset(self):
        self.last_my_action = 'C'
        self.last_opp_action = 'C'

    def get_action(self, my_history, opp_history):
        if not my_history:
            return 'C'
        
        # Dernier coup joués
        m = my_history[-1]
        o = opp_history[-1]
        
        # Si le score précédent était bon (C,C -> 3,3 ou D,C -> 5,0), on garde la même action
        # S'il était mauvais (C,D -> 0,5 ou D,D -> 2,2), on change d'action
        if (m, o) in [('C', 'C'), ('D', 'C')]:
            return m
        else:
            return 'D' if m == 'C' else 'C'

class Pairman(Strategy):
    def __init__(self):
        super().__init__("PAIRMAN")

    def get_action(self, my_history, opp_history):
        if not opp_history:
            return 'C'
        # Compte le nombre total de D et de C joués par l'adversaire
        nb_d = opp_history.count('D')
        nb_c = opp_history.count('C')
        
        if nb_d > nb_c:
            return 'D'
        return 'C'