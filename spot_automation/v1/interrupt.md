---
description:  
---
# Interrupt

>  **Package : spaceone.api.spot_automation.v1**

## Interrupt

{% hint style="info" %}
**Interrupt Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**confirm**](interrupt.md#confirm)|   [ConfirmRequest](interrupt.md#confirmrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**interrupt**](interrupt.md#interrupt)|   [InterruptRequest](interrupt.md#interruptrequest) |   [InterruptInfo](interrupt.md#interruptinfo) |  |
| [**list**](interrupt.md#list)|   [QueryInterruptRequest](interrupt.md#queryinterruptrequest) |   [InterruptsInfo](interrupt.md#interruptsinfo) |  |
| [**stat**](interrupt.md#stat)|   [InterruptStatRequest](interrupt.md#interruptstatrequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">confirm</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ConfirmRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">interrupt</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   InterruptRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   InterruptInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   QueryInterruptRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   InterruptsInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   InterruptStatRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
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
