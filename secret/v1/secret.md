---
description:  
---
# Secret

>  **Package : spaceone.api.secret.v1**

## Secret

{% hint style="info" %}
**Secret Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](secret.md#create)|   [CreateSecretRequest](secret.md#createsecretrequest) |   [SecretInfo](secret.md#secretinfo) |  |
| 2 | [**update**](secret.md#update)|   [UpdateSecretRequest](secret.md#updatesecretrequest) |   [SecretInfo](secret.md#secretinfo) |  |
| 3 | [**delete**](secret.md#delete)|   [SecretRequest](secret.md#secretrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**update_data**](secret.md#update_data)|   [UpdateSecretDataRequest](secret.md#updatesecretdatarequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**get_data**](secret.md#get_data)|   [SecretRequest](secret.md#secretrequest) |   [SecretDataInfo](secret.md#secretdatainfo) |  |
| 6 | [**get**](secret.md#get)|   [GetSecretRequest](secret.md#getsecretrequest) |   [SecretInfo](secret.md#secretinfo) |  |
| 7 | [**list**](secret.md#list)|   [SecretQuery](secret.md#secretquery) |   [SecretsInfo](secret.md#secretsinfo) |  |
| 8 | [**stat**](secret.md#stat)|   [SecretStatQuery](secret.md#secretstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">secret_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>CREDENTIALS</li>
        </ul></td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">list of spaceone.api.core.v1.Tag</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">service_account_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### GetSecretRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### SecretDataInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 2 | encrypted |bool | |
| 3 | encrypted_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### SecretInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">secret_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>CREDENTIALS</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">secret_groups</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">list of spaceone.api.core.v1.Tag</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">service_account_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### SecretQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">secret_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>CREDENTIALS</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">secret_group_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">service_account_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">include_secret_group</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### SecretRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret_id |string|✅| |
| 2 | domain_id |string|✅| |

### SecretStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### SecretsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of SecretInfo](secret.md#secretinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateSecretDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret_id |string|✅| |
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 3 | domain_id |string|✅| |

### UpdateSecretRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret_id |string|✅| |
| 2 | name |string|❌| |
| 3 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 4 | project_id |string|❌| |
| 5 | domain_id |string|✅| |
| 6 | release_project |bool|❌| |
