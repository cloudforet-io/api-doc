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
| [**create**](./Provider#create) | [CreateProviderRequest](Provider#createproviderrequest) | [ProviderInfo](./Provider#providerinfo) |
| [**update**](./Provider#update) | [UpdateProviderRequest](Provider#updateproviderrequest) | [ProviderInfo](./Provider#providerinfo) |
| [**delete**](./Provider#delete) | [ProviderRequest](Provider#providerrequest) | [Empty](./Provider#empty) |
| [**get**](./Provider#get) | [GetProviderRequest](Provider#getproviderrequest) | [ProviderInfo](./Provider#providerinfo) |
| [**list**](./Provider#list) | [ProviderQuery](Provider#providerquery) | [ProvidersInfo](./Provider#providersinfo) |
| [**stat**](./Provider#stat) | [ProviderStatQuery](Provider#providerstatquery) | [Struct](./Provider#struct) |



    
<br>

### create

> **POST** /identity/v1/provider/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /identity/v1/provider/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /identity/v1/provider/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /identity/v1/provider/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /identity/v1/provider/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /identity/v1/provider/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateProviderRequest
* **provider** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: true*

    
* **template** (Struct)  `Required` 

  *is_required: false*

    
* **metadata** (Struct)  `Required` 

  *is_required: false*

    
* **capability** (Struct)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetProviderRequest
* **provider** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProviderInfo
* **provider** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **template** (Struct)  `Required` 

    
* **metadata** (Struct)  `Required` 

    
* **capability** (Struct)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### ProviderQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProviderRequest
* **provider** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProviderStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProvidersInfo
* **results** (ProviderInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateProviderRequest
* **provider** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **template** (Struct)  `Required` 

  *is_required: false*

    
* **metadata** (Struct)  `Required` 

  *is_required: false*

    
* **capability** (Struct)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
