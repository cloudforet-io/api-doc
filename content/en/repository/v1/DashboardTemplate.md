---
title: "DashboardTemplate"
linkTitle: "DashboardTemplate"
weight: 3
bookFlatSection: true
---
# [DashboardTemplate](#DashboardTemplate)



>  **Package : spaceone.api.repository.v1**

<br>
<br>

## DashboardTemplate





**DashboardTemplate Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](./DashboardTemplate#register) | [RegisterDashboardTemplateRequest](DashboardTemplate#registerdashboardtemplaterequest) | [DashboardTemplateInfo](DashboardTemplate#dashboardtemplateinfo) |
| [**update**](./DashboardTemplate#update) | [UpdateDashboardTemplateRequest](DashboardTemplate#updatedashboardtemplaterequest) | [DashboardTemplateInfo](DashboardTemplate#dashboardtemplateinfo) |
| [**deregister**](./DashboardTemplate#deregister) | [DashboardTemplateRequest](DashboardTemplate#dashboardtemplaterequest) | [Empty](DashboardTemplate#empty) |
| [**enable**](./DashboardTemplate#enable) | [DashboardTemplateRequest](DashboardTemplate#dashboardtemplaterequest) | [DashboardTemplateInfo](DashboardTemplate#dashboardtemplateinfo) |
| [**disable**](./DashboardTemplate#disable) | [DashboardTemplateRequest](DashboardTemplate#dashboardtemplaterequest) | [DashboardTemplateInfo](DashboardTemplate#dashboardtemplateinfo) |
| [**get**](./DashboardTemplate#get) | [RepositoryDashboardTemplateRequest](DashboardTemplate#repositorydashboardtemplaterequest) | [DashboardTemplateInfo](DashboardTemplate#dashboardtemplateinfo) |
| [**list**](./DashboardTemplate#list) | [DashboardTemplateQuery](DashboardTemplate#dashboardtemplatequery) | [DashboardTemplatesInfo](DashboardTemplate#dashboardtemplatesinfo) |



    
<br>

### register





> **POST** /repository/v1/dashboard-template/register
>






    
<br>

### update





> **POST** /repository/v1/dashboard-template/update
>






    
<br>

### deregister





> **POST** /repository/v1/dashboard-template/deregister
>






    
<br>

### enable





> **POST** /repository/v1/dashboard-template/enable
>






    
<br>

### disable





> **POST** /repository/v1/dashboard-template/disable
>






    
<br>

### get





> **POST** /repository/v1/dashboard-template/get
>






    
<br>

### list





> **POST** /repository/v1/dashboard-template/list
>






    


<br>
<br>

## Message



### DashboardTemplateInfo
* **template_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **template_type** (DashboardTemplateType)   `Required` 

    
* **dashboards** (ListValue)   `Required` 

    
* **labels** (ListValue)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **repository_info** (RepositoryInfo)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### DashboardTemplateQuery
* **query** (Query)  

    
* **template_id** (string)  

    
* **name** (string)  

    
* **state** (State)  

    
* **template_type** (DashboardTemplateType)  

    
* **repository_id** (string)  

    <br>

### DashboardTemplateRequest
* **template_id** (string)   `Required` 

    <br>

### DashboardTemplatesInfo
* **results** (DashboardTemplateInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### RegisterDashboardTemplateRequest
* **name** (string)   `Required` 

    
* **template_id** (string)  

    
* **template_type** (DashboardTemplateType)  

    
* **dashboards** (ListValue)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>

### RepositoryDashboardTemplateRequest
* **template_id** (string)   `Required` 

    
* **repository_id** (string)  

    <br>

### UpdateDashboardTemplateRequest
* **template_id** (string)   `Required` 

    
* **name** (string)  

    
* **template_type** (DashboardTemplateType)  

    
* **dashboards** (ListValue)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>
