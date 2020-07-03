---
description: null
---

# Schema

> **Package : spaceone.api.repository.v1**

## Schema

{% hint style="info" %}
**Schema Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](schema.md#create) | [CreateSchemaRequest](schema.md#createschemarequest) | [SchemaInfo](schema.md#schemainfo) |  |
| 2 | [update](schema.md#update) | [UpdateSchemaRequest](schema.md#updateschemarequest) | [SchemaInfo](schema.md#schemainfo) |  |
| 3 | [delete](schema.md#delete) | [SchemaRequest](schema.md#schemarequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 4 | [get](schema.md#get) | [GetRepositorySchemaRequest](schema.md#getrepositoryschemarequest) | [SchemaInfo](schema.md#schemainfo) |  |
| 5 | [list](schema.md#list) | [SchemaQuery](schema.md#schemaquery) | [SchemasInfo](schema.md#schemasinfo) |  |
| 6 | [stat](schema.md#stat) | [SchemaStatQuery](schema.md#schemastatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |

### create

> **POST** /repository/v1/schemas

| Type | Message |
| :--- | :--- |
| Request | [CreateSchemaRequest](schema.md#createschemarequest) |
| Response | [SchemaInfo](schema.md#schemainfo) |

### update

> **PUT** /repository/v1/schema/{schema}

| Type | Message |
| :--- | :--- |
| Request | [UpdateSchemaRequest](schema.md#updateschemarequest) |
| Response | [SchemaInfo](schema.md#schemainfo) |

### delete

> **DELETE** /repository/v1/schema/{schema}

| Type | Message |
| :--- | :--- |
| Request | [SchemaRequest](schema.md#schemarequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### get

> **GET** /repository/v1/schemas/{schema}

| Type | Message |
| :--- | :--- |
| Request | [GetRepositorySchemaRequest](schema.md#getrepositoryschemarequest) |
| Response | [SchemaInfo](schema.md#schemainfo) |

### list

> **GET** /repository/v1/schemas
>
> **POST** /repository/v1/schemas/search

| Type | Message |
| :--- | :--- |
| Request | [SchemaQuery](schema.md#schemaquery) |
| Response | [SchemasInfo](schema.md#schemasinfo) |

### stat

> **POST** /repository/v1/schemas/stat

| Type | Message |
| :--- | :--- |
| Request | [SchemaStatQuery](schema.md#schemastatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

## Message

### CreateSchemaRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  | required |
| 2 | service\_type | string |  | required |
| 3 | schema | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | required |
| 4 | labels | string |  | optional |
| 5 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 6 | project\_id | string |  | optional |
| 7 | domain\_id | string |  | required |

### GetRepositorySchemaRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  | required |
| 2 | domain\_id | string |  | required |
| 3 | repository\_id | string |  | optional |
| 4 | only | string |  | optional |

### SchemaInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  |  |
| 2 | service\_type | string |  |  |
| 3 | schema | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 4 | labels | string |  |  |
| 5 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 6 | repository\_info | [RepositoryInfo](schema.md#repositoryinfo) |  |  |
| 7 | project\_id | string |  |  |
| 8 | domain\_id | string |  |  |
| 9 | created\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |

### SchemaQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |  | optional |
| 2 | name | string |  | optional |
| 3 | service\_type | string |  | optional |
| 4 | project\_id | string |  | required |
| 5 | repository\_id | string |  | required |
| 6 | domain\_id | string |  | required |

### SchemaRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  | required |
| 2 | domain\_id | string |  | required |

### SchemaStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |  | required |
| 2 | repository\_id | string |  | required |
| 3 | domain\_id | string |  | required |

### SchemasInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [SchemaInfo](schema.md#schemainfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### UpdateSchemaRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  | required |
| 2 | schema | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 3 | labels | string |  | optional |
| 4 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 5 | domain\_id | string |  | required |

