---
description:  
---
# Controller

>  **Package : spaceone.api.spot_automation.plugin**

## Controller

{% hint style="info" %}
**Controller Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](controller.md#init)|   [InitRequest](controller.md#initrequest) |   [PluginInfo](controller.md#plugininfo) |
| [**verify**](controller.md#verify)|   [VerifyRequest](controller.md#verifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**patch**](controller.md#patch)|   [PatchRequest](controller.md#patchrequest) |   [ResponseInfo](controller.md#responseinfo) | 
 

 
### init


| Type | Message |
| :--- | :--- |
| Request | [InitRequest](controller.md#initrequest) |
| Response |  [PluginInfo](controller.md#plugininfo)  |
 
 

 
### verify


| Type | Message |
| :--- | :--- |
| Request | [VerifyRequest](controller.md#verifyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### patch


| Type | Message |
| :--- | :--- |
| Request | [PatchRequest](controller.md#patchrequest) |
| Response |  [ResponseInfo](controller.md#responseinfo)  |


## 

## Message

### InitRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### PatchRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| action |string|✅| |
| command |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### PluginInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### ResponseInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### VerifyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
