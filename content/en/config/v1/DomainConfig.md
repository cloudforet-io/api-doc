---
title: "DomainConfig"
linkTitle: "DomainConfig"
weight: 3
bookFlatSection: true
---
# [DomainConfig](#DomainConfig)
DomainConfig API which configure environments for domain


>  **Package : spaceone.api.config.v1**

<br>
<br>

## DomainConfig





**DomainConfig Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./DomainConfig#create) | [SetDomainConfigRequest](DomainConfig#setdomainconfigrequest) | [DomainConfigInfo](./DomainConfig#domainconfiginfo) |
| [**update**](./DomainConfig#update) | [SetDomainConfigRequest](DomainConfig#setdomainconfigrequest) | [DomainConfigInfo](./DomainConfig#domainconfiginfo) |
| [**set**](./DomainConfig#set) | [SetDomainConfigRequest](DomainConfig#setdomainconfigrequest) | [DomainConfigInfo](./DomainConfig#domainconfiginfo) |
| [**delete**](./DomainConfig#delete) | [DomainConfigRequest](DomainConfig#domainconfigrequest) | [Empty](./DomainConfig#empty) |
| [**get**](./DomainConfig#get) | [GetDomainConfigRequest](DomainConfig#getdomainconfigrequest) | [DomainConfigInfo](./DomainConfig#domainconfiginfo) |
| [**list**](./DomainConfig#list) | [DomainConfigQuery](DomainConfig#domainconfigquery) | [DomainConfigsInfo](./DomainConfig#domainconfigsinfo) |
| [**stat**](./DomainConfig#stat) | [DomainConfigStatQuery](DomainConfig#domainconfigstatquery) | [Struct](./DomainConfig#struct) |



    
<br>

### create





> **POST** /config/v1/domain-config/create
>






    
<br>

### update





> **POST** /config/v1/domain-config/update
>






    
<br>

### set





> **POST** /config/v1/domain-config/set
>






    
<br>

### delete





> **POST** /config/v1/domain-config/delete
>






    
<br>

### get





> **POST** /config/v1/domain-config/get
>






    
<br>

### list





> **POST** /config/v1/domain-config/list
>






    
<br>

### stat





> **POST** /config/v1/domain-config/stat
>






    


<br>
<br>

## Message



### DomainConfigInfo
* **name** (string)  `Required` 

    
* **data** (Struct)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### DomainConfigQuery
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **name** (string) 

    <br>

### DomainConfigRequest
* **name** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### DomainConfigStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### DomainConfigsInfo
* **results** (DomainConfigInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### GetDomainConfigRequest
* **name** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### SetDomainConfigRequest
* **name** (string)  `Required` 

    
* **data** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **tags** (Struct) 

    <br>
