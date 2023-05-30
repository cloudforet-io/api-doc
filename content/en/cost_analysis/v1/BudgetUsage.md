---
title: "BudgetUsage"
linkTitle: "BudgetUsage"
weight: 3
bookFlatSection: true
---
# [BudgetUsage](#BudgetUsage)



>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## BudgetUsage





**BudgetUsage Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./BudgetUsage#list) | [BudgetUsageQuery](BudgetUsage#budgetusagequery) | [BudgetUsagesInfo](BudgetUsage#budgetusagesinfo) |
| [**analyze**](./BudgetUsage#analyze) | [BudgetUsageAnalyzeQuery](BudgetUsage#budgetusageanalyzequery) | [Struct](BudgetUsage#struct) |
| [**stat**](./BudgetUsage#stat) | [BudgetUsageStatQuery](BudgetUsage#budgetusagestatquery) | [Struct](BudgetUsage#struct) |



    
<br>

### list

Gets a list of all BudgetUsages. You can use a query to get a filtered list of BudgetUsages.



> **POST** /cost-analysis/v1/budget-usage/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[BudgetUsageQuery](./BudgetUsage#budgetusagequery)

* **domain_id** (string)   `Required` 


* **query** (Query)  


* **budget_id** (string)  


* **name** (string)  


* **date** (string)  





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[BudgetUsagesInfo](#BUDGETUSAGESINFO)
* **results** (BudgetUsageInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
       "results": [
           {
               "budget_id": "budget-abb377eb9e8b",
               "name": "Cloudforet-Budget3",
               "date": "2022-01",
               "usd_cost": 7671.164,
               "limit": 10000.0,
               "domain_id": "domain-58010aa2e451",
               "updated_at": "2022-07-19T04:26:08.099Z"
           },
           {
               "budget_id": "budget-abb377eb9e8b",
               "name": "Cloudforet-Budget3",
               "date": "2022-02",
               "usd_cost": 5931.771,
               "limit": 11000.0,
               "domain_id": "domain-58010aa2e451",
               "updated_at": "2022-07-19T04:26:08.105Z"
           }
       ],
       "total_count": 12
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### analyze





> **POST** /cost-analysis/v1/budget-usage/analyze
>






    
<br>

### stat





> **POST** /cost-analysis/v1/budget-usage/stat
>






    


<br>
<br>

## Message



### BudgetUsageAnalyzeQuery
* **query** (TimeSeriesAnalyzeQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### BudgetUsageInfo
* **budget_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **date** (string)   `Required` 

    
* **usd_cost** (float)   `Required` 

    
* **limit** (float)   `Required` 

    
* **cost_types** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### BudgetUsageQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **budget_id** (string)  

    
* **name** (string)  

    
* **date** (string)  

    <br>

### BudgetUsageStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### BudgetUsagesInfo
* **results** (BudgetUsageInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
