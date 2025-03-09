import numpy as np

def Channel(numbers_of_photons, channel_depolarization_probability, photons_states_before_channel):
    """
    Calcula os estados dos fótons após o canal de despolarização.

    Parâmetros:
        numbers_of_photons (int): Número de fótons no canal.
        channel_depolarization_probability (float): Probabilidade de despolarização do canal.
        photons_states_before_channel (array): Estados dos fótons antes do canal.

    Retorna:
        photons_states_after_channel (array): Estados dos fótons após o canal.
    """

    # Inicialização dos estados dos fótons após o canal
    photons_states_after_channel = np.zeros((4, numbers_of_photons))

    # Cálculo dos estados após o canal
    # Para o estado horizontal
    photons_states_after_channel[:, photons_states_before_channel == 1] = np.tile(
        np.array([1 - (2/3) * channel_depolarization_probability, 
                  (2/3) * channel_depolarization_probability, 
                  0.5, 0.5]).reshape(-1, 1), 
        (1, np.sum(photons_states_before_channel == 1))
    )

    # Para o estado vertical
    photons_states_after_channel[:, photons_states_before_channel == 2] = np.tile(
        np.array([(2/3) * channel_depolarization_probability, 
                  1 - (2/3) * channel_depolarization_probability, 
                  0.5, 0.5]).reshape(-1, 1), 
        (1, np.sum(photons_states_before_channel == 2))
    )

    # Para o estado circular-direito
    photons_states_after_channel[:, photons_states_before_channel == 3] = np.tile(
        np.array([0.5, 0.5, 
                  1 - (2/3) * channel_depolarization_probability, 
                  (2/3) * channel_depolarization_probability]).reshape(-1, 1), 
        (1, np.sum(photons_states_before_channel == 3))
    )

    # Para o estado circular-esquerdo
    photons_states_after_channel[:, photons_states_before_channel == 4] = np.tile(
        np.array([0.5, 0.5, 
                  (2/3) * channel_depolarization_probability, 
                  1 - (2/3) * channel_depolarization_probability]).reshape(-1, 1), 
        (1, np.sum(photons_states_before_channel == 4))
    )

    return photons_states_after_channel