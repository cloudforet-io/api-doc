---
title: "CostQuerySet"
linkTitle: "CostQuerySet"
weight: 3
bookFlatSection: true
---
# [CostQuerySet](#CostQuerySet)
A CostQuerySet is a set of saved queries a User frequently uses as a setting.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## CostQuerySet





**CostQuerySet Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CostQuerySet#create) | [CreateCostQuerySetRequest](CostQuerySet#createcostquerysetrequest) | [CostQuerySetInfo](CostQuerySet#costquerysetinfo) |
| [**update**](./CostQuerySet#update) | [UpdateCostQuerySetRequest](CostQuerySet#updatecostquerysetrequest) | [CostQuerySetInfo](CostQuerySet#costquerysetinfo) |
| [**delete**](./CostQuerySet#delete) | [CostQuerySetRequest](CostQuerySet#costquerysetrequest) | [Empty](CostQuerySet#empty) |
| [**get**](./CostQuerySet#get) | [CostQuerySetRequest](CostQuerySet#costquerysetrequest) | [CostQuerySetInfo](CostQuerySet#costquerysetinfo) |
| [**list**](./CostQuerySet#list) | [CostQuerySetQuery](CostQuerySet#costquerysetquery) | [CostQuerySetsInfo](CostQuerySet#costquerysetsinfo) |
| [**stat**](./CostQuerySet#stat) | [CostQuerySetStatQuery](CostQuerySet#costquerysetstatquery) | [Struct](CostQuerySet#struct) |



    
<br>

### create

Creates a new CostQuerySet. You can make your own custom query that meets your needs, and input it as an `option` parameter of the resource. Queries such as `group_by` and `granularity` are provided by default.



> **POST** /cost-analysis/v1/cost-query-set/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateCostQuerySetRequest](./CostQuerySet#createcostquerysetrequest)

* **data_source_id** (string)   `Required` 


* **name** (string)   `Required` 


* **options** (Struct)   `Required` 


* **tags** (Struct)  





{{< highlight json >}}
{
       "data_source_id": "ds-085d1e872789",
       "name": "project_provider_region",
       "options": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CostQuerySetInfo](#COSTQUERYSETINFO)
* **cost_query_set_id** (string)   `Required` 

* **name** (string)   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **data_source_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
       "cost_query_set_id": "query-76a58ea5d02c",
       "name": "project_provider_region",
       "options": {},
       "tags": {},
       "user_id": "test@cloudforet.io",
       "data_source_id": "ds-085d1e872789",
       "domain_id": "domain-58010aa2e451",
       "created_at": "2022-07-19T06:11:03.701Z",
       "updated_at": "2022-07-19T06:11:03.701Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific CostQuerySet. You can make changes in the details of queries.



> **POST** /cost-analysis/v1/cost-query-set/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateCostQuerySetRequest](./CostQuerySet#updatecostquerysetrequest)

* **cost_query_set_id** (string)   `Required` 


* **name** (string)  


* **options** (Struct)  


* **tags** (Struct)  





{{< highlight json >}}
{
       "cost_query_set_id": "query-76a58ea5d02c",
       "name": "project_provider_region",
       "options": {},
       "tags": {},
       "user_id": "test@cloudforet.io",
       "domain_id": "domain-58010aa2e451",
       "created_at": "2022-07-19T06:11:03.701Z",
       "updated_at": "2022-07-19T06:11:03.701Z"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CostQuerySetInfo](#COSTQUERYSETINFO)
* **cost_query_set_id** (string)   `Required` 

* **name** (string)   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **data_source_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
       "cost_query_set_id": "query-76a58ea5d02c",
       "name": "project_provider_region",
       "options": {},
       "tags": {},
       "user_id": "test@cloudforet.io",
       "data_source_id": "ds-085d1e872789",
       "domain_id": "domain-58010aa2e451",
       "created_at": "2022-07-19T06:11:03.701Z",
       "updated_at": "2022-07-19T06:11:03.701Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific CostQuerySet. You must specify the `cost_query_set_id` of the CostQuerySet to delete.



> **POST** /cost-analysis/v1/cost-query-set/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[CostQuerySetRequest](./CostQuerySet#costquerysetrequest)

* **cost_query_set_id** (string)   `Required` 





{{< highlight json >}}
{
   "cost_query_set_id": "query-16ae671dc8fb",
    "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific CostQuerySet. Prints detailed information about the CostQuerySet, including the details of queries.



> **POST** /cost-analysis/v1/cost-query-set/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[CostQuerySetRequest](./CostQuerySet#costquerysetrequest)

* **cost_query_set_id** (string)   `Required` 





{{< highlight json >}}
{
   "cost_query_set_id": "query-16ae671dc8fb",
    "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CostQuerySetInfo](#COSTQUERYSETINFO)
* **cost_query_set_id** (string)   `Required` 

* **name** (string)   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **data_source_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
       "cost_query_set_id": "query-76a58ea5d02c",
       "name": "project_provider_region",
       "options": {},
       "tags": {},
       "user_id": "test@cloudforet.io",
       "data_source_id": "ds-085d1e872789",
       "domain_id": "domain-58010aa2e451",
       "created_at": "2022-07-19T06:11:03.701Z",
       "updated_at": "2022-07-19T06:11:03.701Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all CostQuerySets. You can use a query to get a filtered list of CostQuerySets.



> **POST** /cost-analysis/v1/cost-query-set/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[CostQuerySetQuery](./CostQuerySet#costquerysetquery)

* **data_source_id** (string)   `Required` 


* **query** (Query)  


* **name** (string)  





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CostQuerySetsInfo](#COSTQUERYSETSINFO)
* **results** (CostQuerySetInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
       "results": [
           {
               "cost_query_set_id": "query-16ae671dc8fb",
               "name": "3 month product pie chart",
               "options": {},
               "tags": {},
               "user_id": "yuda@mz.co.kr",
               "data_source_id": "ds-085d1e872789",
               "domain_id": "domain-58010aa2e451",
               "created_at": "2022-03-08T03:37:31.404Z",
               "updated_at": "2022-03-08T03:37:31.404Z"
           },
           {
               "cost_query_set_id": "query-d90addf25e4b",
               "name": "6 month project group",
               "options": {},
               "tags": {},
               "user_id": "yuda@mz.co.kr",
               "data_source_id": "ds-085d1e872789",
               "domain_id": "domain-58010aa2e451",
               "created_at": "2022-03-14T09:29:54.306Z",
               "updated_at": "2022-03-14T09:29:54.306Z"
           }
       ],
       "total_count": 34
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /cost-analysis/v1/cost-query-set/stat
>






    


<br>
<br>

## Message



### CostQuerySetInfo
* **cost_query_set_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### CostQuerySetQuery
* **data_source_id** (string)   `Required` 

    
* **query** (Query)  

    
* **name** (string)  

    <br>

### CostQuerySetRequest
* **cost_query_set_id** (string)   `Required` 

    <br>

### CostQuerySetStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **data_source_id** (string)   `Required` 

    <br>

### CostQuerySetsInfo
* **results** (CostQuerySetInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CreateCostQuerySetRequest
* **data_source_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)  

    <br>

### UpdateCostQuerySetRequest
* **cost_query_set_id** (string)   `Required` 

    
* **name** (string)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>
