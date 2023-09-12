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


* **data_source_id** (string)  


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
               "cost": 7671.164,
               "limit": 10000.0,
               "currency": "USD",
               "provider_filter": {
                   "state": "ENABLED",
                   "providers": [
                       "aws",
                       "google_cloud"
                   ]
               },
               "project_id": "project-1b2b3b4b5b6b",
               "data_source_id": "data-source-1b2b3b4b5b6b",
               "domain_id": "domain-58010aa2e451",
               "updated_at": "2022-07-19T04:26:08.099Z"
           },
           {
               "budget_id": "budget-abb377eb9e8b",
               "name": "Cloudforet-Budget3",
               "date": "2022-02",
               "cost": 5931.771,
               "limit": 11000.0,
               "currency": "USD",
               "provider_filter": {
                   "state": "DISABLED",
                   "providers": []
               },
               "project_id": "project-1b2b3b4b5b6b",
               "data_source_id": "data-source-1b2b3b4b5b6b",
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

    
* **budget_id** (string)  

    
* **data_source_id** (string)  

    <br>

### BudgetUsageInfo
* **budget_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **date** (string)   `Required` 

    
* **cost** (float)   `Required` 

    
* **limit** (float)   `Required` 

    
* **currency** (string)   `Required` 

    
* **provider_filter** (BudgetUsageProviderFilter)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **project_group_id** (string)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### BudgetUsageProviderFilter
* **state** (State)   `Required` 

    
* **providers** (string)  `Repeated`    `Required` 

    <br>

### BudgetUsageQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **budget_id** (string)  

    
* **data_source_id** (string)  

    
* **name** (string)  

    
* **date** (string)  

    <br>

### BudgetUsageStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **budget_id** (string)  

    
* **data_source_id** (string)  

    <br>

### BudgetUsagesInfo
* **results** (BudgetUsageInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
