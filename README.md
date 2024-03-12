# Udacity Capstone Project

## Project Overview

This project is the capstone project for the Udacity Full Stack Developer Nanodegree. The project is a simple web application that allows users to create, read, update, and delete items in a database. The application is built using Python, Flask, and PostgreSQL.

To follow the best practices, the application was developed using Pylint for linting and Pytest for testing.

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

Additionally, the following permissions are available:

<img src="./figures/permissions.png" alt="Auth0 Permissions" width="500"/>

### Movie

#### Get Movies

- **URL**: `/movies`
- **Method**: `GET`
- **Permissions Required**: `get:movie`
- **Roles**: [Casting Assistant, Casting Director, Executive Producer]

#### Post Movie

- **URL**: `/movies`
- **Method**: `POST`
- **Permissions Required**: `post:movie`
- **Roles**: [Executive Producer]

#### Patch Movie

- **URL**: `/movies/<movie_id>`
- **Method**: `PATCH`
- **Permissions Required**: `patch:movie`
- **Roles**: [Executive Producer]

#### Delete Movie

- **URL**: `/movies/<movie_id>`
- **Method**: `DELETE`
- **Permissions Required**: `delete:movie`
- **Roles**: [Executive Producer]

### Actor

#### Get Actors

- **URL**: `/actors`
- **Method**: `GET`
- **Permissions Required**: `get:actor`
- **Roles**: [Casting Assistant, Casting Director, Executive Producer]

#### Post Actor

- **URL**: `/actors`
- **Method**: `POST`
- **Permissions Required**: `post:actor`
- **Roles**: [Casting Director, Executive Producer]

#### Patch Actor

- **URL**: `/actors/<actor_id>`
- **Method**: `PATCH`
- **Permissions Required**: `patch:actor`
- **Roles**: [Casting Director, Executive Producer]

#### Delete Actor

- **URL**: `/actors/<actor_id>`
- **Method**: `DELETE`
- **Permissions Required**: `delete:actor`
- **Roles**: [Casting Director, Executive Producer]

# Jason Web Tokens

**Casting Assistant JWT**: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1QT29qaFVtWDRCQzNwZFJNVU01VSJ9.eyJpc3MiOiJodHRwczovL2Rldi01eHNuZXE4emc2ZGhibXpjLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NWVmMjkwYTBmMjI2NzZmNDg4NTdiMzQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTcxMDI3NzI5MywiZXhwIjoxNzEwMzYzNjkzLCJhenAiOiJnbGNqazB4aEV3ZDZKVnFTRDV2aW5VUjhVdVNiSWFydSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIl19.mkPbEELMkNyWJblD9ZGvaHEkQeBAG1Q2fZIWQwOOuOMxj-WaS1MqtTppeqhITCCrdTzLldfwLspMYvpgZ1cFzoE8VgEBbS9mmAqRlq05ggUXAD42Kks_U6WOTUnbCEi4dBjUMNpxYHsXq7AeQIu8ZXvtRM-LAFrAES0d2Uj0hgMn_YGBJUdYBx_Ld0gcB8s8YyI_TGKtIsM94LugoVAfvt2T5HoDd7RbttQnucKCBMMMCHWeRqHD2afbhKBGXm2GvdQvzEHLe34KPDGpOldB7W51qxOcKgFKP7Imrqs6z8xwehbkHnl4P6UABTfAx1t4XxNoZwNxxG-KTI1zbb8kIQ

**Casting Director JWT**: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1QT29qaFVtWDRCQzNwZFJNVU01VSJ9.eyJpc3MiOiJodHRwczovL2Rldi01eHNuZXE4emc2ZGhibXpjLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NWVmMjk0MGVjZmI1ZDFmZmQzMTlhZGIiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTcxMDI3NzM1MSwiZXhwIjoxNzEwMzYzNzUxLCJhenAiOiJnbGNqazB4aEV3ZDZKVnFTRDV2aW5VUjhVdVNiSWFydSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwb3N0OmFjdG9yIl19.EyRz3q1yLM5ToH6Nt4qoeLxlLj5brUMaGnjTAB2mGtKu4A0eR1mLH8qBG8hJNSCaYACdxdYJzRbplGBMRHD4O3V69z6tkplIe290xVvHwuFDJWqgOVY_EalN5126KjjFjF-QRX2-wTrYBsMB2lblCksHyNj0xYR9_Ipl53d5nKpzEdoCkowaj0SC02VY5pbZA5AppEJJfUlbL2BKucQ-uSmnqQ59xB6Pb8YLs9jpbzwXN6-VfWEfHy-_xpXQCq6eiryvbpkoR4YoRVp-9zb0S6UExrQ-ZRfsPOPdAZcd1hOp60rIu0x3mKRkU3edjuykKRoHC-zBOKgFzuyD110SPg

**Executive Producer JWT**: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1QT29qaFVtWDRCQzNwZFJNVU01VSJ9.eyJpc3MiOiJodHRwczovL2Rldi01eHNuZXE4emc2ZGhibXpjLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NWVmMjk2YWYyOGVjNWJiNWZmMTk5ZDYiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTcxMDI3NzM5NywiZXhwIjoxNzEwMzYzNzk3LCJhenAiOiJnbGNqazB4aEV3ZDZKVnFTRDV2aW5VUjhVdVNiSWFydSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.I6t28xbsbAG-toRIw9jiekj_HmB2V4SoHie7ubIbaXCYtHNV5HxM44CuhxznljiRAI5izNnzfagvZVmHmBmpBJlDRl7LcH078Rf7UcstW0zlEaQ-DoCr0CgxSEu8EpGttMOiNFlCsPg7zyyf2Trotx7k8WXPwQoGe43MK5r3ta_fzb9vp_E-kSqU45AiKjzE0tIWZLgMNw_t_Bn3UrFdU2krrVUPN3kU2GfzorIWI3ipO0-2ow9D95QDrJlRpV-bITR9v5pmPEcZw7QYmMSRrgioM1GmIXKJSuwS2Bwyi8w-xLW4LtdLGHDVihtYfLVWzBRkFka0-iT-pgBw9WCgGw