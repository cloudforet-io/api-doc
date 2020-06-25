---
description: null
---

# Log

> **Package : spaceone.api.monitoring.v1**

## Log

{% hint style="info" %}
**Log Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [list](log.md#list) | [LogRequest](log.md#logrequest) | [LogDataInfo](log.md#logdatainfo) |  |

### list

> **GET** /monitoring/v1/data-source/{data\_source\_id}/logs

| Type | Message |
| :--- | :--- |
| Request | [LogRequest](log.md#logrequest) |
| Response | [LogDataInfo](log.md#logdatainfo) |

## Message

### LogDataInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | logs | [google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) |  |  |
| 2 | domain\_id | string |  |  |

### LogRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | data\_source\_id | string |  | required |
| 2 | resource\_type | string |  | optional |
| 3 | resource\_id | string |  | optional |
| 4 | start | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  | optional |
| 5 | end | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  | optional |
| 6 | filter | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 7 | sort | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 8 | limit | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  | optional |
| 9 | domain\_id | string |  | required |

