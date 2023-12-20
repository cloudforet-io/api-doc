---
title: "PublicDashboard"
linkTitle: "PublicDashboard"
weight: 3
bookFlatSection: true
---
# [PublicDashboard](#PublicDashboard)
description of dashboard


>  **Package : spaceone.api.dashboard.v1**

<br>
<br>

## PublicDashboard





**PublicDashboard Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./PublicDashboard#create) | [CreatePublicDashboardRequest](PublicDashboard#createpublicdashboardrequest) | [PublicDashboardInfo](PublicDashboard#publicdashboardinfo) |
| [**update**](./PublicDashboard#update) | [UpdatePublicDashboardRequest](PublicDashboard#updatepublicdashboardrequest) | [PublicDashboardInfo](PublicDashboard#publicdashboardinfo) |
| [**delete**](./PublicDashboard#delete) | [PublicDashboardRequest](PublicDashboard#publicdashboardrequest) | [Empty](PublicDashboard#empty) |
| [**get**](./PublicDashboard#get) | [PublicDashboardRequest](PublicDashboard#publicdashboardrequest) | [PublicDashboardInfo](PublicDashboard#publicdashboardinfo) |
| [**delete_version**](./PublicDashboard#delete_version) | [PublicDashboardVersionRequest](PublicDashboard#publicdashboardversionrequest) | [Empty](PublicDashboard#empty) |
| [**revert_version**](./PublicDashboard#revert_version) | [PublicDashboardVersionRequest](PublicDashboard#publicdashboardversionrequest) | [PublicDashboardInfo](PublicDashboard#publicdashboardinfo) |
| [**get_version**](./PublicDashboard#get_version) | [PublicDashboardVersionRequest](PublicDashboard#publicdashboardversionrequest) | [PublicDashboardVersionInfo](PublicDashboard#publicdashboardversioninfo) |
| [**list_versions**](./PublicDashboard#list_versions) | [PublicDashboardVersionSearchQuery](PublicDashboard#publicdashboardversionsearchquery) | [PublicDashboardVersionsInfo](PublicDashboard#publicdashboardversionsinfo) |
| [**list**](./PublicDashboard#list) | [PublicDashboardQuery](PublicDashboard#publicdashboardquery) | [PublicDashboardsInfo](PublicDashboard#publicdashboardsinfo) |
| [**stat**](./PublicDashboard#stat) | [PublicDashboardStatQuery](PublicDashboard#publicdashboardstatquery) | [Struct](PublicDashboard#struct) |



    
<br>

### create





> **POST** /dashboard/v1/public-dashboard/create
>






    
<br>

### update





> **POST** /dashboard/v1/public-dashboard/update
>






    
<br>

### delete





> **POST** /dashboard/v1/public-dashboard/delete
>






    
<br>

### get





> **POST** /dashboard/v1/public-dashboard/get
>






    
<br>

### delete_version





> **POST** /dashboard/v1/public-dashboard/delete-version
>






    
<br>

### revert_version





> **POST** /dashboard/v1/public-dashboard/revert-version
>






    
<br>

### get_version





> **POST** /dashboard/v1/public-dashboard/get-version
>






    
<br>

### list_versions





> **POST** /dashboard/v1/public-dashboard/list-versions
>






    
<br>

### list





> **POST** /dashboard/v1/public-dashboard/list
>






    
<br>

### stat





> **POST** /dashboard/v1/public-dashboard/stat
>






    


<br>
<br>

## Message



### CreatePublicDashboardRequest
* **name** (string)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **layouts** (ListValue)  

    
* **variables** (Struct)  

    
* **settings** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### PublicDashboardInfo
* **public_dashboard_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **version** (int32)   `Required` 

    
* **layouts** (ListValue)   `Required` 

    
* **variables** (Struct)   `Required` 

    
* **settings** (Struct)   `Required` 

    
* **variables_schema** (Struct)   `Required` 

    
* **labels** (ListValue)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PublicDashboardQuery
* **query** (Query)  

    
* **public_dashboard_id** (string)  

    
* **name** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### PublicDashboardRequest
* **public_dashboard_id** (string)   `Required` 

    <br>

### PublicDashboardStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### PublicDashboardVersionInfo
* **public_dashboard_id** (string)   `Required` 

    
* **version** (int32)   `Required` 

    
* **latest** (bool)   `Required` 

    
* **layouts** (ListValue)   `Required` 

    
* **variables** (Struct)   `Required` 

    
* **settings** (Struct)   `Required` 

    
* **variables_schema** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### PublicDashboardVersionRequest
* **public_dashboard_id** (string)   `Required` 

    
* **version** (int32)   `Required` 

    <br>

### PublicDashboardVersionSearchQuery
* **public_dashboard_id** (string)   `Required` 

    
* **query** (Query)  

    
* **version** (int32)  

    <br>

### PublicDashboardVersionsInfo
* **results** (PublicDashboardVersionInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### PublicDashboardsInfo
* **results** (PublicDashboardInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePublicDashboardRequest
* **public_dashboard_id** (string)   `Required` 

    
* **name** (string)  

    
* **layouts** (ListValue)  

    
* **variables** (Struct)  

    
* **settings** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>
