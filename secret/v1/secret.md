---
description: A Secret is an external data, encrypted by CluodForet.
---
# Secret

>  **Package : spaceone.api.secret.v1**

## Secret

{% hint style="info" %}
**Secret Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](secret.md#create)|   [CreateSecretRequest](secret.md#createsecretrequest) |   [SecretInfo](secret.md#secretinfo) |
| [**update**](secret.md#update)|   [UpdateSecretRequest](secret.md#updatesecretrequest) |   [SecretInfo](secret.md#secretinfo) |
| [**delete**](secret.md#delete)|   [SecretRequest](secret.md#secretrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**update_data**](secret.md#update_data)|   [UpdateSecretDataRequest](secret.md#updatesecretdatarequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get_data**](secret.md#get_data)|   [SecretRequest](secret.md#secretrequest) |   [SecretDataInfo](secret.md#secretdatainfo) |
| [**get**](secret.md#get)|   [GetSecretRequest](secret.md#getsecretrequest) |   [SecretInfo](secret.md#secretinfo) |
| [**list**](secret.md#list)|   [SecretQuery](secret.md#secretquery) |   [SecretsInfo](secret.md#secretsinfo) |
| [**stat**](secret.md#stat)|   [SecretStatQuery](secret.md#secretstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /secret/v1/secrets
>

> Creates a new Secret. When creating the resource, external `data` is encrypted, and a `secret_id` is issued for data access by other microservices.

| Type | Message |
| :--- | :--- |
| Request | [CreateSecretRequest](secret.md#createsecretrequest) |
| Response |  [SecretInfo](secret.md#secretinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "aws-dev",
    "data": "********",
    "secret_type": "CREDENTIALS",
    "schema": "aws_access_key",
    "service_account_id": "sa-123456789012",
    "project_id": "project-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "secret_id": "secret-123456789012",
    "name": "aws-dev",
    "secret_type": "CREDENTIALS",
    "tags": {},
    "schema": "aws_access_key",
    "provider": "aws",
    "service_account_id": "sa-123456789012",
    "project_id": "project-123456789012",
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T06:10:14.851Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /secret/v1/secret/{secret_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateSecretRequest](secret.md#updatesecretrequest) |
| Response |  [SecretInfo](secret.md#secretinfo)  |
 
 

 
### delete
> **DELETE** /secret/v1/secret/{secret_id}
>

> Deletes a specific Secret. You must specify the `secret_id` of the Secret to delete.

| Type | Message |
| :--- | :--- |
| Request | [SecretRequest](secret.md#secretrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "secret_id": "secret-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update_data
> **PUT** /secret/v1/secret/{secret_id}/data
>

> Updates encrypted data of a specific Secret resource. For example, to change the parameter `data`, external data to encrypt, you can use `update_data` to create new encrypted data based on the changed `data` and store it in the Secret resource.

| Type | Message |
| :--- | :--- |
| Request | [UpdateSecretDataRequest](secret.md#updatesecretdatarequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "secret_id": "secret-123456789012",
    "data": "********",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "data": {
        "encrypted_data": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    },
    "encrypted": true,
    "encrypt_options": {
        "encrypted_data_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "encrypt_algorithm": "CloudForet_DEFAULT"
    }
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get_data
> **GET** /secret/v1/secret/{secret_id}/data
>

> Gets a specific Secret. Prints detailed information about the Secret, including  `name`, `tags`, `schema`, and `provider`.

| Type | Message |
| :--- | :--- |
| Request | [SecretRequest](secret.md#secretrequest) |
| Response |  [SecretDataInfo](secret.md#secretdatainfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "secret_id": "secret-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "data": {
        "encrypted_data": "xxxxxxxxxxxxxxxxxx"
    },
    "encrypted": true,
    "encrypt_options": {
        "encrypt_algorithm": "SPACEONE_DEFAULT",
        "encrypted_data_key": "xxxxxx"
    }
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /secret/v1/secret/{secret_id}
>

> Gets a specific Post. You must specify the `post_id` of the Post to get, and the `board_id` of the Board where the child Post to get belongs. Prints detailed information about the Post.

| Type | Message |
| :--- | :--- |
| Request | [GetSecretRequest](secret.md#getsecretrequest) |
| Response |  [SecretInfo](secret.md#secretinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "secret_id": "secret-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "secret_id": "secret-123456789012",
    "name": "aws-dev",
    "secret_type": "CREDENTIALS",
    "tags": {},
    "schema": "aws_access_key",
    "provider": "aws",
    "service_account_id": "sa-123456789012",
    "project_id": "project-123456789012",
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T06:10:14.851Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /secret/v1/secrets
>
> **POST** /secret/v1/secrets/search


> Gets a list of all Posts. You can use a query to get a filtered list of Posts.

| Type | Message |
| :--- | :--- |
| Request | [SecretQuery](secret.md#secretquery) |
| Response |  [SecretsInfo](secret.md#secretsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "secret_id": "secret-123456789012",
            "name": "aws-dev",
            "secret_type": "CREDENTIALS",
            "tags": {},
            "schema": "aws_access_key",
            "provider": "aws",
            "service_account_id": "sa-123456789012",
            "project_id": "project-123456789012",
            "domain_id": "domain-123456789012",
            "created_at": "2022-01-01T06:10:14.851Z"
        },
        {
            "secret_id": "secret-987654321098",
            "name": "plugin-credentials",
            "secret_type": "CREDENTIALS",
            "tags": {},
            "domain_id": "domain-123456789012",
            "created_at": "2022-01-01T02:31:01.709Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /secret/v1/secrets/stat
>


| Type | Message |
| :--- | :--- |
| Request | [SecretStatQuery](secret.md#secretstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateSecretRequest
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
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>CREDENTIALS</li>
        </ul></td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">service_account_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### GetSecretRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### SecretDataInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| encrypted |bool | |
| encrypt_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### SecretInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>CREDENTIALS</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_groups</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">service_account_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### SecretQuery
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
      <td style="text-align:left; width:100px;">secret_id</td>
      <td style="text-align:left">string</td>
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
      <td style="text-align:left; width:100px;">secret_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>CREDENTIALS</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_group_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">service_account_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">include_secret_group</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### SecretRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_id |string|✔| |
| domain_id |string|✔| |

### SecretStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### SecretsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of SecretInfo](secret.md#secretinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateSecretDataRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_id |string|✔| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| domain_id |string|✔| |
| schema |string|✘| |

### UpdateSecretRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_id |string|✔| |
| name |string|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| project_id |string|✘| |
| domain_id |string|✔| |
| release_project |bool|✘| |
