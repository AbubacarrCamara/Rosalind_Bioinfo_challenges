import re

# Calculates the GC percentage in a given code 
def GC_percentage(sequence):
    C_count = sequence.count('C')
    G_count = sequence.count('G')
    G_C = G_count + C_count
    G_C_percentage = G_C / len(sequence) * 100
    return G_C_percentage

# Extracts data and cleans it so GC percantage function can be ran on it 
def datacleaner():
    data = open('GC_Percentage/rosalind_gc.txt', 'r')
    content = data.read()
    # Removes '>'
    sequences = content.split('>')
    #Removes leading and trainling white spaces
    sequences = [seq.strip() for seq in sequences if seq.strip()]
    #Removes '\n' chacrecters 
    sequences = [seq.replace('\n', '') for seq in sequences if '\n' in seq]

    #Add an "=" whenever a number is followed by a letter to seperate name and sequence 
    for i, seq in enumerate(sequences):
        sequences[i] = re.sub(r'(\d)([A-Za-z])', r'\1 = \2', seq)

    print('sequences', sequences)

    # Creates a dictionary key, value pair of the name and sequence and also removes name from value 
    sequences_dict = {}

    # Assigns the keys to sequences_dict eg "Rosalind_0401" 
    for key in sequences:
        # Splits object at "=" in sequences 
        parts = key.split('=')
        # Ensures parts has two objects within it 
        if len(parts) > 1:
            # selects string in index one at strips any leading or trailing white lines
            dict_key = parts[0].strip()
            # Sets the keys in sequences_dict
            sequences_dict[dict_key] = key

    print(sequences_dict)

    for key in sequences_dict:
        # Assigns DNA string as value by selecting the second index of key
        sequences_dict[key] = sequences_dict[key].split('=')[1].strip()

    print('\nsequences_dict', sequences_dict)

    # Calculate and print GC percentage for each sequence
    for key, value in sequences_dict.items():
        gc_percentage = GC_percentage(value)
        print(f"GC percentage for {key}: {gc_percentage}%")

# Call the datacleaner function
datacleaner()