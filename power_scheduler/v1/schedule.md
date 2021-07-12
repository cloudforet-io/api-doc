---
description:  
---
# Schedule

>  **Package : spaceone.api.power_scheduler.v1**

## Schedule

{% hint style="info" %}
**Schedule Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](schedule.md#create)|   [CreateScheduleRequest](schedule.md#createschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| 2 | [**update**](schedule.md#update)|   [UpdateScheduleRequest](schedule.md#updateschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| 3 | [**enable**](schedule.md#enable)|   [ScheduleRequest](schedule.md#schedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| 4 | [**disable**](schedule.md#disable)|   [ScheduleRequest](schedule.md#schedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| 5 | [**append_resource_group**](schedule.md#append_resource_group)|   [CreateResourceGroupRequest](schedule.md#createresourcegrouprequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| 6 | [**update_resource_group**](schedule.md#update_resource_group)|   [ResourceGroupRequest](schedule.md#resourcegrouprequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| 7 | [**remove_resource_group**](schedule.md#remove_resource_group)|   [ResourceGroupRequest](schedule.md#resourcegrouprequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| 8 | [**delete**](schedule.md#delete)|   [ScheduleRequest](schedule.md#schedulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 9 | [**get**](schedule.md#get)|   [GetScheduleRequest](schedule.md#getschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| 10 | [**list**](schedule.md#list)|   [ScheduleQuery](schedule.md#schedulequery) |   [SchedulesInfo](schedule.md#schedulesinfo) |  |
| 11 | [**stat**](schedule.md#stat)|   [ScheduleStatQuery](schedule.md#schedulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /power-scheduler/v1/schedules
>


| Type | Message |
| :--- | :--- |
| Request | [CreateScheduleRequest](schedule.md#createschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### update
> **PUT** /power-scheduler/v1/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateScheduleRequest](schedule.md#updateschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### enable
> **PUT** /power-scheduler/v1/schedule/{schedule_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](schedule.md#schedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### disable
> **PUT** /power-scheduler/v1/schedule/{schedule_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](schedule.md#schedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### append_resource_group
> **PUT** /power-scheduler/v1/schedule/{schedule_id}/resource_group/{resource_group_id}/append
>


| Type | Message |
| :--- | :--- |
| Request | [CreateResourceGroupRequest](schedule.md#createresourcegrouprequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### update_resource_group
> **PUT** /power-scheduler/v1/schedule/{schedule_id}/resource_group/{resource_group_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ResourceGroupRequest](schedule.md#resourcegrouprequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### remove_resource_group
> **PUT** /power-scheduler/v1/schedule/{schedule_id}/resource_group/{resource_group_id}/remove
>


| Type | Message |
| :--- | :--- |
| Request | [ResourceGroupRequest](schedule.md#resourcegrouprequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### delete
> **DELETE** /power-scheduler/v1/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](schedule.md#schedulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /power-scheduler/v1/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetScheduleRequest](schedule.md#getschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### list
> **GET** /power-scheduler/v1/schedules
>
> **POST** /power-scheduler/v1/schedules/search



| Type | Message |
| :--- | :--- |
| Request | [ScheduleQuery](schedule.md#schedulequery) |
| Response |  [SchedulesInfo](schedule.md#schedulesinfo)  |
 
 

 
### stat
> **POST** /power-scheduler/v1/schedules/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleStatQuery](schedule.md#schedulestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateResourceGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | schedule_id |string|✅| |
| 2 | resource_group_id |string|✅| |
| 3 | priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| 4 | domain_id |string|✅| |

### CreateScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | name |string|✅| |
| 2 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 3 | user_id |string|✅| |
| 4 | project_id |string|✅| |
| 5 | domain_id |string|✅| |

### GetScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | schedule_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### ResourceGroup
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | resource_group_id |string | |
| 2 | priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### ResourceGroupRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | schedule_id |string|✅| |
| 2 | resource_group_id |string|✅| |
| 3 | priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✅| |
| 4 | domain_id |string|✅| |

### ScheduleInfo
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
      <td style="text-align:left">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">resource_groups</td>
      <td style="text-align:left"><a href="schedule.md#resourcegroup">list of ResourceGroup</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">created_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### ScheduleQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">resource_group_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### ScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | schedule_id |string|✅| |
| 2 | domain_id |string|✅| |

### ScheduleStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### SchedulesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of ScheduleInfo](schedule.md#scheduleinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateScheduleRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>


