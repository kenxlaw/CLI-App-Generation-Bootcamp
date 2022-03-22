### ```Welcome to the Cafe App Python MiniProject```

![Guide][1]

[1]: https://media.istockphoto.com/vectors/instructions-manual-concept-user-manual-flat-style-vector-concept-vector-id1165498595?k=20&m=1165498595&s=612x612&w=0&h=L9pU_d_bqf4zLUysQ1glsXut-5KT6atSm5yY1M7PFVw=



### Start by running a virtual environment. 
```sh
python3 -m venv .venv 
```
[windows] cd into: 
```sh 
 cd \.venv\script
```
activate the ```Activate``` file corresponding to your shell within the directory above.

### Install required packages:
```sh 
pip install -r requirements.txt 
```
``` *requires requirements.txt* ```

### Run Docker for MYSQL Database:
```sh 
docker-compose up -d 
```
``` *requires docker-compose.yml* ```

### Connect to Adminer and select the MiniProject tab:
```sh 
http://localhost:8080/ 
```
Input the username and password to login.

### Run the ```Saucy``` app in the \saucy folder:
```sh
py app.py 
```
