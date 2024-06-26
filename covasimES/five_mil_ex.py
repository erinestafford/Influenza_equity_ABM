import covasim as cv
import synthpops as sp
import numpy as np
import os

pars = dict(
    pop_size=5000000,
    pop_type='synthpops',
    pop_infected=10,
    use_waning=False,
    start_day='2020-04-01',
    end_day='2020-08-01',
    verbose=0,
    beta = 0.006
)

if __name__ == '__main__':
	s1 = cv.Sim(pars, label='No Intervention')
	s1.popdict = cv.make_synthpop(s1, country_location='usa', state_location='Washington', location='racial-diff')
	s1.pars['rand_seed']=int(os.environ['SLURM_ARRAY_TASK_ID'])
	s1.pars['prognoses']['severe_probs'] = np.array([[1, 1, 1, 1, 1, 1],
	[2.21, 1.99, 2.52, 2.50, 1.74, 1.05],
	[3.00, 1.48, 1.72, 1.54, 0.96, 0.79],
	[1.26, 0.81, 0.61, 0.63, 0.84, 1.02],
	[1.87, 1.28, 1.29, 1.25, 1.18, 0.93]]) * np.array([0.0002, 0.002, 0.02,0.02,0.2,0.2])
	#np.array([0.11, 0.021, 0.0021, 0.0021, 0.21,0.21])  
	# assuming 75% hosps become critical (guess) and 50% die (from scenario) for each age
	s1.pars['prognoses']['crit_probs'] = np.array([[0.75, 0.75, 0.75, 0.75, 0.75, 0.75],
	[0.75, 0.75, 0.75, 0.75, 0.75, 0.75],
	[0.75, 0.75, 0.75, 0.75, 0.75, 0.75],
	[0.75, 0.75, 0.75, 0.75, 0.75, 0.75],
	[0.75, 0.75, 0.75, 0.75, 0.75, 0.75]])
	#np.array([[1., 1., 1., 1., 1.,1. ],
	#[1.239819, 1.00502513, 0.73412698, 0.836, 0.86206897,1.2],
	#[1.17, 1.27027027, 1.06976744, 0.75974026, 1.39583333,0.91139241],
	#[1.03968254, 1.19753086, 0.93442623, 0.96825397, 1.03571429,1.18627451],
	#[1.04812834, 0.90625, 0.88372093, 0.832, 0.94067797,0.94623656]])* np.array([0.75, 0.75, 0.75, 0.75, 0.75, 0.75])
	s1.pars['prognoses']['death_probs'] = np.array([[0.64, 0.69, 0.69, 0.69, 0.69, 0.69],
	[0.64, 0.69, 0.69, 0.69, 0.69, 0.69],
	[0.64, 0.69, 0.69, 0.69, 0.69, 0.69],
	[0.64, 0.69, 0.69, 0.69, 0.69, 0.69],
	[0.64, 0.69, 0.69, 0.69, 0.69, 0.69]])
	#np.array([[1., 1., 1., 1., 1.,1.],
	#[1.23722628, 0.595, 0.65945946, 0.73205742, 0.79333333,0.73809524],
	#[1.91168091, 2.21808511, 1.19565217, 1.05982906, 0.44776119,0.61111111],
	#[3.32061069, 1.59793814, 0.96491228, 0.75409836, 1.14942529,1.00826446],
	#[1.52040816, 0.68965517, 0.93859649, 1.03846154, 0.96396396,0.80681818]]) * np.array([0.64, 0.69, 0.69, 0.69, 0.69, 0.69])
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
	np.savetxt("results/res5mil/i_num"+str(int(ind))+".txt",infs)
	np.savetxt("results/res5mil/hrr"+str(int(ind))+".txt",hrr)
	np.savetxt("results/res5mil/h_num"+str(int(ind))+".txt",hosps)
	np.savetxt("results/res5mil/d_num"+str(int(ind))+".txt",deaths)
	np.savetxt("results/res5mil/reff"+str(int(ind))+".txt",s1.results['r_eff'])