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

### Retrieve All Movies

- **URL**: `/movies`
- **Method**: `GET`
- **Permissions Required**: `view:movies`

### Retrieve All Actors

- **URL**: `/actors`
- **Method**: `GET`
- **Permissions Required**: `view:actors`

### Create a New Movie

- **URL**: `/movies`
- **Method**: `POST`
- **Permissions Required**: `post:movies`

### Create a New Actor

- **URL**: `/actors`
- **Method**: `POST`
- **Permissions Required**: `post:actors`

### Delete a Movie

- **URL**: `/movies/<movie_id>`
- **Method**: `DELETE`
- **Permissions Required**: `delete:movies`

### Delete an Actor

- **URL**: `/actors/<actor_id>`
- **Method**: `DELETE`
- **Permissions Required**: `delete:actors`

### Update a Movie

- **URL**: `/movies/<movie_id>`
- **Method**: `PATCH`
- **Permissions Required**: `update:movies`

### Update an Actor

- **URL**: `/actors/<actor_id>`
- **Method**: `PATCH`
- **Permissions Required**: `update:actors`