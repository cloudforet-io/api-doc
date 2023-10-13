---
title: "Provider"
linkTitle: "Provider"
weight: 3
bookFlatSection: true
---
# [Provider](#Provider)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## Provider





**Provider Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Provider#create) | [CreateProviderRequest](Provider#createproviderrequest) | [ProviderInfo](Provider#providerinfo) |
| [**update**](./Provider#update) | [UpdateProviderRequest](Provider#updateproviderrequest) | [ProviderInfo](Provider#providerinfo) |
| [**delete**](./Provider#delete) | [ProviderRequest](Provider#providerrequest) | [Empty](Provider#empty) |
| [**get**](./Provider#get) | [GetProviderRequest](Provider#getproviderrequest) | [ProviderInfo](Provider#providerinfo) |
| [**list**](./Provider#list) | [ProviderQuery](Provider#providerquery) | [ProvidersInfo](Provider#providersinfo) |
| [**stat**](./Provider#stat) | [ProviderStatQuery](Provider#providerstatquery) | [Struct](Provider#struct) |



    
<br>

### create





> **POST** /identity/v1/provider/create
>






    
<br>

### update





> **POST** /identity/v1/provider/update
>






    
<br>

### delete





> **POST** /identity/v1/provider/delete
>






    
<br>

### get





> **POST** /identity/v1/provider/get
>






    
<br>

### list





> **POST** /identity/v1/provider/list
>






    
<br>

### stat





> **POST** /identity/v1/provider/stat
>






    


<br>
<br>

## Message



### CreateProviderRequest
* **provider** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **template** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **order** (int32)  

    
* **metadata** (Struct)  

    
* **capability** (Struct)  

    
* **tags** (Struct)  

    <br>

### GetProviderRequest
* **provider** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### ProviderInfo
* **provider** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **order** (int32)   `Required` 

    
* **template** (Struct)   `Required` 

    
* **metadata** (Struct)   `Required` 

    
* **capability** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### ProviderQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **provider** (string)  

    
* **name** (string)  

    <br>

### ProviderRequest
* **provider** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### ProviderStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### ProvidersInfo
* **results** (ProviderInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateProviderRequest
* **provider** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **order** (int32)  

    
* **template** (Struct)  

    
* **metadata** (Struct)  

    
* **capability** (Struct)  

    
* **tags** (Struct)  

    <br>
