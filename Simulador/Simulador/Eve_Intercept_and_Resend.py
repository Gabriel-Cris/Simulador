import numpy as np

def Eve_Intercept_and_Resend(Eve_attack_level, number_of_photons, Alice_polarized_photons_states):
    """
    Função para simular o ataque de interceptação e reenvio de Eve.
    
    Parâmetros:
    Eve_attack_level (float): O nível de ataque de Eve (proporção dos fótons atacados).
    number_of_photons (int): Número total de fótons.
    Alice_polarized_photons_states (numpy array): Estados de polarização dos fótons de Alice.
    
    Retorna:
    polarization_states_after_Eve_attack_if_present (numpy array): Estados de polarização dos fótons após o ataque de Eve.
    Eve_bases_selection (numpy array): Seleção de bases de Eve para os fótons atacados.
    """
    
    # Número inteiro de fótons a serem atacados
    attack_occ = int(np.ceil(Eve_attack_level * number_of_photons))
    
    # Número aleatório de pulsos atacados
    random_pulses_number_attacked = np.random.choice(number_of_photons, attack_occ, replace=False)
    
    # Seleção aleatória das bases de Eve
    Eve_bases_selection = np.round(np.random.rand(attack_occ))
    
    # Fótons que Eve mediu
    selected_indices = Alice_polarized_photons_states[random_pulses_number_attacked]
    
    # Calculando os novos estados dos fótons que Eve atacou
    new_states = np.zeros(attack_occ)

    for i in range(attack_occ):
        if Eve_bases_selection[i] == 0 and (selected_indices[i] == 1 or selected_indices[i] == 2):
            measured_state = selected_indices[i]  # sem mudança

        elif Eve_bases_selection[i] == 1 and (selected_indices[i] == 3 or selected_indices[i] == 4):
            measured_state = selected_indices[i]  # sem mudança

        elif Eve_bases_selection[i] == 0 and (selected_indices[i] == 3 or selected_indices[i] == 4):
            measured_state = 1 + (2 - 1) * np.round(np.random.rand())  # 50% chance de ser horizontal ou vertical

        elif Eve_bases_selection[i] == 1 and (selected_indices[i] == 1 or selected_indices[i] == 2):
            measured_state = 3 + (4 - 3) * np.round(np.random.rand())  # 50% chance de ser circular à direita ou à esquerda

        new_states[i] = measured_state

    # Unindo os estados dos fótons temperados e intocados
    Alice_polarized_photons_states[random_pulses_number_attacked] = new_states
    polarization_states_after_Eve_attack_if_present = Alice_polarized_photons_states

    return polarization_states_after_Eve_attack_if_present, Eve_bases_selection