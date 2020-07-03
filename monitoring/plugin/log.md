---
description: null
---

# Log

> **Package : spaceone.api.monitoring.plugin**

## Log

{% hint style="info" %}
**Log Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [list](log.md#list) | [LogRequest](log.md#logrequest) | [PluginLogsResponse](log.md#pluginlogsresponse) |  |

### list

| Type | Message |
| :--- | :--- |
| Request | [LogRequest](log.md#logrequest) |
| Response | [PluginLogsResponse](log.md#pluginlogsresponse) |

## Message

### LogRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | required |
| 2 | secret\_data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | required |
| 3 | filter | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | required |
| 4 | resource | string |  | optional |
| 5 | start | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  | optional |
| 6 | end | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  | optional |
| 7 | sort | [Sort](log.md#sort) |  | optional |
| 8 | limit | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  | optional |

### LogsInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | logs | [google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) |  |  |

### PluginLogsResponse

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource\_type | string |  | required |
| 2 | actions | [spaceone.api.core.v1.PluginAction](../../core/v1/plugin.md##pluginaction) |  | optional |
| 3 | result | [LogsInfo](log.md#logsinfo) |  | required |

### Sort

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | key | string |  |  |
| 2 | desc | bool |  |  |

