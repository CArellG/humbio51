FROM jupyter/scipy-notebook
MAINTAINER Kundaje Lab <annashch@stanford.edu>
# Update Ubuntu Software repository
USER root
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y upgrade
RUN apt-get install -y libbz2-dev zlib1g-dev libncurses5-dev libncursesw5-dev liblzma-dev zlib1g-dev gcc
RUN apt-get install -y  samtools bedtools  

#course management 
USER jovyan
RUN pip install jupyterhub-ltiauthenticator
RUN conda install -c conda-forge nbgitpuller
RUN conda install -c conda-forge nbgrader
RUN jupyter nbextension install --sys-prefix --py nbgrader --overwrite
RUN jupyter nbextension enable --sys-prefix --py nbgrader
RUN jupyter serverextension enable --sys-prefix --py nbgrader

#Bio tools
RUN conda install -c bioconda pysam 
RUN conda install --channel conda-forge --channel bioconda bedtools htslib
RUN conda install --channel conda-forge --channel bioconda pybedtools
RUN conda install -c conda-forge plotnine 


