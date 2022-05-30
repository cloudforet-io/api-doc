---
description:  
---
# Schema

>  **Package : spaceone.api.repository.v1**

## Schema

{% hint style="info" %}
**Schema Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](schema.md#create)|   [CreateSchemaRequest](schema.md#createschemarequest) |   [SchemaInfo](schema.md#schemainfo) |  |
| [**update**](schema.md#update)|   [UpdateSchemaRequest](schema.md#updateschemarequest) |   [SchemaInfo](schema.md#schemainfo) |  |
| [**delete**](schema.md#delete)|   [SchemaRequest](schema.md#schemarequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](schema.md#get)|   [GetRepositorySchemaRequest](schema.md#getrepositoryschemarequest) |   [SchemaInfo](schema.md#schemainfo) |  |
| [**list**](schema.md#list)|   [SchemaQuery](schema.md#schemaquery) |   [SchemasInfo](schema.md#schemasinfo) |  |
| [**stat**](schema.md#stat)|   [SchemaStatQuery](schema.md#schemastatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](schema.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateSchemaRequest](schema.md#createschemarequest)  </div> | <div style="width:200px; text-align:center;">   [SchemaInfo](schema.md#schemainfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](schema.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateSchemaRequest](schema.md#updateschemarequest)  </div> | <div style="width:200px; text-align:center;">   [SchemaInfo](schema.md#schemainfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](schema.md#delete) </div> | <div style="width:200px; text-align:center;">    [SchemaRequest](schema.md#schemarequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](schema.md#get) </div> | <div style="width:200px; text-align:center;">    [GetRepositorySchemaRequest](schema.md#getrepositoryschemarequest)  </div> | <div style="width:200px; text-align:center;">   [SchemaInfo](schema.md#schemainfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](schema.md#list) </div> | <div style="width:200px; text-align:center;">    [SchemaQuery](schema.md#schemaquery)  </div> | <div style="width:200px; text-align:center;">   [SchemasInfo](schema.md#schemasinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](schema.md#stat) </div> | <div style="width:200px; text-align:center;">    [SchemaStatQuery](schema.md#schemastatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
### create
> **POST** /repository/v1/schemas
>


| Type | Message |
| :--- | :--- |
| Request | [CreateSchemaRequest](schema.md#createschemarequest) |
| Response |  [SchemaInfo](schema.md#schemainfo)  |
 
 

 
### update
> **PUT** /repository/v1/schema/{schema}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateSchemaRequest](schema.md#updateschemarequest) |
| Response |  [SchemaInfo](schema.md#schemainfo)  |
 
 

 
### delete
> **DELETE** /repository/v1/schema/{schema}
>


| Type | Message |
| :--- | :--- |
| Request | [SchemaRequest](schema.md#schemarequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /repository/v1/schemas/{schema}
>


| Type | Message |
| :--- | :--- |
| Request | [GetRepositorySchemaRequest](schema.md#getrepositoryschemarequest) |
| Response |  [SchemaInfo](schema.md#schemainfo)  |
 
 

 
### list
> **GET** /repository/v1/schemas
>
> **POST** /repository/v1/schemas/search



| Type | Message |
| :--- | :--- |
| Request | [SchemaQuery](schema.md#schemaquery) |
| Response |  [SchemasInfo](schema.md#schemasinfo)  |
 
 

 
### stat
> **POST** /repository/v1/schemas/stat
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
| name |string|✅| |
| service_type |string|✅| |
| schema_id |string|✅| |
| schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| project_id |string|❌| |
| domain_id |string|✅| |

### GetRepositorySchemaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| domain_id |string|✅| |
| repository_id |string|❌| |
| only |list of string|❌| |
| schema_id |string|❌| |

### SchemaInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| name |string | |
| service_type |string | |
| schema_id |string | |
| schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| repository_info |[RepositoryInfo](schema.md#repositoryinfo) | |
| project_id |string | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |

### SchemaQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">service_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">repository_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">schema_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### SchemaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| domain_id |string|✅| |
| schema_id |string|❌| |

### SchemaStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| repository_id |string|✅| |
| domain_id |string|✅| |

### SchemasInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of SchemaInfo](schema.md#schemainfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateSchemaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
