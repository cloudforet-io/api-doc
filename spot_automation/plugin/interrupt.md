---
description:  
---
# Interrupt

>  **Package : spaceone.api.spot_automation.plugin**

## Interrupt

{% hint style="info" %}
**Interrupt Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**setup**](interrupt.md#setup)|   [SetupRequest](interrupt.md#setuprequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**confirm**](interrupt.md#confirm)|   [ConfirmInterruptRequest](interrupt.md#confirminterruptrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**handle**](interrupt.md#handle)|   [HandleRequest](interrupt.md#handlerequest) |   [HandleInfo](interrupt.md#handleinfo) |  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**setup**](interrupt.md#setup) </div> | <div style="width:200px; text-align:center;">    [SetupRequest](interrupt.md#setuprequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**confirm**](interrupt.md#confirm) </div> | <div style="width:200px; text-align:center;">    [ConfirmInterruptRequest](interrupt.md#confirminterruptrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**handle**](interrupt.md#handle) </div> | <div style="width:200px; text-align:center;">    [HandleRequest](interrupt.md#handlerequest)  </div> | <div style="width:200px; text-align:center;">   [HandleInfo](interrupt.md#handleinfo)  </div> | <div style="width:400px;">  </div> | 
 

 
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
| data |string|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### HandleInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| spot_group_resource_id |string | |
| resource_id |string | |
| type |string | |

### HandleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data |string|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### SetupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| endpoint |string|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
