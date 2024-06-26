import synthpops as sp
import numpy as np
import matplotlib.pyplot as plt
import random

if __name__ == '__main__':
    pw = np.zeros(100)
    pb = np.zeros(100)
    paina = np.zeros(100)
    pa = np.zeros(100)
    ph = np.zeros(100)

    for i in range(100):
        random.seed(i)
        n = 100000 # how many people in your population
        pop = sp.Pop(n, country_location='usa',state_location='Washington',location ='racial-diff-contacts-same') # create the population
        popdict=pop.to_dict()
        pw[i] =  100*sum(np.where(pop.race_by_uid==0,1,0))/n
        pb[i] = 100*sum(np.where(pop.race_by_uid ==1,1,0))/n
        paina[i] = 100*(sum(np.where(pop.race_by_uid == 2, 1, 0)))/n
        pa[i] = 100*(sum(np.where(pop.race_by_uid == 3, 1, 0)))/n
        ph[i] = 100*(sum(np.where(pop.race_by_uid == 4, 1, 0)))/n




    #for i in range(100): np.savetxt("age_race_dists"+str(i)+".txt",age_race_dists[i])
    b1 = np.array([0.597086872,0.117896465,0.007346395,0.063847708,0.193915297])*100; #HH data
    b2 = np.array([0.591959799, 0.139698492, 0.013065327, 0.063316583, 0.191959799])*100;
    plt.bar(np.arange(5),b2, color =  'black');
    plt.plot([np.average(pw),np.average(pb),np.average(paina),np.average(pa),np.average(ph)], 'o-', markersize = 10);
    print([np.average(pw),np.average(pb),np.average(paina),np.average(pa),np.average(ph)])
    plt.xticks([r for r in range(5)],["W", "B", "AINA", "A", "H"], fontsize = 20);


#pop.plot_contacts() # plot the contact matrix
plt.show() # display contact matrix to screen
