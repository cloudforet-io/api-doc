---
description:  
---
# Interrupt

>  **Package : spaceone.api.spot_automation.v1**

## Interrupt

{% hint style="info" %}
**Interrupt Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**confirm**](interrupt.md#confirm)|   [ConfirmRequest](interrupt.md#confirmrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 2 | [**interrupt**](interrupt.md#interrupt)|   [InterruptRequest](interrupt.md#interruptrequest) |   [InterruptInfo](interrupt.md#interruptinfo) |  |
| 3 | [**list**](interrupt.md#list)|   [QueryInterruptRequest](interrupt.md#queryinterruptrequest) |   [InterruptsInfo](interrupt.md#interruptsinfo) |  |
| 4 | [**stat**](interrupt.md#stat)|   [InterruptStatRequest](interrupt.md#interruptstatrequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | provider |string|✅| |
| 2 | region_code |string|✅| |
| 3 | domain_id |string|✅| |
| 4 | secret_id |string|✅| |
| 5 | token |string|✅| |
| 6 | data |string|✅| |

### InterruptInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | interrupt_id |string | |
| 2 | spot_group_id |string | |
| 3 | type |string | |
| 4 | reference |[InterruptResourceReference](interrupt.md#interruptresourcereference) | |
| 5 | availability_zone |string | |
| 6 | region_code |string | |
| 7 | provider |string | |
| 8 | project_id |string | |
| 9 | domain_id |string | |
| 10 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |

### InterruptRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | provider |string|✅| |
| 2 | region_code |string|✅| |
| 3 | domain_id |string|✅| |
| 4 | secret_id |string|✅| |
| 5 | token |string|✅| |
| 6 | data |string|✅| |

### InterruptResourceReference
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | resource_id |string | |
| 2 | external_link |string | |

### InterruptStatRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### InterruptsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of InterruptInfo](interrupt.md#interruptinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### QueryInterruptRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | spot_group_id |string|❌| |
| 3 | domain_id |string|✅| |
