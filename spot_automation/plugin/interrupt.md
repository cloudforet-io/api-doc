---
description:  
---
# Interrupt

>  **Package : spaceone.api.spot_automation.plugin**

## Interrupt

{% hint style="info" %}
**{{ service.name }} Methods:**
{{ service.description }}
{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**setup**](interrupt.md#setup)|   [SetupRequest](interrupt.md#setuprequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**confirm**](interrupt.md#confirm)|   [ConfirmInterruptRequest](interrupt.md#confirminterruptrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**handle**](interrupt.md#handle)|   [HandleRequest](interrupt.md#handlerequest) |   [HandleInfo](interrupt.md#handleinfo) | 
 

 
### setup


| Type | Message |
| :--- | :--- |
| Request | [SetupRequest](interrupt.md#setuprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### confirm


| Type | Message |
| :--- | :--- |
| Request | [ConfirmInterruptRequest](interrupt.md#confirminterruptrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### handle


| Type | Message |
| :--- | :--- |
| Request | [HandleRequest](interrupt.md#handlerequest) |
| Response |  [HandleInfo](interrupt.md#handleinfo)  |


## 

## Message

### ConfirmInterruptRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data |string|✔| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |

### HandleInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| spot_group_resource_id |string | |
| resource_id |string | |
| type |string | |

### HandleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data |string|✔| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |

### SetupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| endpoint |string|✔| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
