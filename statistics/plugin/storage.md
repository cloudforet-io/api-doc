---
description:  
---
# Storage

>  **Package : spaceone.api.inventory.plugin**

## Storage

{% hint style="info" %}
**Storage Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](storage.md#init)|   [InitRequest](storage.md#initrequest) |   [PluginInfo](storage.md#plugininfo) |
| [**verify**](storage.md#verify)|   [VerifyRequest](storage.md#verifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**export**](storage.md#export)|   [ExportRequest](storage.md#exportrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| 
 

 
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
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| schema |string|❌| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### InitRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### PluginInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### VerifyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| schema |string|❌| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
