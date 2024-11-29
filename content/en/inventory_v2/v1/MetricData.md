---
title: "MetricData"
linkTitle: "MetricData"
weight: 3
bookFlatSection: true
---
# [MetricData](#MetricData)



>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## MetricData





**MetricData Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./MetricData#list) | [MetricDataQuery](MetricData#metricdataquery) | [MetricDatasInfo](MetricData#metricdatasinfo) |
| [**stat**](./MetricData#stat) | [MetricDataStatQuery](MetricData#metricdatastatquery) | [Struct](MetricData#struct) |
| [**analyze**](./MetricData#analyze) | [MetricDataAnalyzeQuery](MetricData#metricdataanalyzequery) | [Struct](MetricData#struct) |



    
<br>

### list





> **POST** /inventory-v2/v1/metric-data/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[MetricDataQuery](./MetricData#metricdataquery)

* **metric_id** (string)   `Required` 


* **query** (Query)  


* **workspace_id** (string)  


* **project_id** (string)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### stat





> **POST** /inventory-v2/v1/metric-data/stat
>






    
<br>

### analyze





> **POST** /inventory-v2/v1/metric-data/analyze
>






    


<br>
<br>

## Message



### MetricDataAnalyzeQuery
* **query** (TimeSeriesAnalyzeQuery)   `Required` 

    
* **metric_id** (string)   `Required` 

    <br>

### MetricDataInfo
* **metric_id** (string)   `Required` 

    
* **value** (float)   `Required` 

    
* **unit** (string)   `Required` 

    
* **labels** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **service_account_id** (string)   `Required` 

    
* **namespace_id** (string)   `Required` 

    
* **created_year** (string)   `Required` 

    
* **created_month** (string)   `Required` 

    
* **created_date** (string)   `Required` 

    <br>

### MetricDataQuery
* **metric_id** (string)   `Required` 

    
* **query** (Query)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### MetricDataStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **metric_id** (string)  

    <br>

### MetricDatasInfo
* **results** (MetricDataInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
