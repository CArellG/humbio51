helm install --namespace jhub --name my-release \
     --set config.LEGO_EMAIL=annashcherbina@gmail.com \
     --set config.LEGO_URL=humbio51.net \
     stable/kube-lego
