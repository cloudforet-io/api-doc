---
description:  
---
# Schema

>  **Package : spaceone.api.repository.v2**

## Schema

{% hint style="info" %}
**Schema Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](schema.md#create)|   [CreateSchemaRequest](schema.md#createschemarequest) |   [SchemaInfo](schema.md#schemainfo) |
| [**update**](schema.md#update)|   [UpdateSchemaRequest](schema.md#updateschemarequest) |   [SchemaInfo](schema.md#schemainfo) |
| [**sync**](schema.md#sync)|   [SchemaRequest](schema.md#schemarequest) |   [SchemaInfo](schema.md#schemainfo) |
| [**delete**](schema.md#delete)|   [SchemaRequest](schema.md#schemarequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](schema.md#get)|   [GetSchemaRequest](schema.md#getschemarequest) |   [SchemaInfo](schema.md#schemainfo) |
| [**list**](schema.md#list)|   [SchemaQuery](schema.md#schemaquery) |   [SchemasInfo](schema.md#schemasinfo) |
| [**stat**](schema.md#stat)|   [SchemaStatQuery](schema.md#schemastatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /repository/v2/schema/create
>


| Type | Message |
| :--- | :--- |
| Request | [CreateSchemaRequest](schema.md#createschemarequest) |
| Response |  [SchemaInfo](schema.md#schemainfo)  |
 
 

 
### update
> **POST** /repository/v2/schema/update
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateSchemaRequest](schema.md#updateschemarequest) |
| Response |  [SchemaInfo](schema.md#schemainfo)  |
 
 

 
### sync
> **POST** /repository/v2/schema/sync
>


| Type | Message |
| :--- | :--- |
| Request | [SchemaRequest](schema.md#schemarequest) |
| Response |  [SchemaInfo](schema.md#schemainfo)  |
 
 

 
### delete
> **POST** /repository/v2/schema/delete
>


| Type | Message |
| :--- | :--- |
| Request | [SchemaRequest](schema.md#schemarequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **POST** /repository/v2/schema/get
>


| Type | Message |
| :--- | :--- |
| Request | [GetSchemaRequest](schema.md#getschemarequest) |
| Response |  [SchemaInfo](schema.md#schemainfo)  |
 
 

 
### list
> **POST** /repository/v2/schema/list
>


| Type | Message |
| :--- | :--- |
| Request | [SchemaQuery](schema.md#schemaquery) |
| Response |  [SchemasInfo](schema.md#schemasinfo)  |
 
 

 
### stat
> **POST** /repository/v2/schema/stat
>


| Type | Message |
| :--- | :--- |
| Request | [SchemaStatQuery](schema.md#schemastatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateSchemaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schema_id |string|✔| |
| name |string|✔| |
| sync_mode |[SyncMode](schema.md#syncmode)|✘| |
| sync_options |[SyncOptions](schema.md#syncoptions)|✘| |
| schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### GetSchemaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schema_id |string|✔| |
| only |list of string|✘| |
| domain_id |string|✔| |

### SchemaInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| schema_id |string | |
| name |string | |
| sync_mode |[SyncMode](schema.md#syncmode) | |
| sync_options |[SyncOptions](schema.md#syncoptions) | |
| schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| remote_repository |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| created_at |string | |

### SchemaQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| schema_id |string|✘| |
| name |string|✘| |
| sync_mode |[SyncMode](schema.md#syncmode)|✘| |
| remote_repository_name |string|✘| |
| domain_id |string|✔| |

### SchemaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schema_id |string|✔| |
| domain_id |string|✔| |

### SchemaStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### SchemasInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of SchemaInfo](schema.md#schemainfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateSchemaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schema_id |string|✔| |
| name |string|✘| |
| sync_mode |[SyncMode](schema.md#syncmode)|✘| |
| sync_options |[SyncOptions](schema.md#syncoptions)|✘| |
| schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
