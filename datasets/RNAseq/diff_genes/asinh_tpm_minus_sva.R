rm(list=ls())
library(ggplot2)
library(limma)
library(edgeR)
library(DESeq2)
library(sva)
library(gplots)
#import data 
tpm_corrected=read.table("../asinh_tpm_minus_sva.tsv",header=TRUE,sep='\t',row.names=1)
zero_rows=which(rowSums(tpm_corrected)==0)
tpm_corrected=tpm_corrected[-zero_rows,]
#get the design matrix 
batches=data.frame(read.table('../rnaseq_batches.txt',header=TRUE,sep='\t'))
keep=which(batches$System %in% c("Blood","Embryonic","Immune","Respiratory"))
batches=batches[keep,]
batches=factor(batches$System)
tpm_corrected=tpm_corrected[,keep]

mod_final=model.matrix(~0+System,data=batches)
fit_tpm <-lmFit(tpm_corrected,mod_final)
e_tpm=eBayes(fit_tpm)
la_tpm=topTable(e_tpm,number=nrow(tpm_corrected),p.value = 0.001,lfc =2)
top_1000=la_tpm[1:1000,]
write.table(top_1000,file="top1000_diff_genes.txt",quote=FALSE,sep='\t',row.names=TRUE,col.names=TRUE)