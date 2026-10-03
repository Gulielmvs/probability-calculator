import copy
import random


class Hat:

    def __init__(self, **ball):
        if not ball:
            raise TypeError('At least one ball is required')
        if not all(i > 0 for i in ball.values()):
            raise ValueError('A number greater than zero is required')
        self.contents = []
        for k, v in ball.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, number):
        if number > len(self.contents):
            result = self.contents[:]
            self.contents.clear()
            return result
        result = []
        for i in range(number):
            random_index = random.randint(0, len(self.contents) - 1)
            random_ball = self.contents.pop(random_index)
            result.append(random_ball)
        return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    times_found = 0
    # Copying contents
    duplicate = copy.deepcopy(hat.contents)
    for experiment in range(num_experiments):
        dict_drawn = {}
        list_drawn = hat.draw(num_balls_drawn)
        for item in list_drawn:
            dict_drawn[item] = dict_drawn.get(item, 0) + 1
        # Looking for matches in both dictionaries
        peer = 0
        for e_color, e_num in expected_balls.items():
            for d_color, d_num in dict_drawn.items():
                if e_color == d_color and e_num <= d_num:
                    peer += 1
        # count how many times
        if peer == len(expected_balls):
            times_found += 1
        # hat.contents.clear()
        # Restoring contents
        hat.contents = copy.deepcopy(duplicate)
    probability = times_found / num_experiments
    return probability
