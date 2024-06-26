import covasim as cv
import synthpops as sp
import numpy as np
import os


if __name__ == '__main__':
	s1=cv.load('cs_1mil.sim')
	s1.pars['rand_seed']=np.random.rand()*float(os.environ['SLURM_ARRAY_TASK_ID'])
	
	s1.pars['prognoses']['severe_probs'] = np.array([[0.0011992 , 0.00025604, 0.00055188, 0.00223684, 0.01007447,0.03337418],
													 [0.00252844, 0.00049197, 0.00111484, 0.00463642, 0.01376219,0.0277261 ],
													 [0.00302885, 0.00034811, 0.00073016, 0.0024266 , 0.00890802, 0.02308576],
													 [0.00147914, 0.00020053, 0.00037253, 0.00134229, 0.00819395,0.03213332],
													 [0.00196771, 0.0003054 , 0.00058204, 0.00217546, 0.00810932,0.02164382]])
	
	s1.pars['prognoses']['crit_probs'] = np.array([[0.17261905, 0.22522523, 0.20588235, 0.21105528, 0.1878453 ,0.1251944 ],
												   [0.21370968, 0.22171946, 0.15204678, 0.17806841, 0.16159696,0.14935305],
												   [0.2011893 , 0.27878788, 0.22222222, 0.16202946, 0.26237054,0.11384919],
												   [0.17924528, 0.26666667, 0.19277108, 0.20481928, 0.19418758,0.14875717],
												   [0.17993631, 0.20422535, 0.18285714, 0.17670683, 0.17630597,0.11730449]])
	s1.pars['prognoses']['death_probs'] = np.array([[0.01724138, 0.04      , 0.10714286, 0.16666667, 0.17058824,0.35403727],
													[0.01886792, 0.02040816, 0.07692308, 0.11864407, 0.1372549 ,0.26237624],
													[0.03448276, 0.10869565, 0.13461538, 0.17171717, 0.07894737,0.21645022],
													[0.05263158, 0.08333333, 0.125     , 0.11764706, 0.19727891,0.35475578],
													[0.02654867, 0.03448276, 0.09375   , 0.17045455, 0.16402116, 0.28723404]])
	#symptomatic rate changed based on vaccination rates
	# adults based on vaccination rates (2/3 - %vax*VE) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9620569/#:~:text=During%20the%202021–22%20season,among%20White%20and%20Asian%20adults
	# not considering children
									 
	s1.pars['prognoses']['symp_probs'] = np.array([[2.0/3.0,2.0/3.0,0.46866667, 0.39566667, 0.28816667, 0.28816667],
												   [2.0/3.0,2.0/3.0,0.51966667, 0.41416667, 0.32766667, 0.32766667],
												   [2.0/3.0,2.0/3.0,0.50416667, 0.46416667, 0.28466667, 0.28466667],
												   [2.0/3.0,2.0/3.0,0.40616667, 0.38916667, 0.26966667, 0.26966667],
												   [2.0/3.0,2.0/3.0,0.50666667, 0.43166667, 0.34066667, 0.34066667]])
	# relative susceptibility same
	s1.pars['prognoses']['sus_ORs']=np.array([[1.00, 1.00, 1.00, 1.00, 1.00, 1.00],
											  [1.00, 1.00, 1.00, 1.00, 1.00, 1.00],
											  [1.00, 1.00, 1.00, 1.00, 1.00, 1.00],
											  [1.00, 1.00, 1.00, 1.00, 1.00, 1.00],
											  [1.00, 1.00, 1.00, 1.00, 1.00, 1.00]])
	s1.run()
	infs = np.array(list(s1.results['infections_by_race_and_age'].values()))
	symp_infs = np.array(list(s1.results['symptomatic_infections_by_race_and_age'].values()))
	hosps = np.array(list(s1.results['hospitalization_by_race_and_age'].values()))
	icus = np.array(list(s1.results['icu_by_race_and_age'].values()))
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
	np.savetxt("results/cs/cs_i_num"+str(int(ind))+".txt",infs)
	np.savetxt("results/cs/cs_si_num" + str(int(ind)) + ".txt", symp_infs )
	np.savetxt("results/cs/cs_hrr"+str(int(ind))+".txt",hrr)
	np.savetxt("results/cs/cs_h_num"+str(int(ind))+".txt",hosps)
	np.savetxt("results/cs/cs_icu_num" + str(int(ind)) + ".txt", icus)
	np.savetxt("results/cs/cs_d_num"+str(int(ind))+".txt",deaths)
	np.savetxt("results/cs/cs_reff"+str(int(ind))+".txt",s1.results['r_eff'])

	