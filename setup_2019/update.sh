#update the docker image
sudo docker build -t humbio51 .
sudo docker login --username=annashcherbina 
sudo docker images  
sudo docker tag f78fff21d534 kundajelab/humbio51:latest
sudo docker push kundajelab/humbio51


#make updates in config.yaml and then run this
RELEASE=jhub

helm upgrade $RELEASE jupyterhub/jupyterhub \
  --version=0.8.2 \
  --values config.yaml
