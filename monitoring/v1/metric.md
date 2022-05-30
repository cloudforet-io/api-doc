---
description:  
---
# Metric

>  **Package : spaceone.api.monitoring.v1**

## Metric

{% hint style="info" %}
**Metric Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**get_data**](metric.md#get_data)|   [MetricDataRequest](metric.md#metricdatarequest) |   [MetricDataInfo](metric.md#metricdatainfo) |  |
| [**list**](metric.md#list)|   [MetricRequest](metric.md#metricrequest) |   [MetricsInfo](metric.md#metricsinfo) |  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**get_data**](metric.md#get_data) </div> | <div style="width:200px; text-align:center;">    [MetricDataRequest](metric.md#metricdatarequest)  </div> | <div style="width:200px; text-align:center;">   [MetricDataInfo](metric.md#metricdatainfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](metric.md#list) </div> | <div style="width:200px; text-align:center;">    [MetricRequest](metric.md#metricrequest)  </div> | <div style="width:200px; text-align:center;">   [MetricsInfo](metric.md#metricsinfo)  </div> | <div style="width:400px;">  </div> | 
 

 
### get_data
> **GET** /monitoring/v1/data-source/{data_source_id}/metric-data
>


| Type | Message |
| :--- | :--- |
| Request | [MetricDataRequest](metric.md#metricdatarequest) |
| Response |  [MetricDataInfo](metric.md#metricdatainfo)  |
 
 

 
### list
> **GET** /monitoring/v1/data-source/{data_source_id}/metrics
>


| Type | Message |
| :--- | :--- |
| Request | [MetricRequest](metric.md#metricrequest) |
| Response |  [MetricsInfo](metric.md#metricsinfo)  |


## 

## Message

### MetricDataInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| resource_values |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |

### MetricDataRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_id |string|✅| |
| resource_type |string|✅| |
| resources |list of string|✅| |
| metric |string|✅| |
| start |string|✅| |
| end |string|✅| |
| period |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| stat |string|❌| |
| domain_id |string|✅| |

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
| data_source_id |string|✅| |
| resource_type |string|✅| |
| resources |list of string|✅| |
| domain_id |string|✅| |

### MetricsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| metrics |[list of MetricInfo](metric.md#metricinfo) | |
| available_resources |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
