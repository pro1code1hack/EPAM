    sudo docker build . -t epam_test -f ./Dockerfile
    sudo docker run -p 8000:8000 epam_test
    sudo docker image ls
    sudo docker ps
################## + во второй консоли 

    sudo netstat -ltnp
    curl -X GET "http://127.0.0.1:8000/posts" -H  "accept: */*"
