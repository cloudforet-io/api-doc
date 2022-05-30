---
description:  
---
# Schedule

>  **Package : spaceone.api.power_scheduler.v1**

## Schedule

{% hint style="info" %}
**Schedule Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](schedule.md#create)|   [CreateScheduleRequest](schedule.md#createschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| [**update**](schedule.md#update)|   [UpdateScheduleRequest](schedule.md#updateschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| [**enable**](schedule.md#enable)|   [ScheduleRequest](schedule.md#schedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| [**disable**](schedule.md#disable)|   [ScheduleRequest](schedule.md#schedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| [**append_resource_group**](schedule.md#append_resource_group)|   [CreateResourceGroupRequest](schedule.md#createresourcegrouprequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| [**update_resource_group**](schedule.md#update_resource_group)|   [ResourceGroupRequest](schedule.md#resourcegrouprequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| [**remove_resource_group**](schedule.md#remove_resource_group)|   [ResourceGroupRequest](schedule.md#resourcegrouprequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| [**delete**](schedule.md#delete)|   [ScheduleRequest](schedule.md#schedulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](schedule.md#get)|   [GetScheduleRequest](schedule.md#getschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| [**list**](schedule.md#list)|   [ScheduleQuery](schedule.md#schedulequery) |   [SchedulesInfo](schedule.md#schedulesinfo) |  |
| [**stat**](schedule.md#stat)|   [ScheduleStatQuery](schedule.md#schedulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

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
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateScheduleRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ScheduleInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateScheduleRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ScheduleInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">enable</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ScheduleRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ScheduleInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">disable</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ScheduleRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ScheduleInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">append_resource_group</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateResourceGroupRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ScheduleInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update_resource_group</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ResourceGroupRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ScheduleInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">remove_resource_group</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ResourceGroupRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ScheduleInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">delete</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ScheduleRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetScheduleRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ScheduleInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ScheduleQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   SchedulesInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ScheduleStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
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
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_id |string|✅| |
| resource_group_id |string|✅| |
| priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| domain_id |string|✅| |

### CreateScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| user_id |string|✅| |
| project_id |string|✅| |
| domain_id |string|✅| |

### GetScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### ResourceGroup
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_group_id |string | |
| priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### ResourceGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_id |string|✅| |
| resource_group_id |string|✅| |
| priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✅| |
| domain_id |string|✅| |

### ScheduleInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource_groups</td>
      <td style="text-align:left"><a href="schedule.md#resourcegroup">list of ResourceGroup</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### ScheduleQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource_group_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### ScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_id |string|✅| |
| domain_id |string|✅| |

### ScheduleStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### SchedulesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ScheduleInfo](schedule.md#scheduleinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateScheduleRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>


