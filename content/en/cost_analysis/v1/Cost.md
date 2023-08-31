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
| [**create**](./Cost#create) | [CreateCostRequest](Cost#createcostrequest) | [CostInfo](Cost#costinfo) |
| [**delete**](./Cost#delete) | [CostRequest](Cost#costrequest) | [Empty](Cost#empty) |
| [**get**](./Cost#get) | [GetCostRequest](Cost#getcostrequest) | [CostInfo](Cost#costinfo) |
| [**list**](./Cost#list) | [CostQuery](Cost#costquery) | [CostsInfo](Cost#costsinfo) |
| [**analyze**](./Cost#analyze) | [CostAnalyzeQuery](Cost#costanalyzequery) | [Struct](Cost#struct) |
| [**stat**](./Cost#stat) | [CostStatQuery](Cost#coststatquery) | [Struct](Cost#struct) |



    
<br>

### create

Creates a new Cost. When creating a Cost, if the parameter `provider` is not entered, the default value of the parameter will be the provider information of the DataSource which collected the raw data of the Cost from the provider. The parameter `billed_at` is the data of when the cost is billed. While the DataSource collects the cost data, if the `billed_at` data does not exist, the value will be replaced with the `created_at` data indicating when the Cost is created. If the cost data collected is based on USD, the Cost is created without the currency exchange.



> **POST** /cost-analysis/v1/cost/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateCostRequest](./Cost#createcostrequest)

* **cost** (float)   `Required` 


* **data_source_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **billed_date** (string)   `Required` 


* **usage_quantity** (float)  


* **usage_unit** (float)  


* **provider** (string)  


* **region_code** (string)  


* **product** (string)  


* **usage_type** (string)  


* **resource** (string)  


* **tags** (Struct)  


* **additional_info** (Struct)  


* **service_account_id** (string)  


* **project_id** (string)  





{{< highlight json >}}
{
       "cost": 142,
       "usage_quantity": 84532,
       "usage_unit": "GB",
       "provider": "aws",
       "region_code": "ap-northeast-1",
       "product": "AWSDataTransfer",
       "account": "722069360300",
       "usage_type": "data-transfer.out",
       "additional_info": {
           "raw_usage_type": "APN1-DataTransfer-Out-Bytes"
       },
       "tags": {
           "Environment": "Dev"
       },
       "data_source_id": "ds-fcba92ca73b1"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CostInfo](#COSTINFO)
* **cost_id** (string)   `Required` 

* **cost** (float)   `Required` 

* **usage_quantity** (float)   `Required` 

* **usage_unit** (string)   `Required` 

* **provider** (string)   `Required` 

* **region_code** (string)   `Required` 

* **region_key** (string)   `Required` 

* **product** (string)   `Required` 

* **usage_type** (string)   `Required` 

* **resource** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **additional_info** (Struct)   `Required` 

* **service_account_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **data_source_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **billed_year** (string)   `Required` 

* **billed_month** (string)   `Required` 

* **billed_date** (string)   `Required` 



{{< highlight json >}}
{
       "cost_id": "cost-c5aae7712ec9",
       "cost": 142,
       "usage_quantity": 84532,
       "usage_unit": "GB",
       "provider": "aws",
       "region_code": "ap-northeast-1",
       "product": "AWSDataTransfer",
       "usage_type": "data-transfer.out",
       "additional_info": {
           "raw_usage_type": "APN1-DataTransfer-Out-Bytes"
       },
       "tags": {
           "Environment": "Dev"
       },
       "data_source_id": "ds-fcba92ca73b1"
       "domain_id": "domain-58010aa2e451",
       "billed_year": "2022",
       "billed_month": "2022-07",
       "billed_date": "2022-07-19"
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

* **cost_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





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

* **cost_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **only** (string)  `Repeated`   





{{< highlight json >}}
{
   "cost_id": "cost-2ad052ed03d7"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CostInfo](#COSTINFO)
* **cost_id** (string)   `Required` 

* **cost** (float)   `Required` 

* **usage_quantity** (float)   `Required` 

* **usage_unit** (string)   `Required` 

* **provider** (string)   `Required` 

* **region_code** (string)   `Required` 

* **region_key** (string)   `Required` 

* **product** (string)   `Required` 

* **usage_type** (string)   `Required` 

* **resource** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **additional_info** (Struct)   `Required` 

* **service_account_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **data_source_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **billed_year** (string)   `Required` 

* **billed_month** (string)   `Required` 

* **billed_date** (string)   `Required` 



{{< highlight json >}}
{
       "cost_id": "cost-c5aae7712ec9",
       "cost": 142,
       "usage_quantity": 84532,
       "usage_unit": "GB",
       "provider": "aws",
       "region_code": "ap-northeast-1",
       "product": "AWSDataTransfer",
       "usage_type": "data-transfer.out",
       "additional_info": {
           "raw_usage_type": "APN1-DataTransfer-Out-Bytes"
       },
       "tags": {
           "Environment": "Dev"
       },
       "data_source_id": "ds-fcba92ca73b1"
       "domain_id": "domain-58010aa2e451",
       "billed_year": "2022",
       "billed_month": "2022-07",
       "billed_date": "2022-07-19"
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

* **domain_id** (string)   `Required` 


* **query** (Query)  


* **cost_id** (string)  


* **provider** (string)  


* **region_code** (string)  


* **region_key** (string)  


* **product** (string)  


* **usage_type** (string)  


* **resource** (string)  


* **service_account_id** (string)  


* **project_id** (string)  


* **data_source_id** (string)  


* **billed_year** (string)  


* **billed_month** (string)  


* **billed_date** (string)  





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CostsInfo](#COSTSINFO)
* **results** (CostInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
       "results": [
           {
               "cost_id": "cost-c5aae7712ec9",
               "cost": 142,
               "usage_quantity": 84532,
               "usage_unit": "GB",
               "provider": "aws",
               "region_code": "ap-northeast-1",
               "product": "AWSDataTransfer",
               "usage_type": "data-transfer.out",
               "additional_info": {
               "raw_usage_type": "APN1-DataTransfer-Out-Bytes"
               },
               "tags": {
               "Environment": "Dev"
               },
               "data_source_id": "ds-fcba92ca73b1"
               "domain_id": "domain-58010aa2e451",
               "billed_year": "2022",
               "billed_month": "2022-07",
               "billed_date": "2022-07-19"
           },
           {
               "cost_id": "cost-1d5e1b0dbf82",
               "cost": 78,
               "usage_quantity": 34523,
               "usage_unit": "Count",
               "provider": "aws",
               "region_code": "ap-northeast-1",
               "product": "AWSQueueService"
               "additional_info": {
                   "raw_usage_type": "APN1-Requests-Tier1"
               },
               "tags": {},
               "data_source_id": "ds-fcba92ca73b1",
               "domain_id": "domain-58010aa2e451",
               "billed_year": "2022",
               "billed_month": "2022-07",
               "billed_date": "2022-07-20"
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






    
<br>

### stat





> **POST** /cost-analysis/v1/cost/stat
>






    


<br>
<br>

## Message



### CostAnalyzeQuery
* **query** (TimeSeriesAnalyzeQuery)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### CostInfo
* **cost_id** (string)   `Required` 

    
* **cost** (float)   `Required` 

    
* **usage_quantity** (float)   `Required` 

    
* **usage_unit** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **region_code** (string)   `Required` 

    
* **region_key** (string)   `Required` 

    
* **product** (string)   `Required` 

    
* **usage_type** (string)   `Required` 

    
* **resource** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **additional_info** (Struct)   `Required` 

    
* **service_account_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **billed_year** (string)   `Required` 

    
* **billed_month** (string)   `Required` 

    
* **billed_date** (string)   `Required` 

    <br>

### CostQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **cost_id** (string)  

    
* **provider** (string)  

    
* **region_code** (string)  

    
* **region_key** (string)  

    
* **product** (string)  

    
* **usage_type** (string)  

    
* **resource** (string)  

    
* **service_account_id** (string)  

    
* **project_id** (string)  

    
* **data_source_id** (string)  

    
* **billed_year** (string)  

    
* **billed_month** (string)  

    
* **billed_date** (string)  

    <br>

### CostRequest
* **cost_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### CostStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### CostsInfo
* **results** (CostInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CreateCostRequest
* **cost** (float)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **billed_date** (string)   `Required` 

    
* **usage_quantity** (float)  

    
* **usage_unit** (float)  

    
* **provider** (string)  

    
* **region_code** (string)  

    
* **product** (string)  

    
* **usage_type** (string)  

    
* **resource** (string)  

    
* **tags** (Struct)  

    
* **additional_info** (Struct)  

    
* **service_account_id** (string)  

    
* **project_id** (string)  

    <br>

### GetCostRequest
* **cost_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>
