---
description:  
---
# Controller

>  **Package : spaceone.api.spot_automation.plugin**

## Controller

{% hint style="info" %}
**Controller Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**init**](controller.md#init)|   [InitRequest](controller.md#initrequest) |   [PluginInfo](controller.md#plugininfo) |  |
| [**verify**](controller.md#verify)|   [VerifyRequest](controller.md#verifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**patch**](controller.md#patch)|   [PatchRequest](controller.md#patchrequest) |   [ResponseInfo](controller.md#responseinfo) |  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**init**](controller.md#init) </div> | <div style="width:200px; text-align:center;">    [InitRequest](controller.md#initrequest)  </div> | <div style="width:200px; text-align:center;">   [PluginInfo](controller.md#plugininfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**verify**](controller.md#verify) </div> | <div style="width:200px; text-align:center;">    [VerifyRequest](controller.md#verifyrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**patch**](controller.md#patch) </div> | <div style="width:200px; text-align:center;">    [PatchRequest](controller.md#patchrequest)  </div> | <div style="width:200px; text-align:center;">   [ResponseInfo](controller.md#responseinfo)  </div> | <div style="width:400px;">  </div> | 
 

 
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
