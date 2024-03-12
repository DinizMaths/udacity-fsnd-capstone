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

**Casting Assistant JWT**: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1QT29qaFVtWDRCQzNwZFJNVU01VSJ9.eyJpc3MiOiJodHRwczovL2Rldi01eHNuZXE4emc2ZGhibXpjLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NWVmMjkwYTBmMjI2NzZmNDg4NTdiMzQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTcxMDE3Mjc0MywiZXhwIjoxNzEwMTc5OTQzLCJhenAiOiJnbGNqazB4aEV3ZDZKVnFTRDV2aW5VUjhVdVNiSWFydSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIl19.hU9AqjwGlG4-f8SQhX8pUMROYOboJuXAV97Ld0AN_bvn0J0FghvlnWBUhYY8M4Ff7HO87FQFXRJB-rp1Q3bVy424XwKXVFqfxqh1uxVWVe1Nn1SYDZrgshI3JGNgy5nqEQjDMFFtWNC4deIrmHiIUJiQjE0cQGQcL1wYU2k2H6ORwv8bgm9w4rBxgjCykLbFSoKz3hNzqTeIXOBIB6iaoSIaUOJIORqgcHRrpzPrRNENwyu4RkvPRJMlgBiERE9kIOkL4iDBUv3YDb7rmWGoKsyN2n5UJ_YquuXZFmcySwRNxv67RR788dnXc5BwZQLPuCrgiU-NHSEewH_CBIKbxQ

**Casting Director JWT**: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1QT29qaFVtWDRCQzNwZFJNVU01VSJ9.eyJpc3MiOiJodHRwczovL2Rldi01eHNuZXE4emc2ZGhibXpjLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NWVmMjk0MGVjZmI1ZDFmZmQzMTlhZGIiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTcxMDE3MjkzOSwiZXhwIjoxNzEwMTgwMTM5LCJhenAiOiJnbGNqazB4aEV3ZDZKVnFTRDV2aW5VUjhVdVNiSWFydSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwb3N0OmFjdG9yIl19.XKsZ0TkAFkl4xLbjIM54WY0wcmStNjvey_-443W_TGMIeXMDF--YqDS2y7o89GIq8dNFvL0ZLAL3klWObhN-kig_8A3KNGy57cdIAjiNhQWvQzptYvXMAYZooL9OJ6fKnB28xS58JFOyiyPfwQBtRUN938RZ3r1Go_fA-qcTt3lknCToCIPdtHDxwGOSniACZz6zL7zQScADhAsTZUvHKfZjtwXBeAQTngmCga1H2pN_CI4mKEcS0GL-jdb5BrhsEG5geMySUqPv5JkuQY5QA22rw47HIP4gUTI0mBJa8ugYS1HZigpt4zCdWHM_lClZiotyOiI0ezhJbF8fMM7VJA

**Executive Producer JWT**: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1QT29qaFVtWDRCQzNwZFJNVU01VSJ9.eyJpc3MiOiJodHRwczovL2Rldi01eHNuZXE4emc2ZGhibXpjLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NWVmMjk2YWYyOGVjNWJiNWZmMTk5ZDYiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTcxMDE3MzE1MiwiZXhwIjoxNzEwMTgwMzUyLCJhenAiOiJnbGNqazB4aEV3ZDZKVnFTRDV2aW5VUjhVdVNiSWFydSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.C-9exm0mubulnGkBexLLopNTBUv7mUCbxCj35U_00ri-j-pxUUD03m8Slh9_FdUHgQmU0WWOe0DGESMyoLy3pQgdt61oRQHXAMzVRF2B4IzOujNWCdnzQoZJlxddLxScf6QDGknHo5TlBA6MOr-Ur84NmclTOU_akH59t4SFj_dLHYjpqodns_w_ATMv6fwe7SRX9xVQzDBe_7bdAah8_Un393NH-JEQ4xvKQQoO3W6KyxewFHlSEsRe3j6bxc0pTCiUqw6ejwjOB0mMRE1qCXG1MIXm4KinTEaALrIN7P0fXGy668pd_golKVQQmvsWxzK3KJqTr4pF5mRDgrbxBA