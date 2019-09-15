helm install --namespace jhub-instructor --name my-release-instructor \
     --set config.LEGO_EMAIL=annashcherbina@gmail.com \
     --set config.LEGO_URL=instructor.humbio51.net \
     stable/kube-lego
