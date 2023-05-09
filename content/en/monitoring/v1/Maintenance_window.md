---
title: "Maintenance_window"
linkTitle: "Maintenance_window"
weight: 3
bookFlatSection: true
---
# [Maintenance_window](#Maintenance_window)
desc: A MaintenanceWindow is a resource snoozing Alerts during maintenance time.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Maintenance_window





**MaintenanceWindow Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./MaintenanceWindow#create) | [CreateMaintenanceWindowRequest](MaintenanceWindow#createmaintenancewindowrequest) | [MaintenanceWindowInfo](./MaintenanceWindow#maintenancewindowinfo) |
| [**update**](./MaintenanceWindow#update) | [UpdateMaintenanceWindowRequest](MaintenanceWindow#updatemaintenancewindowrequest) | [MaintenanceWindowInfo](./MaintenanceWindow#maintenancewindowinfo) |
| [**close**](./MaintenanceWindow#close) | [MaintenanceWindowRequest](MaintenanceWindow#maintenancewindowrequest) | [MaintenanceWindowInfo](./MaintenanceWindow#maintenancewindowinfo) |
| [**get**](./MaintenanceWindow#get) | [GetMaintenanceWindowRequest](MaintenanceWindow#getmaintenancewindowrequest) | [MaintenanceWindowInfo](./MaintenanceWindow#maintenancewindowinfo) |
| [**list**](./MaintenanceWindow#list) | [MaintenanceWindowQuery](MaintenanceWindow#maintenancewindowquery) | [MaintenanceWindowsInfo](./MaintenanceWindow#maintenancewindowsinfo) |
| [**stat**](./MaintenanceWindow#stat) | [MaintenanceWindowStatQuery](MaintenanceWindow#maintenancewindowstatquery) | [Struct](./MaintenanceWindow#struct) |



    
<br>

### create

desc: Creates a new MaintenanceWindow. When creating a MaintenanceWindow, you can set the title and maintenance schedule of the MaintenanceWindow. From the `start_time` to the `end_time` specified by the schedule set in this method, alerts in the Projects linked with the MaintenanceWindow are ceased.
request_example: >-
{
"title": "The dev server is under regular maintenance.",
"projects": ["project-123456789012"],
"start_time": "2022-01-01T09:45:00.000Z",
"end_time": "2022-01-01T10:45:00.000Z",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"maintenance_window_id": "mw-123456789012",
"title": "The dev server is under regular maintenance.",
"state": "OPEN",
"start_time": "2022-01-01T09:45:00.000Z",
"end_time": "2022-01-01T10:45:00.000Z",
"tags": {},
"projects": [
"project-123456789012"
],
"domain_id": "domain-123456789012",
"created_by": "user1@email.com",
"created_at": "2022-06-02T09:46:49.196Z",
"updated_at": "2022-06-02T09:46:49.196Z"
}



> **POST** /monitoring/v1/maintenance-window/create
>






    
<br>

### update

desc: Updates a specific MaintenanceWindow. You can make changes in MaintenanceWindow settings including, the `title` and the schedule.
request_example: >-
{
"maintenance_window_id": "mw-123456789012",
"title": "The dev server is under regular maintenance.",
"projects": ["project-123456789012"],
"start_time": "2022-01-03T00:00:00.000Z",
"end_time": "2022-01-03T01:00:00.000Z",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"maintenance_window_id": "mw-123456789012",
"title": "The dev server is under regular maintenance.",
"state": "OPEN",
"start_time": "2022-06-03T00:00:00.000Z",
"end_time": "2022-06-03T01:00:00.000Z",
"tags": {},
"projects": [
"project-123456789012"
],
"domain_id": "domain-123456789012",
"created_by": "user1@email.com",
"created_at": "2022-01-02T09:46:49.196Z",
"updated_at": "2022-01-02T09:46:49.196Z"
}



> **POST** /monitoring/v1/maintenance-window/update
>






    
<br>

### close

desc: Closes a MaintenanceWindow by changing the state of the MaintenanceWindow to `CLOSED` when the maintenance is completed. As the MaintenanceWindow is not deleted but closed, the maintenance history remains undeleted.
request_example: >-
{
"maintenance_window_id": "mw-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"maintenance_window_id": "mw-123456789012",
"title": "The dev server is under regular maintenance.",
"state": "CLOSED",
"start_time": "2022-06-03T00:00:00.000Z",
"end_time": "2022-06-03T01:00:00.000Z",
"tags": {},
"projects": [
"project-123456789012"
],
"domain_id": "domain-123456789012",
"created_by": "user1@email.com",
"created_at": "2022-01-02T09:46:49.196Z",
"updated_at": "2022-01-02T09:46:49.196Z"
}



> **POST** /monitoring/v1/maintenance-window/close
>






    
<br>

### get

desc: Gets a specific MaintenanceWindow. Prints detailed information about the MaintenanceWindow, including the title and the schedule.
request_example: >-
{
"maintenance_window_id": "mw-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"maintenance_window_id": "mw-123456789012",
"title": "The dev server is under regular maintenance.",
"state": "OPEN",
"start_time": "2022-06-03T00:00:00.000Z",
"end_time": "2022-06-03T01:00:00.000Z",
"tags": {},
"projects": [
"project-123456789012"
],
"domain_id": "domain-123456789012",
"created_by": "user1@email.com",
"created_at": "2022-01-02T09:46:49.196Z",
"updated_at": "2022-01-02T09:46:49.196Z"
}



> **POST** /monitoring/v1/maintenance-window/get
>






    
<br>

### list

desc: Gets a list of all MaintenanceWindows. You can use a query to get a filtered list of MaintenanceWindows.
request_example: >-
{
"query": {},
"domain_id": "domain-123456789012"
}
response_example: >-
{
"results": [
{
"maintenance_window_id": "mw-123456789012",
"title": "The dev server is under regular maintenance.",
"state": "OPEN",
"start_time": "2022-06-03T00:00:00.000Z",
"end_time": "2022-06-03T01:00:00.000Z",
"tags": {},
"projects": [
"project-123456789012"
],
"domain_id": "domain-123456789012",
"created_by": "user1@email.com",
"created_at": "2022-01-01T09:59:01.966Z",
"updated_at": "2022-01-01T09:59:01.966Z"
},
{
"maintenance_window_id": "mw-987654321098",
"title": "The prd server is under regular maintenance.",
"state": "OPEN",
"start_time": "2022-06-03T00:00:00.000Z",
"end_time": "2022-06-03T01:00:00.000Z",
"tags": {},
"projects": [
"project-123456789012"
],
"domain_id": "domain-123456789012",
"created_by": "user2@email.com",
"created_at": "2022-01-02T09:57:28.999Z",
"updated_at": "2022-01-02T09:57:28.999Z"
}
],
"total_count": 50
}



> **POST** /monitoring/v1/maintenance-window/list
>






    
<br>

### stat





> **POST** /monitoring/v1/maintenance-window/stat
>






    


<br>
<br>

## Message



### CreateMaintenanceWindowRequest
* **title** (string)  `Required` 

  *is_required: true*

    
* **projects** (string)  `Required` 

  *is_required: true*

    
* **start_time** (string)  `Required` 

  *is_required: true*

    
* **end_time** (string)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetMaintenanceWindowRequest
* **maintenance_window_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### MaintenanceWindowInfo
* **maintenance_window_id** (string)  `Required` 

    
* **title** (string)  `Required` 

    
* **state** (MaintenanceWindowState)  `Required` 

    
* **start_time** (string)  `Required` 

    
* **end_time** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **projects** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_by** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    
* **closed_at** (string)  `Required` 

    <br>

### MaintenanceWindowQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **maintenance_window_id** (string)  `Required` 

  *is_required: false*

    
* **title** (string)  `Required` 

  *is_required: false*

    
* **state** (MaintenanceWindowState)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **created_by** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### MaintenanceWindowRequest
* **maintenance_window_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### MaintenanceWindowStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### MaintenanceWindowsInfo
* **results** (MaintenanceWindowInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateMaintenanceWindowRequest
* **maintenance_window_id** (string)  `Required` 

  *is_required: true*

    
* **title** (string)  `Required` 

  *is_required: false*

    
* **projects** (string)  `Required` 

  *is_required: false*

    
* **start_time** (string)  `Required` 

  *is_required: false*

    
* **end_time** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
