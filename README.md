Python Hello-World



oc login -u system:admin
Login as admin to create user

oc adm policy add-cluster-role-to-user cluster-admin admin

oc new-project mytestapp

oc new-build --strategy=docker --binary --docker-image=ubuntu:latest --name=mytestapp

oc start-build mytestapp --from-dir . --follow
oc new-app mytestapp -l testapp=true
oc expose svc/mytestapp

oc get pods -l app=mytestapp

oc get pvc

oc get routes -l app=mytestapp

oc delete all --selector app=mytestapp