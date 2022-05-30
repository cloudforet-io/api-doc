---
description:  
---
# Region

>  **Package : spaceone.api.inventory.v1**

## Region

{% hint style="info" %}
**Region Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](region.md#create)|   [CreateRegionRequest](region.md#createregionrequest) |   [RegionInfo](region.md#regioninfo) |  |
| [**update**](region.md#update)|   [UpdateRegionRequest](region.md#updateregionrequest) |   [RegionInfo](region.md#regioninfo) |  |
| [**delete**](region.md#delete)|   [RegionRequest](region.md#regionrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](region.md#get)|   [GetRegionRequest](region.md#getregionrequest) |   [RegionInfo](region.md#regioninfo) |  |
| [**list**](region.md#list)|   [RegionQuery](region.md#regionquery) |   [RegionsInfo](region.md#regionsinfo) |  |
| [**stat**](region.md#stat)|   [RegionStatQuery](region.md#regionstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">create</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateRegionRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   RegionInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateRegionRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   RegionInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">delete</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   RegionRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetRegionRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   RegionInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   RegionQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   RegionsInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   RegionStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
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
