---
title: "CloudServiceQuerySet"
linkTitle: "CloudServiceQuerySet"
weight: 3
bookFlatSection: true
---
# [CloudServiceQuerySet](#CloudServiceQuerySet)
A CloudServiceQuerySet is query set for storing statistics data of CloudService.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## CloudServiceQuerySet





**CloudServiceQuerySet Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CloudServiceQuerySet#create) | [CreateCloudServiceQuerySetRequest](CloudServiceQuerySet#createcloudservicequerysetrequest) | [CloudServiceQuerySetInfo](CloudServiceQuerySet#cloudservicequerysetinfo) |
| [**update**](./CloudServiceQuerySet#update) | [UpdateCloudServiceQuerySetRequest](CloudServiceQuerySet#updatecloudservicequerysetrequest) | [CloudServiceQuerySetInfo](CloudServiceQuerySet#cloudservicequerysetinfo) |
| [**delete**](./CloudServiceQuerySet#delete) | [CloudServiceQuerySetRequest](CloudServiceQuerySet#cloudservicequerysetrequest) | [Empty](CloudServiceQuerySet#empty) |
| [**run**](./CloudServiceQuerySet#run) | [CloudServiceQuerySetRequest](CloudServiceQuerySet#cloudservicequerysetrequest) | [Empty](CloudServiceQuerySet#empty) |
| [**enable**](./CloudServiceQuerySet#enable) | [CloudServiceQuerySetRequest](CloudServiceQuerySet#cloudservicequerysetrequest) | [CloudServiceQuerySetInfo](CloudServiceQuerySet#cloudservicequerysetinfo) |
| [**disable**](./CloudServiceQuerySet#disable) | [CloudServiceQuerySetRequest](CloudServiceQuerySet#cloudservicequerysetrequest) | [CloudServiceQuerySetInfo](CloudServiceQuerySet#cloudservicequerysetinfo) |
| [**get**](./CloudServiceQuerySet#get) | [GetCloudServiceQuerySetRequest](CloudServiceQuerySet#getcloudservicequerysetrequest) | [CloudServiceQuerySetInfo](CloudServiceQuerySet#cloudservicequerysetinfo) |
| [**list**](./CloudServiceQuerySet#list) | [CloudServiceQuerySetQuery](CloudServiceQuerySet#cloudservicequerysetquery) | [CloudServiceQuerySetsInfo](CloudServiceQuerySet#cloudservicequerysetsinfo) |
| [**stat**](./CloudServiceQuerySet#stat) | [CloudServiceQuerySetStatQuery](CloudServiceQuerySet#cloudservicequerysetstatquery) | [Struct](CloudServiceQuerySet#struct) |



    
<br>

### create

Create a new query set. Periodic statistics data is created based on the query set.
`query` parameters refer to AnalyzeQuery.



> **POST** /inventory/v1/cloud-service-query-set/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateCloudServiceQuerySetRequest](./CloudServiceQuerySet#createcloudservicequerysetrequest)

* **name** (string)   `Required` 


* **query** (AnalyzeQuery)   `Required` 


* **domain_id** (string)   `Required` 


* **unit** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "name": "EC2 Count by Instance Type",
   "query": "<AnalyzeQuery>",
   "unit": "Count",
   "tags": {
       "foo": "bar"
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServiceQuerySetInfo](#CLOUDSERVICEQUERYSETINFO)
* **query_set_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **query** (AnalyzeQuery)   `Required` 

* **query_type** (QueryType)   `Required` 

* **unit** (string)   `Required` 

* **provider** (string)   `Required` 

* **cloud_service_group** (string)   `Required` 

* **cloud_service_type** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "query_set_id": "query-set-abcd1234",
   "name": "EC2 Count by Instance Type",
   "state": "ENABLED",
   "query_type": "MANAGED",
   "unit": "Count",
   "provider": "aws",
   "cloud_service_group": "EC2",
   "cloud_service_type": "Instance",
   "tags": {
       "foo": "bar"
   },
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-06-22T01:38:16.301Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Update a specific query set. You can only update the query set of custom type.



> **POST** /inventory/v1/cloud-service-query-set/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateCloudServiceQuerySetRequest](./CloudServiceQuerySet#updatecloudservicequerysetrequest)

* **query_set_id** (string)   `Required` 


* **name** (string)  


* **query** (AnalyzeQuery)  


* **unit** (string)  


* **tags** (Struct)  


* **domain_id** (string)  





{{< highlight json >}}
{
   "query_set_id": "query-set-abcd1234",
   "name": "Changed Name",
   "query": "<AnalyzeQuery>",
   "unit": "Size (GB)",
   "tags": {
       "changed_key": "changed_value"
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServiceQuerySetInfo](#CLOUDSERVICEQUERYSETINFO)
* **query_set_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **query** (AnalyzeQuery)   `Required` 

* **query_type** (QueryType)   `Required` 

* **unit** (string)   `Required` 

* **provider** (string)   `Required` 

* **cloud_service_group** (string)   `Required` 

* **cloud_service_type** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "query_set_id": "query-set-abcd1234",
   "name": "EC2 Count by Instance Type",
   "state": "ENABLED",
   "query_type": "MANAGED",
   "unit": "Count",
   "provider": "aws",
   "cloud_service_group": "EC2",
   "cloud_service_type": "Instance",
   "tags": {
       "foo": "bar"
   },
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-06-22T01:38:16.301Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Delete a specific query set.



> **POST** /inventory/v1/cloud-service-query-set/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[CloudServiceQuerySetRequest](./CloudServiceQuerySet#cloudservicequerysetrequest)

* **query_set_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "query_set_id": "query-set-abcd1234"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### run

Run a specific query set and store the result in the statistics data.



> **POST** /inventory/v1/cloud-service-query-set/delete
>





 {{< tabs " run " >}}

 {{< tab "Request Example" >}}



[CloudServiceQuerySetRequest](./CloudServiceQuerySet#cloudservicequerysetrequest)

* **query_set_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "query_set_id": "query-set-abcd1234"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### enable

Enable a specific query set.



> **POST** /inventory/v1/cloud-service-query-set/get
>





 {{< tabs " enable " >}}

 {{< tab "Request Example" >}}



[CloudServiceQuerySetRequest](./CloudServiceQuerySet#cloudservicequerysetrequest)

* **query_set_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "query_set_id": "query-set-abcd1234"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServiceQuerySetInfo](#CLOUDSERVICEQUERYSETINFO)
* **query_set_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **query** (AnalyzeQuery)   `Required` 

* **query_type** (QueryType)   `Required` 

* **unit** (string)   `Required` 

* **provider** (string)   `Required` 

* **cloud_service_group** (string)   `Required` 

* **cloud_service_type** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "query_set_id": "query-set-abcd1234",
   "name": "EC2 Count by Instance Type",
   "state": "ENABLED",
   "query_type": "MANAGED",
   "unit": "Count",
   "provider": "aws",
   "cloud_service_group": "EC2",
   "cloud_service_type": "Instance",
   "tags": {
       "foo": "bar"
   },
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-06-22T01:38:16.301Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### disable

Disable a specific query set. query set is not executed when disabled.



> **POST** /inventory/v1/cloud-service-query-set/get
>





 {{< tabs " disable " >}}

 {{< tab "Request Example" >}}



[CloudServiceQuerySetRequest](./CloudServiceQuerySet#cloudservicequerysetrequest)

* **query_set_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "query_set_id": "query-set-abcd1234"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServiceQuerySetInfo](#CLOUDSERVICEQUERYSETINFO)
* **query_set_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **query** (AnalyzeQuery)   `Required` 

* **query_type** (QueryType)   `Required` 

* **unit** (string)   `Required` 

* **provider** (string)   `Required` 

* **cloud_service_group** (string)   `Required` 

* **cloud_service_type** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "query_set_id": "query-set-abcd1234",
   "name": "EC2 Count by Instance Type",
   "state": "ENABLED",
   "query_type": "MANAGED",
   "unit": "Count",
   "provider": "aws",
   "cloud_service_group": "EC2",
   "cloud_service_type": "Instance",
   "tags": {
       "foo": "bar"
   },
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-06-22T01:38:16.301Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get

Get a specific query set.



> **POST** /inventory/v1/cloud-service-query-set/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetCloudServiceQuerySetRequest](./CloudServiceQuerySet#getcloudservicequerysetrequest)

* **query_set_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **only** (string)  `Repeated`   





{{< highlight json >}}
{
   "query_set_id": "query-set-abcd1234"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServiceQuerySetInfo](#CLOUDSERVICEQUERYSETINFO)
* **query_set_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **query** (AnalyzeQuery)   `Required` 

* **query_type** (QueryType)   `Required` 

* **unit** (string)   `Required` 

* **provider** (string)   `Required` 

* **cloud_service_group** (string)   `Required` 

* **cloud_service_type** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "query_set_id": "query-set-abcd1234",
   "name": "EC2 Count by Instance Type",
   "state": "ENABLED",
   "query_type": "MANAGED",
   "unit": "Count",
   "provider": "aws",
   "cloud_service_group": "EC2",
   "cloud_service_type": "Instance",
   "tags": {
       "foo": "bar"
   },
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-06-22T01:38:16.301Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all query sets.
You can use a query to get a filtered list of query sets.



> **POST** /inventory/v1/cloud-service-query-set/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[CloudServiceQuerySetQuery](./CloudServiceQuerySet#cloudservicequerysetquery)

* **domain_id** (string)   `Required` 


* **query** (Query)  


* **query_set_id** (string)  


* **name** (string)  


* **state** (State)  


* **query_type** (QueryType)  


* **provider** (string)  


* **cloud_service_group** (string)  


* **cloud_service_type** (string)  





{{< highlight json >}}
{
   "query": <SearchQuery>,
   "query_set_id": "query-set-abcd1234",
   "name": "EC2 Count by Instance Type",
   "state": "ENABLED",
   "query_type": "MANAGED",
   "provider": "aws",
   "cloud_service_group": "EC2",
   "cloud_service_type": "Instance",
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServiceQuerySetsInfo](#CLOUDSERVICEQUERYSETSINFO)
* **results** (CloudServiceQuerySetInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
   {
       "query_set_id": "query-set-abcd1234",
       "name": "EC2 Count by Instance Type",
       "state": "ENABLED",
       "query_type": "MANAGED",
       "unit": "Count",
       "provider": "aws",
       "cloud_service_group": "EC2",
       "cloud_service_type": "Instance",
       "tags": {
           "foo": "bar"
       },
       "domain_id": "domain-58010aa2e451",
       "created_at": "2022-06-22T01:38:16.301Z"
   },
   {...}
   ],
   "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /inventory/v1/cloud-service-query-set/stat
>






    


<br>
<br>

## Message



### CloudServiceQuerySetInfo
* **query_set_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **query** (AnalyzeQuery)   `Required` 

    
* **query_type** (QueryType)   `Required` 

    
* **unit** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **cloud_service_group** (string)   `Required` 

    
* **cloud_service_type** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### CloudServiceQuerySetQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **query_set_id** (string)  

    
* **name** (string)  

    
* **state** (State)  

    
* **query_type** (QueryType)  

    
* **provider** (string)  

    
* **cloud_service_group** (string)  

    
* **cloud_service_type** (string)  

    <br>

### CloudServiceQuerySetRequest
* **query_set_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### CloudServiceQuerySetStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### CloudServiceQuerySetsInfo
* **results** (CloudServiceQuerySetInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CreateCloudServiceQuerySetRequest
* **name** (string)   `Required` 

    
* **query** (AnalyzeQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **unit** (string)  

    
* **tags** (Struct)  

    <br>

### GetCloudServiceQuerySetRequest
* **query_set_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### UpdateCloudServiceQuerySetRequest
* **query_set_id** (string)   `Required` 

    
* **name** (string)  

    
* **query** (AnalyzeQuery)  

    
* **unit** (string)  

    
* **tags** (Struct)  

    
* **domain_id** (string)  

    <br>
