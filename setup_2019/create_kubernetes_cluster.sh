##instructions here: 
##https://zero-to-jupyterhub.readthedocs.io/en/stable/index.html

#gcloud auth login
#gcloud config set project gbsc-gcp-class-humbio51-aut19

#gcloud container clusters create \
#  --machine-type n1-standard-4 \
#  --num-nodes 2 \
#  --zone us-central1-b \
#  --cluster-version latest \
#  humbio51-2019

#kubectl create clusterrolebinding cluster-admin-binding \
#  --clusterrole=cluster-admin \
#  --user=annashch@stanford.edu

##setup helm & tiller

#curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash
#helm init --upgrade
#kubectl --namespace kube-system create serviceaccount tiller
#kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
#helm init --service-account tiller --wait
#kubectl patch deployment tiller-deploy --namespace=kube-system --type=json --patch='[{"op": "add", "path": "/spec/template/spec/containers/0/command", "value": ["/tiller", "--listen=localhost:44134"]}]'
#helm version

## Install jupyterhub
#openssl rand -hex 32
## add secretToken to config.yaml
#helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
#helm repo update

export RELEASE=jhub
export NAMESPACE=jhub

helm upgrade --install $RELEASE jupyterhub/jupyterhub \
     --namespace $NAMESPACE  \
     --version 0.8.2 \
     --values config.yaml
