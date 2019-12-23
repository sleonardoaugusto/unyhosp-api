#unyhosp-api

##Setup
1. Clone this repo <br/>
`$ git clone https://github.com/sleonardoaugusto/unyhosp-api`

2. Build and up containers <br/>
`$ docker-compose build && docker-compose up -d`

3. Reload application <br/>
`$ docker-compose restart`

4. Migrate tables <br/>
`$ docker-compose run api python manage.py migrate`