from scipy.stats import expon
from numpy import exp, ceil

from scipy.optimize import root_scalar

class ExponMixture:

    def __init__(self, ps, scales):
        self.ps = ps
        self.scales = scales
        self.expons = []
        for scale in scales:
            self.expons.append(expon(scale=scale))

    def pdf(self, x):
        result = 0.0
        for p, rv in zip(self.ps, self.expons):
            result += p*rv.pdf(x)
        return result

    def cdf(self, x):
        result = 0.0
        for p, rv in zip(self.ps, self.expons):
            result += p*rv.cdf(x)
        return result

    def sf(self, x):
        return 1.0 - self.cdf(x)

    def partial_exp(self, x):
        result = 0.0
        for p, a in zip(self.ps, self.scales):
            result -= p*((x+a)*exp(-x/a) - a)
        return result

    def find_restart_time(self, n=0.0):
        b = 1.5 * n
        solution = root_scalar(self.__condition, args=(b), x0=10.0 * (b+1.0), x1=b, method='secant', xtol=1.0)
        return ceil(solution.root + b)

    def __condition(self, t, b):
        F = self.cdf(t)
        result = (F - 1.0) * t
        result += F * (1 - F) / (self.pdf(t))
        result -= self.partial_exp(t)
        return result - b