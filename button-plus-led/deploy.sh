echo "BUILDING DOCKER IMAGE"
docker build --tag docker.local/gpio/button-plus-led .

echo "PUSHING TO DOCKER.LOCAL REGISTRY"
docker push docker.local/gpio/button-plus-led
