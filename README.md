### Application overview
A web application to save simple text in backend and file system. Simple UI allows you to view the stored texts and perform some operations.
It implements concepts such as:
- REST Api for storing, viewing and deleting data
- Webhook to post data to other service once saved
- Unit test for api endpoint
- Frontend and backend implementation using pyton (Django), jquery, sql
- Deployment of the application using docker, nginx, gunicorn

### Running the application (Production like environment)
##### Requirements
- For running the application in docker container, **Docker** needs to be installed in the system if not already installed. Please follow the instruction for the installation: https://docs.docker.com/get-docker/

- Clone the project repo: git clone https://github.com/sandip-ghimire/TextMessage

##### Steps
- Open the command line from the root directory of the project, i.e. the path where Dockerfile is located.  Build the docker image with the command:
  >docker build -t webapp .

- Add the webhook url in .env file and run the docker container with the command below: <br />
  >docker run --name=webapp-container --env-file .env -d -p 8008:8008 webapp

  *(The application runs on port 8008)* <br />
  The interface can be accessed at: <br />
  http://localhost:8008/

### Running the application (For debug in local machine - in windows)
##### Requirements
- Clone the project repo: git clone https://github.com/sandip-ghimire/TextMessage

##### Steps
- Set DEBUG=True in settings.py located inside webapp directory.
- Open the command line from the root directory of the project (TextMessage) and create virtual env:
  >python -m venv venv
- Activate virtual env:
  >venv\Scripts\activate
- Install dependencies:
  >pip install -r requirements.txt
- Make migrations:
  >python manage.py makemigrations webapp
- Migrate databases:
  >python manage.py migrate webapp
- Runserver at port 8008:
  >python manage.py runserver 0.0.0.0:8008

  *(The application runs on port 8008)* <br />
  The interface can be accessed at: <br />
  http://localhost:8008/

### Testing the application (Production like environment)
###### Unit Test
- While the application is running, it can be tested primarily using unit test. Command for unit test:
  >docker exec -it webapp-container ./manage.py test
    - The output should be 'OK' if the test is successful.
    
