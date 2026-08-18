from posydon.popsyn.synthetic_population import BinaryPopulation
from posydon.popsyn.io import binarypop_kwargs_from_ini
from posydon.utils.common_functions import convert_metallicity_to_string
import argparse

if __name__ == "__main__":
    from posydon.popsyn.synthetic_population import BinaryPopulation
    from posydon.binary_evol.simulationproperties import SimulationProperties
    from posydon.popsyn.io import binarypop_kwargs_from_ini
    from posydon.utils.common_functions import convert_metallicity_to_string
    import argparse
    from posydon.popsyn.io import simprop_kwargs_from_ini
    ini_kw = binarypop_kwargs_from_ini('./my_population_params.ini')
    sim_kw = simprop_kwargs_from_ini('./my_population_params.ini')
    #print(ini_kw)
    ini_kw['metallicity'] = 1.0
    ini_kw['file_name'] = './solar_DNS.h5'
    sim_prop = SimulationProperties(**sim_kw)
    poprun = BinaryPopulation(population_properties=sim_prop,**ini_kw)
    poprun.evolve(from_hdf=True)
    poprun.save('./rerun_solar_DNS.h5' )