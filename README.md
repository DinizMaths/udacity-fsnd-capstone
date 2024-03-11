# Udacity Capstone Project

## Project Overview

This project is the capstone project for the Udacity Full Stack Developer Nanodegree. The project is a simple web application that allows users to create, read, update, and delete items in a database. The application is built using Python, Flask, and PostgreSQL.


## Running the Application

### Setup

1. Clone the repository

```bash
git clone https://github.com/DinizMaths/udacity-fsnd-capstone.git
```

2. Change into the project directory

```bash
cd udacity-fsnd-capstone
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

## Endpoints

The endpoints are protected by Auth0 and require a valid JWT token to access. The following roles and permissions are available:

<img src="./figures/roles.png" alt="Auth0 Roles" width="500"/>

### Get Movies

- **URL**: `/movies`
- **Method**: `GET`
- **Permissions Required**: `view:movies`
- **Roles**: [Casting Assistant, Casting Director, Executive Producer]

### Get Actors

- **URL**: `/actors`
- **Method**: `GET`
- **Permissions Required**: `view:actors`
- **Roles**: [Casting Assistant, Casting Director, Executive Producer]

### Post a Movie

- **URL**: `/movies`
- **Method**: `POST`
- **Permissions Required**: `post:movies`
- **Roles**: [Executive Producer]

### Post a Actor

- **URL**: `/actors`
- **Method**: `POST`
- **Permissions Required**: `post:actors`
- **Roles**: [Casting Director, Executive Producer]

### Delete Movie

- **URL**: `/movies/<movie_id>`
- **Method**: `DELETE`
- **Permissions Required**: `delete:movies`
- **Roles**: [Executive Producer]

### Delete Actor

- **URL**: `/actors/<actor_id>`
- **Method**: `DELETE`
- **Permissions Required**: `delete:actors`
- **Roles**: [Casting Director, Executive Producer]

### Patch a Movie

- **URL**: `/movies/<movie_id>`
- **Method**: `PATCH`
- **Permissions Required**: `update:movies`
- **Roles**: [Executive Producer]

### Patch an Actor

- **URL**: `/actors/<actor_id>`
- **Method**: `PATCH`
- **Permissions Required**: `update:actors`
- **Roles**: [Casting Director, Executive Producer]