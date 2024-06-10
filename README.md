
# Coinbase project

Auto fetching data from coinbase


## Getting Started
Prerequisites 

- Python 3.x

- Docker

- Docker Compose

- Celery

- Postgres

## Usage
1. Create a virtual environment and activate it:
```commandline
pip install pipenv

pipenv shell
```
2. Install the project dependencies:
```commandline
pip install -r requirements.txt
```
3. Build the Docker images (if needed):
```commandline
docker-compose build
```
4. Start the Docker containers:
```commandline
docker-compose up
```
5. Database migrate(first time)
```commandline
docker-compose run web python manage.py migrate
```    


