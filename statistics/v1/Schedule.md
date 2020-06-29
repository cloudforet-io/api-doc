---
description:  
---
# Schedule

>  **Package : spaceone.api.statistics.v1**

## Schedule

{% hint style="info" %}
**Schedule Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [add](Schedule.md#add)| [AddScheduleRequest](Schedule.md#addschedulerequest) | [ScheduleInfo](Schedule.md#scheduleinfo) |  |
| 2 | [update](Schedule.md#update)| [UpdateScheduleRequest](Schedule.md#updateschedulerequest) | [ScheduleInfo](Schedule.md#scheduleinfo) |  |
| 3 | [enable](Schedule.md#enable)| [ScheduleRequest](Schedule.md#schedulerequest) | [ScheduleInfo](Schedule.md#scheduleinfo) |  |
| 4 | [disable](Schedule.md#disable)| [ScheduleRequest](Schedule.md#schedulerequest) | [ScheduleInfo](Schedule.md#scheduleinfo) |  |
| 5 | [delete](Schedule.md#delete)| [ScheduleRequest](Schedule.md#schedulerequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 6 | [get](Schedule.md#get)| [GetScheduleRequest](Schedule.md#getschedulerequest) | [ScheduleInfo](Schedule.md#scheduleinfo) |  |
| 7 | [list](Schedule.md#list)| [ScheduleQuery](Schedule.md#schedulequery) | [SchedulesInfo](Schedule.md#schedulesinfo) |  |
| 8 | [stat](Schedule.md#stat)| [ScheduleStatQuery](Schedule.md#schedulestatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### add
> **POST** /statistics/v1/schedules
>



| Type | Message |
| :--- | :--- |
| Request | [AddScheduleRequest](Schedule.md#addschedulerequest) |
| Response |  [ScheduleInfo](Schedule.md#scheduleinfo)  |



### update
> **PUT** /statistics/v1/schedule/{schedule_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateScheduleRequest](Schedule.md#updateschedulerequest) |
| Response |  [ScheduleInfo](Schedule.md#scheduleinfo)  |



### enable
> **PUT** /statistics/v1/schedule/{schedule_id}/enable
>



| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](Schedule.md#schedulerequest) |
| Response |  [ScheduleInfo](Schedule.md#scheduleinfo)  |



### disable
> **PUT** /statistics/v1/schedule/{schedule_id}/disable
>



| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](Schedule.md#schedulerequest) |
| Response |  [ScheduleInfo](Schedule.md#scheduleinfo)  |



### delete
> **DELETE** /statistics/v1/schedule/{schedule_id}
>



| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](Schedule.md#schedulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /statistics/v1/schedule/{schedule_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetScheduleRequest](Schedule.md#getschedulerequest) |
| Response |  [ScheduleInfo](Schedule.md#scheduleinfo)  |



### list
> **GET** /statistics/v1/schedules
>
> **POST** /statistics/v1/schedules/search




| Type | Message |
| :--- | :--- |
| Request | [ScheduleQuery](Schedule.md#schedulequery) |
| Response |  [SchedulesInfo](Schedule.md#schedulesinfo)  |



### stat
> **POST** /statistics/v1/schedules/stat
>



| Type | Message |
| :--- | :--- |
| Request | [ScheduleStatQuery](Schedule.md#schedulestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### AddScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | topic |string |✅ ||
| 2 | options |[QueryOption](Schedule.md#queryoption) |✅ ||
| 3 | schedule |[Scheduled](Schedule.md#scheduled) |✅ ||
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | domain_id |string |✅ ||

### GetScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | schedule_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### QueryOption
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | data_source_id |string |❌ ||
| 2 | resource_type |string |✅ ||
| 3 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 4 | join |[ScheduleJoinQuery](Schedule.md#schedulejoinquery) |❌ ||
| 5 | formulas |[ScheduleFormula](Schedule.md#scheduleformula) |❌ ||

### ScheduleFormula
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | formula |string |✅ ||

### ScheduleInfo
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
      <td style="text-align:left">schedule_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">topic</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">
<p>ScheduleInfo.State</p>
        <ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">options</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">schedule</td>
      <td style="text-align:left">
<a href="Schedule.md#scheduled">Scheduled</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">last_scheduled_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
  </tbody>
</table>


### ScheduleJoinQuery
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
      <td style="text-align:left">keys</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">type</td>
      <td style="text-align:left">
<p>ScheduleJoinQuery.JoinType</p>
        <ul>
          	<li>LEFT</li>
          	<li>RIGHT</li>
          	<li>OUTER</li>
          	<li>INNER</li>
        </ul>
</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">data_source_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">resource_type</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">✅</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left">
<a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query">spaceone.api.core.v1.StatisticsQuery</a>
</td><td style="text-align:left">✅</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
  </tbody>
</table>


### ScheduleQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | schedule_id |string |❌ ||
| 3 | topic |string |❌ ||
| 4 | state |string |❌ ||
| 5 | data_source_id |string |❌ ||
| 6 | resource_type |string |❌ ||
| 7 | domain_id |string |✅ ||

### ScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | schedule_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### ScheduleStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### Scheduled
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cron |string | ||
| 2 | interval |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||
| 3 | minutes |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||
| 4 | hours |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### SchedulesInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[ScheduleInfo](Schedule.md#scheduleinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### UpdateScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | schedule_id |string |✅ ||
| 2 | schedule |[Scheduled](Schedule.md#scheduled) |❌ ||
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | domain_id |string |✅ ||
