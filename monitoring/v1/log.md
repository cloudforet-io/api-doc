---
description:  
---
# Log

>  **Package : spaceone.api.monitoring.v1**

## Log

{% hint style="info" %}
**{{ service.name }} Methods:**
{{ service.description }}
{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](log.md#list)|   [LogRequest](log.md#logrequest) |   [LogDataInfo](log.md#logdatainfo) | 
 

 
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
| data_source_id |string|✔| |
| resource_type |string|✔| |
| resource_id |string|✔| |
| start |string|✘| |
| end |string|✘| |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| sort |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| limit |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✘| |
| domain_id |string|✔| |
