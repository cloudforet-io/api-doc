---
description:  
---
# Api key

>  **Package : spaceone.api.identity.v1**

## APIKey

{% hint style="info" %}
**APIKey Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](api-key.md#create)|   [CreateAPIKeyRequest](api-key.md#createapikeyrequest) |   [APIKeyInfo](api-key.md#apikeyinfo) |  |
| 2 | [**enable**](api-key.md#enable)|   [APIKeyRequest](api-key.md#apikeyrequest) |   [APIKeyInfo](api-key.md#apikeyinfo) |  |
| 3 | [**disable**](api-key.md#disable)|   [APIKeyRequest](api-key.md#apikeyrequest) |   [APIKeyInfo](api-key.md#apikeyinfo) |  |
| 4 | [**delete**](api-key.md#delete)|   [APIKeyRequest](api-key.md#apikeyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**get**](api-key.md#get)|   [GetAPIKeyRequest](api-key.md#getapikeyrequest) |   [APIKeyInfo](api-key.md#apikeyinfo) |  |
| 6 | [**list**](api-key.md#list)|   [APIKeyQuery](api-key.md#apikeyquery) |   [APIKeysInfo](api-key.md#apikeysinfo) |  |
| 7 | [**stat**](api-key.md#stat)|   [APIKeyStatQuery](api-key.md#apikeystatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /identity/v1/api-keys
>


| Type | Message |
| :--- | :--- |
| Request | [CreateAPIKeyRequest](api-key.md#createapikeyrequest) |
| Response |  [APIKeyInfo](api-key.md#apikeyinfo)  |
 
 

 
### enable
> **PUT** /identity/v1/api-key/{api_key_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [APIKeyRequest](api-key.md#apikeyrequest) |
| Response |  [APIKeyInfo](api-key.md#apikeyinfo)  |
 
 

 
### disable
> **PUT** /identity/v1/api-key/{api_key_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [APIKeyRequest](api-key.md#apikeyrequest) |
| Response |  [APIKeyInfo](api-key.md#apikeyinfo)  |
 
 

 
### delete
> **DELETE** /identity/v1/api-key/{api_key_id}
>


| Type | Message |
| :--- | :--- |
| Request | [APIKeyRequest](api-key.md#apikeyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /identity/v1/api-key/{api_key_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetAPIKeyRequest](api-key.md#getapikeyrequest) |
| Response |  [APIKeyInfo](api-key.md#apikeyinfo)  |
 
 

 
### list
> **GET** /identity/v1/api-keys
>
> **POST** /identity/v1/api-keys/search



| Type | Message |
| :--- | :--- |
| Request | [APIKeyQuery](api-key.md#apikeyquery) |
| Response |  [APIKeysInfo](api-key.md#apikeysinfo)  |
 
 

 
### stat
> **POST** /identity/v1/api-keys/stat
>


| Type | Message |
| :--- | :--- |
| Request | [APIKeyStatQuery](api-key.md#apikeystatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### APIKeyInfo
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
      <td style="text-align:left">api_key_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">api_key</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE_STATE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">last_accessed_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### APIKeyQuery
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
      <td style="text-align:left">api_key_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE_STATE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### APIKeyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | api_key_id |string|✅| |
| 2 | domain_id |string|✅| |

### APIKeyStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### APIKeysInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of APIKeyInfo](api-key.md#apikeyinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateAPIKeyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_id |string|✅| |
| 2 | domain_id |string|✅| |

### GetAPIKeyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | api_key_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |
