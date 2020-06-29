---
description:  
---
# Log

>  **Package : spaceone.api.monitoring.plugin**

## Log

{% hint style="info" %}
**Log Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [list](Log.md#list)| [LogRequest](Log.md#logrequest) | [PluginLogsResponse](Log.md#pluginlogsresponse) |  |

### list



| Type | Message |
| :--- | :--- |
| Request | [LogRequest](Log.md#logrequest) |
| Response |  [PluginLogsResponse](Log.md#pluginlogsresponse)  |





## Message

### LogRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |✅ ||
| 2 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |✅ ||
| 3 | filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |✅ ||
| 4 | resource |[google.protobuf.Value](https://developers.google.com/protocol-buffers/docs/reference/overview) |❌ ||
| 5 | start |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |❌ ||
| 6 | end |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |❌ ||
| 7 | sort |[Sort](Log.md#sort) |❌ ||
| 8 | limit |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |❌ ||

### LogsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | logs |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | ||

### PluginLogsResponse
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_type |string |✅ ||
| 2 | actions |[spaceone.api.core.v1.PluginAction](../../core/v1/Plugin.md##pluginaction) |❌ ||
| 3 | result |[LogsInfo](Log.md#logsinfo) |✅ ||

### Sort
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | key |string | ||
| 2 | desc |bool | ||
