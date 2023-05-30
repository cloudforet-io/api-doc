---
title: "Metric"
linkTitle: "Metric"
weight: 3
bookFlatSection: true
---
# [Metric](#Metric)
A Metric is a monitoring metric of a specific cloud service delivered from a DataSource.


>  **Package : spaceone.api.monitoring.v1**

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

Gets a list of all Metrics of one or more specified Resources. The parameter `resources` is a list of Resources from which to get a list of Metrics collected.



> **POST** /monitoring/v1/metric/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[MetricRequest](./Metric#metricrequest)

* **data_source_id** (string)   `Required` 


* **resources** (string)  `Repeated`    `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "data_source_id": "ds-31190a65a42a",
   "resources": ["cloud-svc-cd0105d255da"],
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[MetricsInfo](#METRICSINFO)
* **metrics** (MetricInfo)  `Repeated`   `Required` 

* **available_resources** (Struct)   `Required` 

* **domain_id** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get_data

Gets data of a single Metric. You must specify the parameter `metric` to get data of. You can specify the `period` to get data for.



> **POST** /monitoring/v1/metric/get-data
>





 {{< tabs " get_data " >}}

 {{< tab "Request Example" >}}



[MetricDataRequest](./Metric#metricdatarequest)

* **data_source_id** (string)   `Required` 


* **metric_query** (Struct)   `Required` 


* **metric** (string)   `Required` 


* **start** (string)   `Required` 


* **end** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **period** (int32)  


* **stat** (string)  





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[MetricDataInfo](#METRICDATAINFO)
* **labels** (ListValue)   `Required` 

* **values** (Struct)   `Required` 

* **domain_id** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    


<br>
<br>

## Message



### MetricDataInfo
* **labels** (ListValue)   `Required` 

    
* **values** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### MetricDataRequest
* **data_source_id** (string)   `Required` 

    
* **metric_query** (Struct)   `Required` 

    
* **metric** (string)   `Required` 

    
* **start** (string)   `Required` 

    
* **end** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **period** (int32)  

    
* **stat** (string)  

    <br>

### MetricInfo
* **key** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **group** (string)   `Required` 

    
* **unit** (Struct)   `Required` 

    
* **metric_query** (Struct)   `Required` 

    <br>

### MetricRequest
* **data_source_id** (string)   `Required` 

    
* **resources** (string)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### MetricsInfo
* **metrics** (MetricInfo)  `Repeated`    `Required` 

    
* **available_resources** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>
