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
| 1 | [create](Region.md#create)| [CreateRegionRequest](Region.md#createregionrequest) | [RegionInfo](Region.md#regioninfo) |  |
| 2 | [update](Region.md#update)| [UpdateRegionRequest](Region.md#updateregionrequest) | [RegionInfo](Region.md#regioninfo) |  |
| 3 | [delete](Region.md#delete)| [RegionRequest](Region.md#regionrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Region.md#get)| [GetRegionRequest](Region.md#getregionrequest) | [RegionInfo](Region.md#regioninfo) |  |
| 5 | [list](Region.md#list)| [RegionQuery](Region.md#regionquery) | [RegionsInfo](Region.md#regionsinfo) |  |
| 6 | [stat](Region.md#stat)| [RegionStatQuery](Region.md#regionstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /inventory/v1/regions
>



| Type | Message |
| :--- | :--- |
| Request | [CreateRegionRequest](Region.md#createregionrequest) |
| Response |  [RegionInfo](Region.md#regioninfo)  |



### update
> **PUT** /inventory/v1/region/{region_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateRegionRequest](Region.md#updateregionrequest) |
| Response |  [RegionInfo](Region.md#regioninfo)  |



### delete
> **DELETE** /inventory/v1/region/{region_id}
>



| Type | Message |
| :--- | :--- |
| Request | [RegionRequest](Region.md#regionrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /inventory/v1/region/{region_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetRegionRequest](Region.md#getregionrequest) |
| Response |  [RegionInfo](Region.md#regioninfo)  |



### list
> **GET** /inventory/v1/regions
>
> **POST** /inventory/v1/regions/search




| Type | Message |
| :--- | :--- |
| Request | [RegionQuery](Region.md#regionquery) |
| Response |  [RegionsInfo](Region.md#regionsinfo)  |



### stat
> **POST** /inventory/v1/regions/stat
>



| Type | Message |
| :--- | :--- |
| Request | [RegionStatQuery](Region.md#regionstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreateRegionRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅||
| 2 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌||
| 3 | domain_id |string|✅||

### GetRegionRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | region_id |string|✅||
| 2 | domain_id |string|✅||
| 3 | only |string|❌||

### RegionInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">region_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ACTIVE</li>
          	<li>DELETED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">deleted_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>


### RegionQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌||
| 2 | region_id |string|❌||
| 3 | name |string|❌||
| 4 | domain_id |string|✅||

### RegionRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | region_id |string|✅||
| 2 | domain_id |string|✅||

### RegionStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅||
| 2 | domain_id |string|✅||

### RegionsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[RegionInfo](Region.md#regioninfo)|||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|||

### UpdateRegionRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | region_id |string|✅||
| 2 | name |string|❌||
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌||
| 4 | domain_id |string|✅||
