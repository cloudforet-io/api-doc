---
title: "MetricExample"
linkTitle: "MetricExample"
weight: 3
bookFlatSection: true
---
# [MetricExample](#MetricExample)



>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## MetricExample





**MetricExample Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./MetricExample#create) | [CreateMetricExampleRequest](MetricExample#createmetricexamplerequest) | [MetricExampleInfo](MetricExample#metricexampleinfo) |
| [**update**](./MetricExample#update) | [UpdateMetricExampleRequest](MetricExample#updatemetricexamplerequest) | [MetricExampleInfo](MetricExample#metricexampleinfo) |
| [**delete**](./MetricExample#delete) | [MetricExampleRequest](MetricExample#metricexamplerequest) | [Empty](MetricExample#empty) |
| [**get**](./MetricExample#get) | [MetricExampleRequest](MetricExample#metricexamplerequest) | [MetricExampleInfo](MetricExample#metricexampleinfo) |
| [**list**](./MetricExample#list) | [MetricExampleQuery](MetricExample#metricexamplequery) | [MetricExamplesInfo](MetricExample#metricexamplesinfo) |
| [**stat**](./MetricExample#stat) | [MetricExampleStatQuery](MetricExample#metricexamplestatquery) | [Struct](MetricExample#struct) |



    
<br>

### create





> **POST** /inventory/v1/metric-example/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateMetricExampleRequest](./MetricExample#createmetricexamplerequest)

* **metric_id** (string)   `Required` 


* **name** (string)   `Required` 


* **options** (Struct)   `Required` 


* **tags** (Struct)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[MetricExampleInfo](#METRICEXAMPLEINFO)
* **example_id** (string)   `Required` 

* **name** (string)   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **metric_id** (string)   `Required` 

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





> **POST** /inventory/v1/metric-example/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateMetricExampleRequest](./MetricExample#updatemetricexamplerequest)

* **example_id** (string)   `Required` 


* **name** (string)  


* **options** (Struct)  


* **tags** (Struct)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[MetricExampleInfo](#METRICEXAMPLEINFO)
* **example_id** (string)   `Required` 

* **name** (string)   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **metric_id** (string)   `Required` 

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





> **POST** /inventory/v1/metric-example/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[MetricExampleRequest](./MetricExample#metricexamplerequest)

* **example_id** (string)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /inventory/v1/metric-example/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[MetricExampleRequest](./MetricExample#metricexamplerequest)

* **example_id** (string)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[MetricExampleInfo](#METRICEXAMPLEINFO)
* **example_id** (string)   `Required` 

* **name** (string)   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **metric_id** (string)   `Required` 

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





> **POST** /inventory/v1/metric-example/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[MetricExampleQuery](./MetricExample#metricexamplequery)

* **query** (Query)  


* **example_id** (string)  


* **name** (string)  


* **metric_id** (string)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### stat





> **POST** /inventory/v1/metric-example/stat
>






    


<br>
<br>

## Message



### CreateMetricExampleRequest
* **metric_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)  

    <br>

### MetricExampleInfo
* **example_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **metric_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### MetricExampleQuery
* **query** (Query)  

    
* **example_id** (string)  

    
* **name** (string)  

    
* **metric_id** (string)  

    <br>

### MetricExampleRequest
* **example_id** (string)   `Required` 

    <br>

### MetricExampleStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### MetricExamplesInfo
* **results** (MetricExampleInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateMetricExampleRequest
* **example_id** (string)   `Required` 

    
* **name** (string)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>
