---
title: "Region"
linkTitle: "Region"
weight: 3
bookFlatSection: true
---
# [Region](#Region)
A Region is a resource storing regional information from each cloud service provider. Regional data stored by the resource includes the latitude and longitude of the region.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Region





**Region Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Region#create) | [CreateRegionRequest](Region#createregionrequest) | [RegionInfo](Region#regioninfo) |
| [**update**](./Region#update) | [UpdateRegionRequest](Region#updateregionrequest) | [RegionInfo](Region#regioninfo) |
| [**delete**](./Region#delete) | [RegionRequest](Region#regionrequest) | [Empty](Region#empty) |
| [**get**](./Region#get) | [RegionRequest](Region#regionrequest) | [RegionInfo](Region#regioninfo) |
| [**list**](./Region#list) | [RegionQuery](Region#regionquery) | [RegionsInfo](Region#regionsinfo) |
| [**stat**](./Region#stat) | [RegionStatQuery](Region#regionstatquery) | [Struct](Region#struct) |



    
<br>

### create

Creates a new Region. As the parameter `region_key`, which is automatically created when a Region is created, is in a form of `{provider}.{region_code}`, it is unique regardless of providers. You can also specify the latitude, longitude, and continent information in `tags`.



> **POST** /inventory/v1/region/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateRegionRequest](./Region#createregionrequest)

* **name** (string)   `Required` 


* **region_code** (string)   `Required` 


* **provider** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "name": "Asia Pacific (Seoul)",
   "region_code": "ap-northeast-2",
   "provider": "aws",
   "tags": {
       "continent": "asis_pacific",
       "longitude": "73.013805",
       "latitude": "19.147428"
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RegionInfo](#REGIONINFO)
* **region_id** (string)   `Required` 

* **name** (string)   `Required` 

* **region_key** (string)   `Required` 

* **region_code** (string)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
   "region_id": "region-e41deed3c939",
   "name": "Asia Pacific (Seoul)",
   "region_key": "aws.ap-northeast-2",
   "region_code": "ap-northeast-2",
   "provider": "aws",
   "tags": {
       "continent": "asia_pacific",
       "longitude": "73.013805",
       "latitude": "19.147428"
   },
   "domain_id": "domain-x1b3c34v432",
   "workspace_id": "workspace-123456789012",
   "created_at": "2021-11-18T13:07:31.382Z",
   "updated_at": "2022-06-17T00:07:35.469Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Region. You can make changes in Region settings, including `name` and `tags`. The `tags` contain the continent, latitude, and longitude.



> **POST** /inventory/v1/region/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateRegionRequest](./Region#updateregionrequest)

* **region_id** (string)   `Required` 


* **name** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "region_id": "region-e41deed3c939",
   "name": "Region home",
   "tags": {
       "latitude": "6.34545",
       "continent": "asia_pacific",
       "longitude": "5.6433213"
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RegionInfo](#REGIONINFO)
* **region_id** (string)   `Required` 

* **name** (string)   `Required` 

* **region_key** (string)   `Required` 

* **region_code** (string)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
   "region_id": "region-e41deed3c939",
   "name": "Asia Pacific (Seoul)",
   "region_key": "aws.ap-northeast-2",
   "region_code": "ap-northeast-2",
   "provider": "aws",
   "tags": {
       "continent": "asia_pacific",
       "longitude": "73.013805",
       "latitude": "19.147428"
   },
   "domain_id": "domain-x1b3c34v432",
   "workspace_id": "workspace-123456789012",
   "created_at": "2021-11-18T13:07:31.382Z",
   "updated_at": "2022-06-17T00:07:35.469Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific Region. You must specify the `region_id` of the Region to delete.



> **POST** /inventory/v1/region/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[RegionRequest](./Region#regionrequest)

* **region_id** (string)   `Required` 





{{< highlight json >}}
{
   "region_id": "region-e41deed3c939"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Region. Prints detailed information about the Region, including `name`, `region_code`, and a location coordinate.



> **POST** /inventory/v1/region/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[RegionRequest](./Region#regionrequest)

* **region_id** (string)   `Required` 





{{< highlight json >}}
{
   "region_id": "region-e41deed3c939"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RegionInfo](#REGIONINFO)
* **region_id** (string)   `Required` 

* **name** (string)   `Required` 

* **region_key** (string)   `Required` 

* **region_code** (string)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
   "region_id": "region-e41deed3c939",
   "name": "Asia Pacific (Seoul)",
   "region_key": "aws.ap-northeast-2",
   "region_code": "ap-northeast-2",
   "provider": "aws",
   "tags": {
       "continent": "asia_pacific",
       "longitude": "73.013805",
       "latitude": "19.147428"
   },
   "domain_id": "domain-x1b3c34v432",
   "workspace_id": "workspace-123456789012",
   "created_at": "2021-11-18T13:07:31.382Z",
   "updated_at": "2022-06-17T00:07:35.469Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Regions. You can use a query to get a filtered list of Regions.



> **POST** /inventory/v1/region/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[RegionQuery](./Region#regionquery)

* **query** (Query)  


* **region_id** (string)  


* **name** (string)  


* **region_key** (string)  


* **region_code** (string)  


* **provider** (string)  


* **workspace_id** (string)  





{{< highlight json >}}
{
   "query": {
       "filter": [
           {
               "key": "name",
               "value": "Asia Pacific",
               "operator": "contain"
           }
       ]
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RegionsInfo](#REGIONSINFO)
* **results** (RegionInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
       {
           "region_id": "region-e41deed3c939",
           "name": "Asia Pacific (Mumbai)",
           "region_key": "aws.ap-south-1",
           "region_code": "ap-south-1",
           "provider": "aws",
           "tags": {
               "continent": "asia_pacific",
               "longitude": "73.013805",
               "latitude": "19.147428"
           },
           "domain_id": "domain-x1b3c34v432",
           "workspace_id": "workspace-123456789012",
           "created_at": "2021-11-18T13:07:31.382Z",
           "updated_at": "2022-06-17T00:07:35.469Z"
       },
       {
           "region_id": "region-f803eb00b567",
           "name": "Asia Pacific (Seoul)",
           "region_key": "aws.ap-northeast-2",
           "region_code": "ap-northeast-2",
           "provider": "aws",
           "tags": {
               "latitude": "6.34545",
               "continent": "asia_pacific",
               "longitude": "5.6433213"
           },
           "domain_id": "domain-x1b3c34v432",
           "workspace_id": "workspace-123456789012",
           "created_at": "2022-03-21T09:08:31.961Z",
           "updated_at": "2022-06-17T00:07:35.749Z"
       }
   ],
   "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /inventory/v1/region/stat
>






    


<br>
<br>

## Message



### CreateRegionRequest
* **name** (string)   `Required` 

    
* **region_code** (string)   `Required` 

    
* **provider** (string)  

    
* **tags** (Struct)  

    <br>

### RegionInfo
* **region_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **region_key** (string)   `Required` 

    
* **region_code** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### RegionQuery
* **query** (Query)  

    
* **region_id** (string)  

    
* **name** (string)  

    
* **region_key** (string)  

    
* **region_code** (string)  

    
* **provider** (string)  

    
* **workspace_id** (string)  

    <br>

### RegionRequest
* **region_id** (string)   `Required` 

    <br>

### RegionStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### RegionsInfo
* **results** (RegionInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateRegionRequest
* **region_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>
