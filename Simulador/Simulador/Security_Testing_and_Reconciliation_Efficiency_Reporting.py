import numpy as np
import math
from sympy import symbols, Eq, nsolve, log

def binary_entropy(x):
    if x == 0 or x == 1:
        return 0
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)

def Security_Testing_and_Reconciliation_Efficiency_Reporting(number_input_photons, Alice_sifted_key, depolarizing_parameter, eve_attack_level):
    print("\n\n\t\t\t\t-----<<Security Testing and Recommendation Session Initiation>>-----\n")
    
    # Calculating transition probabilities
    transition_probability_alice_bob = (eve_attack_level / 4) + ((2 * depolarizing_parameter) / 3) * (2 - eve_attack_level)
    transition_probability_alice_eve = 0.5 - (eve_attack_level / 4)
    
    # Calculating mutual information
    h_qber = binary_entropy(transition_probability_alice_bob)
    alice_bob_mutual_information = 1 - h_qber
    h_half_minus_q_eve = binary_entropy(transition_probability_alice_eve)
    alice_eve_mutual_information = 1 - h_half_minus_q_eve
    
    # Security check
    secure_question = depolarizing_parameter < ((3 / 4) * ((1 - eve_attack_level) / (2 - eve_attack_level)))
    
    mutual_information_alice_bob_bits = alice_bob_mutual_information * number_input_photons
    mutual_information_alice_eve_bits = alice_eve_mutual_information * number_input_photons

    print("\n\t\t\t\t\t\t-----<<Reporting Mutual Information and Security>>-----\n")
    print(f"The mutual information between Alice and Bob is {mutual_information_alice_bob_bits:.6f} bits.")
    print(f"The mutual information between Alice and Eve is {mutual_information_alice_eve_bits:.6f} bits.")
    
    if secure_question:
        print("Hence, the communication is secure. You may proceed to the post-processing classical schemes.")
    else:
        print("Hence, the communication is unsecure. You should abort the protocol.")
        answer = input("Do you want to calculate the acceptable range of channel depolarizing parameter at your input attack level to satisfy security? [y/n]: ")
        if answer.lower() == 'y':
            print("Processing...")
            depol_threshold = (3 / 4) * ((1 - eve_attack_level) / (2 - eve_attack_level))
            if depol_threshold == 0:
                print("Done... No acceptable range is found; protocol abortion at this attack level in any channel is a must.")
            else:
                print(f"Done... Channel depolarizing parameter should be {depol_threshold} at maximum.")
    
    # Calculating theoretical key length
    if secure_question:
        print("\n\t\t\t\t\t\t-----<<Reporting Key Rates>>-----\n")
        kth = h_half_minus_q_eve - h_qber
        kth_length = kth * len(Alice_sifted_key)
        print(f"The theoretical (maximum) key rate at your input conditions is {kth:.6f}.")
        print(f"The theoretical key length is {kth_length:.2f} out of your {number_input_photons} input bits.")
        
        # Calculating reconciliation efficiency for a target secret-key rate
        answer = input("Do you have a target key rate? [y/n]: ")
        if answer.lower() == 'y':
            while True:
                target_key_rate = float(input("Please input your target secret-key rate: "))
                if 0 < target_key_rate < 1:
                    break
                else:
                    print("Target key rate should be a decimal in the range of (0, 1). Please try again.")
            
            if target_key_rate < kth:
                reconciliation_eff = h_qber / (h_half_minus_q_eve - target_key_rate)
                max_bits_leaked = (1 / reconciliation_eff) * h_qber * len(Alice_sifted_key)
                print(f"The required efficiency of the reconciliation protocol to achieve your target key rate is {reconciliation_eff:.2f} at minimum.")
                print(f"The maximum allowable bits to be leaked in the post-processing schemes is {max_bits_leaked:.2f}.")
            else:
                answer = input("Your target key rate is larger than the theoretical key rate! "
                               "It is not achievable at your input conditions; you might have to lower the depolarizing parameter.\n"
                               "Do you want to calculate the depolarizing parameter range that could achieve your target key rate? [y/n]: ")
                if answer.lower() == 'y':
                    print("Processing...")
                    x = symbols('x')
                    lhs = -x * log(x, 2) - (1 - x) * log(1 - x, 2)
                    rhs = -target_key_rate + h_half_minus_q_eve
                    eqn = Eq(lhs, rhs)
                    initial_guesses = np.random.standard_cauchy(size=1000) * 100 + 0
                    for guess in initial_guesses:
                            solx = nsolve(eqn, x, guess).evalf()
                            if not solx.is_complex:
                                if not math.isnan(solx):
                                    break
                            else:
                                break
                    depol_threshold = ((solx) - (eve_attack_level / 4)) * (3 / (2 * (2 - eve_attack_level)))
                    print("Done")
                    if depol_threshold.is_complex:
                        print("Your target key rate is not achievable, even by lowering the depolarizing parameter. It needs to be below the theoretical key rate.")    
                    elif (depol_threshold <= 0) or (depol_threshold > depolarizing_parameter): 
                        print("Your target key rate is not achievable, even by lowering the depolarizing parameter. It needs to be below the theoretical key rate.")
                    else:
                        print(f"To achieve your target key rate, the depolarizing parameter should be less than {depol_threshold}.")
    
    print("\n\t\t\t\t-----<<End of this Simulation Session>>-----\n")