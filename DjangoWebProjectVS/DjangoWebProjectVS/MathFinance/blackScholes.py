import numpy as np
import scipy.stats as ss
import time 

#Black and Scholes
def d1(S0, K, r, sigma, T):
    return (np.log(S0/K) + (r + sigma**2 / 2) * T)/(sigma * np.sqrt(T))
 
def d2(S0, K, r, sigma, T):
    return (np.log(S0 / K) + (r - sigma**2 / 2) * T) / (sigma * np.sqrt(T))

def BlackScholes(type : str, S0 : float, K : float, r : float, sigma : float, T : float) -> float:
    if type=="C":
        return S0 * ss.norm.cdf(d1(S0, K, r, sigma, T)) - K * np.exp(-r * T) * ss.norm.cdf(d2(S0, K, r, sigma, T))
    else:
       return K * np.exp(-r * T) * ss.norm.cdf(-d2(S0, K, r, sigma, T)) - S0 * ss.norm.cdf(-d1(S0, K, r, sigma, T))

##%% Test
#s=100.
#k=90.
#rate=0.01
#vol=0.2
#timeToExpiry='1.'
#optionType="C"

##%% output
#BlackScholes(optionType,s,k,rate,vol,timeToExpiry)