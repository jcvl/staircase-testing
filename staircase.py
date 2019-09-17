import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import unittest

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
        ''' sets mean of the underlying distribution.
            Input needs to be a real number
        '''
    try:
        np.all(np.isreal(mean)) ==True 
    except ValueError:
        print ('Given Value must be a real number')
    else:
        print ('No exception')

        self.mean = mean

    def get_mean():
        '''returns mean of the underlying distribution'''
        return self.mean

    def set_variance(variance):
       ''' sets variance and standard deviation of underlying distribution
           value needs tobe a positive real number
        ''' 
        try:
            np.all(np.isreal(variance)) == True
            np.all(variance) >= 0 
        except ValueError:
            print ('Given Value must be a positive real number')
        else:
            print ('No exception')
        
        self.variance = variance
        self.stddev = np.sqrt(variance)

    def set_stddev(stddev):
       ''' sets variance and standard deviation of underlying distribution
           value needs tobe a positive real number
        ''' 
        try:
            np.all(np.isreal(variance)) == True
            np.all(variance) >= 0 
        except ValueError:
            print ('Given Value must be a positive real number')
        else:
            print ('No exception')
        self.stddev = stddev
        self.variance = np.power(stddev, 2)
    
    def get_variance():
        return self.variance

    def get_stddev():
        return self.stddev
    
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



class TestStringMethods(unittest.TestCase):

    def test_mean_real(self):
        self.assertRaises(ValueError, hcf_test.set_mean("string"))

    def test_var_positive_real(self):
        self.assertRaises(ValueError, hcf_test.set_variance("string")
        self.assertRaises(ValueError, hcf_test.set_variance(-42)

if __name__ == '__main__':
    unittest.main()
