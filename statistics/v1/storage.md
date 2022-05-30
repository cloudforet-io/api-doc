---
description:  
---
# Storage

>  **Package : spaceone.api.statistics.v1**

## Storage

{% hint style="info" %}
**Storage Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**register**](storage.md#register)|   [RegisterStorageRequest](storage.md#registerstoragerequest) |   [StorageInfo](storage.md#storageinfo) |  |
| [**update**](storage.md#update)|   [UpdateStorageRequest](storage.md#updatestoragerequest) |   [StorageInfo](storage.md#storageinfo) |  |
| [**update_plugin**](storage.md#update_plugin)|   [UpdateStoragePluginRequest](storage.md#updatestoragepluginrequest) |   [StorageInfo](storage.md#storageinfo) |  |
| [**verify_plugin**](storage.md#verify_plugin)|   [StorageRequest](storage.md#storagerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**enable**](storage.md#enable)|   [StorageRequest](storage.md#storagerequest) |   [StorageInfo](storage.md#storageinfo) |  |
| [**disable**](storage.md#disable)|   [StorageRequest](storage.md#storagerequest) |   [StorageInfo](storage.md#storageinfo) |  |
| [**deregister**](storage.md#deregister)|   [StorageRequest](storage.md#storagerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](storage.md#get)|   [GetStorageRequest](storage.md#getstoragerequest) |   [StorageInfo](storage.md#storageinfo) |  |
| [**list**](storage.md#list)|   [StorageQuery](storage.md#storagequery) |   [StoragesInfo](storage.md#storagesinfo) |  |
| [**stat**](storage.md#stat)|   [StorageStatQuery](storage.md#storagestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**register**](storage.md#register) </div> | <div style="width:200px; text-align:center;">    [RegisterStorageRequest](storage.md#registerstoragerequest)  </div> | <div style="width:200px; text-align:center;">   [StorageInfo](storage.md#storageinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](storage.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateStorageRequest](storage.md#updatestoragerequest)  </div> | <div style="width:200px; text-align:center;">   [StorageInfo](storage.md#storageinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update_plugin**](storage.md#update_plugin) </div> | <div style="width:200px; text-align:center;">    [UpdateStoragePluginRequest](storage.md#updatestoragepluginrequest)  </div> | <div style="width:200px; text-align:center;">   [StorageInfo](storage.md#storageinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**verify_plugin**](storage.md#verify_plugin) </div> | <div style="width:200px; text-align:center;">    [StorageRequest](storage.md#storagerequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**enable**](storage.md#enable) </div> | <div style="width:200px; text-align:center;">    [StorageRequest](storage.md#storagerequest)  </div> | <div style="width:200px; text-align:center;">   [StorageInfo](storage.md#storageinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**disable**](storage.md#disable) </div> | <div style="width:200px; text-align:center;">    [StorageRequest](storage.md#storagerequest)  </div> | <div style="width:200px; text-align:center;">   [StorageInfo](storage.md#storageinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**deregister**](storage.md#deregister) </div> | <div style="width:200px; text-align:center;">    [StorageRequest](storage.md#storagerequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](storage.md#get) </div> | <div style="width:200px; text-align:center;">    [GetStorageRequest](storage.md#getstoragerequest)  </div> | <div style="width:200px; text-align:center;">   [StorageInfo](storage.md#storageinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](storage.md#list) </div> | <div style="width:200px; text-align:center;">    [StorageQuery](storage.md#storagequery)  </div> | <div style="width:200px; text-align:center;">   [StoragesInfo](storage.md#storagesinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](storage.md#stat) </div> | <div style="width:200px; text-align:center;">    [StorageStatQuery](storage.md#storagestatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
### register
> **POST** /statistics/v1/storages
>


| Type | Message |
| :--- | :--- |
| Request | [RegisterStorageRequest](storage.md#registerstoragerequest) |
| Response |  [StorageInfo](storage.md#storageinfo)  |
 
 

 
### update
> **PUT** /statistics/v1/storage/{storage_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateStorageRequest](storage.md#updatestoragerequest) |
| Response |  [StorageInfo](storage.md#storageinfo)  |
 
 

 
### update_plugin
> **PUT** /spot-automation/v1/storage/{storage_id}/plugin
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateStoragePluginRequest](storage.md#updatestoragepluginrequest) |
| Response |  [StorageInfo](storage.md#storageinfo)  |
 
 

 
### verify_plugin
> **POST** /spot-automation/v1/storage/{storage_id}/plugin/verify
>


| Type | Message |
| :--- | :--- |
| Request | [StorageRequest](storage.md#storagerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### enable
> **PUT** /statistics/v1/storage/{schedule_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [StorageRequest](storage.md#storagerequest) |
| Response |  [StorageInfo](storage.md#storageinfo)  |
 
 

 
### disable
> **PUT** /statistics/v1/storage/{schedule_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [StorageRequest](storage.md#storagerequest) |
| Response |  [StorageInfo](storage.md#storageinfo)  |
 
 

 
### deregister
> **DELETE** /statistics/v1/storage/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [StorageRequest](storage.md#storagerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /statistics/v1/storage/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetStorageRequest](storage.md#getstoragerequest) |
| Response |  [StorageInfo](storage.md#storageinfo)  |
 
 

 
### list
> **GET** /statistics/v1/storages
>
> **POST** /statistics/v1/storages/search



| Type | Message |
| :--- | :--- |
| Request | [StorageQuery](storage.md#storagequery) |
| Response |  [StoragesInfo](storage.md#storagesinfo)  |
 
 

 
### stat
> **POST** /statistics/v1/storages/stat
>


| Type | Message |
| :--- | :--- |
| Request | [StorageStatQuery](storage.md#storagestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### GetStorageRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| storage_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### PluginInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| plugin_id |string | |
| version |string | |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| secret_id |string | |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### PluginRequest
| Field | Type |  Description |
| :--- | :--- | :--- |
| plugin_id |string | |
| version |string | |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| schema |string | |

### RegisterStorageRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| plugin_info |[PluginRequest](storage.md#pluginrequest)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| user_id |string|✅| |
| domain_id |string|✅| |

### StorageInfo
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
      <td style="text-align:left">storage_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">plugin_info</td>
      <td style="text-align:left"><a href="storage.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### StorageQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| storage_id |string|❌| |
| name |string|❌| |
| state |string|❌| |
| user_id |string|❌| |
| domain_id |string|✅| |

### StorageRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| storage_id |string|✅| |
| domain_id |string|✅| |

### StorageStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### StoragesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of StorageInfo](storage.md#storageinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateStoragePluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| storage_id |string|✅| |
| version |string|❌| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### UpdateStorageRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| storage_id |string|✅| |
| name |string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
