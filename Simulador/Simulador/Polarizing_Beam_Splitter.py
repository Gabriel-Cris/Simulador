import numpy as np

def Polarizing_Beam_Splitter(photons_states_after_beam_splitter, number_of_photons):
    """
    Calcula os estados dos fótons após passarem pelo polarizing beam splitter.

    Parâmetros:
        photons_states_after_beam_splitter (array): Estados dos fótons após o beam splitter.
        number_of_photons (int): Número de fótons.

    Retorna:
        photons_states_after_polarizing_beam_splitter (array): Estados dos fótons após o polarizing beam splitter.
    """
    
    # Inicialização
    photons_states_after_polarizing_beam_splitter = np.zeros(number_of_photons)
    r = np.random.rand(number_of_photons)
    
    for i in range(number_of_photons):
        prob = photons_states_after_beam_splitter[:, i]
        photons_states_after_polarizing_beam_splitter[i] = np.sum(r[i] >= np.cumsum(np.concatenate(([0], prob)), axis=0))
    
    return photons_states_after_polarizing_beam_splitter