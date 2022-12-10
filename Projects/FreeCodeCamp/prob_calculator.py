import copy
import random
print('Scientific Computing with Python - FreeCodeCamp')
print('Project: Probability Calculator')

class Hat:

    def __init__(self, **kwargs):
        self.balls = dict(**kwargs)
        self.contents = []
        self.color = list(self.balls)
        self.quantity = list(self.balls.values())

        for x in range(0, len(self.balls)):
            for n in range(0, self.quantity[x]):
                self.contents.append(self.color[x])

        self.all_balls = copy.copy(self.contents)

    def draw(self, number):

        draw_balls = []

        if number > len(self.contents):
            return self.contents
        else:
            for n in range(0, number):
                ball = random.choice(self.contents)
                draw_balls.append(ball)
                self.contents.remove(ball)
            return draw_balls

hat = Hat(black=6, red=4, green=3)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    # This function calculates the probability of getting the expect balls
    # in each draw experiment.
    m = 0
    expected_balls = Hat(**expected_balls)

    for n in range(0, num_experiments):

        draw = hat.draw(num_balls_drawn)
        draw = [ball for ball in draw if ball in expected_balls.contents]
        check = all([draw.count(item) >= expected_balls.contents.count(item)
                     for item in hat.all_balls])
        if check:
            m += 1

        # For each draw it is necessary to put the balls once again in the hat.
        hat.contents = copy.copy(hat.all_balls)
    return m / num_experiments

random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)

# Outputs - Probability: 0.17066666666666666

'''
Project description: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator
'''