---
description:  
---
# Api key

>  **Package : spaceone.api.identity.v1**

## APIKey

{% hint style="info" %}
**APIKey Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](api-key.md#create)|   [CreateAPIKeyRequest](api-key.md#createapikeyrequest) |   [APIKeyInfo](api-key.md#apikeyinfo) |  |
| [**enable**](api-key.md#enable)|   [APIKeyRequest](api-key.md#apikeyrequest) |   [APIKeyInfo](api-key.md#apikeyinfo) |  |
| [**disable**](api-key.md#disable)|   [APIKeyRequest](api-key.md#apikeyrequest) |   [APIKeyInfo](api-key.md#apikeyinfo) |  |
| [**delete**](api-key.md#delete)|   [APIKeyRequest](api-key.md#apikeyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](api-key.md#get)|   [GetAPIKeyRequest](api-key.md#getapikeyrequest) |   [APIKeyInfo](api-key.md#apikeyinfo) |  |
| [**list**](api-key.md#list)|   [APIKeyQuery](api-key.md#apikeyquery) |   [APIKeysInfo](api-key.md#apikeysinfo) |  |
| [**stat**](api-key.md#stat)|   [APIKeyStatQuery](api-key.md#apikeystatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](api-key.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateAPIKeyRequest](api-key.md#createapikeyrequest)  </div> | <div style="width:200px; text-align:center;">   [APIKeyInfo](api-key.md#apikeyinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**enable**](api-key.md#enable) </div> | <div style="width:200px; text-align:center;">    [APIKeyRequest](api-key.md#apikeyrequest)  </div> | <div style="width:200px; text-align:center;">   [APIKeyInfo](api-key.md#apikeyinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**disable**](api-key.md#disable) </div> | <div style="width:200px; text-align:center;">    [APIKeyRequest](api-key.md#apikeyrequest)  </div> | <div style="width:200px; text-align:center;">   [APIKeyInfo](api-key.md#apikeyinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](api-key.md#delete) </div> | <div style="width:200px; text-align:center;">    [APIKeyRequest](api-key.md#apikeyrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](api-key.md#get) </div> | <div style="width:200px; text-align:center;">    [GetAPIKeyRequest](api-key.md#getapikeyrequest)  </div> | <div style="width:200px; text-align:center;">   [APIKeyInfo](api-key.md#apikeyinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](api-key.md#list) </div> | <div style="width:200px; text-align:center;">    [APIKeyQuery](api-key.md#apikeyquery)  </div> | <div style="width:200px; text-align:center;">   [APIKeysInfo](api-key.md#apikeysinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](api-key.md#stat) </div> | <div style="width:200px; text-align:center;">    [APIKeyStatQuery](api-key.md#apikeystatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
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
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">api_key_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">api_key</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE_STATE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">last_accessed_at</td>
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



### APIKeyQuery
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
      <td style="text-align:left">api_key_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE_STATE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">user_id</td>
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



### APIKeyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| api_key_id |string|✅| |
| domain_id |string|✅| |

### APIKeyStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### APIKeysInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of APIKeyInfo](api-key.md#apikeyinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateAPIKeyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_id |string|✅| |
| domain_id |string|✅| |

### GetAPIKeyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| api_key_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |
