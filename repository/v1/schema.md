---
description: A Schema is a data structure used in all domains. For example, data forms of Google OAuth2 credentials or AWS access keys can be a Schema resource.
---
# Schema

>  **Package : spaceone.api.repository.v1**

## Schema

{% hint style="info" %}
**Schema Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](schema.md#create)|   [CreateSchemaRequest](schema.md#createschemarequest) |   [SchemaInfo](schema.md#schemainfo) |
| [**update**](schema.md#update)|   [UpdateSchemaRequest](schema.md#updateschemarequest) |   [SchemaInfo](schema.md#schemainfo) |
| [**delete**](schema.md#delete)|   [SchemaRequest](schema.md#schemarequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](schema.md#get)|   [GetRepositorySchemaRequest](schema.md#getrepositoryschemarequest) |   [SchemaInfo](schema.md#schemainfo) |
| [**list**](schema.md#list)|   [SchemaQuery](schema.md#schemaquery) |   [SchemasInfo](schema.md#schemasinfo) |
| [**stat**](schema.md#stat)|   [SchemaStatQuery](schema.md#schemastatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /repository/v1/schema/create
>

> Creates a new Schema. You must specify the parameters: `service_type`, `name`, and `schema`(data structure). With the parameter `domain_id`, you can choose whether you will create a Schema in `Local` or externally. The Schema created includes `repository_info`, information about where the resource is managed.

| Type | Message |
| :--- | :--- |
| Request | [CreateSchemaRequest](schema.md#createschemarequest) |
| Response |  [SchemaInfo](schema.md#schemainfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "slack_webhook",
    "service_type": "secret.credentials",
    "schema": {},
    "labels": [],
    "tags": {
        "description": "Slack Webhook"
    },
    "domain_id": "domain-987654321098"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "name": "slack_webhook",
    "service_type": "secret.credentials",
    "schema": {},
    "labels": [],
    "tags": {
        "description": "Slack Webhook"
    },
    "repository_info": {
        "repository_id": "repo-123456789012",
        "name": "Local",
        "repository_type": "local"
    },
    "domain_id": "domain-987654321098",
    "created_at": "2022-01-01T05:46:49.929Z",
    "updated_at": "2022-01-01T05:46:49.929Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /repository/v1/schema/update
>

> Updates a specific Schema. You can make changes in Schema settings, including `name`, `schema`, `labels`, and `tags`.

| Type | Message |
| :--- | :--- |
| Request | [UpdateSchemaRequest](schema.md#updateschemarequest) |
| Response |  [SchemaInfo](schema.md#schemainfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "slack_webhook_test",
    "schema": {},
    "labels": [],
    "tags": {},
    "domain_id": "domain-987654321098"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "name": "slack_webhook_test",
    "service_type": "secret.credentials",
    "schema": {},
    "labels": [],
    "tags": {
        "description": "Slack Webhook"
    },
    "repository_info": {
        "repository_id": "repo-123456789012",
        "name": "Local",
        "repository_type": "local"
    },
    "domain_id": "domain-987654321098",
    "created_at": "2022-01-01T05:46:49.929Z",
    "updated_at": "2022-01-01T05:46:49.929Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** /repository/v1/schema/delete
>

> Deletes a specific Schema. You must specify the `name` of the Schema to delete, as the `name` is an identifier of Schema resources.

| Type | Message |
| :--- | :--- |
| Request | [SchemaRequest](schema.md#schemarequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "slack_webhook"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /repository/v1/schema/get
>

> Gets a specific Schema. You must specify the `name` of the Schema to get, as the `name` is an identifier of Schema resources. You can use the parameter `repository_id` to limit the scope of the method to a specific Repository.

| Type | Message |
| :--- | :--- |
| Request | [GetRepositorySchemaRequest](schema.md#getrepositoryschemarequest) |
| Response |  [SchemaInfo](schema.md#schemainfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "slack_webhook",
    "repository_id": "repo-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "name": "slack_webhook",
    "service_type": "secret.credentials",
    "schema": {},
    "labels": [],
    "tags": {
        "description": "Slack Webhook"
    },
    "repository_info": {
        "repository_id": "repo-123456789012",
        "name": "Local",
        "repository_type": "local"
    },
    "domain_id": "domain-987654321098",
    "created_at": "2022-01-01T10:20:09.064Z",
    "updated_at": "2022-01-01T10:20:09.064Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /repository/v1/schema/list
>

> Gets a list of all Schemas in a specific Repository. The parameter `repository_id` is used as an identifier of a Repository to get its list of Schemas. You can use a query to get a filtered list of Schemas.

| Type | Message |
| :--- | :--- |
| Request | [SchemaQuery](schema.md#schemaquery) |
| Response |  [SchemasInfo](schema.md#schemasinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "name": "slack_webhook",
    "service_type": "secret.credentials",
    "repository_id": "repo-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "name": "slack_webhook",
            "service_type": "secret.credentials",
            "schema": {},
            "labels": [],
            "tags": {
                "description": "Slack Webhook"
            },
            "repository_info": {
                "repository_id": "repo-123456789012",
                "name": "Local",
                "repository_type": "local"
            },
            "domain_id": "domain-987654321098",
            "created_at": "2022-01-01T10:20:09.064Z",
            "updated_at": "2022-01-01T10:20:09.064Z"
        }
    ],
    "total_count": 1
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /repository/v1/schema/stat
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
| name |string|✔| |
| service_type |string|✔| |
| schema_id |string|✔| |
| schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| project_id |string|✘| |
| domain_id |string|✔| |

### GetRepositorySchemaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| domain_id |string|✔| |
| repository_id |string|✘| |
| only |list of string|✘| |
| schema_id |string|✘| |

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
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">service_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">repository_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schema_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### SchemaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| domain_id |string|✔| |
| schema_id |string|✘| |

### SchemaStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| repository_id |string|✔| |
| domain_id |string|✔| |

### SchemasInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of SchemaInfo](schema.md#schemainfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateSchemaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| schema |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
