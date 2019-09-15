#openssl rand -hex 32
## add secretToken to config.yaml

export RELEASE=jhub-instructor
export NAMESPACE=jhub-instructor
helm upgrade --install $RELEASE jupyterhub/jupyterhub \
     --namespace $NAMESPACE  \
     --values config.instructor.yaml


##Your release is named jhub and installed into the namespace jhub.
##You can find if the hub and proxy is ready by doing:
## kubectl --namespace=jhub get pod
## and watching for both those pods to be in status 'Ready'.
## You can find the public IP of the JupyterHub by doing:
## kubectl --namespace=jhub get svc proxy-public
## It might take a few minutes for it to appear!
#kubectl config set-context $(kubectl config current-context) --namespace ${NAMESPACE:-jhub}
