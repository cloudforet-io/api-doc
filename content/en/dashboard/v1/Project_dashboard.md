---
title: "Project_dashboard"
linkTitle: "Project_dashboard"
weight: 3
bookFlatSection: true
---
# [Project_dashboard](#Project_dashboard)
desc: description of dashboard


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




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /dashboard/v1/project-dashboard/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /dashboard/v1/project-dashboard/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /dashboard/v1/project-dashboard/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### delete_version

> **POST** /dashboard/v1/project-dashboard/delete-version
>




 {{< tabs " delete_version " >}}




{{< /tabs >}}

    
<br>

### revert_version

> **POST** /dashboard/v1/project-dashboard/revert-version
>




 {{< tabs " revert_version " >}}




{{< /tabs >}}

    
<br>

### get_version

> **POST** /dashboard/v1/project-dashboard/get-version
>




 {{< tabs " get_version " >}}




{{< /tabs >}}

    
<br>

### list_versions

> **POST** /dashboard/v1/project-dashboard/list-versions
>




 {{< tabs " list_versions " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /dashboard/v1/project-dashboard/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /dashboard/v1/project-dashboard/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateProjectDashboardRequest
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: true*

    
* **viewers** (Viewers)  `Required` 

  *is_required: true*

    
* **layouts** (ListValue)  `Required` 

  *is_required: false*

    
* **variables** (Struct)  `Required` 

  *is_required: false*

    
* **settings** (Struct)  `Required` 

  *is_required: false*

    
* **variables_schema** (Struct)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetProjectDashboardRequest
* **project_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### GetProjectDashboardVersionRequest
* **project_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **version** (int32)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

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
* **query** (Query)  `Required` 

  *is_required: false*

    
* **project_dashboard_id** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **viewers** (Viewers)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectDashboardRequest
* **project_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectDashboardStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

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
* **query** (Query)  `Required` 

  *is_required: false*

    
* **project_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **version** (int32)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectDashboardVersionRequest
* **project_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **version** (int32)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

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

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **layouts** (ListValue)  `Required` 

  *is_required: false*

    
* **variables** (Struct)  `Required` 

  *is_required: false*

    
* **settings** (Struct)  `Required` 

  *is_required: false*

    
* **variables_schema** (Struct)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
