# Checking_balances

[![CircleCI](https://circleci.com/gh/paulovb/checking_balances.svg?style=svg)](https://circleci.com/gh/paulovb/checking_balances)
[![codecov](https://codecov.io/gh/paulovb/checking_balances/branch/master/graph/badge.svg?token=aYJm1Ab91K)](https://codecov.io/gh/paulovb/checking_balances)

You can get the know how to use this API in [API-Document](API-Document.md).

Also, You can use a tool like [PostMan](https://www.getpostman.com/) to help you consumming it.

### Prerequisites

You need have installed python=3.6.6.
But, I believe you prefer a shortcut to set up this application with Docker.

### Installing

You just need run:

```
$ docker-compose build
```

Or, on local machine:
```
$ pip install -r requirements.txt
$ ./manage.py migrate
```

### Running server

To run with Docker:
```
$ docker-compose up -d
```

Or at folder if installed on local machine, run:
```
$ ./manage.py runserver
```

The application running in `http://localhost:8000`.

## Running the tests

To run all tests:
```
$ docker-compose run --rm web ./manage.py test -v2
```

Or:
```
$ ./manage.py test -v2
```

## Deployment

This application have been deployed on Heroku: 

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Clean Architecture](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html) - The application's architecture
* [Docker](https://www.docker.com/) - The container engine used
* [Heroku](https://www.heroku.com/) - The Clound application plataform
