---
description:  
---
# Cost saving

>  **Package : spaceone.api.spot_automation.plugin**

## CostSaving

{% hint style="info" %}
**{{ service.name }} Methods:**
{{ service.description }}
{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get**](cost-saving.md#get)|   [CostSavingRequest](cost-saving.md#costsavingrequest) |   [CostSavingInfo](cost-saving.md#costsavinginfo) | 
 

 
### get


| Type | Message |
| :--- | :--- |
| Request | [CostSavingRequest](cost-saving.md#costsavingrequest) |
| Response |  [CostSavingInfo](cost-saving.md#costsavinginfo)  |


## 

## Message

### CostSavingInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| cost_saving_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### CostSavingRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_id |string|✔| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
