---
title: "Region"
linkTitle: "Region"
weight: 3
bookFlatSection: true
---
# [Region](#Region)
desc: A Region is a resource storing regional information from each cloud service provider. Regional data stored by the resource includes the latitude and longitude of the region.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Region





**Region Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Region#create) | [CreateRegionRequest](Region#createregionrequest) | [RegionInfo](./Region#regioninfo) |
| [**update**](./Region#update) | [UpdateRegionRequest](Region#updateregionrequest) | [RegionInfo](./Region#regioninfo) |
| [**delete**](./Region#delete) | [RegionRequest](Region#regionrequest) | [Empty](./Region#empty) |
| [**get**](./Region#get) | [GetRegionRequest](Region#getregionrequest) | [RegionInfo](./Region#regioninfo) |
| [**list**](./Region#list) | [RegionQuery](Region#regionquery) | [RegionsInfo](./Region#regionsinfo) |
| [**stat**](./Region#stat) | [RegionStatQuery](Region#regionstatquery) | [Struct](./Region#struct) |



    
<br>

### create

desc: Creates a new Region. As the parameter `region_key`, which is automatically created when a Region is created, is in a form of `{provider}.{region_code}`, it is unique regardless of providers. You can also specify the latitude, longitude, and continent information in `tags`.
request_example: >-
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
response_example: >-
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
"created_at": "2021-11-18T13:07:31.382Z",
"updated_at": "2022-06-17T00:07:35.469Z"
}



> **POST** /inventory/v1/region/create
>






    
<br>

### update

desc: Updates a specific Region. You can make changes in Region settings, including `name` and `tags`. The `tags` contain the continent, latitude, and longitude.
request_example: >-
{
"region_id": "region-e41deed3c939",
"name": "Region home",
"tags": {
"latitude": "6.34545",
"continent": "asia_pacific",
"longitude": "5.6433213"
}
}
response_example: >-
{
"region_id": "region-e41deed3c939",
"name": "Region home",
"region_key": "aws.ap-northeast-2",
"region_code": "ap-northeast-2",
"provider": "aws",
"tags": {
"latitude": "6.34545",
"continent": "asia_pacific",
"longitude": "5.6433213"
},
"domain_id": "domain-x1b3c34v432",
"created_at": "2021-11-18T13:07:31.382Z",
"updated_at": "2022-06-17T00:07:35.469Z"
}



> **POST** /inventory/v1/region/update
>






    
<br>

### delete

desc: Deletes a specific Region. You must specify the `region_id` of the Region to delete.
request_example: >-
{
"region_id": "region-e41deed3c939"
}



> **POST** /inventory/v1/region/delete
>






    
<br>

### get

desc: Gets a specific Region. Prints detailed information about the Region, including `name`, `region_code`, and a location coordinate.
request_example: >-
{
"region_id": "region-f803eb00b567"
}
response_example: >-
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
"created_at": "2022-03-21T09:08:31.961Z",
"updated_at": "2022-06-17T00:07:35.749Z"
}



> **POST** /inventory/v1/region/get
>






    
<br>

### list

desc: Gets a list of all Regions. You can use a query to get a filtered list of Regions.
request_example: >-
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
response_example: >-
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
"created_at": "2022-03-21T09:08:31.961Z",
"updated_at": "2022-06-17T00:07:35.749Z"
}
],
"total_count": 2
}



> **POST** /inventory/v1/region/list
>






    
<br>

### stat





> **POST** /inventory/v1/region/stat
>






    


<br>
<br>

## Message



### CreateRegionRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **region_code** (string)  `Required` 

  *is_required: true*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetRegionRequest
* **region_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### RegionInfo
* **region_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **region_key** (string)  `Required` 

    
* **region_code** (string)  `Required` 

    
* **provider** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### RegionQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **region_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **region_key** (string)  `Required` 

  *is_required: false*

    
* **region_code** (string)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### RegionRequest
* **region_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### RegionStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### RegionsInfo
* **results** (RegionInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateRegionRequest
* **region_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
