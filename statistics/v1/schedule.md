---
description:  
---
# Schedule

>  **Package : spaceone.api.statistics.v1**

## Schedule

{% hint style="info" %}
**Schedule Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**add**](schedule.md#add)|   [AddScheduleRequest](schedule.md#addschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| [**update**](schedule.md#update)|   [UpdateScheduleRequest](schedule.md#updateschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| [**enable**](schedule.md#enable)|   [ScheduleRequest](schedule.md#schedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| [**disable**](schedule.md#disable)|   [ScheduleRequest](schedule.md#schedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| [**delete**](schedule.md#delete)|   [ScheduleRequest](schedule.md#schedulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](schedule.md#get)|   [GetScheduleRequest](schedule.md#getschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| [**list**](schedule.md#list)|   [ScheduleQuery](schedule.md#schedulequery) |   [SchedulesInfo](schedule.md#schedulesinfo) |  |
| [**stat**](schedule.md#stat)|   [ScheduleStatQuery](schedule.md#schedulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**add**](schedule.md#add) </div> | <div style="width:200px; text-align:center;">    [AddScheduleRequest](schedule.md#addschedulerequest)  </div> | <div style="width:200px; text-align:center;">   [ScheduleInfo](schedule.md#scheduleinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](schedule.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateScheduleRequest](schedule.md#updateschedulerequest)  </div> | <div style="width:200px; text-align:center;">   [ScheduleInfo](schedule.md#scheduleinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**enable**](schedule.md#enable) </div> | <div style="width:200px; text-align:center;">    [ScheduleRequest](schedule.md#schedulerequest)  </div> | <div style="width:200px; text-align:center;">   [ScheduleInfo](schedule.md#scheduleinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**disable**](schedule.md#disable) </div> | <div style="width:200px; text-align:center;">    [ScheduleRequest](schedule.md#schedulerequest)  </div> | <div style="width:200px; text-align:center;">   [ScheduleInfo](schedule.md#scheduleinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](schedule.md#delete) </div> | <div style="width:200px; text-align:center;">    [ScheduleRequest](schedule.md#schedulerequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](schedule.md#get) </div> | <div style="width:200px; text-align:center;">    [GetScheduleRequest](schedule.md#getschedulerequest)  </div> | <div style="width:200px; text-align:center;">   [ScheduleInfo](schedule.md#scheduleinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](schedule.md#list) </div> | <div style="width:200px; text-align:center;">    [ScheduleQuery](schedule.md#schedulequery)  </div> | <div style="width:200px; text-align:center;">   [SchedulesInfo](schedule.md#schedulesinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](schedule.md#stat) </div> | <div style="width:200px; text-align:center;">    [ScheduleStatQuery](schedule.md#schedulestatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
### add
> **POST** /statistics/v1/schedules
>


| Type | Message |
| :--- | :--- |
| Request | [AddScheduleRequest](schedule.md#addschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### update
> **PUT** /statistics/v1/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateScheduleRequest](schedule.md#updateschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### enable
> **PUT** /statistics/v1/schedule/{schedule_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](schedule.md#schedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### disable
> **PUT** /statistics/v1/schedule/{schedule_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](schedule.md#schedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### delete
> **DELETE** /statistics/v1/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](schedule.md#schedulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /statistics/v1/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetScheduleRequest](schedule.md#getschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### list
> **GET** /statistics/v1/schedules
>
> **POST** /statistics/v1/schedules/search



| Type | Message |
| :--- | :--- |
| Request | [ScheduleQuery](schedule.md#schedulequery) |
| Response |  [SchedulesInfo](schedule.md#schedulesinfo)  |
 
 

 
### stat
> **POST** /statistics/v1/schedules/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleStatQuery](schedule.md#schedulestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### AddScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| topic |string|✅| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| schedule |[Scheduled](schedule.md#scheduled)|✅| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| user_id |string|✅| |
| domain_id |string|✅| |

### GetScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### QueryOption
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| aggregate |[StatAggregate](schedule.md#stataggregate)|✅| |
| page |[StatPage](schedule.md#statpage)|❌| |

### ScheduleInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">topic</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">schedule</td>
      <td style="text-align:left"><a href="schedule.md#scheduled">Scheduled</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">last_scheduled_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### ScheduleQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| schedule_id |string|❌| |
| topic |string|❌| |
| state |string|❌| |
| resource_type |string|❌| |
| domain_id |string|✅| |

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
| schedule_id |string|✅| |
| schedule |[Scheduled](schedule.md#scheduled)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| storage_id |string|✅| |
| domain_id |string|✅| |
