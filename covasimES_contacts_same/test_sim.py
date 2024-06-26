import covasim as cv
import numpy as np

pars = dict(
    pop_size=1000,
    pop_type='synthpops',
    pop_infected=10,
    use_waning=False,
    start_day='2020-04-01',
    end_day='2020-08-01',
    verbose=0
)


if __name__ == '__main__':
    s1 = cv.Sim(pars)
    s1.popdict = cv.make_synthpop(s1, country_location='usa', state_location='Washington', location='rd-small-wp')
    s1.run()
    print("done")