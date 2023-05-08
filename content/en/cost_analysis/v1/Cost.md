---
title: "Cost"
linkTitle: "Cost"
weight: 3
bookFlatSection: true
---
# [Cost](#Cost)
desc: A Cost is a resource of raw cost data collected by the cost_analysis.DataSource.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## Cost


**Cost Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Cost#create) | [CreateCostRequest](Cost#createcostrequest) | [CostInfo](./Cost#costinfo) |
| [**delete**](./Cost#delete) | [CostRequest](Cost#costrequest) | [Empty](./Cost#empty) |
| [**get**](./Cost#get) | [GetCostRequest](Cost#getcostrequest) | [CostInfo](./Cost#costinfo) |
| [**list**](./Cost#list) | [CostQuery](Cost#costquery) | [CostsInfo](./Cost#costsinfo) |
| [**analyze**](./Cost#analyze) | [CostAnalyzeQuery](Cost#costanalyzequery) | [Struct](./Cost#struct) |
| [**analyze_v2**](./Cost#analyze_v2) | [CostAnalyzeV2Query](Cost#costanalyzev2query) | [Struct](./Cost#struct) |
| [**stat**](./Cost#stat) | [CostStatQuery](Cost#coststatquery) | [Struct](./Cost#struct) |



    
<br>

### create

> **POST** /cost-analysis/v1/cost/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /cost-analysis/v1/cost/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /cost-analysis/v1/cost/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /cost-analysis/v1/cost/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### analyze

> **POST** /cost-analysis/v1/cost/analyze
>




 {{< tabs " analyze " >}}




{{< /tabs >}}

    
<br>

### analyze_v2

> **POST** /cost-analysis/v1/cost/analyze-v2
>




 {{< tabs " analyze_v2 " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /cost-analysis/v1/cost/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CostAnalyzeQuery
* **granularity** (Granularity)  `Required` 

  *is_required: true*

    
* **start** (string)  `Required` 

  *is_required: true*

    
* **end** (string)  `Required` 

  *is_required: true*

    
* **group_by** (string)  `Required` 

  *is_required: false*

    
* **filter** (ListValue)  `Required` 

  *is_required: false*

    
* **limit** (int32)  `Required` 

  *is_required: false*

    
* **page** (Page)  `Required` 

  *is_required: false*

    
* **sort** (Sort)  `Required` 

  *is_required: false*

    
* **include_usage_quantity** (bool)  `Required` 

  *is_required: false*

    
* **include_others** (bool)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CostAnalyzeV2Query
* **query** (TimeSeriesAnalyzeQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CostInfo
* **cost_id** (string)  `Required` 

    
* **usd_cost** (float)  `Required` 

    
* **original_currency** (string)  `Required` 

    
* **original_cost** (float)  `Required` 

    
* **usage_quantity** (float)  `Required` 

    
* **provider** (string)  `Required` 

    
* **region_code** (string)  `Required` 

    
* **region_key** (string)  `Required` 

    
* **category** (string)  `Required` 

    
* **product** (string)  `Required` 

    
* **account** (string)  `Required` 

    
* **usage_type** (string)  `Required` 

    
* **resource_group** (string)  `Required` 

    
* **resource** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **additional_info** (Struct)  `Required` 

    
* **service_account_id** (string)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **data_source_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **billed_at** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### CostQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **cost_id** (string)  `Required` 

  *is_required: false*

    
* **original_currency** (string)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **region_code** (string)  `Required` 

  *is_required: false*

    
* **region_key** (string)  `Required` 

  *is_required: false*

    
* **category** (string)  `Required` 

  *is_required: false*

    
* **product** (string)  `Required` 

  *is_required: false*

    
* **account** (string)  `Required` 

  *is_required: false*

    
* **usage_type** (string)  `Required` 

  *is_required: false*

    
* **resource_group** (string)  `Required` 

  *is_required: false*

    
* **resource** (string)  `Required` 

  *is_required: false*

    
* **service_account_id** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **data_source_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CostRequest
* **cost_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CostStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CostsInfo
* **results** (CostInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CreateCostRequest
* **original_cost** (float)  `Required` 

  *is_required: true*

    
* **original_currency** (string)  `Required` 

  *is_required: true*

    
* **usd_cost** (float)  `Required` 

  *is_required: false*

    
* **usage_quantity** (float)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **region_code** (string)  `Required` 

  *is_required: false*

    
* **category** (string)  `Required` 

  *is_required: false*

    
* **product** (string)  `Required` 

  *is_required: false*

    
* **account** (string)  `Required` 

  *is_required: false*

    
* **usage_type** (string)  `Required` 

  *is_required: false*

    
* **resource_group** (string)  `Required` 

  *is_required: false*

    
* **resource** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **additional_info** (Struct)  `Required` 

  *is_required: false*

    
* **service_account_id** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **data_source_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **billed_at** (string)  `Required` 

  *is_required: false*

    <br>

### GetCostRequest
* **cost_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>
