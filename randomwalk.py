from random import choice


class Ant:
    '''
    Ant class: keep track of the position, number of steps and status of each ant.
    '''

    def __init__(self):
        self.x = 0
        self.y = 0
        self.status = 'running'
        self.steps = 0

    # ant makes a step
    def step(self):
        if self.status == 'running':
            dx, dy = choice([(0, 1), (-1, 0), (0, -1), (1, 0)])
            self.x += dx
            self.y += dy
            self.steps += 1

    # checks whether ant has reached the boundary
    def boundary(self):
        x = self.x
        y = self.y
        out = (abs(x) == 2) or (abs(y) == 2)
        if out:
            self.status = 'stopped'


def generate(nb_ants, steps_limit):
    '''
    Generate a Random Walk of "nb_ants" and limits the number of steps for each to "steps_limit".
    '''
    # to compute the expected value of number of steps
    expected_value = 0
    # keep track of all running ants
    ants = [Ant() for _ in range(nb_ants)]
    while ants:
        for ant in ants:
            # ant takes a step
            ant.step()
            # ant stops if "steps_limit" is reached
            if ant.steps >= steps_limit:
                ant.status == 'stopped'
            # check for the boundary
            ant.boundary()
            # stop the ant
            if ant.status == 'stopped':
                ants.remove(ant)
                expected_value += ant.steps
    # return the expected value
    expected_value = expected_value/nb_ants
    print(expected_value)


if __name__ == '__main__':
    generate(1000, 100)
