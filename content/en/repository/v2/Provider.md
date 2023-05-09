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
| [**create**](./Provider#create) | [CreateProviderRequest](Provider#createproviderrequest) | [ProviderInfo](./Provider#providerinfo) |
| [**update**](./Provider#update) | [UpdateProviderRequest](Provider#updateproviderrequest) | [ProviderInfo](./Provider#providerinfo) |
| [**sync**](./Provider#sync) | [ProviderRequest](Provider#providerrequest) | [ProviderInfo](./Provider#providerinfo) |
| [**delete**](./Provider#delete) | [ProviderRequest](Provider#providerrequest) | [Empty](./Provider#empty) |
| [**get**](./Provider#get) | [GetProviderRequest](Provider#getproviderrequest) | [ProviderInfo](./Provider#providerinfo) |
| [**list**](./Provider#list) | [ProviderQuery](Provider#providerquery) | [ProvidersInfo](./Provider#providersinfo) |



    
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
* **trusted_service_account** (string)  `Required` 

    <br>

### CreateProviderRequest
* **provider** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: true*

    
* **sync_mode** (SyncMode)  `Required` 

  *is_required: false*

    
* **sync_options** (SyncOptions)  `Required` 

  *is_required: false*

    
* **description** (Description)  `Required` 

  *is_required: false*

    
* **schema** (ProviderSchema)  `Required` 

  *is_required: false*

    
* **capability** (Capability)  `Required` 

  *is_required: false*

    
* **color** (string)  `Required` 

  *is_required: false*

    
* **icon** (string)  `Required` 

  *is_required: false*

    
* **reference** (Reference)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### Description
* **resource_type** (string)  `Required` 

    
* **body** (Struct)  `Required` 

    <br>

### GetProviderRequest
* **provider** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### ProviderInfo
* **provider** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **sync_mode** (SyncMode)  `Required` 

    
* **sync_options** (SyncOptions)  `Required` 

    
* **description** (Description)  `Required` 

    
* **schema** (ProviderSchema)  `Required` 

    
* **capability** (Capability)  `Required` 

    
* **color** (string)  `Required` 

    
* **icon** (string)  `Required` 

    
* **reference** (Reference)  `Required` 

    
* **labels** (ListValue)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **remote_repository** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### ProviderQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **sync_mode** (SyncMode)  `Required` 

  *is_required: false*

    
* **remote_repository_name** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### ProviderRequest
* **provider** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### ProviderSchema
* **resource_type** (string)  `Required` 

    
* **secret_type** (string)  `Required` 

    
* **schema_id** (string)  `Required` 

    <br>

### ProvidersInfo
* **results** (ProviderInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### Reference
* **resource_type** (string)  `Required` 

    
* **link** (Struct)  `Required` 

    <br>

### UpdateProviderRequest
* **provider** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **sync_mode** (SyncMode)  `Required` 

  *is_required: false*

    
* **sync_options** (SyncOptions)  `Required` 

  *is_required: false*

    
* **description** (Description)  `Required` 

  *is_required: false*

    
* **schema** (ProviderSchema)  `Required` 

  *is_required: false*

    
* **capability** (Capability)  `Required` 

  *is_required: false*

    
* **color** (string)  `Required` 

  *is_required: false*

    
* **icon** (string)  `Required` 

  *is_required: false*

    
* **reference** (Reference)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>
