Local Development
=================

Prerequisites
~~~~~~~~~~~~~

- Github account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

In the rest of the documentation on local development, it is assumed that the `python` command in your OS shell runs the Python interpreter mentioned above (unless a virtual environment is activated).

Cloning the Repository (Unix-like Systems)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``cd /path/to/put/project/in``
- ``git clone https://github.com/nopalpite/OCP13.git``

Cloning the Repository (Windows)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Navigate to the directory where you want to put the project.
- Clone the repository by running:
  
  ::
  
    git clone https://github.com/nopalpite/OCP13.git

Creating the Virtual Environment (Unix-like Systems)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``cd /path/to/OCP13``
- Create the virtual environment:
  
  ::
  
    python -m venv venv
    
- If you encounter package not found errors on Ubuntu, install the python3-venv package:
  
  ::
  
    apt-get install python3-venv
    
- Activate the environment:
  
  ::
  
    source venv/bin/activate
    
- Confirm that the `python` command runs the Python interpreter within the virtual environment:
  
  ::
  
    which python
    
- Confirm that the Python interpreter version is 3.6 or higher:
  
  ::
  
    python --version
    
- Confirm that the `pip` command runs the pip executable within the virtual environment:
  
  ::
  
    which pip
    
- To deactivate the environment:
  
  ::
  
    deactivate

Creating the Virtual Environment (Windows)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Open a command prompt and navigate to the `OCP13` directory.
- Create the virtual environment:
  
  ::
  
    python -m venv venv
    
- Activate the environment:
  
  ::
  
    venv\Scripts\activate
    
- Confirm that the `python` command runs the Python interpreter within the virtual environment:
  
  ::
  
    where python
    
- Confirm that the Python interpreter version is 3.6 or higher:
  
  ::
  
    python --version
    
- Confirm that the `pip` command runs the pip executable within the virtual environment:
  
  ::
  
    where pip
    
- To deactivate the environment:
  
  ::
  
    deactivate

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

Creating the `.env` File
------------------------

- In the project's root directory, create a file named `.env` if it doesn't already exist.
- Open the `.env` file in a text editor of your choice.

Defining Environment Variables
-------------------------------

- In the `.env` file, add the necessary environment variables. For the Django secret key and Sentry DSN, use appropriate variable names and assign them the corresponding values:

  ::
  
    DJANGO_SECRET_KEY=YourDjangoSecretKey
    SENTRY_DSN=YourSentryDSN
    
  Make sure to replace `YourDjangoSecretKey` with your actual Django secret key and `YourSentryDSN` with your real Sentry DSN.

Running the Website
~~~~~~~~~~~~~~~~~~~

- ``cd /path/to/OCP13``
- ``source venv/bin/activate``
- ``pip install --requirement requirements.txt``
- If `DEBUG` is set to `False` in your Django settings, make sure to collect static files first:
  
  ::
  
    python manage.py collectstatic
    
- Start the server:
  
  ::
  
    python manage.py runserver
    
- Open your web browser and navigate to `http://localhost:8000`.
- Confirm that the website is functioning, and you can navigate it (you should see multiple profiles and locations).

Linting
~~~~~~~

- Navigate to the project directory:
  
  ::
  
    cd /path/to/OCP13
    
- Activate the virtual environment:
  
  - For Unix-like systems:
    
    ::
    
      source venv/bin/activate
      
  - For Windows:
    
    ::
    
      venv\Scripts\activate
      
- Run the linter with `flake8`

Unit Tests
~~~~~~~~~~

- Navigate to the project directory:
  
  ::
  
    cd /path/to/OCP13
    
- Activate the virtual environment:
  
  - For Unix-like systems:
    
    ::
    
      source venv/bin/activate
      
  - For Windows:
    
    ::
    
      venv\Scripts\activate
      
- Run tests with `pytest`

Database
~~~~~~~~

- ``cd /path/to/OCP13``
- Open a shell session with `sqlite3`
- Connect to the database ``.open oc-lettings-site.sqlite3``
- Display tables in the database ``.tables``
- Display columns in the `profiles_profile` table: ``pragma table_info(profiles_profile);``
- Execute a query on the `profiles_profile` table: ``select user_id, favorite_city from profiles_profile where favorite_city like 'B%';``
- ``.quit`` to exit

Admin Panel
~~~~~~~~~~~

- Go to `http://localhost:8000/admin`
- Connect with username `admin`, password `Abc1234!`

Docker
~~~~~~

Creating a Docker Image and Run It Locally
------------------------------------------

1. Ensure that Docker is installed on your system. You can download Docker from the official website: https://www.docker.com/get-started.

2. Navigate to the root directory of your OCP13 project where the Dockerfile is located.

3. Open a terminal or command prompt.

4. To build the Docker image, use the following command:

   ::
   
     docker build -t your-image-name .
     
    `your-image-name` is the name you want to give to your Docker image.

5. Docker will now build the image based on the instructions in the Dockerfile. Once complete, you can check the list of local Docker images using the command:

   ::
   
     docker images
     
6. Running the Docker image

   ::
   
     docker run --rm -p 8000:8000 --env-file .env <your-image-name>
     
Pulling a Docker Image from Docker Hub and Run It Locally
----------------------------------------------------------

1. Ensure that Docker is installed on your system. You can download Docker from the official website: https://www.docker.com/get-started.

2. Go to the Docker repository: https://hub.docker.com/repository/docker/nopalpite/ocp13/tags

3. Copy the tag you would like to use (preferably the most recent).

4. Running the Docker image

   ::
   
     docker run --rm -p 8000:8000 nopalpite/ocp13:<image-tag>
     
    `image-tag` is the tag you've previously copied.