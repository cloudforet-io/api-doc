---
title: "Metric"
linkTitle: "Metric"
weight: 3
bookFlatSection: true
---
# [Metric](#Metric)
A Metric is a monitoring metric data delivered from an external cloud service via a DataSource.


>  **Package : spaceone.api.monitoring.plugin**

<br>
<br>

## Metric





**Metric Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./Metric#list) | [MetricRequest](Metric#metricrequest) | [MetricsInfo](Metric#metricsinfo) |
| [**get_data**](./Metric#get_data) | [MetricDataRequest](Metric#metricdatarequest) | [MetricDataInfo](Metric#metricdatainfo) |



    
<br>

### list

Gets a list of all Metrics from a specific cloud service. You can use the method to list up the Metrics to collect before using the `get_data` method to collect the Metrics.








    
<br>

### get_data

Gets a Metric from a specific cloud service resource `instance`. By specifying the time period to collect the Metric, the Metric data value of the `instance` during the period is returned.








    


<br>
<br>

## Message



### MetricDataInfo
* **labels** (ListValue)   `Required` 

    
* **values** (Struct)   `Required` 

    <br>

### MetricDataRequest
* **options** (Struct)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **metric_query** (Struct)   `Required` 

    
* **metric** (string)   `Required` 

  *metric identifier in case of requested metric info is not a single.*

    
* **start** (string)   `Required` 

    
* **end** (string)   `Required` 

    
* **period** (int32)  

    
* **stat** (string)  

    
* **schema** (string)  

    <br>

### MetricInfo
* **key** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **group** (string)   `Required` 

    
* **unit** (Struct)   `Required` 

    
* **metric_query** (Struct)   `Required` 

    <br>

### MetricRequest
* **options** (Struct)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **query** (Struct)   `Required` 

    
* **schema** (string)  

    <br>

### MetricsInfo
* **metrics** (MetricInfo)  `Repeated`    `Required` 

    <br>
