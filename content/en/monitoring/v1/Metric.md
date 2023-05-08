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

> **POST** /monitoring/v1/metric/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### get_data

> **POST** /monitoring/v1/metric/get-data
>




 {{< tabs " get_data " >}}




{{< /tabs >}}

    


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
