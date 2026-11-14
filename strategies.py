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