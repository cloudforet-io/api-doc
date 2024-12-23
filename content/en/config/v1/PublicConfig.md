---
title: "PublicConfig"
linkTitle: "PublicConfig"
weight: 3
bookFlatSection: true
---
# [PublicConfig](#PublicConfig)



>  **Package : spaceone.api.config.v1**

<br>
<br>

## PublicConfig





**PublicConfig Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./PublicConfig#create) | [SetPublicConfigRequest](PublicConfig#setpublicconfigrequest) | [PublicConfigInfo](PublicConfig#publicconfiginfo) |
| [**update**](./PublicConfig#update) | [SetPublicConfigRequest](PublicConfig#setpublicconfigrequest) | [PublicConfigInfo](PublicConfig#publicconfiginfo) |
| [**set**](./PublicConfig#set) | [SetPublicConfigRequest](PublicConfig#setpublicconfigrequest) | [PublicConfigInfo](PublicConfig#publicconfiginfo) |
| [**delete**](./PublicConfig#delete) | [PublicConfigRequest](PublicConfig#publicconfigrequest) | [Empty](PublicConfig#empty) |
| [**get**](./PublicConfig#get) | [PublicConfigRequest](PublicConfig#publicconfigrequest) | [PublicConfigInfo](PublicConfig#publicconfiginfo) |
| [**list**](./PublicConfig#list) | [PublicConfigSearchQuery](PublicConfig#publicconfigsearchquery) | [PublicConfigsInfo](PublicConfig#publicconfigsinfo) |



    
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
<br>

## Message



### PublicConfigInfo
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
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

### SetPublicConfigRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **tags** (Struct)  

    <br>
