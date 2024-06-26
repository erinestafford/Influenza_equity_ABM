def protect_elderly(sim):
    if sim.t == sim.day('2020-04-01'):
        elderly = sim.people.age>70
        sim.people.rel_sus[elderly] = 0.0

def protect_the_prime(sim):
    if sim.t == sim.day('2020-04-01'):
        are_prime = sim.people.prime
        sim.people.rel_sus[are_prime] = 0.0

