helm install --namespace jhub-instructor  \
     --set config.LEGO_EMAIL=annashcherbina@gmail.com \
     --set config.LEGO_URL=instructor.humbio51.net \
     --generate-name \
     stable/kube-lego
