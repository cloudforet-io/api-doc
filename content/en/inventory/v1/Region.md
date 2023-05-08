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

> **POST** /inventory/v1/region/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /inventory/v1/region/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /inventory/v1/region/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /inventory/v1/region/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /inventory/v1/region/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /inventory/v1/region/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


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
