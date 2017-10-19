genes=open('genes','r').read().strip().split('\n')
gene_dict=dict()
for line in genes:
    gene_dict[line]=1
    
data=open("../asinh_tpm_minus_sva.tsv",'r').read().strip().split('\n')
outf=open("diff_genes_top_1000.tsv",'w')
outf.write(data[0]+'\n')
for line in data[1::]:
    tokens=line.split('\t')
    gene=tokens[0]
    if gene in genes:
        outf.write(line+'\n')
        
