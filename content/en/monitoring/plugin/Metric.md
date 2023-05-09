---
title: "Metric"
linkTitle: "Metric"
weight: 3
bookFlatSection: true
---
# [Metric](#Metric)
desc: A Metric is a monitoring metric data delivered from an external cloud service via a DataSource.


>  **Package : spaceone.api.monitoring.plugin**

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

desc: Gets a list of all Metrics from a specific cloud service. You can use the method to list up the Metrics to collect before using the `get_data` method to collect the Metrics.








    
<br>

### get_data

desc: Gets a Metric from a specific cloud service resource `instance`. By specifying the time period to collect the Metric, the Metric data value of the `instance` during the period is returned.








    


<br>
<br>

## Message



### MetricDataInfo
* **labels** (ListValue)  `Required` 

    
* **values** (Struct)  `Required` 

    <br>

### MetricDataRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **secret_data** (Struct)  `Required` 

  *is_required: true*

    
* **metric_query** (Struct)  `Required` 

  *is_required: true*

    
* **metric** (string)  `Required` 

  *is_required: true
desc: metric identifier in case of requested metric info is not a single.*

    
* **start** (string)  `Required` 

  *is_required: true*

    
* **end** (string)  `Required` 

  *is_required: true*

    
* **period** (int32)  `Required` 

  *is_required: false*

    
* **stat** (string)  `Required` 

  *is_required: false*

    
* **schema** (string)  `Required` 

  *is_required: false*

    <br>

### MetricInfo
* **key** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **group** (string)  `Required` 

    
* **unit** (Struct)  `Required` 

    
* **metric_query** (Struct)  `Required` 

    <br>

### MetricRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **secret_data** (Struct)  `Required` 

  *is_required: true*

    
* **query** (Struct)  `Required` 

  *is_required: true*

    
* **schema** (string)  `Required` 

  *is_required: false*

    <br>

### MetricsInfo
* **metrics** (MetricInfo)  `Required` 

    <br>
