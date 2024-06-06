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

    
* **description** (string)  

    
* **layouts** (Layout)  `Repeated`   

    
* **vars** (Struct)  

    
* **options** (Struct)  

    
* **variables** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    
* **folder_id** (string)  

    <br>

### Layout
* **name** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **widgets** (Struct)  `Repeated`    `Required` 

    <br>

### PublicDashboardInfo
* **dashboard_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **version** (string)   `Required` 

    
* **layouts** (Layout)  `Repeated`    `Required` 

    
* **vars** (Struct)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **variables** (Struct)   `Required` 

    
* **variables_schema** (Struct)   `Required` 

    
* **labels** (ListValue)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **folder_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PublicDashboardQuery
* **query** (Query)  

    
* **dashboard_id** (string)  

    
* **name** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    
* **folder_id** (string)  

    <br>

### PublicDashboardRequest
* **dashboard_id** (string)   `Required` 

    <br>

### PublicDashboardStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### PublicDashboardsInfo
* **results** (PublicDashboardInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePublicDashboardRequest
* **dashboard_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **layouts** (Layout)  `Repeated`   

    
* **vars** (Struct)  

    
* **options** (Struct)  

    
* **variables** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    
* **folder_id** (string)  

    <br>
