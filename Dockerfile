FROM jupyter:scipy-notebook
MAINTAINER Kundaje Lab <annashch@stanford.edu>
# Update Ubuntu Software repository
RUN apt-get -y update
RUN apt-get -y upgrade
RUN pip install nbgitpuller

RUN apt-get install -y bedtools
RUN pip install pybedtools plotnine 
