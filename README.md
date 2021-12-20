   
    <h3>Commercial project for the steell-shop</h3>
   
    
    
    sudo docker build . -t epam_test -f ./Dockerfile
    sudo docker run -p 8000:8000 epam_test
    sudo docker image ls
    sudo docker ps
    
    For the previous usage of the project open a new terminal session and use these commands:
    sudo netstat -ltnp
    curl -X GET "http://127.0.0.1:8000/posts" -H  "accept: */*"
    ================================================================================================================================================================
    Otherwise , if you want to run the app.py using gunicorn input the next command into the terminal
    
    gunicorn  app:app -w 2 --threads 2 -b 192.168.0.108:8000
