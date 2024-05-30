---
title: "Metric"
linkTitle: "Metric"
weight: 3
bookFlatSection: true
---
# [Metric](#Metric)



>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Metric





**Metric Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Metric#create) | [CreateMetricRequest](Metric#createmetricrequest) | [MetricInfo](Metric#metricinfo) |
| [**update**](./Metric#update) | [UpdateMetricRequest](Metric#updatemetricrequest) | [MetricInfo](Metric#metricinfo) |
| [**delete**](./Metric#delete) | [MetricRequest](Metric#metricrequest) | [Empty](Metric#empty) |
| [**run**](./Metric#run) | [MetricRequest](Metric#metricrequest) | [Empty](Metric#empty) |
| [**test**](./Metric#test) | [MetricTestRequest](Metric#metrictestrequest) | [Struct](Metric#struct) |
| [**get**](./Metric#get) | [MetricRequest](Metric#metricrequest) | [MetricInfo](Metric#metricinfo) |
| [**list**](./Metric#list) | [MetricQuery](Metric#metricquery) | [MetricsInfo](Metric#metricsinfo) |
| [**stat**](./Metric#stat) | [MetricStatQuery](Metric#metricstatquery) | [Struct](Metric#struct) |



    
<br>

### create





> **POST** /inventory/v1/metric/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateMetricRequest](./Metric#createmetricrequest)

* **name** (string)   `Required` 


* **metric_type** (MetricType)   `Required` 


* **resource_type** (string)   `Required` 


* **query_options** (AnalyzeQuery)   `Required` 


* **namespace_id** (string)   `Required` 


* **resource_group** (ResourceGroup)   `Required` 


* **metric_id** (string)  


* **date_field** (string)  


* **unit** (string)  


* **tags** (Struct)  


* **workspace_id** (string)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[MetricInfo](#METRICINFO)
* **metric_id** (string)   `Required` 

* **name** (string)   `Required` 

* **metric_type** (MetricType)   `Required` 

* **resource_type** (string)   `Required` 

* **query_options** (AnalyzeQuery)   `Required` 

* **date_field** (string)   `Required` 

* **unit** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **labels_info** (Struct)  `Repeated`   `Required` 

* **is_managed** (bool)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **namespace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update





> **POST** /inventory/v1/metric/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateMetricRequest](./Metric#updatemetricrequest)

* **metric_id** (string)   `Required` 


* **name** (string)  


* **query_options** (AnalyzeQuery)  


* **date_field** (string)  


* **unit** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[MetricInfo](#METRICINFO)
* **metric_id** (string)   `Required` 

* **name** (string)   `Required` 

* **metric_type** (MetricType)   `Required` 

* **resource_type** (string)   `Required` 

* **query_options** (AnalyzeQuery)   `Required` 

* **date_field** (string)   `Required` 

* **unit** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **labels_info** (Struct)  `Repeated`   `Required` 

* **is_managed** (bool)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **namespace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /inventory/v1/metric/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[MetricRequest](./Metric#metricrequest)

* **metric_id** (string)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### run





> **POST** /inventory/v1/metric/run
>





 {{< tabs " run " >}}

 {{< tab "Request Example" >}}



[MetricRequest](./Metric#metricrequest)

* **metric_id** (string)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### test





> **POST** /inventory/v1/metric/test
>





 {{< tabs " test " >}}

 {{< tab "Request Example" >}}



[MetricTestRequest](./Metric#metrictestrequest)

* **metric_id** (string)   `Required` 


* **query_options** (AnalyzeQuery)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /inventory/v1/metric/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[MetricRequest](./Metric#metricrequest)

* **metric_id** (string)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[MetricInfo](#METRICINFO)
* **metric_id** (string)   `Required` 

* **name** (string)   `Required` 

* **metric_type** (MetricType)   `Required` 

* **resource_type** (string)   `Required` 

* **query_options** (AnalyzeQuery)   `Required` 

* **date_field** (string)   `Required` 

* **unit** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **labels_info** (Struct)  `Repeated`   `Required` 

* **is_managed** (bool)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **namespace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /inventory/v1/metric/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[MetricQuery](./Metric#metricquery)

* **query** (Query)  


* **metric_id** (string)  


* **metric_type** (MetricType)  


* **resource_type** (string)  


* **is_managed** (string)  


* **workspace_id** (string)  


* **namespace_id** (string)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### stat





> **POST** /inventory/v1/metric/stat
>






    


<br>
<br>

## Message



### CreateMetricRequest
* **name** (string)   `Required` 

    
* **metric_type** (MetricType)   `Required` 

    
* **resource_type** (string)   `Required` 

    
* **query_options** (AnalyzeQuery)   `Required` 

    
* **namespace_id** (string)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **metric_id** (string)  

    
* **date_field** (string)  

    
* **unit** (string)  

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    <br>

### MetricInfo
* **metric_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **metric_type** (MetricType)   `Required` 

    
* **resource_type** (string)   `Required` 

    
* **query_options** (AnalyzeQuery)   `Required` 

    
* **date_field** (string)   `Required` 

    
* **unit** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **labels_info** (Struct)  `Repeated`    `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **namespace_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### MetricQuery
* **query** (Query)  

    
* **metric_id** (string)  

    
* **metric_type** (MetricType)  

    
* **resource_type** (string)  

    
* **is_managed** (string)  

    
* **workspace_id** (string)  

    
* **namespace_id** (string)  

    <br>

### MetricRequest
* **metric_id** (string)   `Required` 

    <br>

### MetricStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### MetricTestRequest
* **metric_id** (string)   `Required` 

    
* **query_options** (AnalyzeQuery)   `Required` 

    <br>

### MetricsInfo
* **results** (MetricInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateMetricRequest
* **metric_id** (string)   `Required` 

    
* **name** (string)  

    
* **query_options** (AnalyzeQuery)  

    
* **date_field** (string)  

    
* **unit** (string)  

    
* **tags** (Struct)  

    <br>
