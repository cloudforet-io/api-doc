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
| [**create**](./PrivateDashboard#create) | [CreatePrivateDashboardRequest](PrivateDashboard#createprivatedashboardrequest) | [PrivateDashboardInfo](PrivateDashboard#privatedashboardinfo) |
| [**update**](./PrivateDashboard#update) | [UpdatePrivateDashboardRequest](PrivateDashboard#updateprivatedashboardrequest) | [PrivateDashboardInfo](PrivateDashboard#privatedashboardinfo) |
| [**change_folder**](./PrivateDashboard#change_folder) | [ChangeFolderPrivateDashboardRequest](PrivateDashboard#changefolderprivatedashboardrequest) | [PrivateDashboardInfo](PrivateDashboard#privatedashboardinfo) |
| [**delete**](./PrivateDashboard#delete) | [PrivateDashboardRequest](PrivateDashboard#privatedashboardrequest) | [Empty](PrivateDashboard#empty) |
| [**get**](./PrivateDashboard#get) | [PrivateDashboardRequest](PrivateDashboard#privatedashboardrequest) | [PrivateDashboardInfo](PrivateDashboard#privatedashboardinfo) |
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

### change_folder





> **POST** /dashboard/v1/private-dashboard/change-folder
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



### ChangeFolderPrivateDashboardRequest
* **dashboard_id** (string)   `Required` 

    
* **folder_id** (string)  

    <br>

### CreatePrivateDashboardRequest
* **name** (string)   `Required` 

    
* **description** (string)  

    
* **layouts** (Layout)  `Repeated`   

    
* **vars** (Struct)  

    
* **vars_schema** (Struct)  

    
* **options** (Struct)  

    
* **variables** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    
* **folder_id** (string)  

    <br>

### PrivateDashboardInfo
* **dashboard_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **version** (string)   `Required` 

    
* **layouts** (Layout)  `Repeated`    `Required` 

    
* **vars** (Struct)   `Required` 

    
* **vars_schema** (Struct)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **variables** (Struct)   `Required` 

    
* **variables_schema** (Struct)   `Required` 

    
* **labels** (ListValue)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **folder_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PrivateDashboardQuery
* **query** (Query)  

    
* **dashboard_id** (string)  

    
* **name** (string)  

    
* **workspace_id** (string)  

    
* **folder_id** (string)  

    <br>

### PrivateDashboardRequest
* **dashboard_id** (string)   `Required` 

    <br>

### PrivateDashboardStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### PrivateDashboardsInfo
* **results** (PrivateDashboardInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePrivateDashboardRequest
* **dashboard_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **layouts** (Layout)  `Repeated`   

    
* **vars** (Struct)  

    
* **vars_schema** (Struct)  

    
* **options** (Struct)  

    
* **variables** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    
* **folder_id** (string)  

    <br>
