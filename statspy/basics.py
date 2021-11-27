import numpy as np
from scipy.stats import norm
   
def rnorm(n, mean=0, sd=1):
    """
    Random generation for the normal distribution with mean 
    equal to mean and standard deviation equation to sd
    same functions as rnorm in r: ``rnorm(n, mean=0, sd=1)``

    :param n: the number of the observations
    :param mean: vector of means
    :param sd: vector of standard deviations
    :return: the vector of the random numbers  

    :author: Wenqiang Feng
    :email:  von198@gmail.com
    """
    return norm.rvs(loc=mean, scale=sd, size=n)

def dnorm(x, mean=0, sd=1, log=False):
    """
    Density of the normal distribution with mean 
    equal to mean and standard deviation equation to sd
    same functions as rnorm in r: ``dnorm(x, mean=0, sd=1, log=FALSE)``

    :param x: the vector od quantiles
    :param mean: vector of means
    :param sd: vector of standard deviations
    :return: the list of the density  

    :author: Wenqiang Feng
    :email:  von198@gmail.com    
    """
    if log:
        return np.log(norm.pdf(x=x, loc=mean, scale=sd))
    else:
        return norm.pdf(x=x, loc=mean, scale=sd)

def runif(n, min=0, max=1):
    """
    Random generation from the uniform distribution
    same functions as rnorm in r: ``runif(n, min=0, max=1)``

    :param n: the number of the observations
    :param min: the lower limit of the distribution 
    :param max: the upper limit of the distribution
    :return: the list of n uniform random numers 

    :author: Wenqiang Feng
    :email:  von198@gmail.com  
    """
    return np.random.uniform(min, max, size=n)

