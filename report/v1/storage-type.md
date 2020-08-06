---
description:  
---
# Storage type

>  **Package : spaceone.api.report.v1**

## StorageType

{% hint style="info" %}
**StorageType Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**get**](storage-type.md#get)|   [GetStorageTypeRequest](storage-type.md#getstoragetyperequest) |   [StorageTypeInfo](storage-type.md#storagetypeinfo) |  |
| 2 | [**list**](storage-type.md#list)|   [StorageTypeQuery](storage-type.md#storagetypequery) |   [StorageTypesInfo](storage-type.md#storagetypesinfo) |  | 
 

 
### get
> **POST** /report/v1/storage_type/{storage_type_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetStorageTypeRequest](storage-type.md#getstoragetyperequest) |
| Response |  [StorageTypeInfo](storage-type.md#storagetypeinfo)  |
 
 

 
### list
> **GET** /report/v1/storage_types
>
> **POST** /report/v1/storage_types/search



| Type | Message |
| :--- | :--- |
| Request | [StorageTypeQuery](storage-type.md#storagetypequery) |
| Response |  [StorageTypesInfo](storage-type.md#storagetypesinfo)  |


## 

## Message

### GetStorageTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | storage_type_id |string|✅| |
| 3 | only |string|❌| |

### StorageTypeInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | storage_type_id |string| |
| 2 | name |string| |
| 3 | storage_type |string| |
| 4 | provider |string| |
| 5 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| |

### StorageTypeQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 3 | storage_type_id |string|❌| |
| 4 | name |string|❌| |
| 5 | storage_type |string|❌| |

### StorageTypesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[StorageTypeInfo](storage-type.md#storagetypeinfo)| |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)| |
