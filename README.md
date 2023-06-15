# driverapp

``` bash
# build the Docker image using the following command
docker build -t driver-app .

# run a Docker container
docker run -p 8000:8000 driver-app


```

## Directory Structure
```
project-root/
├── rest-api/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── api.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── wsgi.py
├── database/
├── docker-compose.yml

```

## Docker COmmands
```
docker-compose down
docker-compose down -v
docker rmi $(docker images -q)
docker-compose up --build

```

## Now you can build and run your services using Docker Compose:

```bash
chmod +x start.sh
docker-compose down -v --remove-orphans && docker-compose up --build
docker-compose up --build
```




## Rebuild all

1. Stop any running Docker containers related to the driver_app. Open a terminal or command prompt and run the following command to stop and remove all running containers:

```bash
docker stop $(docker ps -aq) && docker rm $(docker ps -aq)
```

2. Next, delete the Docker images associated with the driver_app. Run the following command to remove all Docker images:
```bash
docker rmi $(docker images -q)
```
4. Delete any Docker volumes that might be associated with the driver_app. Run the following command to remove all Docker volumes:
```bash
docker volume prune
```
5. Lastly, navigate to the root directory (driver-app/) that contains your Docker-related files (docker-compose.yml, Dockerfile, etc.). Run the following command to rebuild and start the Docker containers:
```bash
docker-compose up --build
```
    This command will rebuild the Docker image using the updated Dockerfile and restart the containers specified in the docker-compose.yml file.

By following these steps, you will effectively delete and rebuild all Docker-related components associated with the driver_app.