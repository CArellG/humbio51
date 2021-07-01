#This script aggregates Daniel Kim's processed RNA-seq data for multiple tissues/cell types to generate gene x cell-type matrices with TPM, FPKM, and Expected_Count values for the RSEM-processed data
import argparse
import numpy as np
import pdb

# This method of loading the metadata file w/ numpy is not currently used due to some issues with how the
# metadata file is stored

def load_metadata(metadata):
    dtype_dict=dict()
    dtype_dict['names']=("folder_name",
                         "encode_expt_accession",
                         "common_name",
                         "eid",
                         "rep_folder",
                         "encode_biosample_ids",
                         "rsem_quant_file",
                         "system",
                         "organ",
                         "cell_type",
                         "color",
                         "lab",
                         "sex",
                         "biosample_type",
                         "biosample_term_id",
                         "biosample_term_name",
                         "life_stage",
                         "age",
                         "age_units",
                         "treatments",
                         "description")
    dtype_dict['formats']=('S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36',
                           'S36')
    data=np.genfromtxt(metadata,
                       dtype=dtype_dict['formats'],
                       names=dtype_dict['names'],
                       skip_header=True,
                       loose=True,
                       invalid_raise=False,
                       delimiter='\t')
    return data 

#write the contents of the output file 
def write_output(outf,dictionary,celltypes):
    outf.write('Gene\t'+'\t'.join(celltypes)+'\n')
    for gene in dictionary:
        outf.write(gene)
        for celltype in celltypes:
            outf.write('\t'+str(dictionary[gene][celltype]))
        outf.write('\n')
        
        
def parse_args():
    parser=argparse.ArgumentParser("This script aggregates Daniel Kim's processed RNA-seq data for multiple tissues/cell types to generate gene x cell-type matrices with TPM, FPKM, and Expected_Count values for the RSEM-processed data")
    parser.add_argument("--metadata",help="tab-delimited file for metadata",default="rna_metadata_edited_2016-10-12.tsv")
    parser.add_argument("--output_prefix",help="prefix to use for generating output files",default="multicell_rnaseq")
    return parser.parse_args()

def main():
    args=parse_args()
    data=open(args.metadata,'r').read().strip().split('\n')
    #keep track of fpkm, tpm, and expected count values for the various cell types.
    expected_count_dict=dict()
    tpm_dict=dict()
    fpkm_dict=dict()
    datasets=set([]) 
    for line in data[1::]:
        tokens=line.split('\t')
        folder_name=tokens[0]
        datasets.add(folder_name)
        print(str(folder_name))
        data_path=tokens[6]
        rsem=open(data_path,'r').read().strip().split('\n')        
        for rsem_line in rsem[1::]:
            rsem_tokens=rsem_line.split('\t')
            gene=rsem_tokens[0]
            expected_count=int(round(float(rsem_tokens[4])))
            tpm=rsem_tokens[5]
            fpkm=rsem_tokens[6]
            #if this is the first time we are encountering this gene, add it to all the dictionaries 
            if gene not in expected_count_dict:
                expected_count_dict[gene]=dict()
                tpm_dict[gene]=dict()
                fpkm_dict[gene]=dict()
            expected_count_dict[gene][folder_name]=expected_count
            tpm_dict[gene][folder_name]=tpm
            fpkm_dict[gene][folder_name]=fpkm
    datasets=list(datasets)
    #read in all the datasets! generate output file
    outf=open(args.output_prefix+".expected_count",'w')
    write_output(outf,expected_count_dict,datasets)
    outf=open(args.output_prefix+".tpm",'w')
    write_output(outf,tpm_dict,datasets)
    outf=open(args.output_prefix+".fpkm",'w')
    write_output(outf,fpkm_dict,datasets)
    
            
if __name__=="__main__":
    main() 
