import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

class hcf_test():
    nos 
    mean 
    stddev
    variance 
    strategy
    strategy_list = ("up-down-static")
#    distribution = "normal"
#    distribution_list = ("normal", "log_normal")

    def set_nos(nos):
        '''sets the number of specimen used for the staircase test'''
        self.nos = nos

    def return_nos():
        '''gets the number of specimen used for the staircase test'''
        return self.nos

    def set_mean(mean):
        self.mean = mean

    def get_mean():
        return self.mean

    def set_variance(variance):
        self.variance = variance
        self.stddev = np.sqrt(variance)

    def set_stddev(stddev):
        self.stddev = stddev
    
    def get_variance():
        return self.variance

    def set_strategy(strategy):
        assert (strategy in strategy_list)
        self.strategy = strategy

    def check_for_runout(value):
        
        rand = sp.stats.uniform.rvs()
        val = sp.stats.norm.cdf(value, self.mean, self.variance)        

        if rand >= val:
            return False
        else
            return True



