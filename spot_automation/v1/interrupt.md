---
description:  
---
# Interrupt

>  **Package : spaceone.api.spot_automation.v1**

## Interrupt

{% hint style="info" %}
**Interrupt Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**confirm**](interrupt.md#confirm)|   [ConfirmRequest](interrupt.md#confirmrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**interrupt**](interrupt.md#interrupt)|   [InterruptRequest](interrupt.md#interruptrequest) |   [InterruptInfo](interrupt.md#interruptinfo) |
| [**list**](interrupt.md#list)|   [QueryInterruptRequest](interrupt.md#queryinterruptrequest) |   [InterruptsInfo](interrupt.md#interruptsinfo) |
| [**stat**](interrupt.md#stat)|   [InterruptStatRequest](interrupt.md#interruptstatrequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### confirm
> **POST** /spot-automation/v1/interrupt/confirm
>


| Type | Message |
| :--- | :--- |
| Request | [ConfirmRequest](interrupt.md#confirmrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### interrupt
> **POST** /spot-automation/v1/interrupt/interrupt
>


| Type | Message |
| :--- | :--- |
| Request | [InterruptRequest](interrupt.md#interruptrequest) |
| Response |  [InterruptInfo](interrupt.md#interruptinfo)  |
 
 

 
### list
> **GET** /spot-automation/v1/interrupts
>
> **POST** /spot-automation/v1/interrupts/search



| Type | Message |
| :--- | :--- |
| Request | [QueryInterruptRequest](interrupt.md#queryinterruptrequest) |
| Response |  [InterruptsInfo](interrupt.md#interruptsinfo)  |
 
 

 
### stat
> **POST** /spot-automation/v1/interrupts/stat
>


| Type | Message |
| :--- | :--- |
| Request | [InterruptStatRequest](interrupt.md#interruptstatrequest) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### ConfirmRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| provider |string|✅| |
| region_code |string|✅| |
| domain_id |string|✅| |
| secret_id |string|✅| |
| token |string|✅| |
| data |string|✅| |

### InterruptInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| interrupt_id |string | |
| spot_group_id |string | |
| type |string | |
| reference |[InterruptResourceReference](interrupt.md#interruptresourcereference) | |
| availability_zone |string | |
| region_code |string | |
| provider |string | |
| created_at |string | |

### InterruptRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| provider |string|✅| |
| region_code |string|✅| |
| domain_id |string|✅| |
| secret_id |string|✅| |
| token |string|✅| |
| data |string|✅| |

### InterruptResourceReference
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_id |string | |
| external_link |string | |

### InterruptStatRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### InterruptsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of InterruptInfo](interrupt.md#interruptinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### QueryInterruptRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| spot_group_id |string|❌| |
| domain_id |string|✅| |
