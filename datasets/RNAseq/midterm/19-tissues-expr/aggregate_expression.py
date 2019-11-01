mypath="/users/annashch/humbio51/datasets/RNAseq/midterm/19-tissues-expr"
from os import listdir
from os.path import isfile, join
onlyfiles = ['/'.join([mypath,f]) for f in listdir(mypath) if isfile(join(mypath, f))]

samples=set([]) 
expression_dict=dict()
for cur_file in onlyfiles:
    if cur_file.endswith('.expr'):
        sample=cur_file.split('/')[-1].split('.')[0]
        samples.add(sample)
        from os.path import isfile, join
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        data=open(cur_file,'r').read().strip().split('\n')
        for line in data[1::]:
            tokens=line.split('\t')
            gene=tokens[0]
            expr=tokens[5]
            if gene not in expression_dict:
                expression_dict[gene]=dict()
            expression_dict[gene][sample]=expr
outf=open("mm9.rnaseq.fpkm.tsv",'w')
samples=list(samples)
outf.write('\t'.join(samples)+'\n')
for gene in expression_dict:
    outf.write(gene)
    for sample in samples:
        if sample not in expression_dict[gene]:
            outf.write('\t0')
        else: 
            outf.write('\t'+expression_dict[gene][sample])
    outf.write('\n')

