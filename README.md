# Odoo REST API Module
This is simple odoo module for REST API

# How to run?
- Fresh Install:
  - `docker-compose up -d` in your terminal (if you want to run using docker and/or you want to fresh install odoo)

- Existing Installation
  - move `addons/odoo-rest-api` into your odoo addons directory (if you have odoo), install in Apps then check in `GET /api/ping`
  - if you have existing odoo in docker and want to install this addons, mount directory `addons/odoo-rest-api` to odoo image which is running in docker and follow a step above
