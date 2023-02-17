---
description:  
---
# Api key

>  **Package : spaceone.api.identity.v1**

## APIKey

{% hint style="info" %}
**APIKey Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](api-key.md#create)|   [CreateAPIKeyRequest](api-key.md#createapikeyrequest) |   [APIKeyInfo](api-key.md#apikeyinfo) |
| [**enable**](api-key.md#enable)|   [APIKeyRequest](api-key.md#apikeyrequest) |   [APIKeyInfo](api-key.md#apikeyinfo) |
| [**disable**](api-key.md#disable)|   [APIKeyRequest](api-key.md#apikeyrequest) |   [APIKeyInfo](api-key.md#apikeyinfo) |
| [**delete**](api-key.md#delete)|   [APIKeyRequest](api-key.md#apikeyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](api-key.md#get)|   [GetAPIKeyRequest](api-key.md#getapikeyrequest) |   [APIKeyInfo](api-key.md#apikeyinfo) |
| [**list**](api-key.md#list)|   [APIKeyQuery](api-key.md#apikeyquery) |   [APIKeysInfo](api-key.md#apikeysinfo) |
| [**stat**](api-key.md#stat)|   [APIKeyStatQuery](api-key.md#apikeystatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /identity/v1/api-key/create
>


| Type | Message |
| :--- | :--- |
| Request | [CreateAPIKeyRequest](api-key.md#createapikeyrequest) |
| Response |  [APIKeyInfo](api-key.md#apikeyinfo)  |
 
 

 
### enable
> **POST** /identity/v1/api-key/enable
>


| Type | Message |
| :--- | :--- |
| Request | [APIKeyRequest](api-key.md#apikeyrequest) |
| Response |  [APIKeyInfo](api-key.md#apikeyinfo)  |
 
 

 
### disable
> **POST** /identity/v1/api-key/disable
>


| Type | Message |
| :--- | :--- |
| Request | [APIKeyRequest](api-key.md#apikeyrequest) |
| Response |  [APIKeyInfo](api-key.md#apikeyinfo)  |
 
 

 
### delete
> **POST** /identity/v1/api-key/delete
>


| Type | Message |
| :--- | :--- |
| Request | [APIKeyRequest](api-key.md#apikeyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **POST** /identity/v1/api-key/get
>


| Type | Message |
| :--- | :--- |
| Request | [GetAPIKeyRequest](api-key.md#getapikeyrequest) |
| Response |  [APIKeyInfo](api-key.md#apikeyinfo)  |
 
 

 
### list
> **POST** /identity/v1/api-key/list
>


| Type | Message |
| :--- | :--- |
| Request | [APIKeyQuery](api-key.md#apikeyquery) |
| Response |  [APIKeysInfo](api-key.md#apikeysinfo)  |
 
 

 
### stat
> **POST** /identity/v1/api-key/stat
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
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">api_key_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">api_key</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE_STATE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">last_accessed_at</td>
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



### APIKeyQuery
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
      <td style="text-align:left; width:100px;">api_key_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE_STATE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
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



### APIKeyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| api_key_id |string|✔| |
| domain_id |string|✔| |

### APIKeyStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### APIKeysInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of APIKeyInfo](api-key.md#apikeyinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateAPIKeyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_id |string|✔| |
| domain_id |string|✔| |

### GetAPIKeyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| api_key_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |
