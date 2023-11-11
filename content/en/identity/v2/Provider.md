---
title: "Provider"
linkTitle: "Provider"
weight: 3
bookFlatSection: true
---
# [Provider](#Provider)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Provider





**Provider Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Provider#create) | [CreateProviderRequest](Provider#createproviderrequest) | [ProviderInfo](Provider#providerinfo) |
| [**update**](./Provider#update) | [UpdateProviderRequest](Provider#updateproviderrequest) | [ProviderInfo](Provider#providerinfo) |
| [**delete**](./Provider#delete) | [ProviderRequest](Provider#providerrequest) | [Empty](Provider#empty) |
| [**get**](./Provider#get) | [ProviderRequest](Provider#providerrequest) | [ProviderInfo](Provider#providerinfo) |
| [**list**](./Provider#list) | [ProviderSearchQuery](Provider#providersearchquery) | [ProvidersInfo](Provider#providersinfo) |
| [**stat**](./Provider#stat) | [ProviderStatQuery](Provider#providerstatquery) | [Struct](Provider#struct) |



    
<br>

### create





> **POST** /identity/v2/provider/create
>






    
<br>

### update





> **POST** /identity/v2/provider/update
>






    
<br>

### delete





> **POST** /identity/v2/provider/delete
>






    
<br>

### get





> **POST** /identity/v2/provider/get
>






    
<br>

### list





> **POST** /identity/v2/provider/list
>






    
<br>

### stat





> **POST** /identity/v2/provider/stat
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

### ProviderRequest
* **provider** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### ProviderSearchQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **provider** (string)  

    
* **name** (string)  

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
