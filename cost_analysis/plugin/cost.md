---
description:  
---
# Cost

>  **Package : spaceone.api.cost_analysis.job**

## Cost

{% hint style="info" %}
**Cost Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**get_data**](cost.md#get_data)|   [GetDataRequest](cost.md#getdatarequest) |   [CostsInfo](cost.md#costsinfo) |  | 
 

 
### get_data


| Type | Message |
| :--- | :--- |
| Request | [GetDataRequest](cost.md#getdatarequest) |
| Response |  [CostsInfo](cost.md#costsinfo)  |


## 

## Message

### CostInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | cost_key |string | |
| 2 | cost |float | |
| 3 | currency |string | |
| 4 | usage_quantity |float | |
| 5 | provider |string | |
| 6 | region_code |string | |
| 7 | product |string | |
| 8 | account |string | |
| 9 | resource_type |string | |
| 10 | resource_group |string | |
| 11 | resource |string | |
| 12 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 13 | additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 14 | billed_at |string | |

### CostsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of CostInfo](cost.md#costinfo) | |

### GetDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 2 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 3 | schema |string|❌| |
| 4 | start |string|✅| |
| 5 | end |string|✅| |
| 6 | task_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
