import numpy as np

def Beam_Splitter(photons_states_after_channel, Bob_basis_selection):
    """
    Calcula os estados dos fótons após passarem pelo beam splitter.

    Parâmetros:
        photons_states_after_channel (array): Estados dos fótons após o canal.
        Bob_basis_selection (array): Seleção de bases de Bob (0 para retangular, 1 para circular).

    Retorna:
        photons_states_after_beam_splitter (array): Estados dos fótons após o beam splitter.
    """

    # Inicializa o array de saída como uma cópia do estado após o canal
    photons_states_after_beam_splitter = photons_states_after_channel

    # Encontra as posições das bases reticuladas e circulares
    rect = np.where(Bob_basis_selection == 0)[0]  # Posições da base retangular
    circ = np.where(Bob_basis_selection == 1)[0]  # Posições da base circular

    # Se a base reticulada for selecionada, os resultados da base circular serão impossíveis
    photons_states_after_beam_splitter[2:4, rect] = 0  # Resultados 3 e 4 (circular)

    # Se a base circular for selecionada, os resultados da base retangular serão impossíveis
    photons_states_after_beam_splitter[0:2, circ] = 0  # Resultados 1 e 2 (retangular)

    return photons_states_after_beam_splitter