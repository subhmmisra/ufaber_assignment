# ufaber_assignment
## This project is a Task Management Web App which is developed using the tech stack of Django Rest Framework for backend and Django templates for frontend.

We have used sqlite3 db for this project.

List of APIs:

1: Project APIS ENDPOINTS
 - Create Project API
 - Retrieve Project API (Project Detail)
 - List Project API
 - Edit Project API
 - Delete Project API
 
2: Tasks APIS ENDPOINTS
 - Create Task API
 - Retrieve Task API (Project Detail)
 - List Tasks API
 - Edit Tasks API
 - Delete Tasks API
 
 
 
 Documentation for Project APIs:
 - Project Creation
    - [POST] api/projects
    - data: {
    "name": "tt3",
    "description": "xyz",
    "duration": 2
}
   - response: {
            "id": "8b7eb0e4-b1de-4a48-9561-24af3a7d79e0",
            "name": "tt3",
            "description": "xyz",
            "duration": 2
        }

- Project Lists
   - [GET] api/projects
   - response: {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "9825cf53-1ec9-4d4f-884b-574ecd5f5c8c",
            "name": "tt3",
            "description": "xyz",
            "duration": 2   
        }
        ]}
        
- Project Update API
   - [PUT] api/projects/{project_id}
   - data: {
    "name": "tt3",
    "description": "xyz",
    "duration": 2
}
   
   
   - response: 
        {
            "id": "9825cf53-1ec9-4d4f-884b-574ecd5f5c8c",
            "name": "tt3",
            "description": "xyz",
            "duration": 2   
        }





- Project Retrieve API
   - [GET] api/projects/{project_id}
   - response: 
        {
            "id": "9825cf53-1ec9-4d4f-884b-574ecd5f5c8c",
            "name": "tt3",
            "description": "xyz",
            "duration": 2   
        }

- Project Retrieve API
   - [GET] api/projects/{project_id}
   - response: 
        {
            "id": "9825cf53-1ec9-4d4f-884b-574ecd5f5c8c",
            "name": "tt3",
            "description": "xyz",
            "duration": 2   
        }

- Project Delete API
   - [DELETE] api/projects/{project_id}
   - response: 
        {
            no-content
        }

- Project Tasks List
  - [GET] api/projects/{project_id}/tasks
  - response: 
        {
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "9825cf53-1ec9-4d4f-884b-574ecd5f5c8c",
            "name": "tt3",
            "description": "xyz",
            "start_date": "2021-12-12",
            "end_date": "2021-12-13",
            "project": {
                "id": "337e4d30-0c38-44b4-93ae-7942bca6fe4a",
                "name": "t4"
            }
        }]
        }



Documentation for Tasks APIs:
 - Tasks Creation
   - [POST] api/tasks
   - data: {
    "name": "tt3",
    "description": "xyz",
    "start_date": "2021-01-01",
    "end_date": "2021-01-02"
    "project": "337e4d30-0c38-44b4-93ae-7942bca6fe4a"
}
  -  response: {
            "id": "9825cf53-1ec9-4d4f-884b-574ecd5f5c8c",
            "name": "tt3",
            "description": "xyz",
            "start_date": "2021-12-12",
            "end_date": "2021-12-13",
            "project": {
                "id": "337e4d30-0c38-44b4-93ae-7942bca6fe4a",
                "name": "t4"
        }
        }

- Tasks Lists
   - [GET] api/tasks
   - response: {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "9825cf53-1ec9-4d4f-884b-574ecd5f5c8c",
            "name": "tt3",
            "description": "xyz",
            "start_date": "2021-12-12",
            "end_date": "2021-12-13",
            "project": {
                "id": "337e4d30-0c38-44b4-93ae-7942bca6fe4a",
                "name": "t4"
            }
        }]
        
- Task Update API
   - [PUT] api/tasks/{task_id}
   - data: {
    "name": "tt3",
    "description": "xyz",
    "start_date": "2021-12-12",
    "end_date": "2021-12-13",
    "project": "337e4d30-0c38-44b4-93ae-7942bca6fe4a"
}
   - response: 
        {
            "id": "9825cf53-1ec9-4d4f-884b-574ecd5f5c8c",
            "name": "tt3",
            "description": "xyz",
            "start_date": "2021-12-12",
            "end_date": "2021-12-13",
            "project": {
                "id": "337e4d30-0c38-44b4-93ae-7942bca6fe4a",
                "name": "t4"
            }
        }

- Task Retrieve API
   - [GET] api/tasks/{task_id}
   - response: 
        {
            "id": "9825cf53-1ec9-4d4f-884b-574ecd5f5c8c",
            "name": "tt3",
            "description": "xyz",
            "start_date": "2021-12-12",
            "end_date": "2021-12-13",
            "project": {
                "id": "337e4d30-0c38-44b4-93ae-7942bca6fe4a",
                "name": "t4"
            }
        }


- Task Delete API
   - [DELETE] api/tasks/{task_id}
   - response: 
        {
            no-content
        }


