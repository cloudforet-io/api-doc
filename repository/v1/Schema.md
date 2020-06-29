---
description:  
---
# Schema

>  **Package : spaceone.api.repository.v1**

## Schema

{% hint style="info" %}
**Schema Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Schema.md#create)| [CreateSchemaRequest](Schema.md#createschemarequest) | [SchemaInfo](Schema.md#schemainfo) |  |
| 2 | [update](Schema.md#update)| [UpdateSchemaRequest](Schema.md#updateschemarequest) | [SchemaInfo](Schema.md#schemainfo) |  |
| 3 | [delete](Schema.md#delete)| [SchemaRequest](Schema.md#schemarequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Schema.md#get)| [GetRepositorySchemaRequest](Schema.md#getrepositoryschemarequest) | [SchemaInfo](Schema.md#schemainfo) |  |
| 5 | [list](Schema.md#list)| [SchemaQuery](Schema.md#schemaquery) | [SchemasInfo](Schema.md#schemasinfo) |  |
| 6 | [stat](Schema.md#stat)| [SchemaStatQuery](Schema.md#schemastatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /repository/v1/schemas
>



| Type | Message |
| :--- | :--- |
| Request | [CreateSchemaRequest](Schema.md#createschemarequest) |
| Response |  [SchemaInfo](Schema.md#schemainfo)  |



### update
> **PUT** /repository/v1/schema/{schema}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateSchemaRequest](Schema.md#updateschemarequest) |
| Response |  [SchemaInfo](Schema.md#schemainfo)  |



### delete
> **DELETE** /repository/v1/schema/{schema}
>



| Type | Message |
| :--- | :--- |
| Request | [SchemaRequest](Schema.md#schemarequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /repository/v1/schemas/{schema}
>



| Type | Message |
| :--- | :--- |
| Request | [GetRepositorySchemaRequest](Schema.md#getrepositoryschemarequest) |
| Response |  [SchemaInfo](Schema.md#schemainfo)  |



### list
> **GET** /repository/v1/schemas
>
> **POST** /repository/v1/schemas/search




| Type | Message |
| :--- | :--- |
| Request | [SchemaQuery](Schema.md#schemaquery) |
| Response |  [SchemasInfo](Schema.md#schemasinfo)  |



### stat
> **POST** /repository/v1/schemas/stat
>



| Type | Message |
| :--- | :--- |
| Request | [SchemaStatQuery](Schema.md#schemastatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreateSchemaRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | service_type |string |✅ ||
| 3 | schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |✅ ||
| 4 | labels |string |❌ ||
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 6 | project_id |string |❌ ||
| 7 | domain_id |string |✅ ||

### GetRepositorySchemaRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | repository_id |string |❌ ||
| 4 | only |string |❌ ||

### SchemaInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string | ||
| 2 | service_type |string | ||
| 3 | schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 4 | labels |string | ||
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 6 | repository_info |[RepositoryInfo](Schema.md#repositoryinfo) | ||
| 7 | project_id |string | ||
| 8 | domain_id |string | ||
| 9 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### SchemaQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | name |string |❌ ||
| 3 | service_type |string |❌ ||
| 4 | project_id |string |✅ ||
| 5 | repository_id |string |✅ ||
| 6 | domain_id |string |✅ ||

### SchemaRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | domain_id |string |✅ ||

### SchemaStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | repository_id |string |✅ ||
| 3 | domain_id |string |✅ ||

### SchemasInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[SchemaInfo](Schema.md#schemainfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### UpdateSchemaRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 3 | labels |string |❌ ||
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | domain_id |string |✅ ||
