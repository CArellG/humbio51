#openssl rand -hex 32
## add secretToken to config.instructor.yaml

gcloud container clusters create \
  --machine-type n1-standard-4 \
  --num-nodes 2 \
  --zone us-central1-b \
  --cluster-version latest \
  --disk-size=40Gi \
  humbio51-2021-instructor

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
  --cluster humbio51-2021-instructor



kubectl create -f namespace_jhub_instructor.yaml
kubectl get namespace
#note: first manually create a disk for data store, which is reference in data_pv_instructor.yaml
kubectl --namespace jhub-instructor apply -f data_pv_instructor.yaml 
kubectl --namespace jhub-instructor apply -f data_pvc_instructor.yaml 
kubectl --namespace jhub-instructor get pvc

export RELEASE=jhub-instructor
export NAMESPACE=jhub-instructor
helm upgrade --install $RELEASE jupyterhub/jupyterhub \
     --namespace $NAMESPACE  \
     --version=0.9.6 \
     --values config.instructor.yaml


##Your release is named jhub and installed into the namespace jhub.
##You can find if the hub and proxy is ready by doing:
## kubectl --namespace=jhub-instructor get pod
## and watching for both those pods to be in status 'Ready'.
## You can find the public IP of the JupyterHub by doing:
## kubectl --namespace=jhub get svc proxy-public
## It might take a few minutes for it to appear!
#kubectl config set-context $(kubectl config current-context) --namespace ${NAMESPACE:-jhub}
