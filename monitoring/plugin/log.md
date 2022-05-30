---
description:  
---
# Log

>  **Package : spaceone.api.monitoring.plugin**

## Log

{% hint style="info" %}
**Log Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**list**](log.md#list)|   [LogRequest](log.md#logrequest) | **`stream`**   [LogsDataInfo](log.md#logsdatainfo) |  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**list**](log.md#list) </div> | <div style="width:200px; text-align:center;">    [LogRequest](log.md#logrequest)  </div> | <div style="width:200px; text-align:center;"> **`stream`**   [LogsDataInfo](log.md#logsdatainfo)  </div> | <div style="width:400px;">  </div> | 
 

 
### list


| Type | Message |
| :--- | :--- |
| Request | [LogRequest](log.md#logrequest) |
| Response |  [LogsDataInfo](log.md#logsdatainfo)  |


## 

## Message

### LogRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| resource |[google.protobuf.Value](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| start |string|❌| |
| end |string|❌| |
| sort |[Sort](log.md#sort)|❌| |
| limit |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| schema |string|❌| |

### LogsDataInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| logs |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |

### Sort
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| desc |bool | |
