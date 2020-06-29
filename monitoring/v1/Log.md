---
description:  
---
# Log

>  **Package : spaceone.api.monitoring.v1**

## Log

{% hint style="info" %}
**Log Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [list](Log.md#list)| [LogRequest](Log.md#logrequest) | [LogDataInfo](Log.md#logdatainfo) |  |

### list
> **GET** /monitoring/v1/data-source/{data_source_id}/logs
>



| Type | Message |
| :--- | :--- |
| Request | [LogRequest](Log.md#logrequest) |
| Response |  [LogDataInfo](Log.md#logdatainfo)  |





## Message

### LogDataInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | logs |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | ||
| 2 | domain_id |string | ||

### LogRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | data_source_id |string |✅ ||
| 2 | resource_type |string |❌ ||
| 3 | resource_id |string |❌ ||
| 4 | start |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |❌ ||
| 5 | end |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |❌ ||
| 6 | filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 7 | sort |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 8 | limit |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |❌ ||
| 9 | domain_id |string |✅ ||
