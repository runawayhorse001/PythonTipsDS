import numpy as np
import scipy.stats as stats
import inspect

def t_test(x, y=None, mu=0.0, conf_level=0.95):
    """
    Performs one and two sample t-tests on vectors of data.\n
    same functions as t.test in r: ``t.test(x, ...)``\n
    ``t.test(x, y = NULL,``\n
           ``alternative = c("two.sided", "less", "greater"),``\n
           ``mu = 0, paired = FALSE, var.equal = FALSE,``\n
           ``conf.level = 0.95, ...)``

    :param x: a (non-empty) numeric vector of data values.
    :param y: an optional (non-empty) numeric vector of data values.
    :param mu: vector of standard deviations.
    :param conf_level: confidence level of the interval.    
    :return: the vector of the random numbers.  

    :author: Wenqiang Feng
    :email:  von198@gmail.com
    """
    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1]
    string = inspect.getframeinfo(frame[0]).code_context[0].strip()
    args = string[string.find('(') + 1:-1].split(',')

    names = []
    for i in args:
        if i.find('=') != -1:
            names.append(i.split('=')[1].strip())

        else:
            names.append(i)

    #print(names)
   
    
    if y==None:
        t , p = stats.ttest_1samp(x,popmean=mu)
        n = len(x) # lenth of the the list
        df = n-1   # degree of the freedom
        sigma = np.std(x)/np.sqrt(df)  # Sample stdev/sample size
        (lower, upper) = stats.t.interval(
                         0.95,  # Confidence level
                         df = df, # Degrees of freedom
                         loc = np.mean(x), # Sample mean
                         scale= sigma) # Standard dev estimate 

    s = f"""
    {'-'*80}
    #       One Sample t-test
    # data:  {names}
    # t = {t}, df = {df}, p-value = {p}
    # alternative hypothesis: true mean is not equal to {mu}
    # {conf_level*100} percent confidence interval:
    # {lower}, {upper} 
    # mean of x 
    #         {np.mean(x)}
    {'-'*80}
    """
    print(s)

