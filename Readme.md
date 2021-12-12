# Django API

This is a simple django API base project

# Techs
- Django
- Dajngo restframework
- Postgres

# How to start development server

- Build docker container using `docker-compose up --build`
- Create `.env` file with `cp .env.example .env`
- Generate secret key `chmod +x ./generate_secret.sh && ./generate_secret.sh`, copy the generated key to `SECRET_KEY` value in your `.env` file
- Fill `.env` file with the correct database credentials
- Run migrations with `docker-compose run --rm web python manage.py migrate`
- Create a new superadmin user `docker-compose run --rm web python manage create_user <admin/user> user@app.com  <password>`. Example: `docker-compose run --rm web python manage.py create_user admin user@app.com django`
- Run the docker container `docker-compose up`
- Install node dependencies `npm install`
- Run webpack `npm run dev`

# Useful commands

- Run project: `docker-compose up`
- Create migrations: `docker-compose run --rm web python manage.py makemigrations <app_name>`
- Run migrations: `docker-compose run --rm web python manage.py migrate <app_name>`
- Generate secret key: `chmod +x ./generate_secret.sh && ./generate_secret.sh`
- Create messages: `docker-compose run --rm web python manage.py makemessages -a`
- Compile messages: `docker-compose run --rm web python manage.py compilemessages`
- Create API Key: `docker-compose run --rm web python manage.py create_api_key <client_name>`
- Remove API Key: `docker-compose run --rm web python manage.py remove_api_key <client_name>`
