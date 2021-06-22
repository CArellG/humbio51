RELEASE=kube-lego-instructor
URL=instructor.humbio51.net
helm install --namespace jhub --name $RELEASE \
     --set config.LEGO_EMAIL=annashcherbina@gmail.com \
     --set config.LEGO_URL=$URL \
     stable/kube-lego
