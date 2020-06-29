---
description:  
---
# Collector

>  **Package : spaceone.api.inventory.v1**

## Collector

{% hint style="info" %}
**Collector Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Collector.md#create)| [CreateCollectorRequest](Collector.md#createcollectorrequest) | [CollectorInfo](Collector.md#collectorinfo) |  |
| 2 | [update](Collector.md#update)| [UpdateCollectorRequest](Collector.md#updatecollectorrequest) | [CollectorInfo](Collector.md#collectorinfo) |  |
| 3 | [delete](Collector.md#delete)| [CollectorRequest](Collector.md#collectorrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Collector.md#get)| [GetCollectorRequest](Collector.md#getcollectorrequest) | [CollectorInfo](Collector.md#collectorinfo) |  |
| 5 | [enable](Collector.md#enable)| [CollectorRequest](Collector.md#collectorrequest) | [CollectorInfo](Collector.md#collectorinfo) |  |
| 6 | [disable](Collector.md#disable)| [CollectorRequest](Collector.md#collectorrequest) | [CollectorInfo](Collector.md#collectorinfo) |  |
| 7 | [list](Collector.md#list)| [CollectorQuery](Collector.md#collectorquery) | [CollectorsInfo](Collector.md#collectorsinfo) |  |
| 8 | [stat](Collector.md#stat)| [CollectorStatQuery](Collector.md#collectorstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| 9 | [collect](Collector.md#collect)| [CollectRequest](Collector.md#collectrequest) | [JobInfo](Collector.md#jobinfo) |  |
| 10 | [verify_plugin](Collector.md#verify_plugin)| [VerifyPluginRequest](Collector.md#verifypluginrequest) | [VerifyInfo](Collector.md#verifyinfo) |  |
| 11 | [add_schedule](Collector.md#add_schedule)| [CreateScheduleRequest](Collector.md#createschedulerequest) | [ScheduleInfo](Collector.md#scheduleinfo) |  |
| 12 | [get_schedule](Collector.md#get_schedule)| [ScheduleRequest](Collector.md#schedulerequest) | [ScheduleInfo](Collector.md#scheduleinfo) |  |
| 13 | [update_schedule](Collector.md#update_schedule)| [UpdateScheduleRequest](Collector.md#updateschedulerequest) | [ScheduleInfo](Collector.md#scheduleinfo) |  |
| 14 | [delete_schedule](Collector.md#delete_schedule)| [DeleteScheduleRequest](Collector.md#deleteschedulerequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 15 | [list_schedules](Collector.md#list_schedules)| [ScheduleQuery](Collector.md#schedulequery) | [SchedulesInfo](Collector.md#schedulesinfo) |  |

### create
> **POST** /inventory/v1/collectors
>



| Type | Message |
| :--- | :--- |
| Request | [CreateCollectorRequest](Collector.md#createcollectorrequest) |
| Response |  [CollectorInfo](Collector.md#collectorinfo)  |



### update
> **PUT** /inventory/v1/collector/{collector_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateCollectorRequest](Collector.md#updatecollectorrequest) |
| Response |  [CollectorInfo](Collector.md#collectorinfo)  |



### delete
> **DELETE** /inventory/v1/collector/{collector_id}
>



| Type | Message |
| :--- | :--- |
| Request | [CollectorRequest](Collector.md#collectorrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /inventory/v1/collector/{collector_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetCollectorRequest](Collector.md#getcollectorrequest) |
| Response |  [CollectorInfo](Collector.md#collectorinfo)  |



### enable
> **PUT** /inventory/v1/collector/{collector_id}/enable
>



| Type | Message |
| :--- | :--- |
| Request | [CollectorRequest](Collector.md#collectorrequest) |
| Response |  [CollectorInfo](Collector.md#collectorinfo)  |



### disable
> **PUT** /inventory/v1/collector/{collector_id}/disable
>



| Type | Message |
| :--- | :--- |
| Request | [CollectorRequest](Collector.md#collectorrequest) |
| Response |  [CollectorInfo](Collector.md#collectorinfo)  |



### list
> **GET** /inventory/v1/collectors
>
> **POST** /inventory/v1/collectors/search




| Type | Message |
| :--- | :--- |
| Request | [CollectorQuery](Collector.md#collectorquery) |
| Response |  [CollectorsInfo](Collector.md#collectorsinfo)  |



### stat
> **POST** /inventory/v1/collectors/stat
>



| Type | Message |
| :--- | :--- |
| Request | [CollectorStatQuery](Collector.md#collectorstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |



### collect
> **POST** /inventory/v1/collector/{collector_id}/collect
>



| Type | Message |
| :--- | :--- |
| Request | [CollectRequest](Collector.md#collectrequest) |
| Response |  [JobInfo](Collector.md#jobinfo)  |



### verify_plugin
> **POST** /inventory/v1/collector/{collector_id}/plugin/verify
>



| Type | Message |
| :--- | :--- |
| Request | [VerifyPluginRequest](Collector.md#verifypluginrequest) |
| Response |  [VerifyInfo](Collector.md#verifyinfo)  |



### add_schedule
> **POST** /inventory/v1/collector/{collector_id}/schedule
>



| Type | Message |
| :--- | :--- |
| Request | [CreateScheduleRequest](Collector.md#createschedulerequest) |
| Response |  [ScheduleInfo](Collector.md#scheduleinfo)  |



### get_schedule
> **GET** /inventory/v1/collector/{collector_id}/schedule/{schedule_id}
>



| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](Collector.md#schedulerequest) |
| Response |  [ScheduleInfo](Collector.md#scheduleinfo)  |



### update_schedule
> **POST** /inventory/v1/collector/{collector_id}/schedule/{schedule_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateScheduleRequest](Collector.md#updateschedulerequest) |
| Response |  [ScheduleInfo](Collector.md#scheduleinfo)  |



### delete_schedule
> **DELETE** /inventory/v1/collector/{collector_id}/schedule/{schedule_id}
>



| Type | Message |
| :--- | :--- |
| Request | [DeleteScheduleRequest](Collector.md#deleteschedulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### list_schedules
> **GET** /inventory/v1/collector/{collector_id}/schedules
>
> **POST** /inventory/v1/collector/{collector_id}/schedules/search




| Type | Message |
| :--- | :--- |
| Request | [ScheduleQuery](Collector.md#schedulequery) |
| Response |  [SchedulesInfo](Collector.md#schedulesinfo)  |





## Message

### CollectRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | collector_id |string | ||
| 2 | filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 3 | secret_id |string | ||
| 4 | collect_mode |string | ||
| 5 | domain_id |string | ||
| 6 | use_cache |bool | |optional|

### CollectorInfo
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
      <td style="text-align:left">collector_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
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
<p>CollectorInfo.State</p>
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
      <td style="text-align:left">plugin_info</td>
      <td style="text-align:left">
<a href="Collector.md#plugininfo">PluginInfo</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">priority</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a>
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
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">last_collected_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">capability</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
  </tbody>
</table>


### CollectorQuery
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
      <td style="text-align:left">query</td>
      <td style="text-align:left">
<a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">collector_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">
<p>CollectorQuery.State</p>
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
      <td style="text-align:left">5</td>
      <td style="text-align:left">priority</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">plugin_id</td>
      <td style="text-align:left">

string

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
  </tbody>
</table>


### CollectorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | collector_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### CollectorStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### CollectorsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[CollectorInfo](Collector.md#collectorinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### CreateCollectorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | plugin_info |[PluginInfo](Collector.md#plugininfo) |✅ ||
| 3 | priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |❌ ||
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | domain_id |string |✅ ||

### CreateScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string | ||
| 2 | collector_id |string | ||
| 3 | name |string | ||
| 4 | collect_mode |string | ||
| 5 | schedule |[Scheduled](Collector.md#scheduled) | ||
| 6 | filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||

### DeleteScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string | ||
| 2 | schedule_id |string | ||
| 3 | collector_id |string | ||

### GetCollectorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | collector_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### JobInfo
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
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">job_id</td>
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
<p>JobInfo.State</p>
        <ul>
          	<li>NONE</li>
          	<li>CREATED</li>
          	<li>CANCELED</li>
          	<li>IN_PROGRESS</li>
          	<li>FINISHED</li>
          	<li>FAILURE</li>
          	<li>TIMEOUT</li>
        </ul>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">created_count</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">updated_count</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">collect_mode</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">finished_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">collector_info</td>
      <td style="text-align:left">
<a href="Collector.md#collectorinfo">CollectorInfo</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">filter</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">collected_resources</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
  </tbody>
</table>


### PluginInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | plugin_id |string | ||
| 2 | version |string | ||
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 4 | secret_id |string | ||
| 5 | secret_group_id |string | ||
| 6 | provider |string | ||

### ScheduleInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string | ||
| 2 | schedule_id |string | ||
| 3 | name |string | ||
| 4 | collect_mode |string | ||
| 5 | schedule |[Scheduled](Collector.md#scheduled) | ||
| 6 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||
| 7 | last_scheduled_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||
| 8 | collector_info |[CollectorInfo](Collector.md#collectorinfo) | ||
| 9 | filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||

### ScheduleQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) | ||
| 2 | collector_id |string | ||
| 3 | schedule_id |string | ||
| 4 | domain_id |string | ||

### ScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string | ||
| 2 | schedule_id |string | ||
| 3 | collector_id |string | ||

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
| 1 | results |[ScheduleInfo](Collector.md#scheduleinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### UpdateCollectorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | collector_id |string |✅ ||
| 2 | name |string |✅ ||
| 3 | plugin_info |[PluginInfo](Collector.md#plugininfo) |✅ ||
| 4 | priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |❌ ||
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 6 | domain_id |string |✅ ||

### UpdateScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string | ||
| 2 | schedule_id |string | ||
| 3 | collector_id |string | ||
| 4 | name |string | ||
| 5 | collect_mode |string | ||
| 6 | schedule |[Scheduled](Collector.md#scheduled) | ||
| 7 | filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||

### VerifyInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | status |bool | ||

### VerifyPluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | collector_id |string |✅ ||
| 2 | secret_id |string |✅ ||
| 3 | domain_id |string |✅ ||
