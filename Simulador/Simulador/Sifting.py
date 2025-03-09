import numpy as np

def Sifting(key_bits, Alice_basis_selection, Bob_basis_selection, measured_bits):
    """
    Realiza o processo de "sifting" para calcular as chaves peneiradas de Alice e Bob e a Taxa de Erro de Bit Quântico (QBER).

    Parâmetros:
        key_bits (array): Bits da chave de Alice antes do sifting.
        Alice_basis_selection (array): Bases escolhidas por Alice para cada bit.
        Bob_basis_selection (array): Bases escolhidas por Bob para medir os bits.
        measured_bits (array): Bits medidos por Bob após o processo de polarização.

    Retorna:
        QBER (float): Taxa de Erro de Bit Quântico.
        positions_of_unmatched_bases (array): Posições onde as bases de Alice e Bob não coincidem.
        Alice_sifted_key (array): Chave peneirada de Alice.
        Bob_sifted_key (array): Chave peneirada de Bob.
    """
    
    # Encontrar posições onde as bases de Alice e Bob não coincidem
    positions_of_unmatched_bases = np.where(Alice_basis_selection != Bob_basis_selection)[0]
    
    # Extrair bits das chaves peneiradas
    matched_positions = np.setdiff1d(np.arange(len(key_bits)), positions_of_unmatched_bases)
    Alice_sifted_key = key_bits[matched_positions]
    Bob_sifted_key = measured_bits[matched_positions]
    
    # Calcular a QBER
    QBER = np.sum(Alice_sifted_key != Bob_sifted_key) / len(Alice_sifted_key)

    return QBER, positions_of_unmatched_bases, Alice_sifted_key, Bob_sifted_key