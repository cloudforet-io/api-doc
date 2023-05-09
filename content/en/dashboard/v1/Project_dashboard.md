---
title: "Project_dashboard"
linkTitle: "Project_dashboard"
weight: 3
bookFlatSection: true
---
# [Project_dashboard](#Project_dashboard)
description of dashboard


>  **Package : spaceone.api.dashboard.v1**

<br>
<br>

## Project_dashboard





**ProjectDashboard Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./ProjectDashboard#create) | [CreateProjectDashboardRequest](ProjectDashboard#createprojectdashboardrequest) | [ProjectDashboardInfo](./ProjectDashboard#projectdashboardinfo) |
| [**update**](./ProjectDashboard#update) | [UpdateProjectDashboardRequest](ProjectDashboard#updateprojectdashboardrequest) | [ProjectDashboardInfo](./ProjectDashboard#projectdashboardinfo) |
| [**delete**](./ProjectDashboard#delete) | [ProjectDashboardRequest](ProjectDashboard#projectdashboardrequest) | [Empty](./ProjectDashboard#empty) |
| [**get**](./ProjectDashboard#get) | [GetProjectDashboardRequest](ProjectDashboard#getprojectdashboardrequest) | [ProjectDashboardInfo](./ProjectDashboard#projectdashboardinfo) |
| [**delete_version**](./ProjectDashboard#delete_version) | [ProjectDashboardVersionRequest](ProjectDashboard#projectdashboardversionrequest) | [Empty](./ProjectDashboard#empty) |
| [**revert_version**](./ProjectDashboard#revert_version) | [ProjectDashboardVersionRequest](ProjectDashboard#projectdashboardversionrequest) | [ProjectDashboardInfo](./ProjectDashboard#projectdashboardinfo) |
| [**get_version**](./ProjectDashboard#get_version) | [GetProjectDashboardVersionRequest](ProjectDashboard#getprojectdashboardversionrequest) | [ProjectDashboardVersionInfo](./ProjectDashboard#projectdashboardversioninfo) |
| [**list_versions**](./ProjectDashboard#list_versions) | [ProjectDashboardVersionQuery](ProjectDashboard#projectdashboardversionquery) | [ProjectDashboardVersionsInfo](./ProjectDashboard#projectdashboardversionsinfo) |
| [**list**](./ProjectDashboard#list) | [ProjectDashboardQuery](ProjectDashboard#projectdashboardquery) | [ProjectDashboardsInfo](./ProjectDashboard#projectdashboardsinfo) |
| [**stat**](./ProjectDashboard#stat) | [ProjectDashboardStatQuery](ProjectDashboard#projectdashboardstatquery) | [Struct](./ProjectDashboard#struct) |



    
<br>

### create





> **POST** /dashboard/v1/project-dashboard/create
>






    
<br>

### update





> **POST** /dashboard/v1/project-dashboard/update
>






    
<br>

### delete





> **POST** /dashboard/v1/project-dashboard/delete
>






    
<br>

### get





> **POST** /dashboard/v1/project-dashboard/get
>






    
<br>

### delete_version





> **POST** /dashboard/v1/project-dashboard/delete-version
>






    
<br>

### revert_version





> **POST** /dashboard/v1/project-dashboard/revert-version
>






    
<br>

### get_version





> **POST** /dashboard/v1/project-dashboard/get-version
>






    
<br>

### list_versions





> **POST** /dashboard/v1/project-dashboard/list-versions
>






    
<br>

### list





> **POST** /dashboard/v1/project-dashboard/list
>






    
<br>

### stat





> **POST** /dashboard/v1/project-dashboard/stat
>






    


<br>
<br>

## Message



### CreateProjectDashboardRequest
* **project_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **viewers** (Viewers)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **layouts** (ListValue) 

    
* **variables** (Struct) 

    
* **settings** (Struct) 

    
* **variables_schema** (Struct) 

    
* **labels** (ListValue) 

    
* **tags** (Struct) 

    <br>

### GetProjectDashboardRequest
* **project_dashboard_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### GetProjectDashboardVersionRequest
* **project_dashboard_id** (string)  `Required` 

    
* **version** (int32)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### ProjectDashboardInfo
* **project_dashboard_id** (string)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **viewers** (Viewers)  `Required` 

    
* **version** (int32)  `Required` 

    
* **layouts** (ListValue)  `Required` 

    
* **variables** (Struct)  `Required` 

    
* **settings** (Struct)  `Required` 

    
* **variables_schema** (Struct)  `Required` 

    
* **labels** (ListValue)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **user_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### ProjectDashboardQuery
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **project_dashboard_id** (string) 

    
* **project_id** (string) 

    
* **name** (string) 

    
* **viewers** (Viewers) 

    
* **user_id** (string) 

    <br>

### ProjectDashboardRequest
* **project_dashboard_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### ProjectDashboardStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### ProjectDashboardVersionInfo
* **project_dashboard_id** (string)  `Required` 

    
* **version** (int32)  `Required` 

    
* **latest** (bool)  `Required` 

    
* **layouts** (ListValue)  `Required` 

    
* **variables** (Struct)  `Required` 

    
* **settings** (Struct)  `Required` 

    
* **variables_schema** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### ProjectDashboardVersionQuery
* **project_dashboard_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **version** (int32) 

    <br>

### ProjectDashboardVersionRequest
* **project_dashboard_id** (string)  `Required` 

    
* **version** (int32)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### ProjectDashboardVersionsInfo
* **results** (ProjectDashboardVersionInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### ProjectDashboardsInfo
* **results** (ProjectDashboardInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateProjectDashboardRequest
* **project_dashboard_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **name** (string) 

    
* **layouts** (ListValue) 

    
* **variables** (Struct) 

    
* **settings** (Struct) 

    
* **variables_schema** (Struct) 

    
* **labels** (ListValue) 

    
* **tags** (Struct) 

    <br>
