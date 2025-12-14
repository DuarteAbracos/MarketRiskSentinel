import numpy as np
from scipy.stats import norm


class ParametricVar:

    def __init__(self, confidence, horizon):
        self.confidence = confidence
        self.horizon = horizon

    def calculate_risk(self, returns):
        average = np.mean(returns) * self.horizon
        sigma = np.std(returns) * np.sqrt(self.horizon)
        z_score = norm.ppf(1 - self.confidence)

        var = average + (z_score*sigma)
        return var