# REST API for Project Management

This project implements a REST API using **FastAPI** to manage projects, allowing for project creation, time logging, and project deletion. The projects are stored in an **SQLite** database.

## Description

The API allows the following actions on projects:

1. **Create a project**: If the project does not exist, a new project is created with an initial time of 0.
2. **Get all projects**: Displays all projects and their associated time.
3. **Log time**: Allows adding time to an existing project.
4. **Delete a project**: Removes a project from the database.
5. **Snapshot**: *(Future)* Functionality to create a snapshot of a project.

Projects are represented by their **name** and an associated **time** (in minutes).

