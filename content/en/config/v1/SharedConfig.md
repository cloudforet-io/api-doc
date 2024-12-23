---
title: "SharedConfig"
linkTitle: "SharedConfig"
weight: 3
bookFlatSection: true
---
# [SharedConfig](#SharedConfig)



>  **Package : spaceone.api.config.v1**

<br>
<br>

## SharedConfig





**SharedConfig Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./SharedConfig#create) | [CreateSharedConfigRequest](SharedConfig#createsharedconfigrequest) | [SharedConfigInfo](SharedConfig#sharedconfiginfo) |
| [**update**](./SharedConfig#update) | [UpdateSharedConfigRequest](SharedConfig#updatesharedconfigrequest) | [SharedConfigInfo](SharedConfig#sharedconfiginfo) |
| [**delete**](./SharedConfig#delete) | [SharedConfigRequest](SharedConfig#sharedconfigrequest) | [Empty](SharedConfig#empty) |
| [**get**](./SharedConfig#get) | [SharedConfigSearchQuery](SharedConfig#sharedconfigsearchquery) | [SharedConfigInfo](SharedConfig#sharedconfiginfo) |
| [**list**](./SharedConfig#list) | [SharedConfigSearchQuery](SharedConfig#sharedconfigsearchquery) | [SharedConfigsInfo](SharedConfig#sharedconfigsinfo) |



    
<br>

### create





> **POST** /config/v1/shared-config/create
>






    
<br>

### update





> **POST** /config/v1/shared-config/update
>






    
<br>

### delete





> **POST** /config/v1/shared-config/delete
>






    
<br>

### get





> **POST** /config/v1/shared-config/get
>






    
<br>

### list





> **POST** /config/v1/shared-config/list
>






    


<br>
<br>

## Message



### CreateSharedConfigRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### SharedConfigInfo
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### SharedConfigRequest
* **name** (string)   `Required` 

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### SharedConfigSearchQuery
* **query** (Query)  

    
* **name** (string)  

    <br>

### SharedConfigStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### SharedConfigsInfo
* **results** (SharedConfigInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateSharedConfigRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>
