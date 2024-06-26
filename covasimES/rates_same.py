import covasim as cv
import synthpops as sp
import numpy as np
import os

pars = dict(
    pop_size=5000000,
    pop_type='synthpops',
    pop_infected=10,
    use_waning=False,
    start_day='2020-10-01',
    end_day='2021-05-01',
    verbose=0,
    rand_seed = np.random.rand()*float(os.environ['SLURM_ARRAY_TASK_ID'])
)


if __name__ == '__main__':
	s1 = cv.Sim(pars, label='Default')
	s1.popdict = cv.make_synthpop(s1, country_location='usa', state_location='Washington', location='racial-diff')
	#symptomatic rate changed based on vaccination rates
	# adults based on vaccination rates (2/3 - %vax*VE) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9620569/#:~:text=During%20the%202021–22%20season,among%20White%20and%20Asian%20adults
	# not considering children

	s1.pars['prognoses']['severe_probs']=np.array([[0.00204957, 0.00028594, 0.00050416, 0.00180137, 0.00869, 0.02671089],
												   [0.00204957, 0.00028594, 0.00050416, 0.00180137, 0.00869, 0.02671089],
												   [0.00204957, 0.00028594, 0.00050416, 0.00180137, 0.00869, 0.02671089],
												   [0.00204957, 0.00028594, 0.00050416, 0.00180137, 0.00869, 0.02671089],
												   [0.00204957, 0.00028594, 0.00050416, 0.00180137, 0.00869, 0.02671089]])
												   
       										
	s1.pars['prognoses']['crit_probs']=np.array([[0.17261905, 0.20422535, 0.15204678, 0.16202946, 0.16159696,0.11384919],
												 [0.17261905, 0.20422535, 0.15204678, 0.16202946, 0.16159696,0.11384919],
												 [0.17261905, 0.20422535, 0.15204678, 0.16202946, 0.16159696,0.11384919],
												 [0.17261905, 0.20422535, 0.15204678, 0.16202946, 0.16159696,0.11384919],
												 [0.17261905, 0.20422535, 0.15204678, 0.16202946, 0.16159696,0.11384919]])
												 
	s1.pars['prognoses']['death_probs']=np.array([[0.01724138, 0.02040816, 0.07692308, 0.11764706, 0.07894737,0.21645022],
												 [0.01724138, 0.02040816, 0.07692308, 0.11764706, 0.07894737, 0.21645022],
												 [0.01724138, 0.02040816, 0.07692308, 0.11764706, 0.07894737, 0.21645022],
												 [0.01724138, 0.02040816, 0.07692308, 0.11764706, 0.07894737, 0.21645022],
												 [0.01724138, 0.02040816, 0.07692308, 0.11764706, 0.07894737, 0.21645022]])

											 
	
	s1.run()
	infs = s1.results['infections_by_race_and_age']
	symp_infs = s1.results['symptomatic_infections_by_race_and_age']
	hosps = s1.results['hospitalization_by_race_and_age']
	icus = s1.results['icu_by_race_and_age']
	deaths = s1.results['mortality_by_race_and_age']
	pops = s1.results['race_and_age']
	hr = hosps/pops
	hrr = np.ones((6, 5))
	for r in range(5):
		for a in range(6):
			if hr[a, 0] == 0:
				hr[a, 0] = 1 / pops[a, 0]
			hrr[a, r] = hr[a, r] / hr[a, 0]
	ind = int(os.environ['SLURM_ARRAY_TASK_ID'])
	np.savetxt("results/rs_5mil/infections/i_num"+str(int(ind))+".txt",infs)
	np.savetxt("results/rs_5mil/symptomatic_infections/si_num" + str(int(ind)) + ".txt", symp_infs )
	np.savetxt("results/rs_5mil/hrr/hrr"+str(int(ind))+".txt",hrr)
	np.savetxt("results/rs_5mil/hospitalizations/h_num"+str(int(ind))+".txt",hosps)
	np.savetxt("results/rs_5mil/icu/icu_num" + str(int(ind)) + ".txt", icus)
	np.savetxt("results/rs_5mil/deaths/d_num"+str(int(ind))+".txt",deaths)
	np.savetxt("results/rs_5mil/r_eff/reff"+str(int(ind))+".txt",s1.results['r_eff'])
	np.savetxt("results/rs_5mil/pop/pop"+str(int(ind))+".txt",pops)