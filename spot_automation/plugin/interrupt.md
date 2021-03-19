---
description:  
---
# Interrupt

>  **Package : spaceone.api.spot_automation.plugin**

## Interrupt

{% hint style="info" %}
**Interrupt Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**setup**](interrupt.md#setup)|   [SetupRequest](interrupt.md#setuprequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 2 | [**handle**](interrupt.md#handle)|   [HandleRequest](interrupt.md#handlerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  | 
 

 
### setup


| Type | Message |
| :--- | :--- |
| Request | [SetupRequest](interrupt.md#setuprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### handle


| Type | Message |
| :--- | :--- |
| Request | [HandleRequest](interrupt.md#handlerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |


## 

## Message

### HandleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | spot_group_resource_id |string|✅| |
| 2 | resource_id |string|✅| |
| 3 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### SetupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
