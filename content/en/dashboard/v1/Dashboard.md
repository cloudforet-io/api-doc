---
title: "Dashboard"
linkTitle: "Dashboard"
weight: 3
bookFlatSection: true
---
# [Dashboard](#Dashboard)
description of dashboard


>  **Package : spaceone.api.dashboard.v1**

<br>
<br>

## Dashboard





**Dashboard Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Dashboard#create) | [CreateDashboardRequest](Dashboard#createdashboardrequest) | [DashboardInfo](Dashboard#dashboardinfo) |
| [**update**](./Dashboard#update) | [UpdateDashboardRequest](Dashboard#updatedashboardrequest) | [DashboardInfo](Dashboard#dashboardinfo) |
| [**delete**](./Dashboard#delete) | [DashboardRequest](Dashboard#dashboardrequest) | [Empty](Dashboard#empty) |
| [**get**](./Dashboard#get) | [DashboardRequest](Dashboard#dashboardrequest) | [DashboardInfo](Dashboard#dashboardinfo) |
| [**delete_version**](./Dashboard#delete_version) | [DashboardVersionRequest](Dashboard#dashboardversionrequest) | [Empty](Dashboard#empty) |
| [**revert_version**](./Dashboard#revert_version) | [DashboardVersionRequest](Dashboard#dashboardversionrequest) | [DashboardInfo](Dashboard#dashboardinfo) |
| [**get_version**](./Dashboard#get_version) | [DashboardVersionRequest](Dashboard#dashboardversionrequest) | [DashboardVersionInfo](Dashboard#dashboardversioninfo) |
| [**list_versions**](./Dashboard#list_versions) | [DashboardVersionSearchQuery](Dashboard#dashboardversionsearchquery) | [DashboardVersionsInfo](Dashboard#dashboardversionsinfo) |
| [**list**](./Dashboard#list) | [DashboardQuery](Dashboard#dashboardquery) | [DashboardsInfo](Dashboard#dashboardsinfo) |
| [**stat**](./Dashboard#stat) | [DashboardStatQuery](Dashboard#dashboardstatquery) | [Struct](Dashboard#struct) |



    
<br>

### create





> **POST** /dashboard/v1/dashboard/create
>






    
<br>

### update





> **POST** /dashboard/v1/dashboard/update
>






    
<br>

### delete





> **POST** /dashboard/v1/dashboard/delete
>






    
<br>

### get





> **POST** /dashboard/v1/dashboard/get
>






    
<br>

### delete_version





> **POST** /dashboard/v1/dashboard/delete-version
>






    
<br>

### revert_version





> **POST** /dashboard/v1/dashboard/revert-version
>






    
<br>

### get_version





> **POST** /dashboard/v1/dashboard/get-version
>






    
<br>

### list_versions





> **POST** /dashboard/v1/dashboard/list-versions
>






    
<br>

### list





> **POST** /dashboard/v1/dashboard/list
>






    
<br>

### stat





> **POST** /dashboard/v1/dashboard/stat
>






    


<br>
<br>

## Message



### CreateDashboardRequest
* **name** (string)   `Required` 

    
* **dashboard_type** (DashboardType)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **layouts** (ListValue)  

    
* **variables** (Struct)  

    
* **settings** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    
* **project_id** (string)  

    <br>

### DashboardInfo
* **dashboard_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **dashboard_type** (DashboardType)   `Required` 

    
* **version** (int32)   `Required` 

    
* **layouts** (ListValue)   `Required` 

    
* **variables** (Struct)   `Required` 

    
* **settings** (Struct)   `Required` 

    
* **variables_schema** (Struct)   `Required` 

    
* **labels** (ListValue)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### DashboardQuery
* **query** (Query)  

    
* **dashboard_id** (string)  

    
* **name** (string)  

    
* **dashboard_type** (DashboardType)  

    
* **user_id** (string)  

    
* **resource_group** (ResourceGroup)  

    
* **project_id** (string)  

    
* **workspace_id** (string)  

    <br>

### DashboardRequest
* **dashboard_id** (string)   `Required` 

    <br>

### DashboardStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### DashboardVersionInfo
* **dashboard_id** (string)   `Required` 

    
* **version** (int32)   `Required` 

    
* **latest** (bool)   `Required` 

    
* **layouts** (ListValue)   `Required` 

    
* **variables** (Struct)   `Required` 

    
* **settings** (Struct)   `Required` 

    
* **variables_schema** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### DashboardVersionRequest
* **dashboard_id** (string)   `Required` 

    
* **version** (int32)   `Required` 

    <br>

### DashboardVersionSearchQuery
* **dashboard_id** (string)   `Required` 

    
* **query** (Query)  

    
* **version** (int32)  

    <br>

### DashboardVersionsInfo
* **results** (DashboardVersionInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### DashboardsInfo
* **results** (DashboardInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateDashboardRequest
* **dashboard_id** (string)   `Required` 

    
* **name** (string)  

    
* **layouts** (ListValue)  

    
* **variables** (Struct)  

    
* **settings** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>
