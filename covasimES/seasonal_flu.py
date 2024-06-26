import covasim as cv
import synthpops as sp
import numpy as np
import os


if __name__ == '__main__':
	s1=cv.load('pre_loaded_pop_1mil.sim')
	s1.pars['rand_seed']=np.random.rand()*float(os.environ['SLURM_ARRAY_TASK_ID'])#change to random seed
	s1.pars['beta']=0.018
	#age_cutoffs=np.array([0, 5, 18, 50, 65, 75])
	#https://cdn.jamanetwork.com/ama/content_public/journal/jamanetworkopen/938744/zoi210646supp1_prod_1629209780.30356.pdf?Expires=1695694562&Signature=CLSsbGQV7TQQCBYh7vJw~zy7WMzTAAitqVaQLCye78ASbuRhs93cXZbdniHyYF3phi17MQpGz3lAc0PfLWhtUdq0E9tWmWYBM2oOzDT2pZ3GLB3Ahq04O9aTJX1vUUoneVGANqBisryb6pNA1AyhdeK~ipDwZQJmGf0ZtHobRKfEmxoW03d96Np~lhvwpplBlmcJf3B1M874e~cH8WDDa96nspcnaeDe8ZJeFPwcAqkHXMwkTRk47EBA87ZO9vwchHmjVwuQLOFVry1FEsO9EUoSi6A8Yvr-z2HUwkuOwxbLPfQJ7VSotE0OBUNCHnzsv8L58TeWTk0gnIa7M~TW8Q__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA
	s1.pars['asymp_factor'] = 0.5
	s1.pars['prognoses']['symp_probs'] = np.array([2.0/3.0,2.0/3.0,2.0/3.0,2.0/3.0,2.0/3.0,2.0/3.0])
	s1.pars['prognoses']['sus_ORs']=np.array([1.00, 1.00, 1.00, 1.00, 1.00, 1.00])
	#change to equally susceptible
	s1.pars['prognoses']['severe_probs'] = np.array([[0.00099543, 0.00020524, 0.00103698, 0.00372349, 0.01181774,0.03881003],
	[0.00210766, 0.00040415, 0.00233935, 0.0082774 , 0.01908901,0.03940482],
	[0.00279201, 0.00029904, 0.00150905, 0.00455371, 0.009658  ,0.02609111],
	[0.00182221, 0.0002603 , 0.0012907 , 0.00442529, 0.01271878,0.03364786],
	[0.00117092, 0.00016417, 0.00055515, 0.00196907, 0.00806355,0.03335155]])
	#np.array([[0.00107142, 0.00019022, 0.00183545, 0.00668225, 0.02084699,0.06826118],
	#[0.00224984, 0.00037197, 0.00416261, 0.01508437, 0.03467942,0.06936168],
	#[0.00298776, 0.00027565, 0.00268106, 0.00869657, 0.01816624,0.0476815 ],
	#[0.00195335, 0.00024119, 0.00225572, 0.00790584, 0.02303025,0.05957913],
	#[0.00124377, 0.00015113, 0.00096708, 0.00352303, 0.01426431,0.05890563]])
	#np.array([[0.00160713, 0.00028533, 0.00275317, 0.01002337, 0.03127049,0.10239177],
	#[0.00337476, 0.00055796, 0.00624392, 0.02262656, 0.05201913,0.10404252],
	#[0.00448164, 0.00041348, 0.00402159, 0.01304485, 0.02724936,0.07152225],
	#[0.00293003, 0.00036179, 0.00338358, 0.01185876, 0.03454538,0.08936869],
	#[0.00186566, 0.0002267 , 0.00145062, 0.00528454, 0.02139647,0.08835845]])
	s1.pars['prognoses']['crit_probs'] = np.array([[0.17261905, 0.22522523, 0.20588235, 0.21105528, 0.1878453 ,0.1251944 ],
	[0.21370968, 0.22171946, 0.15204678, 0.17806841, 0.16159696,0.14935305],
	[0.2011893 , 0.27878788, 0.22222222, 0.16202946, 0.26237054,0.11384919],
	[0.17993631, 0.20422535, 0.18285714, 0.17670683, 0.17630597,0.11730449],
	[0.18009479, 0.26666667, 0.19277108, 0.20481928, 0.19418758,0.14875717]])
	#np.array([[0.17261905, 0.22522523, 0.20588235, 0.21105528, 0.1878453 , 0.1251944 ],
	#[0.21370968, 0.22171946, 0.15204678, 0.17806841, 0.16159696, 0.14935305],
    #[0.2011893 , 0.27878788, 0.22222222, 0.16202946, 0.26237054,0.11384919],
    #[0.17993631, 0.20422535, 0.18285714, 0.17670683, 0.17630597,0.11730449],
    #[0.18009479, 0.26666667, 0.19277108, 0.20481928, 0.19418758,0.14875717]])
	s1.pars['prognoses']['death_probs'] = np.array([[0.01724138, 0.04      , 0.10714286, 0.16666667, 0.17058824, 0.35403727],
	[0.01886792, 0.02040816, 0.07692308, 0.11864407, 0.1372549 ,0.26237624],
	[0.03448276, 0.10869565, 0.13461538, 0.17171717, 0.07894737,0.21645022],
	[0.02654867, 0.03448276, 0.09375   , 0.17045455, 0.16402116,0.28723404],
	[0.05263158, 0.08333333, 0.125     , 0.11764706, 0.19727891,0.35475578]])
	#np.array([[0.01724138, 0.04      , 0.10714286, 0.16666667, 0.17058824,0.35403727],
	#[0.01886792, 0.02040816, 0.07692308, 0.11864407, 0.1372549 ,0.26237624],
	#[0.03448276, 0.10869565, 0.13461538, 0.17171717, 0.07894737,0.21645022],
	#[0.02654867, 0.03448276, 0.09375   , 0.17045455, 0.16402116,0.28723404],
	#[0.05263158, 0.08333333, 0.125     , 0.11764706, 0.19727891,0.35475578]])
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
	np.savetxt("results/seasonal_flu/infections/si_num_beta0.018_"+str(int(ind))+".txt",infs)
	np.savetxt("results/seasonal_flu/hrr/hrr_beta0.018_"+str(int(ind))+".txt",hrr)
	np.savetxt("results/seasonal_flu/hosps/h_num_beta0.018_"+str(int(ind))+".txt",hosps)
	np.savetxt("results/seasonal_flu/deaths/d_num_beta0.018_"+str(int(ind))+".txt",deaths)
	np.savetxt("results/seasonal_flu/reff/reff_beta0.018_"+str(int(ind))+".txt",s1.results['r_eff'])