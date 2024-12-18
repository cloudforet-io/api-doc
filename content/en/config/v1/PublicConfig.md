---
title: "PublicConfig"
linkTitle: "PublicConfig"
weight: 3
bookFlatSection: true
---
# [PublicConfig](#PublicConfig)
DomainConfig API which configure environments for domain


>  **Package : spaceone.api.config.v1**

<br>
<br>

## PublicConfig





**PublicConfig Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./PublicConfig#create) | [CreatePublicConfigRequest](PublicConfig#createpublicconfigrequest) | [PublicConfigInfo](PublicConfig#publicconfiginfo) |
| [**update**](./PublicConfig#update) | [UpdatePublicConfigRequest](PublicConfig#updatepublicconfigrequest) | [PublicConfigInfo](PublicConfig#publicconfiginfo) |
| [**delete**](./PublicConfig#delete) | [PublicConfigRequest](PublicConfig#publicconfigrequest) | [Empty](PublicConfig#empty) |
| [**get**](./PublicConfig#get) | [PublicConfigSearchQuery](PublicConfig#publicconfigsearchquery) | [PublicConfigInfo](PublicConfig#publicconfiginfo) |
| [**get_accessible_configs**](./PublicConfig#get_accessible_configs) | [PublicConfigSearchQuery](PublicConfig#publicconfigsearchquery) | [PublicConfigsInfo](PublicConfig#publicconfigsinfo) |
| [**list**](./PublicConfig#list) | [PublicConfigSearchQuery](PublicConfig#publicconfigsearchquery) | [PublicConfigsInfo](PublicConfig#publicconfigsinfo) |
| [**stat**](./PublicConfig#stat) | [PublicConfigStatQuery](PublicConfig#publicconfigstatquery) | [Struct](PublicConfig#struct) |



    
<br>

### create





> **POST** /config/v1/public-config/create
>






    
<br>

### update





> **POST** /config/v1/public-config/update
>






    
<br>

### delete





> **POST** /config/v1/public-config/delete
>






    
<br>

### get





> **POST** /config/v1/public-config/get
>






    
<br>

### get_accessible_configs

This API for retrieving domain scoped configs that are accessible to users.



> **POST** /config/v1/public-config/get-accessible-configs
>






    
<br>

### list





> **POST** /config/v1/public-config/list
>






    
<br>

### stat





> **POST** /config/v1/public-config/stat
>






    


<br>
<br>

## Message



### CreatePublicConfigRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### PublicConfigInfo
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

### PublicConfigRequest
* **name** (string)   `Required` 

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### PublicConfigSearchQuery
* **query** (Query)  

    
* **name** (string)  

    <br>

### PublicConfigStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### PublicConfigsInfo
* **results** (PublicConfigInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePublicConfigRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>
