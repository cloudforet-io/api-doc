---
title: "Storage"
linkTitle: "Storage"
weight: 3
bookFlatSection: true
---
# [Storage](#Storage)



>  **Package : spaceone.api.statistics.v1**

<br>
<br>

## Storage





**Storage Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](./Storage#register) | [RegisterStorageRequest](Storage#registerstoragerequest) | [StorageInfo](./Storage#storageinfo) |
| [**update**](./Storage#update) | [UpdateStorageRequest](Storage#updatestoragerequest) | [StorageInfo](./Storage#storageinfo) |
| [**update_plugin**](./Storage#update_plugin) | [UpdateStoragePluginRequest](Storage#updatestoragepluginrequest) | [StorageInfo](./Storage#storageinfo) |
| [**verify_plugin**](./Storage#verify_plugin) | [StorageRequest](Storage#storagerequest) | [Empty](./Storage#empty) |
| [**enable**](./Storage#enable) | [StorageRequest](Storage#storagerequest) | [StorageInfo](./Storage#storageinfo) |
| [**disable**](./Storage#disable) | [StorageRequest](Storage#storagerequest) | [StorageInfo](./Storage#storageinfo) |
| [**deregister**](./Storage#deregister) | [StorageRequest](Storage#storagerequest) | [Empty](./Storage#empty) |
| [**get**](./Storage#get) | [GetStorageRequest](Storage#getstoragerequest) | [StorageInfo](./Storage#storageinfo) |
| [**list**](./Storage#list) | [StorageQuery](Storage#storagequery) | [StoragesInfo](./Storage#storagesinfo) |
| [**stat**](./Storage#stat) | [StorageStatQuery](Storage#storagestatquery) | [Struct](./Storage#struct) |



    
<br>

### register





> **POST** /statistics/v1/storage/register
>






    
<br>

### update





> **POST** /statistics/v1/storage/update
>






    
<br>

### update_plugin





> **POST** /statistics/v1/storage/update-plugin
>






    
<br>

### verify_plugin





> **POST** /statistics/v1/storage/verify-plugin
>






    
<br>

### enable





> **POST** /statistics/v1/storage/enable
>






    
<br>

### disable





> **POST** /statistics/v1/storage/disable
>






    
<br>

### deregister





> **POST** /statistics/v1/storage/deregister
>






    
<br>

### get





> **POST** /statistics/v1/storage/get
>






    
<br>

### list





> **POST** /statistics/v1/storage/list
>






    
<br>

### stat





> **POST** /statistics/v1/storage/stat
>






    


<br>
<br>

## Message



### GetStorageRequest
* **storage_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### PluginInfo
* **plugin_id** (string)  `Required` 

    
* **version** (string)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **secret_id** (string)  `Required` 

    
* **metadata** (Struct)  `Required` 

    <br>

### PluginRequest
* **plugin_id** (string)  `Required` 

    
* **version** (string)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **secret_data** (Struct)  `Required` 

    
* **schema** (string)  `Required` 

    <br>

### RegisterStorageRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **plugin_info** (PluginRequest)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### StorageInfo
* **storage_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **capability** (Struct)  `Required` 

    
* **plugin_info** (PluginInfo)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **user_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### StorageQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **storage_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **state** (string)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### StorageRequest
* **storage_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### StorageStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### StoragesInfo
* **results** (StorageInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateStoragePluginRequest
* **storage_id** (string)  `Required` 

  *is_required: true*

    
* **version** (string)  `Required` 

  *is_required: false*

    
* **options** (Struct)  `Required` 

  *is_required: false*

    
* **secret_data** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateStorageRequest
* **storage_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
