
#define a function to write the RNA nucleotide sequence
#from a DNA sequence in FASTA format

def write_RNA_from_DNA(FASTAsequence,start,stop):
    FASTAsequence=open(FASTAsequence,'r')
    DNAsequence=(FASTAsequence.readlines()[1:])
    DNAsequence=''.join(DNAsequence)
    DNAsequence=DNAsequence.replace('\n','')
    RNAsequence='' #this defines the variable 'complementarysequence'
    for i in DNAsequence[start:stop]:
        if i=='T':
            RNAsequence=RNAsequence+'U'
        else:
            RNAsequence=RNAsequence+ i
    return(RNAsequence)

#define a function to write the protein amino acid sequence
#from an mRNA coding sequence in FASTA format


def write_protein_from_RNA(RNAsequence,start,stop):

    #defines the python dictionary for the one letter genetic code 
    geneticcode1let={'UUU':'F','UUC':'F','UUA':'L','UUG':'L',
         'CUU':'L','CUC':'L','CUA':'L','CUG':'L',
         'AUU':'I','AUC':'I','AUA':'I','AUG':'M',
         'GUU':'V','GUC':'V','GUA':'V','GUG':'V',
         'UCU':'S','UCC':'S','UCA':'S','UCG':'S',
         'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
         'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
         'GCU':'A','GCC':'A','GCA':'A','GCG':'A',
         'UAU':'Y','UAC':'Y','UAA':'*','UAG':'*',
         'CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
         'AAU':'N','AAC':'N','AAA':'K','AAG':'K',
         'GAU':'D','GAC':'D','GAA':'E','GAG':'E',
         'UGU':'C','UGC':'C','UGA':'*','UGG':'W',
         'CGU':'R','CGC':'R','CGA':'R','CGG':'R',
         'AGU':'S','AGC':'S','AGA':'R','AGG':'R',
         'GGU':'G','GGC':'G','GGA':'G','GGG':'G'}

    #defines the string variable proteinseq
    proteinseq=''

    #range command (start,stop(not included),step)

    for i in range(start-1,stop-1,3): 
        proteinseq=proteinseq+str(geneticcode1let[RNAsequence[i:i+3]])

    return (proteinseq)