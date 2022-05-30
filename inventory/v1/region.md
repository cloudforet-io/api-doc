---
description:  
---
# Region

>  **Package : spaceone.api.inventory.v1**

## Region

{% hint style="info" %}
**Region Methods:**

{%  endhint %}


| Method | Request | Response |
| :-----: | :--------: | :--------: |
| [**create**](region.md#create)|   [CreateRegionRequest](region.md#createregionrequest) |   [RegionInfo](region.md#regioninfo) |
| [**update**](region.md#update)|   [UpdateRegionRequest](region.md#updateregionrequest) |   [RegionInfo](region.md#regioninfo) |
| [**delete**](region.md#delete)|   [RegionRequest](region.md#regionrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](region.md#get)|   [GetRegionRequest](region.md#getregionrequest) |   [RegionInfo](region.md#regioninfo) |
| [**list**](region.md#list)|   [RegionQuery](region.md#regionquery) |   [RegionsInfo](region.md#regionsinfo) |
| [**stat**](region.md#stat)|   [RegionStatQuery](region.md#regionstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
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
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| region_code |string|✅| |
| provider |string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### GetRegionRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| region_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### RegionInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| region_id |string | |
| name |string | |
| region_key |string | |
| region_code |string | |
| provider |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |

### RegionQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| region_id |string|❌| |
| name |string|❌| |
| region_key |string|❌| |
| region_code |string|❌| |
| provider |string|❌| |
| domain_id |string|✅| |

### RegionRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| region_id |string|✅| |
| domain_id |string|✅| |

### RegionStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### RegionsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of RegionInfo](region.md#regioninfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateRegionRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| region_id |string|✅| |
| name |string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
