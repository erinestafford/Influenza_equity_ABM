import covasim as cv
import numpy as np
import sciris as sc

class CustomLayer(cv.Layer):
    ''' Create a custom layer that updates daily based on supplied contacts '''

    def __init__(self, layer, contact_data):
        ''' Convert an existing layer to a custom layer and store contact data '''
        for k,v in layer.items():
            self[k] = v
        self.contact_data = contact_data
        return

    def update(self, people):
        ''' Update the contacts '''
        pop_size = len(people)
        n_new = self.contact_data[people.t] # Pull out today's contacts
        self['p1']   = np.array(cv.choose_r(max_n=pop_size, n=n_new), dtype=cv.default_int) # Choose with replacement
        self['p2']   = np.array(cv.choose_r(max_n=pop_size, n=n_new), dtype=cv.default_int) # Paired contact
        self['beta'] = np.ones(n_new, dtype=cv.default_float) # Per-contact transmission (just 1.0)
        return


