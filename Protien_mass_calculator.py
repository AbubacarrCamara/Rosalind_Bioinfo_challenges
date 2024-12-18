def protien_mass():

    protien = 'TITLRTFSTRAVISMWMDDCCDHFHLIDWKLELGCAHCVFWEAKYAKDHTYYHMVHSYAYSHFHWGLYINLSTPNACCKKILLWRYEAFLDTGRSMQLIAVNQYQCHMVNTTYWHPEKQVFLHKQTVKYRYKKVEIMDYDQFQPWETNCCLYQMWIENKHKTACHHEIGDPDHRMYWETNNHGGKVDWVHLGMYEFDAMMSNGVTCGMRKLTEKKHNNDERADMSKRPFHKAHATPVYSLNAQKRRAKALAVGTKPRHSWCKEHLRTGEEQFMHVFQWHYIYIEACFHYMFPFTSIASVGGQWEFQISCRWSGLGNHRHLPQLRRGDGYAPAYFWSPAKEHWNPWRHWEYLAPLNWPVRGVRTHQDVGGNMNVCCMNAQSIFFRQRAERSNGVCNDKKKPANKIAYCPAKDGFNGPRTQMSWGVPRCIGLRLFNVGYPALNREEWQKDERAKRAMRDLHNLVGLNYHQDHSIPHFDIEGEHMFGDQHWIHNDFQEQSISFNNDQSMCFPCSSQIRPRWQMQNMSGNMQKITTVLYGFFMAGETWLPANTQAWWNEWYFCEKTNCSQDPTKFYRQVMQYFEPGEIKNFIQCYDPVGCSDHFWVLVCSKWCHLERCGGSAHLRTRVKNRTTELPDEDSPESLERMRSAGWHMMIHHWIKHWTWWYERSTLCGRAITMKNRLSGSERQDLEPQTCVRLLTSSMYWMSTDMQEPAKCSYPARDRHVWFAVHPKSEYMAEWKCDRFCASNHWYHSHWKIVEINVWKVWNLGCLCMLVKMMQWLHYEAQACTESTTCTEWYCYFEKFIVLHKVWIIDLSQCTVSTLGQMCDMYTSTYNNGGYSVIQMKRPYYWINDQNISGSARQFMDPTFFKHDHLYFVKQADTLEYHVEFFKGPPGHKSNPFEVWCHNLIKAAVIIIARFRSQPQWMGKVDHMWQSLHEHIQGYWENHHMSSASCCVRYWGCWKVQD'
    # Splits string into individual character strings
    protien_split = [char for char in protien]
    print('protien', protien_split)

    # Opens mass table and splits the string into singular strings
    mass_table = open('Protein_mass/Monoisotopic_mass_table.txt', 'r').read().split()
    print('mass_table', mass_table)
    
    # Collects all the letterd amino acids 
    alpha_list = [alpha for alpha in mass_table if len(alpha) == 1]
    print('\nalpha_list', alpha_list)

    # Collects corresponding weights for amino acides
    weight_list = [mass for mass in mass_table if len(mass) > 1]
    print('\nweight_list', weight_list)
    
    # Creates a dictionary with the amino acids as the key and the weights as values
    mass_dict = dict(zip(alpha_list, weight_list))
    print('\nmass_dict', mass_dict)

    # Finds all the associated weights for each amino acid in the protien amino acid sequence 
    protien_masses = [float(mass_dict[key]) for key in protien if key in mass_dict]
    
    # Sums all the values in the protien masses array
    total_mass = sum(protien_masses)
    print('\ntotal_mass', total_mass)

    # Rounds final answer to three decimal places
    round_total_mass = round(total_mass, 3)
    print('\nround_total_mass', round_total_mass)

protien_mass()


