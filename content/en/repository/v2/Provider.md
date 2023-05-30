---
title: "Provider"
linkTitle: "Provider"
weight: 3
bookFlatSection: true
---
# [Provider](#Provider)



>  **Package : spaceone.api.repository.v2**

<br>
<br>

## Provider





**Provider Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Provider#create) | [CreateProviderRequest](Provider#createproviderrequest) | [ProviderInfo](Provider#providerinfo) |
| [**update**](./Provider#update) | [UpdateProviderRequest](Provider#updateproviderrequest) | [ProviderInfo](Provider#providerinfo) |
| [**sync**](./Provider#sync) | [ProviderRequest](Provider#providerrequest) | [ProviderInfo](Provider#providerinfo) |
| [**delete**](./Provider#delete) | [ProviderRequest](Provider#providerrequest) | [Empty](Provider#empty) |
| [**get**](./Provider#get) | [GetProviderRequest](Provider#getproviderrequest) | [ProviderInfo](Provider#providerinfo) |
| [**list**](./Provider#list) | [ProviderQuery](Provider#providerquery) | [ProvidersInfo](Provider#providersinfo) |



    
<br>

### create





> **POST** /repository/v2/provider/create
>






    
<br>

### update





> **POST** /repository/v2/provider/update
>






    
<br>

### sync





> **POST** /repository/v2/provider/sync
>






    
<br>

### delete





> **POST** /repository/v2/provider/delete
>






    
<br>

### get





> **POST** /repository/v2/provider/get
>






    
<br>

### list





> **POST** /repository/v2/providers/list
>






    


<br>
<br>

## Message



### Capability
* **trusted_service_account** (string)   `Required` 

    <br>

### CreateProviderRequest
* **provider** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **sync_mode** (SyncMode)  

    
* **sync_options** (SyncOptions)  

    
* **description** (Description)  `Repeated`   

    
* **schema** (ProviderSchema)  `Repeated`   

    
* **capability** (Capability)  

    
* **color** (string)  

    
* **icon** (string)  

    
* **reference** (Reference)  `Repeated`   

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    
* **domain_id** (string)  

    <br>

### Description
* **resource_type** (string)   `Required` 

    
* **body** (Struct)   `Required` 

    <br>

### GetProviderRequest
* **provider** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    
* **domain_id** (string)  

    <br>

### ProviderInfo
* **provider** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **sync_mode** (SyncMode)   `Required` 

    
* **sync_options** (SyncOptions)   `Required` 

    
* **description** (Description)  `Repeated`    `Required` 

    
* **schema** (ProviderSchema)  `Repeated`    `Required` 

    
* **capability** (Capability)   `Required` 

    
* **color** (string)   `Required` 

    
* **icon** (string)   `Required` 

    
* **reference** (Reference)  `Repeated`    `Required` 

    
* **labels** (ListValue)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **remote_repository** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### ProviderQuery
* **query** (Query)  

    
* **provider** (string)  

    
* **name** (string)  

    
* **sync_mode** (SyncMode)  

    
* **remote_repository_name** (string)  

    
* **domain_id** (string)  

    <br>

### ProviderRequest
* **provider** (string)   `Required` 

    
* **domain_id** (string)  

    <br>

### ProviderSchema
* **resource_type** (string)   `Required` 

    
* **secret_type** (string)   `Required` 

    
* **schema_id** (string)   `Required` 

    <br>

### ProvidersInfo
* **results** (ProviderInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### Reference
* **resource_type** (string)   `Required` 

    
* **link** (Struct)   `Required` 

    <br>

### UpdateProviderRequest
* **provider** (string)   `Required` 

    
* **name** (string)  

    
* **sync_mode** (SyncMode)  

    
* **sync_options** (SyncOptions)  

    
* **description** (Description)  `Repeated`   

    
* **schema** (ProviderSchema)  `Repeated`   

    
* **capability** (Capability)  

    
* **color** (string)  

    
* **icon** (string)  

    
* **reference** (Reference)  `Repeated`   

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    
* **domain_id** (string)  

    <br>
