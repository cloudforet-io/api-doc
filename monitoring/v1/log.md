---
description:  
---
# Log

>  **Package : spaceone.api.monitoring.v1**

## Log

{% hint style="info" %}
**Log Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**list**](log.md#list)|   [LogRequest](log.md#logrequest) |   [LogDataInfo](log.md#logdatainfo) |  |TEST

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
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   LogRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   LogDataInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
### list
> **GET** /monitoring/v1/data-source/{data_source_id}/logs
>


| Type | Message |
| :--- | :--- |
| Request | [LogRequest](log.md#logrequest) |
| Response |  [LogDataInfo](log.md#logdatainfo)  |


## 

## Message

### LogDataInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| logs |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| domain_id |string | |

### LogRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_id |string|✅| |
| resource_type |string|✅| |
| resource_id |string|✅| |
| start |string|❌| |
| end |string|❌| |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| sort |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| limit |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| domain_id |string|✅| |
