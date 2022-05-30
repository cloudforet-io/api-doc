---
description:  
---
# Schedule

>  **Package : spaceone.api.cost_analysis.v1**

## Schedule

{% hint style="info" %}
**Schedule Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](schedule.md#create)|   [CreateScheduleRequest](schedule.md#createschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |
| [**update**](schedule.md#update)|   [UpdateScheduleRequest](schedule.md#updateschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |
| [**enable**](schedule.md#enable)|   [ScheduleRequest](schedule.md#schedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |
| [**disable**](schedule.md#disable)|   [ScheduleRequest](schedule.md#schedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |
| [**delete**](schedule.md#delete)|   [ScheduleRequest](schedule.md#schedulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](schedule.md#get)|   [GetScheduleRequest](schedule.md#getschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |
| [**list**](schedule.md#list)|   [ScheduleQuery](schedule.md#schedulequery) |   [SchedulesInfo](schedule.md#schedulesinfo) |
| [**stat**](schedule.md#stat)|   [ScheduleStatQuery](schedule.md#schedulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /cost-analysis/v1/schedules
>


| Type | Message |
| :--- | :--- |
| Request | [CreateScheduleRequest](schedule.md#createschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### update
> **PUT** /cost-analysis/v1/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateScheduleRequest](schedule.md#updateschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### enable
> **PUT** /cost-analysis/v1/schedule/{schedule_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](schedule.md#schedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### disable
> **PUT** /cost-analysis/v1/schedule/{schedule_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](schedule.md#schedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### delete
> **DELETE** /cost-analysis/v1/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](schedule.md#schedulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /cost-analysis/v1/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetScheduleRequest](schedule.md#getschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/schedules
>
> **POST** /cost-analysis/v1/schedules/search



| Type | Message |
| :--- | :--- |
| Request | [ScheduleQuery](schedule.md#schedulequery) |
| Response |  [SchedulesInfo](schedule.md#schedulesinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v1/schedules/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleStatQuery](schedule.md#schedulestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✘| |
| schedule |[Scheduled](schedule.md#scheduled)|✔| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| data_source_id |string|✔| |
| domain_id |string|✔| |

### GetScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

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
      <td style="text-align:left; width:100px;">schedule</td>
      <td style="text-align:left"><a href="schedule.md#scheduled">Scheduled</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data_source_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">last_scheduled_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### ScheduleQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| schedule_id |string|✘| |
| name |string|✘| |
| state |string|✘| |
| data_source_id |string|✘| |
| domain_id |string|✔| |

### ScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_id |string|✔| |
| domain_id |string|✔| |

### ScheduleStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### Scheduled
| Field | Type |  Description |
| :--- | :--- | :--- |
| cron |string | |
| interval |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| minutes |[list of int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| hours |[list of int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### SchedulesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ScheduleInfo](schedule.md#scheduleinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_id |string|✔| |
| name |string|✘| |
| schedule |[Scheduled](schedule.md#scheduled)|✘| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
