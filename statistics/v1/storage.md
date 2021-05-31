---
description:  
---
# Storage

>  **Package : spaceone.api.statistics.v1**

## Storage

{% hint style="info" %}
**Storage Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**register**](storage.md#register)|   [RegisterStorageRequest](storage.md#registerstoragerequest) |   [StorageInfo](storage.md#storageinfo) |  |
| 2 | [**update**](storage.md#update)|   [UpdateStorageRequest](storage.md#updatestoragerequest) |   [StorageInfo](storage.md#storageinfo) |  |
| 3 | [**update_plugin**](storage.md#update_plugin)|   [UpdateStoragePluginRequest](storage.md#updatestoragepluginrequest) |   [StorageInfo](storage.md#storageinfo) |  |
| 4 | [**verify_plugin**](storage.md#verify_plugin)|   [StorageRequest](storage.md#storagerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**enable**](storage.md#enable)|   [StorageRequest](storage.md#storagerequest) |   [StorageInfo](storage.md#storageinfo) |  |
| 6 | [**disable**](storage.md#disable)|   [StorageRequest](storage.md#storagerequest) |   [StorageInfo](storage.md#storageinfo) |  |
| 7 | [**deregister**](storage.md#deregister)|   [StorageRequest](storage.md#storagerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 8 | [**get**](storage.md#get)|   [GetStorageRequest](storage.md#getstoragerequest) |   [StorageInfo](storage.md#storageinfo) |  |
| 9 | [**list**](storage.md#list)|   [StorageQuery](storage.md#storagequery) |   [StoragesInfo](storage.md#storagesinfo) |  |
| 10 | [**stat**](storage.md#stat)|   [StorageStatQuery](storage.md#storagestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | storage_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### PluginInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | plugin_id |string | |
| 2 | version |string | |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 4 | secret_id |string | |
| 5 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### PluginRequest
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | plugin_id |string | |
| 2 | version |string | |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 4 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 5 | schema |string | |

### RegisterStorageRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | plugin_info |[PluginRequest](storage.md#pluginrequest)|❌| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | user_id |string|✅| |
| 5 | domain_id |string|✅| |

### StorageInfo
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
      <td style="text-align:left">storage_id</td>
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
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">plugin_info</td>
      <td style="text-align:left"><a href="storage.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### StorageQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | storage_id |string|❌| |
| 3 | name |string|❌| |
| 4 | state |string|❌| |
| 5 | user_id |string|❌| |
| 6 | domain_id |string|✅| |

### StorageRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | storage_id |string|✅| |
| 2 | domain_id |string|✅| |

### StorageStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### StoragesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of StorageInfo](storage.md#storageinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateStoragePluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | storage_id |string|✅| |
| 2 | version |string|❌| |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | domain_id |string|✅| |

### UpdateStorageRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | storage_id |string|✅| |
| 2 | name |string|❌| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | domain_id |string|✅| |
