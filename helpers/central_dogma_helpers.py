
def write_mRNA_from_DNA(filename_FASTAgenesequence):
    FASTAgenesequence=open(filename_FASTAgenesequence,'r')
    genesequence=(FASTAgenesequence.readlines()[1:])
    genesequence=''.join(genesequence)
    genesequence=genesequence.replace('\n','')
    RNAsequence='' #this defines the variable 'complementarysequence'
    for i in genesequence:
        if i=='T':
            RNAsequence=RNAsequence+'U'
        else:
            RNAsequence=RNAsequence+ i
    return(RNAsequence)

def write_protein_from_mRNA(RNAsequence):

#defines the python dictionary for the three letter genetic code 
    geneticcode3let={'UUU':'Phe','UUC':'Phe','UUA':'Leu','UUG':'Leu',
         'CUU':'Leu','CUC':'Leu','CUA':'Leu','CUG':'Leu',
         'AUU':'Ile','AUC':'Ile','AUA':'Ile','AUG':'Met',
         'GUU':'Val','GUC':'Val','GUA':'Val','GUG':'Val',
         'UCU':'Ser','UCC':'Ser','UCA':'Ser','UCG':'Ser',
         'CCU':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro',
         'ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr',
         'GCU':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala',
         'UAU':'Tyr','UAC':'Tyr','UAA':'Stop','UAG':'Stop',
         'CAU':'His','CAC':'His','CAA':'Gln','CAG':'Gln',
         'AAU':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys',
         'GAU':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu',
         'UGU':'Cys','UGC':'Cys','UGA':'Stop','UGG':'Trp',
         'CGU':'Arg','CGC':'Arg','CGA':'Arg','CGG':'Arg',
         'AGU':'Ser','AGC':'Ser','AGA':'Arg','AGG':'Arg',
         'GGU':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'}

#translates the RNAsequence into protein 

#In the range command: 
#The first number is the start codon using numbering starting at zero.
#The second number is the stop codon using numbering starting at zero, so that the stop codon is included. 
#The third number is the number of basepairs that are skipped every iteration since codons come in threes. 

    proteinseq=''

    for i in range(59,390,3): 
        proteinseq=proteinseq+str(geneticcode3let[RNAsequence[i:i+3]])
    return (proteinseq)