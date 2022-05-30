---
description:  
---
# Cost saving

>  **Package : spaceone.api.spot_automation.plugin**

## CostSaving

{% hint style="info" %}
**CostSaving Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**get**](cost-saving.md#get)|   [CostSavingRequest](cost-saving.md#costsavingrequest) |   [CostSavingInfo](cost-saving.md#costsavinginfo) |  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**get**](cost-saving.md#get) </div> | <div style="width:200px; text-align:center;">    [CostSavingRequest](cost-saving.md#costsavingrequest)  </div> | <div style="width:200px; text-align:center;">   [CostSavingInfo](cost-saving.md#costsavinginfo)  </div> | <div style="width:400px;">  </div> | 
 

 
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
| resource_id |string|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
