---
description: A Metric is a monitoring metric of a specific cloud service delivered from a DataSource.
---
# Metric

>  **Package : spaceone.api.monitoring.v1**

## Metric

{% hint style="info" %}
**Metric Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](metric.md#list)|   [MetricRequest](metric.md#metricrequest) |   [MetricsInfo](metric.md#metricsinfo) |
| [**get_data**](metric.md#get_data)|   [MetricDataRequest](metric.md#metricdatarequest) |   [MetricDataInfo](metric.md#metricdatainfo) | 
 

 
### list
> **POST** /monitoring/v1/metric/list
>

> Gets a list of all Metrics of one or more specified Resources. The parameter `resources` is a list of Resources from which to get a list of Metrics collected.

| Type | Message |
| :--- | :--- |
| Request | [MetricRequest](metric.md#metricrequest) |
| Response |  [MetricsInfo](metric.md#metricsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "data_source_id": "ds-31190a65a42a",
    "resources": [
        "cloud-svc-cd0105d255da"
    ],
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "metrics": [
        {
            "key": "CPUUtilization",
            "group": "AWS/EC2",
            "name": "CPUUtilization",
            "unit": {
                "y": "Percent",
                "x": "Timestamp"
            },
            "metric_query": {
                "cloud-svc-cd0105d255da": {
                    "Dimensions": [
                        {
                            "Name": "InstanceId",
                            "Value": "i-0400cdd39f1a4d5e9"
                        }
                    ],
                    "MetricName": "CPUUtilization",
                    "Namespace": "AWS/EC2"
                }
            }
        },
        {
            "key": "NetworkIn",
            "group": "AWS/EC2",
            "name": "NetworkIn",
            "unit": {
                "y": "Bytes",
                "x": "Timestamp"
            },
            "metric_query": {
                "cloud-svc-cd0105d255da": {
                    "Dimensions": [
                        {
                            "Name": "InstanceId",
                            "Value": "i-0400cdd39f1a4d5e9"
                        }
                    ],
                    "MetricName": "NetworkIn",
                    "Namespace": "AWS/EC2"
                }
            }
        }
    ],
    "available_resources": {
        "cloud-svc-cd0105d255da": true
    },
    "domain_id": "domain-31190a65a42a"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get_data
> **POST** /monitoring/v1/metric/get-data
>

> Gets data of a single Metric. You must specify the parameter `metric` to get data of. You can specify the `period` to get data for.

| Type | Message |
| :--- | :--- |
| Request | [MetricDataRequest](metric.md#metricdatarequest) |
| Response |  [MetricDataInfo](metric.md#metricdatainfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "data_source_id": "ds-31190a65a42a",
    "metric_query": {
        "cloud-svc-cd0105d255da": {
            "Dimensions": [
                {
                    "Name": "InstanceId",
                    "Value": "i-0400cdd39f1a4d5e9"
                }
            ],
            "MetricName": "CPUUtilization",
            "Namespace": "AWS/EC2"
        }
    },
    "metric": "CPUUtilization",
    "start": "2022-06-21T03:11:29.438Z",
    "end": "2022-06-21T04:11:29.438Z",
    "stat": "AVERAGE",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "labels": [
        "2022-06-21T03:13:00.000Z",
        "2022-06-21T03:18:00.000Z",
        "2022-06-21T03:23:00.000Z",
        "2022-06-21T03:28:00.000Z",
        "2022-06-21T03:33:00.000Z",
        "2022-06-21T03:38:00.000Z",
        "2022-06-21T03:43:00.000Z",
        "2022-06-21T03:48:00.000Z",
        "2022-06-21T03:53:00.000Z",
        "2022-06-21T03:58:00.000Z",
        "2022-06-21T04:03:00.000Z",
        "2022-06-21T04:08:00.000Z"
    ],
    "resource_values": {
        "cloud-svc-cd0105d255da": [
            0.099999999999999,
            0.10001852366397981,
            0.10001852366397981,
            0.1328230362675432,
            0.099472075576548,
            0.06507936507936621,
            0.166703713994628,
            0.1338983050847476,
            0.1327868852458988,
            0.1339168287487284,
            0.1328610417160508,
            0.10056497175141618
        ]
    },
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}
{% endtabs %}


## 

## Message

### MetricDataInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| values |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |

### MetricDataRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_id |string|✔| |
| metric_query |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| metric |string|✔| |
| start |string|✔| |
| end |string|✔| |
| period |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✘| |
| stat |string|✘| |
| domain_id |string|✔| |

### MetricInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| name |string | |
| group |string | |
| unit |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| metric_query |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### MetricRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_id |string|✔| |
| resources |list of string|✔| |
| domain_id |string|✔| |

### MetricsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| metrics |[list of MetricInfo](metric.md#metricinfo) | |
| available_resources |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
