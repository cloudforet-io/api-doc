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

    
* **layouts** (ListValue)  

    
* **vars** (Struct)  

    
* **settings** (Struct)  

    
* **variables** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### PublicDashboardInfo
* **public_dashboard_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **version** (string)   `Required` 

    
* **layouts** (ListValue)   `Required` 

    
* **vars** (Struct)   `Required` 

    
* **settings** (Struct)   `Required` 

    
* **variables** (Struct)   `Required` 

    
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

### PublicDashboardsInfo
* **results** (PublicDashboardInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePublicDashboardRequest
* **public_dashboard_id** (string)   `Required` 

    
* **name** (string)  

    
* **layouts** (ListValue)  

    
* **vars** (Struct)  

    
* **settings** (Struct)  

    
* **variables** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>
