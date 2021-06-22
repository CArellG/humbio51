#!/bin/bash 
# if you try to create kubernetes cluster on default gcp project created by Keith, you may get this error:
# ERROR: (gcloud.container.clusters.create) ResponseError: code=400, message=Clusters/node pools cannot be created while "startup-script-url" is specified in the project metadata.

# The solution is to remove the -key startup-script-url from project metadata

gcloud compute project-info remove-metadata --keys startup-script-url
