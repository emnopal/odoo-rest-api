# Odoo REST API Module
This is simple odoo module for REST API

# How to run?
- Fresh Install:
  - `docker-compose up -d` in your terminal (if you want to run using docker and/or you want to fresh install odoo)

- Existing Installation
  - move `addons/odoo-rest-api` into your odoo addons directory (if you have odoo), install in Apps then check the API in `GET /api/ping`
  - if you have existing odoo in docker and want to install this addons, mount directory `addons/odoo-rest-api` to odoo image which is running in docker and follow a step above

# Endpoint
- Check if API is working or server is active
  - `GET /api/ping`
  - `GET /api/check`
  - `GET /api/check/health`
  - `GET /api/health`
- List of Database in Odoo (which is model in odoo)
  - `GET /api/db`
  - `GET /api/database`
- Authentication and Authorization
  - `POST /api/auth/login`
  - `GET /api/auth/logout`
  - `POST /api/auth/logout`
- Get Data
  -  `GET /api/model/:model`
  -  `GET /api/model/:field`
  -  `GET /api/model/:rec_id`
  -  `GET /api/model/:rec_id/:field`
- Post Data
  - `POST /api/model/:model`
- Put Data
  - `PUT /api/model/:model`
  - `PUT /api/model/:model/:rec_id`
- Delete Data
  - `DELETE /api/model/:model`
  - `DELETE /api/model/:model/:rec_id`
