---
title: "Region"
linkTitle: "Region"
weight: 3
bookFlatSection: true
---
# [Region](#Region)
A Region is a resource storing regional information from each cloud service provider. Regional data stored by the resource includes the latitude and longitude of the region.


>  **Package : spaceone.api.inventory.v2**

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



> **POST** /inventory/v2/region/create
>






    
<br>

### update

Updates a specific Region. You can make changes in Region settings, including `name` and `tags`. The `tags` contain the continent, latitude, and longitude.



> **POST** /inventory/v2/region/update
>






    
<br>

### delete

Deletes a specific Region. You must specify the `region_id` of the Region to delete.



> **POST** /inventory/v2/region/delete
>






    
<br>

### get

Gets a specific Region. Prints detailed information about the Region, including `name`, `region_code`, and a location coordinate.



> **POST** /inventory/v2/region/get
>






    
<br>

### list

Gets a list of all Regions. You can use a query to get a filtered list of Regions.



> **POST** /inventory/v2/region/list
>






    
<br>

### stat





> **POST** /inventory/v2/region/stat
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
