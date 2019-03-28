Python Hello-World




oc new-build --strategy=docker --binary --docker-image=ubuntu:latest --name=myapp
oc start-build myapp --from-dir . --follow
oc new-app myapp -l testapp=true
oc expose svc/myapp
oc get pvc