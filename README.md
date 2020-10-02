# Roll A Dice: a flask micro service example



## Application packaging and deployment in k8s

Note: you must replace **MY_REGISTRY** variable in commands and deployment files with the correct address and port of your docker registry.

Expample:

```bash
export MY_REGISTRY=10.81.74.65:32000
```

### Build docker image

```bash
docker build -t rolladice:v1 .
```

### Tag application on registry
```bash
docker tag rolladice:v1 MY_REGISTRY/rolladice:v1
```
### Push to registry

```bash
docker push MY_REGISTRY/rolladice:v1
```

### Initial deployment on the kubernetes cluster (default namespace)

Create pod :

```bash
kubectl apply -f k8s/rolladice-deployment.yaml
```

Create service :

```bash
kubectl apply -f k8s/rolladice-service.yaml
```

## How to update app and deploy a new version in kubernetes (dumb version)

### Rebuild a new version, tag and push to registry

```bash
docker build -t rolladice:v2 .
docker tag rolladice:v2 MY_REGISTRY/rolladice:v2
docker push MY_REGISTRY/rolladice:v2
```
### Push update to kubernetes

```bash
kubectl set image deployments/rolladice rolladice=MY_REGISTRY/rolladice:v2
```


