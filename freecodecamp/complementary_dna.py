
DNA_SEQUENCE = "ACGT"

def get_complementary_dna(strand:str) -> str:
    "Given a dna sequence, returns its complementary strand"

    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

    strand = "".join(complement.get(letter, letter) for letter in strand)

    return strand


print(get_complementary_dna(DNA_SEQUENCE))
