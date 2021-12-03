---
description:  
---
# Region

>  **Package : spaceone.api.inventory.v1**

## Region

{% hint style="info" %}
**Region Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](region.md#create)|   [CreateRegionRequest](region.md#createregionrequest) |   [RegionInfo](region.md#regioninfo) |  |
| 2 | [**update**](region.md#update)|   [UpdateRegionRequest](region.md#updateregionrequest) |   [RegionInfo](region.md#regioninfo) |  |
| 3 | [**delete**](region.md#delete)|   [RegionRequest](region.md#regionrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](region.md#get)|   [GetRegionRequest](region.md#getregionrequest) |   [RegionInfo](region.md#regioninfo) |  |
| 5 | [**list**](region.md#list)|   [RegionQuery](region.md#regionquery) |   [RegionsInfo](region.md#regionsinfo) |  |
| 6 | [**stat**](region.md#stat)|   [RegionStatQuery](region.md#regionstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /inventory/v1/regions
>


| Type | Message |
| :--- | :--- |
| Request | [CreateRegionRequest](region.md#createregionrequest) |
| Response |  [RegionInfo](region.md#regioninfo)  |
 
 

 
### update
> **PUT** /inventory/v1/region/{region_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateRegionRequest](region.md#updateregionrequest) |
| Response |  [RegionInfo](region.md#regioninfo)  |
 
 

 
### delete
> **DELETE** /inventory/v1/region/{region_id}
>


| Type | Message |
| :--- | :--- |
| Request | [RegionRequest](region.md#regionrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /inventory/v1/region/{region_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetRegionRequest](region.md#getregionrequest) |
| Response |  [RegionInfo](region.md#regioninfo)  |
 
 

 
### list
> **GET** /inventory/v1/regions
>
> **POST** /inventory/v1/regions/search



| Type | Message |
| :--- | :--- |
| Request | [RegionQuery](region.md#regionquery) |
| Response |  [RegionsInfo](region.md#regionsinfo)  |
 
 

 
### stat
> **POST** /inventory/v1/regions/stat
>


| Type | Message |
| :--- | :--- |
| Request | [RegionStatQuery](region.md#regionstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateRegionRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | name |string|✅| |
| 2 | region_code |string|✅| |
| 3 | provider |string|❌| |
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | domain_id |string|✅| |

### GetRegionRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | region_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### RegionInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | region_id |string | |
| 2 | name |string | |
| 3 | region_key |string | |
| 4 | region_code |string | |
| 5 | provider |string | |
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 7 | domain_id |string | |
| 8 | created_at |string | |
| 9 | updated_at |string | |

### RegionQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | region_id |string|❌| |
| 3 | name |string|❌| |
| 4 | region_key |string|❌| |
| 5 | region_code |string|❌| |
| 6 | provider |string|❌| |
| 7 | domain_id |string|✅| |

### RegionRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | region_id |string|✅| |
| 2 | domain_id |string|✅| |

### RegionStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### RegionsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of RegionInfo](region.md#regioninfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateRegionRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | region_id |string|✅| |
| 2 | name |string|❌| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | domain_id |string|✅| |
