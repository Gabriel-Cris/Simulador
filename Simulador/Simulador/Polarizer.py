import numpy as np

def Polarizer(alice_basis_selection, key_bits, number_of_photons):
    """
    Função para calcular os estados de polarização dos fótons baseados na seleção de bases
    e bits de chave da Alice no protocolo BB84.

    Parâmetros:
        alice_basis_selection (array): Seleção da base de Alice (0 para retangular, 1 para circular).
        key_bits (array): Bits da chave de Alice (0 ou 1).
        number_of_photons (int): Número de fótons a serem polarizados.

    Retorna:
        alice_polarized_photon_states (array): Array com os estados polarizados dos fótons.
    """

    # Inicialização dos estados polarizados dos fótons
    alice_polarized_photon_states = np.zeros(number_of_photons, dtype=int)

    # Cálculo dos estados de polarização
    for i in range(number_of_photons):
        if alice_basis_selection[i] == 0 and key_bits[i] == 0:
            state = 1  # Polarização horizontal (0 graus): bit 0
        elif alice_basis_selection[i] == 0 and key_bits[i] == 1:
            state = 2  # Polarização vertical (90 graus): bit 1
        elif alice_basis_selection[i] == 1 and key_bits[i] == 0:
            state = 3  # Polarização circular à direita (45 graus): bit 0
        elif alice_basis_selection[i] == 1 and key_bits[i] == 1:
            state = 4  # Polarização circular à esquerda (-45 graus): bit 1

        alice_polarized_photon_states[i] = state

    return alice_polarized_photon_states