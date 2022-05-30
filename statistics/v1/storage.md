---
description:  
---
# Storage

>  **Package : spaceone.api.statistics.v1**

## Storage

{% hint style="info" %}
**Storage Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](storage.md#register)|   [RegisterStorageRequest](storage.md#registerstoragerequest) |   [StorageInfo](storage.md#storageinfo) |
| [**update**](storage.md#update)|   [UpdateStorageRequest](storage.md#updatestoragerequest) |   [StorageInfo](storage.md#storageinfo) |
| [**update_plugin**](storage.md#update_plugin)|   [UpdateStoragePluginRequest](storage.md#updatestoragepluginrequest) |   [StorageInfo](storage.md#storageinfo) |
| [**verify_plugin**](storage.md#verify_plugin)|   [StorageRequest](storage.md#storagerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**enable**](storage.md#enable)|   [StorageRequest](storage.md#storagerequest) |   [StorageInfo](storage.md#storageinfo) |
| [**disable**](storage.md#disable)|   [StorageRequest](storage.md#storagerequest) |   [StorageInfo](storage.md#storageinfo) |
| [**deregister**](storage.md#deregister)|   [StorageRequest](storage.md#storagerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](storage.md#get)|   [GetStorageRequest](storage.md#getstoragerequest) |   [StorageInfo](storage.md#storageinfo) |
| [**list**](storage.md#list)|   [StorageQuery](storage.md#storagequery) |   [StoragesInfo](storage.md#storagesinfo) |
| [**stat**](storage.md#stat)|   [StorageStatQuery](storage.md#storagestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
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
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">storage_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">plugin_info</td>
      <td style="text-align:left"><a href="storage.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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
      <td style="text-align:left; width:100px;">created_at</td>
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
