# Travel Planner API 

## Overview
This is a CRUD RESTful API application designed to help travellers plan trips and collect desired places to visit. For thsi task Django and Django REST Framework were used*.

The application allows users to manage travel projects, add places retrieved from a public API, attach personal notes. It includes specific business logic such as capacity limits, validations against external APIs, and automatic status updates.


## How to Run the Application with Docker 
1. Clone the repository:
   `git clone git@github.com:olesiakostak/Python-engineer-test-assessment-Travel-Planner.git`

   `cd Travel_Planner`
2. Build and start the containers:
    `docker-compose up --build`
3. The API will be available at: http://127.0.0.1:8000/api/


## API Endpoints
The API provides a fully browsable web interface provided by Django REST Framework at the base URL: http://127.0.0.1:8000/api/


GET /api/projects/ - List all travel projects

POST /api/projects/ - Create a new project

GET /api/projects/{id}/ - Retrieve a specific project (includes its places and is_completed status)

PUT / PATCH /api/projects/{id}/ - Update project details

DELETE /api/projects/{id}/ - Delete a project (fails if any place is visited)

### Example POST Request (Creating a project with places):
```bash
{
    "name": "Art Weekend in Chicago",
    "description": "Visiting the best artworks",
    "places_data": [
        {"external_id": "129884", "notes": "Must see!"},
        {"external_id": "111628"}
    ]
}
```