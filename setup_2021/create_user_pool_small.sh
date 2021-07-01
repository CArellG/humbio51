gcloud beta container node-pools create user-pool-4cpu-20gi \
  --machine-type n1-standard-4 \
  --num-nodes 1 \
  --enable-autoscaling \
  --min-nodes=0 \
  --max-nodes=20 \
  --node-labels hub.jupyter.org/node-purpose=user \
  --node-taints hub.jupyter.org_dedicated=user:NoSchedule \
  --zone us-central1-b \
  --disk-size=20Gi \
  --cluster humbio51-2019

