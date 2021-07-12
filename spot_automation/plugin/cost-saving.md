---
description:  
---
# Cost saving

>  **Package : spaceone.api.spot_automation.plugin**

## CostSaving

{% hint style="info" %}
**CostSaving Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**get**](cost-saving.md#get)|   [CostSavingRequest](cost-saving.md#costsavingrequest) |   [CostSavingInfo](cost-saving.md#costsavinginfo) |  | 
 

 
### get


| Type | Message |
| :--- | :--- |
| Request | [CostSavingRequest](cost-saving.md#costsavingrequest) |
| Response |  [CostSavingInfo](cost-saving.md#costsavinginfo)  |


## 

## Message

### CostSavingInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | cost_saving_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### CostSavingRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | resource_id |string|✅| |
| 2 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
