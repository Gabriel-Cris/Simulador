import numpy as np

def SPAD(photons_states_after_polarizing_beam_splitter):
    """
    Calcula os bits medidos com base nos estados dos fótons após o polarizing beam splitter.

    Parâmetros:
        photons_states_after_polarizing_beam_splitter (array): Estados dos fótons após o polarizing beam splitter.

    Retorna:
        measured_bits (array): Bits medidos.
    """
    
    # Inicialização dos bits medidos com o mesmo tamanho que os estados dos fótons
    measured_bits = np.zeros_like(photons_states_after_polarizing_beam_splitter)

    # Cálculo dos bits medidos
    measured_bits[photons_states_after_polarizing_beam_splitter == 1] = 0
    measured_bits[photons_states_after_polarizing_beam_splitter == 2] = 1
    measured_bits[photons_states_after_polarizing_beam_splitter == 3] = 0
    measured_bits[photons_states_after_polarizing_beam_splitter == 4] = 1

    return measured_bits