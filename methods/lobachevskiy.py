import numpy as np


def normalize(polynomial):
    if (polynomial[0] < 0):
        polynomial = [-el for el in polynomial]
    return polynomial


def end_condition(prev, next, eps):
    N = len(prev)
    l = np.array(N)
    l.fill(1)
    diff = l - [next[i] / (prev[i] ** 2) for i in range(N)]
    return np.sqrt(diff.dot(diff)) < eps


def squared(polynomial):
    N = len(polynomial)
    new_polynomial = np.zeros(N)
    for k in range(0, N):
        tail = np.zeros(N)
        for j in range(1, N - k):
            if k - j < 0 or k + 1 > N:
                break
            tail[j - 1] = (1 if j % 2 == 0 else -1) * polynomial[k - j] * polynomial[k + j]
        new_polynomial[k] = polynomial[k] ** 2 + 2 * sum(tail)
    return new_polynomial


def calculate_polynomial(x, original_polynomial):
    return sum((x ** (i + 1)) * original_polynomial[i] for i in range(len(original_polynomial)))


def select_roots(roots, original_polynomial):
    return [-root
            if
            abs(calculate_polynomial(-root, original_polynomial)) < abs(
                calculate_polynomial(root, original_polynomial))
            else root for root in
            roots]


def roots(polynomial, p, original_polynomial):
    xs = []
    N = len(polynomial)
    power = 1 / (2 ** p)
    for i in range(0, N - 1):
        a = polynomial[N - i - 2]
        b = polynomial[N - i - 1]
        xs.append((a / b) ** power)
    return select_roots(xs, original_polynomial)


def process(polynomial, eps=1e-3):
    polynomial.reverse()
    polynomial = normalize(polynomial)
    prev_pol = polynomial
    p = 1
    while True:
        new_pol = squared(prev_pol)
        if end_condition(prev_pol, new_pol, eps):
            return roots(new_pol, p, polynomial)
        prev_pol = new_pol
        p += 1
