---
description:  
---
# Metric

>  **Package : spaceone.api.monitoring.plugin**

## Metric

{% hint style="info" %}
**Metric Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [list](Metric.md#list)| [MetricRequest](Metric.md#metricrequest) | [PluginMetricsResponse](Metric.md#pluginmetricsresponse) |  |
| 2 | [get_data](Metric.md#get_data)| [MetricDataRequest](Metric.md#metricdatarequest) | [PluginMetricDataResponse](Metric.md#pluginmetricdataresponse) |  |

### list



| Type | Message |
| :--- | :--- |
| Request | [MetricRequest](Metric.md#metricrequest) |
| Response |  [PluginMetricsResponse](Metric.md#pluginmetricsresponse)  |



### get_data



| Type | Message |
| :--- | :--- |
| Request | [MetricDataRequest](Metric.md#metricdatarequest) |
| Response |  [PluginMetricDataResponse](Metric.md#pluginmetricdataresponse)  |





## Message

### MetricDataInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | ||
| 2 | values |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | ||

### MetricDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |✅ ||
| 2 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |✅ ||
| 3 | resource |[google.protobuf.Value](https://developers.google.com/protocol-buffers/docs/reference/overview) |✅ ||
| 4 | metric |string |✅ ||
| 5 | start |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |✅ ||
| 6 | end |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |✅ ||
| 7 | period |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |✅ ||
| 8 | stat |string |✅ ||

### MetricInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | key |string | ||
| 2 | name |string | ||
| 3 | unit |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 4 | chart_type |string | ||
| 5 | chart_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||

### MetricRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |✅ ||
| 2 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |✅ ||
| 3 | resource |[google.protobuf.Value](https://developers.google.com/protocol-buffers/docs/reference/overview) |✅ ||

### MetricsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | metrics |[MetricInfo](Metric.md#metricinfo) | ||

### PluginMetricDataResponse
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_type |string |✅ ||
| 2 | actions |[spaceone.api.core.v1.PluginAction](../../core/v1/Plugin.md##pluginaction) |❌ ||
| 3 | result |[MetricDataInfo](Metric.md#metricdatainfo) |✅ ||

### PluginMetricsResponse
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_type |string |✅ ||
| 2 | actions |[spaceone.api.core.v1.PluginAction](../../core/v1/Plugin.md##pluginaction) |❌ ||
| 3 | result |[MetricsInfo](Metric.md#metricsinfo) |✅ ||
