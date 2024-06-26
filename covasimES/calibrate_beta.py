import covasim as cv
import synthpops as sp
import numpy as np
import os


if __name__ == '__main__':
	s1=cv.load('pre_loaded_pop_1mil.sim')
	s1.pars['rand_seed']=1
	s1.pars['beta']=0.001*int(os.environ['SLURM_ARRAY_TASK_ID'])
	s1.pars['asymp_factor'] = 0.5
	s1.pars['prognoses']['symp_probs'] = np.array([2/3,2/3,2/3,2/3,2/3,2/3])
	s1.pars['prognoses']['sus_ORs']=np.array([1.00, 1.00, 1.00, 1.00, 1.00, 1.00])
	s1.pars['prognoses']['severe_probs'] = np.array([[0.00160713, 0.00028533, 0.00275317, 0.01002337, 0.03127049,0.10239177],
	[0.00337476, 0.00055796, 0.00624392, 0.02262656, 0.05201913,0.10404252],
	[0.00448164, 0.00041348, 0.00402159, 0.01304485, 0.02724936,0.07152225],
	[0.00293003, 0.00036179, 0.00338358, 0.01185876, 0.03454538,0.08936869],
	[0.00186566, 0.0002267 , 0.00145062, 0.00528454, 0.02139647,0.08835845]])
	s1.pars['prognoses']['crit_probs'] = np.array([[0.17261905, 0.22522523, 0.20588235, 0.21105528, 0.1878453 , 0.1251944 ],
	[0.21370968, 0.22171946, 0.15204678, 0.17806841, 0.16159696, 0.14935305],
    [0.2011893 , 0.27878788, 0.22222222, 0.16202946, 0.26237054,0.11384919],
    [0.17993631, 0.20422535, 0.18285714, 0.17670683, 0.17630597,0.11730449],
    [0.18009479, 0.26666667, 0.19277108, 0.20481928, 0.19418758,0.14875717]])
	s1.pars['prognoses']['death_probs'] = np.array([[0.01724138, 0.04      , 0.10714286, 0.16666667, 0.17058824,0.35403727],
	[0.01886792, 0.02040816, 0.07692308, 0.11864407, 0.1372549 ,0.26237624],
	[0.03448276, 0.10869565, 0.13461538, 0.17171717, 0.07894737,0.21645022],
	[0.02654867, 0.03448276, 0.09375   , 0.17045455, 0.16402116,0.28723404],
	[0.05263158, 0.08333333, 0.125     , 0.11764706, 0.19727891,0.35475578]])
	s1.run()
	infs = np.array(list(s1.results['infections_by_race_and_age'].values()))
	hosps = np.array(list(s1.results['hospitalization_by_race_and_age'].values()))
	deaths = np.array(list(s1.results['mortality_by_race_and_age'].values()))
	pops = np.array(list(s1.results['race_and_age'].values()))
	hr = hosps/pops
	hrr = np.ones((6, 5))
	for r in range(5):
		for a in range(6):
			if hr[a, 0] == 0:
				hr[a, 0] = 1 / pops[a, 0]
			hrr[a, r] = hr[a, r] / hr[a, 0]
	ind = int(os.environ['SLURM_ARRAY_TASK_ID'])
	np.savetxt("results/cal_b/same_sus_reff"+str(int(ind))+".txt",s1.results['r_eff'])