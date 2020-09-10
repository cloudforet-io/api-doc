---
description:  
---
# Storage

>  **Package : spaceone.api.report.v1**

## Storage

{% hint style="info" %}
**Storage Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**get**](storage.md#get)|   [GetStorageRequest](storage.md#getstoragerequest) |   [StorageInfo](storage.md#storageinfo) |  |
| 2 | [**list**](storage.md#list)|   [StorageQuery](storage.md#storagequery) |   [StoragesInfo](storage.md#storagesinfo) |  |
| 3 | [**register**](storage.md#register)|   [RegisterStorageRequest](storage.md#registerstoragerequest) |   [StorageInfo](storage.md#storageinfo) |  |
| 4 | [**deregister**](storage.md#deregister)|   [DeregisterStorageRequest](storage.md#deregisterstoragerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**update**](storage.md#update)|   [UpdateStorageRequest](storage.md#updatestoragerequest) |   [StorageInfo](storage.md#storageinfo) |  | 
 

 
### get
> **GET** /report/v1/storage/{storage_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetStorageRequest](storage.md#getstoragerequest) |
| Response |  [StorageInfo](storage.md#storageinfo)  |
 
 

 
### list
> **GET** /report/v1/storages
>
> **POST** /report/v1/storages/search



| Type | Message |
| :--- | :--- |
| Request | [StorageQuery](storage.md#storagequery) |
| Response |  [StoragesInfo](storage.md#storagesinfo)  |
 
 

 
### register
> **POST** /report/v1/storage
>


| Type | Message |
| :--- | :--- |
| Request | [RegisterStorageRequest](storage.md#registerstoragerequest) |
| Response |  [StorageInfo](storage.md#storageinfo)  |
 
 

 
### deregister
> **DELETE** /report/v1/storage/{storage_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DeregisterStorageRequest](storage.md#deregisterstoragerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### update
> **PUT** /report/v1/storage/{storage_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateStorageRequest](storage.md#updatestoragerequest) |
| Response |  [StorageInfo](storage.md#storageinfo)  |


## 

## Message

### DeregisterStorageRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | storage_id |string|✅| |

### GetStorageRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | storage_id |string|✅| |
| 3 | only |list of string|❌| |

### RegisterStorageRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | name |string|✅| |
| 3 | secret_id |string|✅| |
| 4 | storage_type_id |string|✅| |
| 5 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### StorageInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | domain_id |string | |
| 2 | storage_id |string | |
| 3 | name |string | |
| 4 | secret_id |string | |
| 5 | storage_type_info |[StorageTypeInfo](storage.md#storagetypeinfo) | |
| 6 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 7 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |

### StorageQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 3 | storage_id |string|❌| |
| 4 | storage_type_id |string|❌| |
| 5 | secret_id |string|❌| |
| 6 | name |string|❌| |

### StoragesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[StorageInfo](storage.md#storageinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateStorageRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | storage_id |string|✅| |
| 3 | secret_id |string|❌| |
| 4 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | name |string|❌| |
