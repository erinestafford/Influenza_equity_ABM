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

    school_dists = []
    school_sizes = []
    workplace_dists = []
    workplace_avg_ages = []
    workplace_sizes=[]
    age_race_dists = {}
    bins = [0, 5, 18, 30, 40, 50, 60, 65, 75,100]
    age_bins = {0: [], 5: [], 18: [],30: [], 40: [], 50: [],60: [],65: [], 75: []}
    for i in range(100):
            age_race_dists[i]=[]

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
        for school in pop.schools:
            school_rd = pop.race_by_uid[school['student_uids']]
            school_size = len(school_rd)
            school_sizes.append(school_size)
            spw = 100 * sum(np.where(school_rd == 0, 1, 0)) / school_size
            spb = 100 * sum(np.where(school_rd == 1, 1, 0)) / school_size
            spaina = 100 * (sum(np.where(school_rd == 2, 1, 0))) / school_size
            spa = 100 * (sum(np.where(school_rd == 3, 1, 0))) / school_size
            sph = 100 * (sum(np.where(school_rd == 4, 1, 0))) / school_size
            school_dists.append([spw,spb,spaina,spa,sph])
        for workplace in pop.workplaces:
            workplace_rd = pop.race_by_uid[workplace['member_uids']]
            workplace_size=len(workplace_rd)
            workplace_avg_ages.append(np.mean(pop.age_by_uid[workplace['member_uids']]))
            workplace_sizes.append(workplace_size)
            wpw = 100 * sum(np.where(workplace_rd == 0, 1, 0)) / workplace_size
            wpb = 100 * sum(np.where(workplace_rd == 1, 1, 0)) / workplace_size
            wpaina = 100 * (sum(np.where(workplace_rd == 2, 1, 0))) / workplace_size
            wpa = 100 * (sum(np.where(workplace_rd == 3, 1, 0))) / workplace_size
            wph = 100 * (sum(np.where(workplace_rd == 4, 1, 0))) / workplace_size
            workplace_dists.append([wpw,wpb,wpaina,wpa,wph])
        bin_num = 1
        bins = [0, 5, 18, 30, 40, 50, 60, 65, 75,100]
        age_bins_temps = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
        for j in range(100):
            races_for_age = pop.race_by_uid[pop.age_by_uid == j]
            m = len(races_for_age )
            pwa = sum(np.where(races_for_age == 0, 1, 0))
            pba = sum(np.where(races_for_age == 1, 1, 0))
            painaa = sum(np.where(races_for_age == 2, 1, 0))
            paa = sum(np.where(races_for_age == 3, 1, 0))
            pha = sum(np.where(races_for_age == 4, 1, 0))
            age_race_dists[j].append([pwa/m,pba/m,painaa/m,paa/m,pha/m])
            if j < bins[bin_num]:
                age_bins_temps[bin_num-1,:] =age_bins_temps[bin_num-1,:]+np.array([pwa,pba,painaa,paa,pha])
            else:
                bin_num = bin_num+1
        bin_num = 0
        for bin in bins[:-1]:
            age_bins[bin].append(age_bins_temps[bin_num,:].tolist())
            bin_num = bin_num+1
        print(age_bins)




    np.savetxt("workplace_ages.txt", workplace_avg_ages)
    np.savetxt("workplace_sizes.txt",workplace_sizes)
    np.savetxt("workplace_dists.txt",workplace_dists)
    np.savetxt("school_dists.txt",school_dists)
    #for i in range(100): np.savetxt("age_race_dists"+str(i)+".txt",age_race_dists[i])
    b1 = np.array([0.597086872, 0.117896465, 0.007346395, 0.063847708, 0.193915297]) * 100;  # HH data
    b2 = np.array([0.591959799, 0.139698492, 0.013065327, 0.063316583, 0.191959799]) * 100;
    plt.bar(np.arange(5), b2, color='black');
    plt.plot([np.average(pw), np.average(pb), np.average(paina), np.average(pa), np.average(ph)], 'o-', markersize=10);
    print([np.average(pw), np.average(pb), np.average(paina), np.average(pa), np.average(ph)])
    plt.xticks([r for r in range(5)], ["W", "B", "AINA", "A", "H"], fontsize=20);

#pop.plot_contacts() # plot the contact matrix
plt.show() # display contact matrix to screen