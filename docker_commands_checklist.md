# Complete Docker Commands Checklist (Placement + Project Ready)

## 1. Version & System Info

docker --version docker version docker info

## 2. Images

docker images docker build -t image_name . docker build -t
image_name:tag . docker pull image_name docker rmi image_name docker rmi
-f image_name docker image prune

## 3. Containers

docker run image_name docker run -it image_name docker run -d image_name
docker run -d -p 5000:5000 image_name docker run --name container_name
image_name docker ps docker ps -a docker stop container_id docker start
container_id docker restart container_id docker rm container_id docker
rm -f container_id docker container prune

## 4. Logs & Debugging

docker logs container_id docker logs -f container_id docker inspect
container_id docker top container_id docker stats

## 5. Execute Inside Container

docker exec -it container_id bash docker exec -it container_id sh docker
exec container_id command

## 6. Volumes

docker volume create volume_name docker volume ls docker volume inspect
volume_name docker volume rm volume_name docker volume prune docker run
-v volume_name:/app image_name docker run -v \$(pwd):/app image_name

## 7. Networking

docker network ls docker network create network_name docker network
inspect network_name docker network rm network_name docker run --network
network_name image_name

## 8. Tagging

docker tag image_name username/image_name docker tag image_name
username/image_name:v1

## 9. Docker Hub

docker login docker push username/image_name docker pull
username/image_name docker logout

## 10. Cleanup

docker system prune docker system prune -a docker image prune docker
container prune docker volume prune docker network prune

## 11. Save & Load Images

docker save -o image.tar image_name docker load -i image.tar

## 12. Export & Import Containers

docker export container_id \> container.tar docker import container.tar

## 13. Docker Compose

docker compose up docker compose up -d docker compose down docker
compose up --build docker compose ps docker compose logs docker compose
stop service_name

## 14. Advanced Commands

docker diff container_id docker pause container_id docker unpause
container_id docker rename old_name new_name docker attach container_id
docker cp file.txt container_id:/app docker cp container_id:/app
file.txt
