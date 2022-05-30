---
description:  
---
# Cost

>  **Package : spaceone.api.cost_analysis.plugin**

## Cost

{% hint style="info" %}
**Cost Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**get_data**](cost.md#get_data)|   [GetDataRequest](cost.md#getdatarequest) | **`stream`**   [CostsInfo](cost.md#costsinfo) |  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**get_data**](cost.md#get_data) </div> | <div style="width:200px; text-align:center;">    [GetDataRequest](cost.md#getdatarequest)  </div> | <div style="width:200px; text-align:center;"> **`stream`**   [CostsInfo](cost.md#costsinfo)  </div> | <div style="width:400px;">  </div> | 
 

 
### get_data


| Type | Message |
| :--- | :--- |
| Request | [GetDataRequest](cost.md#getdatarequest) |
| Response |  [CostsInfo](cost.md#costsinfo)  |


## 

## Message

### CostInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| cost |float | |
| currency |string | |
| usage_quantity |float | |
| provider |string | |
| region_code |string | |
| category |string | |
| product |string | |
| account |string | |
| usage_type |string | |
| resource_group |string | |
| resource |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| billed_at |string | |

### CostsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CostInfo](cost.md#costinfo) | |

### GetDataRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| schema |string|❌| |
| task_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
