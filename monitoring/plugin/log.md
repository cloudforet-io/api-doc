---
description:  
---
# Log

>  **Package : spaceone.api.monitoring.plugin**

## Log

{% hint style="info" %}
**Log Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](log.md#list)|   [LogRequest](log.md#logrequest) | **`stream`**   [LogsDataInfo](log.md#logsdatainfo) | 
 

 
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
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| schema |string|✘| |
| query |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| keyword |string|✘| |
| start |string|✔| |
| end |string|✔| |
| sort |[Sort](log.md#sort)|✘| |
| limit |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✘| |

### LogsDataInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| logs |[list of google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### Sort
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| desc |bool | |
