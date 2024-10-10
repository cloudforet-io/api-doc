---
title: "UnifiedCost"
linkTitle: "UnifiedCost"
weight: 3
bookFlatSection: true
---
# [UnifiedCost](#UnifiedCost)
Unified Cost service is a service that provides unified cost based on the cost data from various DataSources registered in each domain.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## UnifiedCost





**UnifiedCost Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get**](./UnifiedCost#get) | [UnifiedCostRequest](UnifiedCost#unifiedcostrequest) | [UnifiedCostInfo](UnifiedCost#unifiedcostinfo) |
| [**list**](./UnifiedCost#list) | [UnifiedCostQuery](UnifiedCost#unifiedcostquery) | [UnifiedCostsInfo](UnifiedCost#unifiedcostsinfo) |
| [**analyze**](./UnifiedCost#analyze) | [UnifiedCostAnalyzeQuery](UnifiedCost#unifiedcostanalyzequery) | [Struct](UnifiedCost#struct) |
| [**stat**](./UnifiedCost#stat) | [UnifiedCostStatQuery](UnifiedCost#unifiedcoststatquery) | [Struct](UnifiedCost#struct) |



    
<br>

### get





> **POST** /cost-analysis/v1/unified-cost/get
>





 {{< tabs " get " >}}



 {{< tab "Response Example" >}}

[UnifiedCostInfo](#UNIFIEDCOSTINFO)
* **unified_cost_id** (string)   `Required` 

* **cost** (Struct)   `Required` 

* **billed_month** (string)   `Required` 

  ex). 2021-01

* **billed_year** (string)   `Required` 

  ex). 2021

* **aggregation_date** (string)   `Required` 

  ex). 2021-01-01

* **exchange_date** (string)   `Required` 

* **exchange_source** (string)   `Required` 

  ex). Yahoo Finance

* **currency** (string)   `Required` 

  Original currency of cost

* **is_confirmed** (bool)   `Required` 

* **provider** (string)   `Required` 

* **region_code** (string)   `Required` 

* **region_key** (string)   `Required` 

* **product** (string)   `Required` 

* **usage_type** (string)   `Required` 

* **usage_unit** (string)   `Required` 

* **service_account_name** (string)   `Required` 

* **data_source_name** (string)   `Required` 

* **project_name** (string)   `Required` 

* **workspace_name** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **data_source_id** (string)   `Required` 

* **service_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
 "unified_cost_id": "unified-cost-11153fceca11",
 "cost": {
   "KRW": 13000,
   "USD": 1,
   "JPY": 100
 },
 "billed_month": "2024-08",
 "billed_year": "2024",
 "exchange_date": "2024-08-14",
 "exchange_source": "Yahoo Finance!",
 "aggregation_date": "2024-08-15",
 "currency": "USD",
 "is_confirmed": true,
 "provider": "aws",
 "region_code": "AP2",
 "region_key": "aws.AP2",
 "product": "AmazonS3",
 "data_source_name": "AWS",
 "workspace_name": "SpaceONE",
 "data_source_id": "ds-1acca85666c1",
 "project_id": project-1acca85666c1,
 "workspace_id": "workspace-1acca85666c1",
 "domain_id": "domain-1acca85666c1",
 "created_at": "2024-09-30T08:00:03.945Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /cost-analysis/v1/unified-cost/list
>






    
<br>

### analyze





> **POST** /cost-analysis/v1/unified-cost/analyze
>






    
<br>

### stat





> **POST** /cost-analysis/v1/unified-cost/stat
>






    


<br>
<br>

## Message



### UnifiedCostAnalyzeQuery
* **query** (TimeSeriesAnalyzeQuery)   `Required` 

    
* **is_confirmed** (bool)   `Required` 

    <br>

### UnifiedCostInfo
* **unified_cost_id** (string)   `Required` 

    
* **cost** (Struct)   `Required` 

    
* **billed_month** (string)   `Required` 

  *ex). 2021-01*

    
* **billed_year** (string)   `Required` 

  *ex). 2021*

    
* **aggregation_date** (string)   `Required` 

  *ex). 2021-01-01*

    
* **exchange_date** (string)   `Required` 

    
* **exchange_source** (string)   `Required` 

  *ex). Yahoo Finance*

    
* **currency** (string)   `Required` 

  *Original currency of cost*

    
* **is_confirmed** (bool)   `Required` 

    
* **provider** (string)   `Required` 

    
* **region_code** (string)   `Required` 

    
* **region_key** (string)   `Required` 

    
* **product** (string)   `Required` 

    
* **usage_type** (string)   `Required` 

    
* **usage_unit** (string)   `Required` 

    
* **service_account_name** (string)   `Required` 

    
* **data_source_name** (string)   `Required` 

    
* **project_name** (string)   `Required` 

    
* **workspace_name** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **service_account_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### UnifiedCostQuery
* **query** (Query)  

    
* **unified_cost_id** (string)  

    <br>

### UnifiedCostRequest
* **unified_cost_id** (string)   `Required` 

    <br>

### UnifiedCostStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### UnifiedCostsInfo
* **results** (UnifiedCostInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
