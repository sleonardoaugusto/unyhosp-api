# unyhosp-api
[![Build Status](https://travis-ci.org/sleonardoaugusto/unyhosp-frontend.svg?branch=master)](https://travis-ci.org/sleonardoaugusto/unyhosp-frontend)

## Setup
1. Clone this repo <br/>
`$ git clone https://github.com/sleonardoaugusto/unyhosp-api`

2. Fire up containers
* Develop <br/>
`$ docker-compose -f docker-compose.yml up -d --build`
* Production <br/>
`$ docker-compose -f docker-compose.prod.yml up -d --build`

## Tests
* Run tests <br/>
`$ docker exec -it unyhosp_api pytest`