---
title: "DomainDashboard"
linkTitle: "DomainDashboard"
weight: 3
bookFlatSection: true
---
# [DomainDashboard](#DomainDashboard)
description of dashboard


>  **Package : spaceone.api.dashboard.v1**

<br>
<br>

## DomainDashboard





**DomainDashboard Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./DomainDashboard#create) | [CreateDomainDashboardRequest](DomainDashboard#createdomaindashboardrequest) | [DomainDashboardInfo](DomainDashboard#domaindashboardinfo) |
| [**update**](./DomainDashboard#update) | [UpdateDomainDashboardRequest](DomainDashboard#updatedomaindashboardrequest) | [DomainDashboardInfo](DomainDashboard#domaindashboardinfo) |
| [**delete**](./DomainDashboard#delete) | [DomainDashboardRequest](DomainDashboard#domaindashboardrequest) | [Empty](DomainDashboard#empty) |
| [**get**](./DomainDashboard#get) | [GetDomainDashboardRequest](DomainDashboard#getdomaindashboardrequest) | [DomainDashboardInfo](DomainDashboard#domaindashboardinfo) |
| [**delete_version**](./DomainDashboard#delete_version) | [DomainDashboardVersionRequest](DomainDashboard#domaindashboardversionrequest) | [Empty](DomainDashboard#empty) |
| [**revert_version**](./DomainDashboard#revert_version) | [DomainDashboardVersionRequest](DomainDashboard#domaindashboardversionrequest) | [DomainDashboardInfo](DomainDashboard#domaindashboardinfo) |
| [**get_version**](./DomainDashboard#get_version) | [GetDomainDashboardVersionRequest](DomainDashboard#getdomaindashboardversionrequest) | [DomainDashboardVersionInfo](DomainDashboard#domaindashboardversioninfo) |
| [**list_versions**](./DomainDashboard#list_versions) | [DomainDashboardVersionQuery](DomainDashboard#domaindashboardversionquery) | [DomainDashboardVersionsInfo](DomainDashboard#domaindashboardversionsinfo) |
| [**list**](./DomainDashboard#list) | [DomainDashboardQuery](DomainDashboard#domaindashboardquery) | [DomainDashboardsInfo](DomainDashboard#domaindashboardsinfo) |
| [**stat**](./DomainDashboard#stat) | [DomainDashboardStatQuery](DomainDashboard#domaindashboardstatquery) | [Struct](DomainDashboard#struct) |



    
<br>

### create





> **POST** /dashboard/v1/domain-dashboard/create
>






    
<br>

### update





> **POST** /dashboard/v1/domain-dashboard/update
>






    
<br>

### delete





> **POST** /dashboard/v1/domain-dashboard/delete
>






    
<br>

### get





> **POST** /dashboard/v1/domain-dashboard/get
>






    
<br>

### delete_version





> **POST** /dashboard/v1/domain-dashboard/delete-version
>






    
<br>

### revert_version





> **POST** /dashboard/v1/domain-dashboard/revert-version
>






    
<br>

### get_version





> **POST** /dashboard/v1/domain-dashboard/get-version
>






    
<br>

### list_versions





> **POST** /dashboard/v1/domain-dashboard/list-versions
>






    
<br>

### list





> **POST** /dashboard/v1/domain-dashboard/list
>






    
<br>

### stat





> **POST** /dashboard/v1/domain-dashboard/stat
>






    


<br>
<br>

## Message



### CreateDomainDashboardRequest
* **name** (string)   `Required` 

    
* **viewers** (Viewers)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **layouts** (ListValue)  

    
* **variables** (Struct)  

    
* **settings** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>

### DomainDashboardInfo
* **domain_dashboard_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **viewers** (Viewers)   `Required` 

    
* **version** (int32)   `Required` 

    
* **layouts** (ListValue)   `Required` 

    
* **variables** (Struct)   `Required` 

    
* **settings** (Struct)   `Required` 

    
* **variables_schema** (Struct)   `Required` 

    
* **labels** (ListValue)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### DomainDashboardQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **domain_dashboard_id** (string)  

    
* **name** (string)  

    
* **viewers** (Viewers)  

    
* **user_id** (string)  

    <br>

### DomainDashboardRequest
* **domain_dashboard_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### DomainDashboardStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### DomainDashboardVersionInfo
* **domain_dashboard_id** (string)   `Required` 

    
* **version** (int32)   `Required` 

    
* **latest** (bool)   `Required` 

    
* **layouts** (ListValue)   `Required` 

    
* **variables** (Struct)   `Required` 

    
* **settings** (Struct)   `Required` 

    
* **variables_schema** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### DomainDashboardVersionQuery
* **domain_dashboard_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **version** (int32)  

    <br>

### DomainDashboardVersionRequest
* **domain_dashboard_id** (string)   `Required` 

    
* **version** (int32)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### DomainDashboardVersionsInfo
* **results** (DomainDashboardVersionInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### DomainDashboardsInfo
* **results** (DomainDashboardInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### GetDomainDashboardRequest
* **domain_dashboard_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### GetDomainDashboardVersionRequest
* **domain_dashboard_id** (string)   `Required` 

    
* **version** (int32)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### UpdateDomainDashboardRequest
* **domain_dashboard_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **layouts** (ListValue)  

    
* **variables** (Struct)  

    
* **settings** (Struct)  

    
* **variables_schema** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>
