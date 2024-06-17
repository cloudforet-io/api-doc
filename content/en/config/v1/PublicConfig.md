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
| [**update**](./PublicConfig#update) | [CreatePublicConfigRequest](PublicConfig#createpublicconfigrequest) | [PublicConfigInfo](PublicConfig#publicconfiginfo) |
| [**set**](./PublicConfig#set) | [CreatePublicConfigRequest](PublicConfig#createpublicconfigrequest) | [PublicConfigInfo](PublicConfig#publicconfiginfo) |
| [**delete**](./PublicConfig#delete) | [PublicConfigRequest](PublicConfig#publicconfigrequest) | [Empty](PublicConfig#empty) |
| [**get**](./PublicConfig#get) | [PublicConfigRequest](PublicConfig#publicconfigrequest) | [PublicConfigInfo](PublicConfig#publicconfiginfo) |
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

### set





> **POST** /config/v1/public-config/set
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

    <br>
