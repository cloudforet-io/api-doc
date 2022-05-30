---
description:  
---
# Metric

>  **Package : spaceone.api.monitoring.plugin**

## Metric

{% hint style="info" %}
**Metric Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**list**](metric.md#list)|   [MetricRequest](metric.md#metricrequest) |   [MetricsInfo](metric.md#metricsinfo) |  |
| [**get_data**](metric.md#get_data)|   [MetricDataRequest](metric.md#metricdatarequest) |   [MetricDataInfo](metric.md#metricdatainfo) |  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**list**](metric.md#list) </div> | <div style="width:200px; text-align:center;">    [MetricRequest](metric.md#metricrequest)  </div> | <div style="width:200px; text-align:center;">   [MetricsInfo](metric.md#metricsinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get_data**](metric.md#get_data) </div> | <div style="width:200px; text-align:center;">    [MetricDataRequest](metric.md#metricdatarequest)  </div> | <div style="width:200px; text-align:center;">   [MetricDataInfo](metric.md#metricdatainfo)  </div> | <div style="width:400px;">  </div> | 
 

 
### list


| Type | Message |
| :--- | :--- |
| Request | [MetricRequest](metric.md#metricrequest) |
| Response |  [MetricsInfo](metric.md#metricsinfo)  |
 
 

 
### get_data


| Type | Message |
| :--- | :--- |
| Request | [MetricDataRequest](metric.md#metricdatarequest) |
| Response |  [MetricDataInfo](metric.md#metricdatainfo)  |


## 

## Message

### MetricDataInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| resource_values |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### MetricDataRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| resource |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| metric |string|✅| metric identifier in case of requested metric info is not a single.|
| start |string|✅| |
| end |string|✅| |
| period |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| stat |string|❌| |
| schema |string|❌| |

### MetricInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| name |string | |
| unit |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| chart_type |string | |
| chart_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### MetricRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| resource |[google.protobuf.Value](https://developers.google.com/protocol-buffers/docs/reference/overview)|✅| |
| schema |string|❌| |

### MetricsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| metrics |[list of MetricInfo](metric.md#metricinfo) | |
