---
description:  
---
# Metric

>  **Package : spaceone.api.monitoring.v1**

## Metric

{% hint style="info" %}
**Metric Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [get_data](Metric.md#get_data)| [MetricDataRequest](Metric.md#metricdatarequest) | [MetricDataInfo](Metric.md#metricdatainfo) |  |
| 2 | [list](Metric.md#list)| [MetricRequest](Metric.md#metricrequest) | [MetricsInfo](Metric.md#metricsinfo) |  |

### get_data
> **GET** /monitoring/v1/data-source/{data_source_id}/metric-data
>



| Type | Message |
| :--- | :--- |
| Request | [MetricDataRequest](Metric.md#metricdatarequest) |
| Response |  [MetricDataInfo](Metric.md#metricdatainfo)  |



### list
> **GET** /monitoring/v1/data-source/{data_source_id}/metrics
>



| Type | Message |
| :--- | :--- |
| Request | [MetricRequest](Metric.md#metricrequest) |
| Response |  [MetricsInfo](Metric.md#metricsinfo)  |





## Message

### MetricDataInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | ||
| 2 | resource_values |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 3 | domain_id |string | ||

### MetricDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | data_source_id |string |✅ ||
| 2 | resource_type |string |✅ ||
| 3 | resources |string |✅ ||
| 4 | metric |string |✅ ||
| 5 | start |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |✅ ||
| 6 | end |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |✅ ||
| 7 | period |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |❌ ||
| 8 | stat |string |❌ ||
| 9 | domain_id |string |✅ ||

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
| 1 | data_source_id |string |✅ ||
| 2 | resource_type |string |✅ ||
| 3 | resources |string |✅ ||
| 4 | domain_id |string |✅ ||

### MetricsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | metrics |[MetricInfo](Metric.md#metricinfo) | ||
| 2 | available_resources |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 3 | domain_id |string | ||
