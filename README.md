# falcon-jwt-sample
Sample implementation of Python 3.8, Falcon API, and falcon-auth on Docker.

# How to run?
1. Make sure you have `Python 3.8` and `Virtualenv` on your machine.
```
    $ sudo apt-get install python3.8 virtualenv
```

2. Clone the repository by running:
```
    $ git clone https://github.com/ndato/falcon-jwt-sample.git
```

3. Create a virtual environment for Python by executing the following commands:
```
    $ cd falcon-jwt-sample
    $ python3 -m virtualenv .venv --python=/usr/bin/python3.8
```

4. Activate the virtual environment.
```
    $ source .venv/bin/activate
```

5. Install the packages needed to run the program:
```
    (.venv) $ pip install -r requirements.txt --no-cache
```
6. Fill up the .env details
```
    (.venv) $ cp .env.sample .env
    (.venv) $ nano .env
```

7. Run the Dockerized version of the application.
```
    (.venv) $ sudo docker-compose up --build
```