---
description: null
---

# Metric

> **Package : spaceone.api.monitoring.v1**

## Metric

{% hint style="info" %}
**Metric Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [get\_data](metric.md#get_data) | [MetricDataRequest](metric.md#metricdatarequest) | [MetricDataInfo](metric.md#metricdatainfo) |  |
| 2 | [list](metric.md#list) | [MetricRequest](metric.md#metricrequest) | [MetricsInfo](metric.md#metricsinfo) |  |

### get\_data

> **GET** /monitoring/v1/data-source/{data\_source\_id}/metric-data

| Type | Message |
| :--- | :--- |
| Request | [MetricDataRequest](metric.md#metricdatarequest) |
| Response | [MetricDataInfo](metric.md#metricdatainfo) |

### list

> **GET** /monitoring/v1/data-source/{data\_source\_id}/metrics

| Type | Message |
| :--- | :--- |
| Request | [MetricRequest](metric.md#metricrequest) |
| Response | [MetricsInfo](metric.md#metricsinfo) |

## Message

### MetricDataInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | labels | [google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) |  |  |
| 2 | resource\_values | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 3 | domain\_id | string |  |  |

### MetricDataRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | data\_source\_id | string | ✅ |  |
| 2 | resource\_type | string | ✅ |  |
| 3 | resources | string | ✅ |  |
| 4 | metric | string | ✅ |  |
| 5 | start | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ✅ |  |
| 6 | end | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ✅ |  |
| 7 | period | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ❌ |  |
| 8 | stat | string | ❌ |  |
| 9 | domain\_id | string | ✅ |  |

### MetricInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | key | string |  |  |
| 2 | name | string |  |  |
| 3 | unit | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 4 | chart\_type | string |  |  |
| 5 | chart\_options | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |

### MetricRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | data\_source\_id | string | ✅ |  |
| 2 | resource\_type | string | ✅ |  |
| 3 | resources | string | ✅ |  |
| 4 | domain\_id | string | ✅ |  |

### MetricsInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | metrics | [MetricInfo](metric.md#metricinfo) |  |  |
| 2 | available\_resources | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 3 | domain\_id | string |  |  |

