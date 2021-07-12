---
description:  
---
# Storage

>  **Package : spaceone.api.inventory.plugin**

## Storage

{% hint style="info" %}
**Storage Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**init**](storage.md#init)|   [InitRequest](storage.md#initrequest) |   [PluginInfo](storage.md#plugininfo) |  |
| 2 | [**verify**](storage.md#verify)|   [VerifyRequest](storage.md#verifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 3 | [**export**](storage.md#export)|   [ExportRequest](storage.md#exportrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  | 
 

 
### init


| Type | Message |
| :--- | :--- |
| Request | [InitRequest](storage.md#initrequest) |
| Response |  [PluginInfo](storage.md#plugininfo)  |
 
 

 
### verify


| Type | Message |
| :--- | :--- |
| Request | [VerifyRequest](storage.md#verifyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### export


| Type | Message |
| :--- | :--- |
| Request | [ExportRequest](storage.md#exportrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |


## 

## Message

### ExportRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 2 | schema |string|❌| |
| 3 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 4 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### InitRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### PluginInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### VerifyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 2 | schema |string|❌| |
| 3 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
