docker stop userbase_container
docker rm userbase_container
docker rmi userbase
docker container prune
docker image prune
docker build -t userbase .
docker run -d -p 5432:5432 --name userbase_container userbase
