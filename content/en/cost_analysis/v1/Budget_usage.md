---
title: "Budget_usage"
linkTitle: "Budget_usage"
weight: 3
bookFlatSection: true
---
# [Budget_usage](#Budget_usage)



>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## Budget_usage


**BudgetUsage Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./BudgetUsage#list) | [BudgetUsageQuery](BudgetUsage#budgetusagequery) | [BudgetUsagesInfo](./BudgetUsage#budgetusagesinfo) |
| [**analyze**](./BudgetUsage#analyze) | [BudgetUsageAnalyzeQuery](BudgetUsage#budgetusageanalyzequery) | [Struct](./BudgetUsage#struct) |
| [**stat**](./BudgetUsage#stat) | [BudgetUsageStatQuery](BudgetUsage#budgetusagestatquery) | [Struct](./BudgetUsage#struct) |



    
<br>

### list

> **POST** /cost-analysis/v1/budget-usage/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### analyze

> **POST** /cost-analysis/v1/budget-usage/analyze
>




 {{< tabs " analyze " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /cost-analysis/v1/budget-usage/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### BudgetUsageAnalyzeQuery
* **query** (TimeSeriesAnalyzeQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### BudgetUsageInfo
* **budget_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **date** (string)  `Required` 

    
* **usd_cost** (float)  `Required` 

    
* **limit** (float)  `Required` 

    
* **cost_types** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### BudgetUsageQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **budget_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **date** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### BudgetUsageStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### BudgetUsagesInfo
* **results** (BudgetUsageInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>
