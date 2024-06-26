import synthpops as sp
import numpy as np
import matplotlib.pyplot as plt
import random

if __name__ == '__main__':
   n = 10000
   pop = sp.Pop(n, country_location='usa',state_location='Washington',location ='racial-diff')
   popdict=pop.to_dict()

