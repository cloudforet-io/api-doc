---
description:  
---
# Secret

>  **Package : spaceone.api.secret.v1**

## Secret

{% hint style="info" %}
**Secret Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](secret.md#create)|   [CreateSecretRequest](secret.md#createsecretrequest) |   [SecretInfo](secret.md#secretinfo) |  |
| [**update**](secret.md#update)|   [UpdateSecretRequest](secret.md#updatesecretrequest) |   [SecretInfo](secret.md#secretinfo) |  |
| [**delete**](secret.md#delete)|   [SecretRequest](secret.md#secretrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**update_data**](secret.md#update_data)|   [UpdateSecretDataRequest](secret.md#updatesecretdatarequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get_data**](secret.md#get_data)|   [SecretRequest](secret.md#secretrequest) |   [SecretDataInfo](secret.md#secretdatainfo) |  |
| [**get**](secret.md#get)|   [GetSecretRequest](secret.md#getsecretrequest) |   [SecretInfo](secret.md#secretinfo) |  |
| [**list**](secret.md#list)|   [SecretQuery](secret.md#secretquery) |   [SecretsInfo](secret.md#secretsinfo) |  |
| [**stat**](secret.md#stat)|   [SecretStatQuery](secret.md#secretstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](secret.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateSecretRequest](secret.md#createsecretrequest)  </div> | <div style="width:200px; text-align:center;">   [SecretInfo](secret.md#secretinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](secret.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateSecretRequest](secret.md#updatesecretrequest)  </div> | <div style="width:200px; text-align:center;">   [SecretInfo](secret.md#secretinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](secret.md#delete) </div> | <div style="width:200px; text-align:center;">    [SecretRequest](secret.md#secretrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update_data**](secret.md#update_data) </div> | <div style="width:200px; text-align:center;">    [UpdateSecretDataRequest](secret.md#updatesecretdatarequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get_data**](secret.md#get_data) </div> | <div style="width:200px; text-align:center;">    [SecretRequest](secret.md#secretrequest)  </div> | <div style="width:200px; text-align:center;">   [SecretDataInfo](secret.md#secretdatainfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](secret.md#get) </div> | <div style="width:200px; text-align:center;">    [GetSecretRequest](secret.md#getsecretrequest)  </div> | <div style="width:200px; text-align:center;">   [SecretInfo](secret.md#secretinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](secret.md#list) </div> | <div style="width:200px; text-align:center;">    [SecretQuery](secret.md#secretquery)  </div> | <div style="width:200px; text-align:center;">   [SecretsInfo](secret.md#secretsinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](secret.md#stat) </div> | <div style="width:200px; text-align:center;">    [SecretStatQuery](secret.md#secretstatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
### create
> **POST** /secret/v1/secrets
>


| Type | Message |
| :--- | :--- |
| Request | [CreateSecretRequest](secret.md#createsecretrequest) |
| Response |  [SecretInfo](secret.md#secretinfo)  |
 
 

 
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


| Type | Message |
| :--- | :--- |
| Request | [SecretRequest](secret.md#secretrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### update_data
> **PUT** /secret/v1/secret/{secret_id}/data
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateSecretDataRequest](secret.md#updatesecretdatarequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get_data
> **GET** /secret/v1/secret/{secret_id}/data
>


| Type | Message |
| :--- | :--- |
| Request | [SecretRequest](secret.md#secretrequest) |
| Response |  [SecretDataInfo](secret.md#secretdatainfo)  |
 
 

 
### get
> **GET** /secret/v1/secret/{secret_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetSecretRequest](secret.md#getsecretrequest) |
| Response |  [SecretInfo](secret.md#secretinfo)  |
 
 

 
### list
> **GET** /secret/v1/secrets
>
> **POST** /secret/v1/secrets/search



| Type | Message |
| :--- | :--- |
| Request | [SecretQuery](secret.md#secretquery) |
| Response |  [SecretsInfo](secret.md#secretsinfo)  |
 
 

 
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
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">secret_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>CREDENTIALS</li>
        </ul></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">service_account_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### GetSecretRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

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
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">secret_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>CREDENTIALS</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">secret_groups</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">service_account_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### SecretQuery
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
      <td style="text-align:left">secret_id</td>
      <td style="text-align:left">string</td>
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
      <td style="text-align:left">secret_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>CREDENTIALS</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">secret_group_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">service_account_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">include_secret_group</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### SecretRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_id |string|✅| |
| domain_id |string|✅| |

### SecretStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### SecretsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of SecretInfo](secret.md#secretinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateSecretDataRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_id |string|✅| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| domain_id |string|✅| |
| schema |string|❌| |

### UpdateSecretRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_id |string|✅| |
| name |string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| project_id |string|❌| |
| domain_id |string|✅| |
| release_project |bool|❌| |
