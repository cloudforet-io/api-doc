---
title: "App"
linkTitle: "App"
weight: 3
bookFlatSection: true
---
# [App](#App)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## App





**App Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./App#create) | [CreateAppRequest](App#createapprequest) | [AppInfo](App#appinfo) |
| [**update**](./App#update) | [UpdateAppRequest](App#updateapprequest) | [AppInfo](App#appinfo) |
| [**generate_client_secret**](./App#generate_client_secret) | [GenerateAPIKeyAppRequest](App#generateapikeyapprequest) | [AppInfo](App#appinfo) |
| [**enable**](./App#enable) | [AppRequest](App#apprequest) | [AppInfo](App#appinfo) |
| [**disable**](./App#disable) | [AppRequest](App#apprequest) | [AppInfo](App#appinfo) |
| [**delete**](./App#delete) | [AppRequest](App#apprequest) | [Empty](App#empty) |
| [**get**](./App#get) | [AppRequest](App#apprequest) | [AppInfo](App#appinfo) |
| [**check**](./App#check) | [AppCheckRequest](App#appcheckrequest) | [CheckAppInfo](App#checkappinfo) |
| [**list**](./App#list) | [AppSearchQuery](App#appsearchquery) | [AppsInfo](App#appsinfo) |
| [**stat**](./App#stat) | [AppStatQuery](App#appstatquery) | [Struct](App#struct) |



    
<br>

### create





> **POST** /identity/v2/app/create
>






    
<br>

### update





> **POST** /identity/v2/app/update
>






    
<br>

### generate_client_secret





> **POST** /identity/v2/app/generate-client-secret
>






    
<br>

### enable





> **POST** /identity/v2/app/enable
>






    
<br>

### disable





> **POST** /identity/v2/app/disable
>






    
<br>

### delete





> **POST** /identity/v2/app/delete
>






    
<br>

### get





> **POST** /identity/v2/app/get
>






    
<br>

### check










    
<br>

### list





> **POST** /identity/v2/app/list
>






    
<br>

### stat





> **POST** /identity/v2/app/stat
>






    


<br>
<br>

## Message



### AppCheckRequest
* **client_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### AppInfo
* **app_id** (string)   `Required` 

    
* **client_secret** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    
* **client_id** (string)   `Required` 

    
* **project_group_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **expired_at** (string)   `Required` 

    
* **last_accessed_at** (string)   `Required` 

    <br>

### AppRequest
* **app_id** (string)   `Required` 

    <br>

### AppSearchQuery
* **query** (Query)  

    
* **app_id** (string)  

    
* **name** (string)  

    
* **state** (State)  

    
* **role_type** (RoleType)  

    
* **workspace_id** (string)  

    
* **role_id** (string)  

    
* **client_id** (string)  

    <br>

### AppStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### AppsInfo
* **results** (AppInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CheckAppInfo
* **permissions** (string)  `Repeated`    `Required` 

    
* **projects** (string)  `Repeated`    `Required` 

    <br>

### CreateAppRequest
* **name** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **project_group_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **tags** (Struct)  

    
* **expired_at** (string)  

    
* **workspace_id** (string)  

    <br>

### GenerateAPIKeyAppRequest
* **app_id** (string)   `Required` 

    
* **expired_at** (string)  

    <br>

### UpdateAppRequest
* **app_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>
