---
title: "Metric"
linkTitle: "Metric"
weight: 3
bookFlatSection: true
---
# [Metric](#Metric)
desc: A Metric is a monitoring metric of a specific cloud service delivered from a DataSource.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Metric





**Metric Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./Metric#list) | [MetricRequest](Metric#metricrequest) | [MetricsInfo](./Metric#metricsinfo) |
| [**get_data**](./Metric#get_data) | [MetricDataRequest](Metric#metricdatarequest) | [MetricDataInfo](./Metric#metricdatainfo) |



    
<br>

### list

desc: Gets a list of all Metrics of one or more specified Resources. The parameter `resources` is a list of Resources from which to get a list of Metrics collected.
request_example: >-
{
"data_source_id": "ds-31190a65a42a",
"resources": ["cloud-svc-cd0105d255da"],
"domain_id": "domain-58010aa2e451"
}
response_example: >-
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



> **POST** /monitoring/v1/metric/list
>






    
<br>

### get_data

desc: Gets data of a single Metric. You must specify the parameter `metric` to get data of. You can specify the `period` to get data for.
request_example: >-
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
response_example: >-
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



> **POST** /monitoring/v1/metric/get-data
>






    


<br>
<br>

## Message



### MetricDataInfo
* **labels** (ListValue)  `Required` 

    
* **values** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### MetricDataRequest
* **data_source_id** (string)  `Required` 

  *is_required: true*

    
* **metric_query** (Struct)  `Required` 

  *is_required: true*

    
* **metric** (string)  `Required` 

  *is_required: true*

    
* **start** (string)  `Required` 

  *is_required: true*

    
* **end** (string)  `Required` 

  *is_required: true*

    
* **period** (int32)  `Required` 

  *is_required: false*

    
* **stat** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### MetricInfo
* **key** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **group** (string)  `Required` 

    
* **unit** (Struct)  `Required` 

    
* **metric_query** (Struct)  `Required` 

    <br>

### MetricRequest
* **data_source_id** (string)  `Required` 

  *is_required: true*

    
* **resources** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### MetricsInfo
* **metrics** (MetricInfo)  `Required` 

    
* **available_resources** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>
