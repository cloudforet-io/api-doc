---
description:  
---
# Cost saving

>  **Package : spaceone.api.spot_automation.plugin**

## CostSaving

{% hint style="info" %}
**CostSaving Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**get**](cost-saving.md#get)|   [CostSavingRequest](cost-saving.md#costsavingrequest) |   [CostSavingInfo](cost-saving.md#costsavinginfo) |  |TEST

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
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CostSavingRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CostSavingInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
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
