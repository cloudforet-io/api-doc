---
description:  
---
# Spot group

>  **Package : spaceone.api.spot_automation.v1**

## SpotGroup

{% hint style="info" %}
**SpotGroup Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](spot-group.md#create)|   [CreateSpotGroupRequest](spot-group.md#createspotgrouprequest) |   [SpotGroupInfo](spot-group.md#spotgroupinfo) |  |
| 2 | [**update**](spot-group.md#update)|   [UpdateSpotGroupRequest](spot-group.md#updatespotgrouprequest) |   [SpotGroupInfo](spot-group.md#spotgroupinfo) |  |
| 3 | [**delete**](spot-group.md#delete)|   [SpotGroupRequest](spot-group.md#spotgrouprequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](spot-group.md#get)|   [GetSpotGroupRequest](spot-group.md#getspotgrouprequest) |   [SpotGroupInfo](spot-group.md#spotgroupinfo) |  |
| 5 | [**list**](spot-group.md#list)|   [SpotGroupQuery](spot-group.md#spotgroupquery) |   [SpotGroupsInfo](spot-group.md#spotgroupsinfo) |  |
| 6 | [**interrupt**](spot-group.md#interrupt)|   [InterruptRequest](spot-group.md#interruptrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 7 | [**stat**](spot-group.md#stat)|   [SpotGroupStatQuery](spot-group.md#spotgroupstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /spot-automation/v1/spot-groups
>


| Type | Message |
| :--- | :--- |
| Request | [CreateSpotGroupRequest](spot-group.md#createspotgrouprequest) |
| Response |  [SpotGroupInfo](spot-group.md#spotgroupinfo)  |
 
 

 
### update
> **PUT** /spot-automation/v1/spot-group/{spot_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateSpotGroupRequest](spot-group.md#updatespotgrouprequest) |
| Response |  [SpotGroupInfo](spot-group.md#spotgroupinfo)  |
 
 

 
### delete
> **DELETE** /spot-automation/v1/spot-group/{spot_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [SpotGroupRequest](spot-group.md#spotgrouprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /spot-automation/v1/spot-group/{spot_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetSpotGroupRequest](spot-group.md#getspotgrouprequest) |
| Response |  [SpotGroupInfo](spot-group.md#spotgroupinfo)  |
 
 

 
### list
> **GET** /spot-automation/v1/spot-groups
>
> **POST** /spot-automation/v1/spot-groups/search



| Type | Message |
| :--- | :--- |
| Request | [SpotGroupQuery](spot-group.md#spotgroupquery) |
| Response |  [SpotGroupsInfo](spot-group.md#spotgroupsinfo)  |
 
 

 
### interrupt
> **POST** /spot-automation/v1/spot-groups/interrupt
>


| Type | Message |
| :--- | :--- |
| Request | [InterruptRequest](spot-group.md#interruptrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### stat
> **POST** /spot-automation/v1/spot-groups/stat
>


| Type | Message |
| :--- | :--- |
| Request | [SpotGroupStatQuery](spot-group.md#spotgroupstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateSpotGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | resource_id |string|✅| |
| 3 | resource_type |string|✅| |
| 4 | provider |string|✅| |
| 5 | options |[SpotGroupOptions](spot-group.md#spotgroupoptions)|❌| |
| 6 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 7 | user_id |string|✅| |
| 8 | project_id |string|✅| |
| 9 | domain_id |string|✅| |

### GetSpotGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | spot_group_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### InterruptRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | provider |string|✅| |
| 2 | data |string|✅| |

### SpotGroupInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | spot_group_id |string | |
| 2 | name |string | |
| 3 | resource_id |string | |
| 4 | resource_type |string | |
| 5 | provider |string | |
| 6 | options |[SpotGroupOptions](spot-group.md#spotgroupoptions) | |
| 7 | project_id |string | |
| 8 | tags |list of spaceone.api.core.v1.Tag | |
| 9 | domain_id |string | |
| 10 | created_by |string | |
| 11 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | |

### SpotGroupOptions
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">min_ondemand_size</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">min_ondemand_ratio</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">recommend_types</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">replace_strategy</td>
      <td style="text-align:left"><ul>
          	<li>CHEAPEST</li>
          	<li>OPTIMAL</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### SpotGroupQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | spot_group_id |string|❌| |
| 3 | name |string|❌| |
| 4 | resource_id |string|❌| |
| 5 | resource_type |string|❌| |
| 6 | provider |string|❌| |
| 7 | project_id |string|❌| |
| 8 | domain_id |string|✅| |

### SpotGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | spot_group_id |string|✅| |
| 2 | domain_id |string|✅| |

### SpotGroupStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### SpotGroupsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of SpotGroupInfo](spot-group.md#spotgroupinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateSpotGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | spot_group_id |string|✅| |
| 2 | name |string|❌| |
| 3 | options |[SpotGroupOptions](spot-group.md#spotgroupoptions)|❌| |
| 4 | tags |list of spaceone.api.core.v1.Tag|| |
| 5 | domain_id |string|✅| |
