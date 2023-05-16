---
title: "Cost"
linkTitle: "Cost"
weight: 3
bookFlatSection: true
---
# [Cost](#Cost)
A Cost is a resource of raw cost data collected by the cost_analysis.DataSource.


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

Creates a new Cost. When creating a Cost, if the parameter `provider` is not entered, the default value of the parameter will be the provider information of the DataSource which collected the raw data of the Cost from the provider. The parameter `billed_at` is the data of when the cost is billed. While the DataSource collects the cost data, if the `billed_at` data does not exist, the value will be replaced with the `created_at` data indicating when the Cost is created. If the cost data collected is based on USD, the Cost is created without the currency exchange.



> **POST** /cost-analysis/v1/cost/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateCostRequest](./Cost#createcostrequest)

* **original_cost** (float)  `Required` 


* **original_currency** (string)  `Required` 


* **data_source_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **usd_cost** (float) 


* **usage_quantity** (float) 


* **provider** (string) 


* **region_code** (string) 


* **category** (string) 


* **product** (string) 


* **account** (string) 


* **usage_type** (string) 


* **resource_group** (string) 


* **resource** (string) 


* **tags** (Struct) 


* **additional_info** (Struct) 


* **service_account_id** (string) 


* **project_id** (string) 


* **billed_at** (string) 





{{< highlight json >}}
{
       "original_cost": 4.50528e-08,
       "original_currency": "USD",
       "usd_cost": 4.50528e-08,
       "usage_quantity": 4.11e-07,
       "provider": "aws",
       "region_code": "ap-northeast-1",
       "product": "AWSDataTransfer",
       "account": "722069360300",
       "usage_type": "data-transfer.out",
       "additional_info": {
           "raw_usage_type": "APN1-DataTransfer-Out-Bytes"
       },
       "data_source_id": "ds-fcba92ca73b1"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CostInfo](#COSTINFO)
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

* **usage_unit** (string)  `Required` 

* **resource** (string)  `Required` 

* **tags** (Struct)  `Required` 

* **additional_info** (Struct)  `Required` 

* **service_account_id** (string)  `Required` 

* **project_id** (string)  `Required` 

* **data_source_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **billed_at** (string)  `Required` 

* **created_at** (string)  `Required` 



{{< highlight json >}}
{
       "cost_id": "cost-c5aae7712ec9",
       "usd_cost": 4.50528e-08,
       "original_currency": "USD",
       "original_cost": 4.50528e-08,
       "usage_quantity": 4.11e-07,
       "provider": "aws",
       "region_code": "ap-northeast-1",
       "product": "AWSDataTransfer",
       "account": "722069360300",
       "usage_type": "data-transfer.out",
       "tags": {},
       "additional_info": {
           "raw_usage_type": "APN1-DataTransfer-Out-Bytes"
       },
       "data_source_id": "ds-fcba92ca73b1",
       "domain_id": "domain-58010aa2e451",
       "billed_at": "2022-07-19T09:44:27.326Z",
       "created_at": "2022-07-19T09:44:27.373Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific Cost. You must specify the `cost_id` of the Cost to delete.



> **POST** /cost-analysis/v1/cost/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[CostRequest](./Cost#costrequest)

* **cost_id** (string)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "cost_id": "cost-2ad052ed03d7"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Cost. Prints detailed information about the Cost, including  `region_code` and `account`.



> **POST** /cost-analysis/v1/cost/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetCostRequest](./Cost#getcostrequest)

* **cost_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **only** (string) 





{{< highlight json >}}
{
   "cost_id": "cost-2ad052ed03d7"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CostInfo](#COSTINFO)
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

* **usage_unit** (string)  `Required` 

* **resource** (string)  `Required` 

* **tags** (Struct)  `Required` 

* **additional_info** (Struct)  `Required` 

* **service_account_id** (string)  `Required` 

* **project_id** (string)  `Required` 

* **data_source_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **billed_at** (string)  `Required` 

* **created_at** (string)  `Required` 



{{< highlight json >}}
{
       "cost_id": "cost-c5aae7712ec9",
       "usd_cost": 4.50528e-08,
       "original_currency": "USD",
       "original_cost": 4.50528e-08,
       "usage_quantity": 4.11e-07,
       "provider": "aws",
       "region_code": "ap-northeast-1",
       "product": "AWSDataTransfer",
       "account": "722069360300",
       "usage_type": "data-transfer.out",
       "tags": {},
       "additional_info": {
           "raw_usage_type": "APN1-DataTransfer-Out-Bytes"
       },
       "data_source_id": "ds-fcba92ca73b1",
       "domain_id": "domain-58010aa2e451",
       "billed_at": "2022-07-19T09:44:27.326Z",
       "created_at": "2022-07-19T09:44:27.373Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Costs. You can use a query to get a filtered list of Costs.



> **POST** /cost-analysis/v1/cost/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[CostQuery](./Cost#costquery)

* **domain_id** (string)  `Required` 


* **query** (Query) 


* **cost_id** (string) 


* **original_currency** (string) 


* **provider** (string) 


* **region_code** (string) 


* **region_key** (string) 


* **category** (string) 


* **product** (string) 


* **account** (string) 


* **usage_type** (string) 


* **resource_group** (string) 


* **resource** (string) 


* **service_account_id** (string) 


* **project_id** (string) 


* **data_source_id** (string) 





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CostsInfo](#COSTSINFO)
* **results** (CostInfo)  `Required` 

* **total_count** (int32)  `Required` 



{{< highlight json >}}
{
       "results": [
           {
               "cost_id": "cost-2ad052ed03d7",
               "usd_cost": 4.50528e-08,
               "original_currency": "USD",
               "original_cost": 4.50528e-08,
               "usage_quantity": 4.11e-07,
               "provider": "aws",
               "region_code": "ap-northeast-1",
               "product": "AWSDataTransfer",
               "account": "722069360300",
               "usage_type": "data-transfer.out",
               "tags": {},
               "additional_info": {
                   "raw_usage_type": "APN1-DataTransfer-Out-Bytes"
               },
               "data_source_id": "ds-fcba92ca73b1",
               "domain_id": "domain-58010aa2e451",
               "billed_at": "2021-01-01T00:00:00.000Z",
               "created_at": "2022-04-06T13:49:39.669Z"
           },
           {
               "cost_id": "cost-1d5e1b0dbf82",
               "usd_cost": 1.04e-05,
               "original_currency": "USD",
               "original_cost": 1.04e-05,
               "usage_quantity": 26.0,
               "provider": "aws",
               "region_code": "ap-northeast-1",
               "product": "AWSQueueService",
               "account": "722069360300",
               "tags": {},
               "additional_info": {
                   "raw_usage_type": "APN1-Requests-Tier1"
               },
               "data_source_id": "ds-fcba92ca73b1",
               "domain_id": "domain-58010aa2e451",
               "billed_at": "2021-01-01T00:00:00.000Z",
               "created_at": "2022-04-06T13:49:39.675Z"
           }
       ],
       "total_count": 307066
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### analyze

Gets the Cost information of specific `product`s based on the time granularity: `DAILY`, `MONTHLY`, or `ACCUMULATED`. For `DAILY` granularity, this method can get the Cost data of at most 31 days. For `MONTHLY` or `ACCUMULATED` granularity, this method can get the Cost data of at most 12 months.



> **POST** /cost-analysis/v1/cost/analyze
>





 {{< tabs " analyze " >}}

 {{< tab "Request Example" >}}



[CostAnalyzeQuery](./Cost#costanalyzequery)

* **granularity** (Granularity)  `Required` 


* **start** (string)  `Required` 


* **end** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **group_by** (string) 


* **filter** (ListValue) 


* **limit** (int32) 


* **page** (Page) 


* **sort** (Sort) 


* **include_usage_quantity** (bool) 


* **include_others** (bool) 





{{< highlight json >}}
{
   "granularity": "MONTHLY",
   "start": "2022-05",
   "end": "2022-07",
   "group_by": ["product"],
   "filter": [],
   "limit": 15,
   "include_others": true,
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### analyze_v2





> **POST** /cost-analysis/v1/cost/analyze-v2
>






    
<br>

### stat





> **POST** /cost-analysis/v1/cost/stat
>






    


<br>
<br>

## Message



### CostAnalyzeQuery
* **granularity** (Granularity)  `Required` 

    
* **start** (string)  `Required` 

    
* **end** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **group_by** (string) 

    
* **filter** (ListValue) 

    
* **limit** (int32) 

    
* **page** (Page) 

    
* **sort** (Sort) 

    
* **include_usage_quantity** (bool) 

    
* **include_others** (bool) 

    <br>

### CostAnalyzeV2Query
* **query** (TimeSeriesAnalyzeQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

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

    
* **usage_unit** (string)  `Required` 

    
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
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **cost_id** (string) 

    
* **original_currency** (string) 

    
* **provider** (string) 

    
* **region_code** (string) 

    
* **region_key** (string) 

    
* **category** (string) 

    
* **product** (string) 

    
* **account** (string) 

    
* **usage_type** (string) 

    
* **resource_group** (string) 

    
* **resource** (string) 

    
* **service_account_id** (string) 

    
* **project_id** (string) 

    
* **data_source_id** (string) 

    <br>

### CostRequest
* **cost_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### CostStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### CostsInfo
* **results** (CostInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CreateCostRequest
* **original_cost** (float)  `Required` 

    
* **original_currency** (string)  `Required` 

    
* **data_source_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **usd_cost** (float) 

    
* **usage_quantity** (float) 

    
* **provider** (string) 

    
* **region_code** (string) 

    
* **category** (string) 

    
* **product** (string) 

    
* **account** (string) 

    
* **usage_type** (string) 

    
* **resource_group** (string) 

    
* **resource** (string) 

    
* **tags** (Struct) 

    
* **additional_info** (Struct) 

    
* **service_account_id** (string) 

    
* **project_id** (string) 

    
* **billed_at** (string) 

    <br>

### GetCostRequest
* **cost_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>
