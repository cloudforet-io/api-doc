---
title: "UnifiedCost"
linkTitle: "UnifiedCost"
weight: 3
bookFlatSection: true
---
# [UnifiedCost](#UnifiedCost)



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

    
* **exchange_date** (string)   `Required` 

    
* **exchange_source** (string)   `Required` 

  *ex). Yahoo Finance*

    
* **currency** (string)   `Required` 

    
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
