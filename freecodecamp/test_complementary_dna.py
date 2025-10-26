from complementary_dna import get_complementary_dna

def test_complementary_dna_case_1():
    assert get_complementary_dna("ACGT") == "TGCA"

def test_complementary_dna_case_2():
    assert get_complementary_dna("ATGCGTACGTTAGC") == "TACGCATGCAATCG"

def test_complementary_dna_case_3():
    assert get_complementary_dna("GGCTTACGATCGAAG") == "CCGAATGCTAGCTTC"

def test_complementary_dna_case_4():
    assert get_complementary_dna("GATCTAGCTAGGCTAGCTAG") == "CTAGATCGATCCGATCGATC"