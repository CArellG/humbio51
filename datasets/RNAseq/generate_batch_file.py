#generate batch file for use with differential gene expression analysis, surrogate variable analysis, and k-means clustering
import argparse
import numpy as np
import pdb
def parse_args():
    parser=argparse.ArgumentParser("generate batch file for use with differential gene expression analysis, surrogate variable analysis, and k-means clustering")
    parser.add_argument("--metadata",help="tab-delimited file for metadata",default='rna_metadata_edited_2016-10-12.tsv')
    parser.add_argument("--outf",help="output batch file name",default="rnaseq_batches.txt")
    parser.add_argument("--corresponding_data_file",help="corresponding data file, the header of this file will be used for ordering the batches file",default="multicell_rnaseq.tpm")
    return parser.parse_args()

def main():
    args=parse_args()
    metadata=open(args.metadata,'r').read().strip().split('\n')
    outf=open(args.outf,'w')
    outf.write('Sample\tSystem\tOrgan\tCellType\n')
    unique_entries=dict() 
    for line in metadata[1::]:
        tokens=line.split('\t')
        sample=tokens[0]
        system=tokens[7]
        organ=tokens[8]
        celltype=tokens[9]
        entry=tuple([sample,system,organ,celltype])
        unique_entries[sample]=entry
    data_order=open(args.corresponding_data_file,'r').read().strip().split('\n')[0].split('\t')[1::]
    print(str(data_order))
    for sample in data_order: 
        outf.write('\t'.join(unique_entries[sample])+'\n')
        
    
if __name__=="__main__":
    main()
    
