---
description:  
---
# Controller

>  **Package : spaceone.api.spot_automation.plugin**

## Controller

{% hint style="info" %}
**Controller Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**init**](controller.md#init)|   [InitRequest](controller.md#initrequest) |   [PluginInfo](controller.md#plugininfo) |  |
| 2 | [**verify**](controller.md#verify)|   [VerifyRequest](controller.md#verifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 3 | [**patch**](controller.md#patch)|   [PatchRequest](controller.md#patchrequest) |   [ResponseInfo](controller.md#responseinfo) |  | 
 

 
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
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### PatchRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 2 | action |string|✅| |
| 3 | command |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### PluginInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### ResponseInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### VerifyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 2 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
