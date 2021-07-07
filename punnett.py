from sys import argv

def main():
    if len(argv) != 3:
        print("Usage: punnett.py genotype1 genotype2")
        return 1

    if (len(argv[1]), len(argv[2])) != (2, 2):
        print("Unsupported number of genes")
        return 2

    alleles_1, alleles_2 = [i for i in argv[1]], [j for j in argv[2]]
    if not (alleles_1[0].lower() == alleles_2[0].lower() and alleles_1[1].lower() == alleles_2[1].lower()):
        print("Not supported!")
        return 3

    print("    | " + '   | '.join(alleles_1) + '   |')

    for allele_2 in alleles_2:
        print(f" {allele_2}  | " +  '  | '.join([i + allele_2 for i in alleles_1]) + '  | ')

if __name__ == "__main__":
    main()
