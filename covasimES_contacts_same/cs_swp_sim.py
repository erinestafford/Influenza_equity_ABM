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
	s1.popdict = cv.make_synthpop(s1, country_location='usa', state_location='Washington', location='rd-small-wp')
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
	ind =int(os.environ['SLURM_ARRAY_TASK_ID'])
	np.savetxt("results/swp_5mil/infections/i_num"+str(int(ind))+".txt",infs)
	np.savetxt("results/swp_5mil/symptomatic_infections/si_num" + str(int(ind)) + ".txt", symp_infs )
	np.savetxt("results/swp_5mil/hrr/hrr"+str(int(ind))+".txt",hrr)
	np.savetxt("results/swp_5mil/hospitalizations/h_num"+str(int(ind))+".txt",hosps)
	np.savetxt("results/swp_5mil/icu/icu_num" + str(int(ind)) + ".txt", icus)
	np.savetxt("results/swp_5mil/deaths/d_num"+str(int(ind))+".txt",deaths)
	np.savetxt("results/swp_5mil/r_eff/reff"+str(int(ind))+".txt",s1.results['r_eff'])
	np.savetxt("results/swp_5mil/pop/pop"+str(int(ind))+".txt",pops)

	