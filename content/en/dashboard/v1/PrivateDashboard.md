---
title: "PrivateDashboard"
linkTitle: "PrivateDashboard"
weight: 3
bookFlatSection: true
---
# [PrivateDashboard](#PrivateDashboard)
description of dashboard


>  **Package : spaceone.api.dashboard.v1**

<br>
<br>

## PrivateDashboard





**PrivateDashboard Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./PrivateDashboard#create) | [PrivateCreateDashboardRequest](PrivateDashboard#privatecreatedashboardrequest) | [PrivateDashboardInfo](PrivateDashboard#privatedashboardinfo) |
| [**update**](./PrivateDashboard#update) | [PrivateUpdateDashboardRequest](PrivateDashboard#privateupdatedashboardrequest) | [PrivateDashboardInfo](PrivateDashboard#privatedashboardinfo) |
| [**delete**](./PrivateDashboard#delete) | [PrivateDashboardRequest](PrivateDashboard#privatedashboardrequest) | [Empty](PrivateDashboard#empty) |
| [**get**](./PrivateDashboard#get) | [PrivateDashboardRequest](PrivateDashboard#privatedashboardrequest) | [PrivateDashboardInfo](PrivateDashboard#privatedashboardinfo) |
| [**delete_version**](./PrivateDashboard#delete_version) | [PrivateDashboardVersionRequest](PrivateDashboard#privatedashboardversionrequest) | [Empty](PrivateDashboard#empty) |
| [**revert_version**](./PrivateDashboard#revert_version) | [PrivateDashboardVersionRequest](PrivateDashboard#privatedashboardversionrequest) | [PrivateDashboardInfo](PrivateDashboard#privatedashboardinfo) |
| [**get_version**](./PrivateDashboard#get_version) | [PrivateDashboardVersionRequest](PrivateDashboard#privatedashboardversionrequest) | [PrivateDashboardVersionInfo](PrivateDashboard#privatedashboardversioninfo) |
| [**list_versions**](./PrivateDashboard#list_versions) | [PrivateDashboardVersionSearchQuery](PrivateDashboard#privatedashboardversionsearchquery) | [PrivateDashboardVersionsInfo](PrivateDashboard#privatedashboardversionsinfo) |
| [**list**](./PrivateDashboard#list) | [PrivateDashboardQuery](PrivateDashboard#privatedashboardquery) | [PrivateDashboardsInfo](PrivateDashboard#privatedashboardsinfo) |
| [**stat**](./PrivateDashboard#stat) | [PrivateDashboardStatQuery](PrivateDashboard#privatedashboardstatquery) | [Struct](PrivateDashboard#struct) |



    
<br>

### create





> **POST** /dashboard/v1/private-dashboard/create
>






    
<br>

### update





> **POST** /dashboard/v1/private-dashboard/update
>






    
<br>

### delete





> **POST** /dashboard/v1/private-dashboard/delete
>






    
<br>

### get





> **POST** /dashboard/v1/private-dashboard/get
>






    
<br>

### delete_version





> **POST** /dashboard/v1/private-dashboard/delete-version
>






    
<br>

### revert_version





> **POST** /dashboard/v1/private-dashboard/revert-version
>






    
<br>

### get_version





> **POST** /dashboard/v1/private-dashboard/get-version
>






    
<br>

### list_versions





> **POST** /dashboard/v1/private-dashboard/list-versions
>






    
<br>

### list





> **POST** /dashboard/v1/private-dashboard/list
>






    
<br>

### stat





> **POST** /dashboard/v1/private-dashboard/stat
>






    


<br>
<br>

## Message



### PrivateCreateDashboardRequest
* **name** (string)   `Required` 

    
* **layouts** (ListValue)  

    
* **variables** (Struct)  

    
* **settings** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>

### PrivateDashboardInfo
* **private_dashboard_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **version** (int32)   `Required` 

    
* **layouts** (ListValue)   `Required` 

    
* **variables** (Struct)   `Required` 

    
* **settings** (Struct)   `Required` 

    
* **variables_schema** (Struct)   `Required` 

    
* **labels** (ListValue)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PrivateDashboardQuery
* **query** (Query)  

    
* **private_dashboard_id** (string)  

    
* **name** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### PrivateDashboardRequest
* **private_dashboard_id** (string)   `Required` 

    <br>

### PrivateDashboardStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### PrivateDashboardVersionInfo
* **private_dashboard_id** (string)   `Required` 

    
* **version** (int32)   `Required` 

    
* **latest** (bool)   `Required` 

    
* **layouts** (ListValue)   `Required` 

    
* **variables** (Struct)   `Required` 

    
* **settings** (Struct)   `Required` 

    
* **variables_schema** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### PrivateDashboardVersionRequest
* **private_dashboard_id** (string)   `Required` 

    
* **version** (int32)   `Required` 

    <br>

### PrivateDashboardVersionSearchQuery
* **private_dashboard_id** (string)   `Required` 

    
* **query** (Query)  

    
* **version** (int32)  

    <br>

### PrivateDashboardVersionsInfo
* **results** (PrivateDashboardVersionInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### PrivateDashboardsInfo
* **results** (PrivateDashboardInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### PrivateUpdateDashboardRequest
* **private_dashboard_id** (string)   `Required` 

    
* **name** (string)  

    
* **layouts** (ListValue)  

    
* **variables** (Struct)  

    
* **settings** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>
