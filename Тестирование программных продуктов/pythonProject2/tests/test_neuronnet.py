import pytest

from function.neuronnet import *

n = net(3, 2, 1)
n.weights(1, 0, 0, 0.3)
n.weights(1, 0, 1, 0.3)
n.weights(1, 0, 2, 0)
n.weights(1, 1, 0, 0.4)
n.weights(1, 1, 1, -0.6)
n.weights(1, 1, 2, 1)
n.weights(2, 0, 0, -1)
n.weights(2, 0, 1, 1)

p = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]


@pytest.mark.parametrize('a', p)
def test_neuron_predict(a):
    t = [[], [], []]
    if a[0] == 1:
        t[0] = 'с квартирой'
    else:
        t[0] = 'без квартиры'
    if a[1] == 1:
        t[1] = 'и слушает рок музыку,'
    else:
        t[1] = 'и слушает классическую музыку,'
    if a[2] == 1:
        t[2] = 'Симпатичный парень'
    else:
        t[2] = 'Уродливый парень'
    v = n.predict(a)
    if v[0] == 1:
        print('\n', t[2], t[0], t[1], 'ты мне нравишься, давай дружить')
    else:
        print('\n', t[2], t[0], t[1], 'мы с тобой созвонимся может быть потом')


def test_print_summary_neuronnet():
    print(n.summary())
