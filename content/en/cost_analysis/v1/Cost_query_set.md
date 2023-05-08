---
title: "Cost_query_set"
linkTitle: "Cost_query_set"
weight: 3
bookFlatSection: true
---
# [Cost_query_set](#Cost_query_set)
desc: A CostQuerySet is a set of saved queries a User frequently uses as a setting.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## Cost_query_set


**CostQuerySet Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CostQuerySet#create) | [CreateCostQuerySetRequest](CostQuerySet#createcostquerysetrequest) | [CostQuerySetInfo](./CostQuerySet#costquerysetinfo) |
| [**update**](./CostQuerySet#update) | [UpdateCostQuerySetRequest](CostQuerySet#updatecostquerysetrequest) | [CostQuerySetInfo](./CostQuerySet#costquerysetinfo) |
| [**delete**](./CostQuerySet#delete) | [CostQuerySetRequest](CostQuerySet#costquerysetrequest) | [Empty](./CostQuerySet#empty) |
| [**get**](./CostQuerySet#get) | [GetCostQuerySetRequest](CostQuerySet#getcostquerysetrequest) | [CostQuerySetInfo](./CostQuerySet#costquerysetinfo) |
| [**list**](./CostQuerySet#list) | [CostQuerySetQuery](CostQuerySet#costquerysetquery) | [CostQuerySetsInfo](./CostQuerySet#costquerysetsinfo) |
| [**stat**](./CostQuerySet#stat) | [CostQuerySetStatQuery](CostQuerySet#costquerysetstatquery) | [Struct](./CostQuerySet#struct) |



    
<br>

### create

> **POST** /cost-analysis/v1/cost-query-set/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /cost-analysis/v1/cost-query-set/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /cost-analysis/v1/cost-query-set/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /cost-analysis/v1/cost-query-set/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /cost-analysis/v1/cost-query-sets/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /cost-analysis/v1/cost-query-sets/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CostQuerySetInfo
* **cost_query_set_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **user_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### CostQuerySetQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **cost_query_set_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CostQuerySetRequest
* **cost_query_set_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CostQuerySetStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CostQuerySetsInfo
* **results** (CostQuerySetInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CreateCostQuerySetRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetCostQuerySetRequest
* **cost_query_set_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### UpdateCostQuerySetRequest
* **cost_query_set_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **options** (Struct)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
