from collections import defaultdict
class Markov(object):
    bin  = '(q0)'
    def __init__(self):
        self.states = []
        self.x = defaultdict(lambda: defaultdict(float))
        self.yy = defaultdict(lambda: defaultdict(float))

    def add(self, curr_state, transition_dict={}, emission_dict={}):
        self.states.append(curr_state)
        for destination_state, prob in transition_dict.items():
            self.x[curr_state][destination_state] = prob
        for observation, prob in emission_dict.items():
            self.yy[curr_state][observation] = prob

    def algoForward(self, code):
        self.forward = [{}]
        for names in self.states:
            self.forward[0][names] = self.x[self.bin][names] * self.yy[names][code[0]]
        for rrs in range(1, len(code)):
            self.forward.append({})
            for names in self.states:
                self.forward[rrs][names] = sum((self.forward[rrs - 1][y0] * self.x[y0][
                    names] * self.yy[names][code[rrs]]) for y0 in self.states)
        prob = sum((self.forward[len(code) - 1][s]) for s in self.states)
        return prob
    def calculate_probability(self, observations):
        probability = self.algoForward(observations)
        print('Answer for {} = {}'.format(observations,probability))


Model = Markov()
Model.add(Markov.bin, dict(H=0.8, C=0.2))
Model.add('H', dict(H=0.7, C=0.3), {1: .2, 2: .4, 3: .4})
Model.add('C', dict(H=0.4, C=0.6), {1: .5, 2: .4, 3: .1})
Model.calculate_probability([3, 3, 1, 1, 2, 3, 3, 1, 2])
Model.calculate_probability([3, 3, 1, 1, 2, 2, 3, 1, 3])

# The probability for the given observation [3, 3, 1, 1, 2, 3, 3, 1, 2] is 3.9516275425280015e-05
# The probability for the given observation [3, 3, 1, 1, 2, 2, 3, 1, 3] is 3.575714750873601e-05