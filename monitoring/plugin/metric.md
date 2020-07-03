---
description: null
---

# Metric

> **Package : spaceone.api.monitoring.plugin**

## Metric

{% hint style="info" %}
**Metric Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [list](metric.md#list) | [MetricRequest](metric.md#metricrequest) | [PluginMetricsResponse](metric.md#pluginmetricsresponse) |  |
| 2 | [get\_data](metric.md#get_data) | [MetricDataRequest](metric.md#metricdatarequest) | [PluginMetricDataResponse](metric.md#pluginmetricdataresponse) |  |

### list

| Type | Message |
| :--- | :--- |
| Request | [MetricRequest](metric.md#metricrequest) |
| Response | [PluginMetricsResponse](metric.md#pluginmetricsresponse) |

### get\_data

| Type | Message |
| :--- | :--- |
| Request | [MetricDataRequest](metric.md#metricdatarequest) |
| Response | [PluginMetricDataResponse](metric.md#pluginmetricdataresponse) |

## Message

### MetricDataInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | labels | [google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) |  |  |
| 2 | values | [google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) |  |  |

### MetricDataRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | required |
| 2 | secret\_data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | required |
| 3 | resource | string |  | required |
| 4 | metric | string |  | required |
| 5 | start | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  | required |
| 6 | end | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  | required |
| 7 | period | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  | required |
| 8 | stat | string |  | required |

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
| 1 | options | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | required |
| 2 | secret\_data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | required |
| 3 | resource | string |  | required |

### MetricsInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | metrics | [MetricInfo](metric.md#metricinfo) |  |  |

### PluginMetricDataResponse

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource\_type | string |  | required |
| 2 | actions | [spaceone.api.core.v1.PluginAction](../../core/v1/plugin.md##pluginaction) |  | optional |
| 3 | result | [MetricDataInfo](metric.md#metricdatainfo) |  | required |

### PluginMetricsResponse

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource\_type | string |  | required |
| 2 | actions | [spaceone.api.core.v1.PluginAction](../../core/v1/plugin.md##pluginaction) |  | optional |
| 3 | result | [MetricsInfo](metric.md#metricsinfo) |  | required |

