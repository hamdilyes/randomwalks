from random import choice
from tqdm import tqdm


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
        else:
            pass

    # checks whether ant has reached the boundary
    def boundary(self, type):
        x = self.x
        y = self.y
        if type == 'square':
            out = (abs(x) == 2) or (abs(y) == 2)
        elif type == 'diagonal':
            out = (x+y == 1)
        elif type == 'outer_disk':
            out = (((x-0.25)/3)**2 + ((y-0.25)/4)**2 >= 1)
        if out:
            self.status = 'stopped'


def generate(nb_ants, steps_limit, boundary_type='square'):
    '''
    Generate a Random Walk of "nb_ants" and limits the number of steps for each to "steps_limit".
    '''
    # print type
    print('##############################     ' +
          boundary_type.upper()+'     ##############################')
    # to compute the expected value of number of steps
    expected_value = 0
    # keep track of all running ants
    ants = [Ant() for _ in range(nb_ants)]
    # progress bar
    pbar = tqdm(total=nb_ants, desc='Stopped Ants')
    # one step at a time
    while ants:
        ants2 = ants.copy()
        for ant in ants:
            # ant takes a step
            ant.step()
            # ant stops if "steps_limit" is reached
            if ant.steps == steps_limit:
                ant.status = 'stopped'
            # check for the boundary
            ant.boundary(type=boundary_type)
            # stop the ant
            if ant.status == 'stopped':
                pbar.update(1)
                expected_value += ant.steps
                ants2.remove(ant)
        ants = ants2.copy()
    pbar.close()
    # return the expected value
    expected_value = expected_value/nb_ants
    expected_value = round(expected_value, 2)
    print('\n           Expected number of steps: %s \n' % expected_value)


if __name__ == '__main__':
    generate(nb_ants=100000, steps_limit=100, boundary_type='square')
    generate(nb_ants=100000, steps_limit=100, boundary_type='diagonal')
    generate(nb_ants=100000, steps_limit=100, boundary_type='outer_disk')
