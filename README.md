   
    ****Real commercial project for the steell-shop****
    
    This project represents the REST-API internet shop, where you can:
    1) Use CRUD operations with items through the json format
    2) USE CRUD operations with received orders from the client through json format
    3) Make CRUD items via special admin panel to manage the store   
   ----------------------------------------------------------------------------------------------
    Essential links:
    1) http://127.0.0.1:8000/swagger
    2) http://127.0.0.1:8000/
    3) http://127.0.0.1:8000/admin
    ----------------------------------------------------------------------------------------------
    **You can easily run the app from docker using these commands**:
  
    git clone: ...
    sudo docker build . -t epam_test -f ./Dockerfile
    sudo docker run -p 8000:8000 epam_test
    sudo docker image ls
    sudo docker ps
    
    For the preliminaril usage of the project open a new terminal session and use these commands:
    sudo netstat -ltnp
    curl -X GET "http://127.0.0.1:8000/items" -H  "accept: */*"
    ----------------------------------------------------------------------------------------------
    Otherwise , if you want to run the app.py using gunicorn, input the next command into the terminal
    
    gunicorn  app:app -w 2 --threads 2 -b 191.*.*.*:8000
