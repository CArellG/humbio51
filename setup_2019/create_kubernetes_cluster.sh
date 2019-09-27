##instructions here: 
##https://zero-to-jupyterhub.readthedocs.io/en/stable/index.html

#gcloud auth login
#gcloud auth application-default login
#gcloud config set project gbsc-gcp-class-humbio51-aut19

gcloud container clusters create \
  --machine-type n1-standard-4 \
  --num-nodes 2 \
  --zone us-central1-b \
  --cluster-version latest \
  --disk-size=40Gi \
  humbio51-2019

kubectl create clusterrolebinding cluster-admin-binding \
   --clusterrole=cluster-admin \
  --user=annashch@stanford.edu


gcloud beta container node-pools create user-pool \
  --machine-type n1-standard-8 \
  --num-nodes 1 \
  --enable-autoscaling \
  --min-nodes=0 \
  --max-nodes=40 \
  --node-labels hub.jupyter.org/node-purpose=user \
  --node-taints hub.jupyter.org_dedicated=user:NoSchedule \
  --zone us-central1-b \
  --disk-size=20Gi \
  --cluster humbio51-2019


##setup helm & tiller -- to install/uninstall easily,  refer here: https://medium.com/@pczarkowski/easily-install-uninstall-helm-on-rbac-kubernetes-8c3c0e22d0d7

#curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash
kubectl --namespace kube-system create serviceaccount tiller
kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
helm init --service-account tiller --wait
#kubectl patch deployment tiller-deploy --namespace=kube-system --type=json --patch='[{"op": "add", "path": "/spec/template/spec/containers/0/command", "value": ["/tiller", "--listen=localhost:44134"]}]'
#helm version

## Install jupyterhub
#openssl rand -hex 32
## add secretToken to config.yaml
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
helm repo update


#kubectl create -f namespace_jhub.yaml
#kubectl get namespace
#kubectl --namespace jhub apply -f data_pvc.yaml 
#kubectl --namespace jhub get pvc

export RELEASE=jhub
export NAMESPACE=jhub
helm upgrade --install $RELEASE jupyterhub/jupyterhub \
     --namespace $NAMESPACE  \
     --values config.canvas.yaml


##Your release is named jhub and installed into the namespace jhub.
##You can find if the hub and proxy is ready by doing:
## kubectl --namespace=jhub get pod
## and watching for both those pods to be in status 'Ready'.
## You can find the public IP of the JupyterHub by doing:
## kubectl --namespace=jhub get svc proxy-public
## It might take a few minutes for it to appear!
#kubectl config set-context $(kubectl config current-context) --namespace ${NAMESPACE:-jhub}
