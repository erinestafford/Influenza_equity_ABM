import covasim as cv
import synthpops as sp
import numpy as np
import os

pars = dict(
    pop_size=1000000,
    pop_type='synthpops',
    pop_infected=10,
    use_waning=False,
    start_day='2020-10-01',
    end_day='2021-05-01',
    verbose=0
)
if __name__ == '__main__':
    s1 = cv.Sim(pars, label='Default')
    s1.popdict = cv.make_synthpop(s1, country_location='usa', state_location='Washington', location='rd-small-wp')
    s1.save(filename='~/covasimES_contacts_same/swp_1mil.sim', keep_people=True)
    
    s2 = cv.Sim(pars, label='Default')
    s2.popdict = cv.make_synthpop(s2, country_location='usa', state_location='Washington', location='rd-wmp')
    s2.save(filename='~/covasimES_contacts_same/wmp_1mil.sim', keep_people=True)
    print("done")