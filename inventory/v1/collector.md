---
description:  
---
# Collector

>  **Package : spaceone.api.inventory.v1**

## Collector

{% hint style="info" %}
**Collector Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](collector.md#create)|   [CreateCollectorRequest](collector.md#createcollectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |  |
| [**update**](collector.md#update)|   [UpdateCollectorRequest](collector.md#updatecollectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |  |
| [**update_plugin**](collector.md#update_plugin)|   [UpdatePluginRequest](collector.md#updatepluginrequest) |   [CollectorInfo](collector.md#collectorinfo) |  |
| [**verify_plugin**](collector.md#verify_plugin)|   [VerifyPluginRequest](collector.md#verifypluginrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**delete**](collector.md#delete)|   [CollectorRequest](collector.md#collectorrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](collector.md#get)|   [GetCollectorRequest](collector.md#getcollectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |  |
| [**enable**](collector.md#enable)|   [CollectorRequest](collector.md#collectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |  |
| [**disable**](collector.md#disable)|   [CollectorRequest](collector.md#collectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |  |
| [**list**](collector.md#list)|   [CollectorQuery](collector.md#collectorquery) |   [CollectorsInfo](collector.md#collectorsinfo) |  |
| [**stat**](collector.md#stat)|   [CollectorStatQuery](collector.md#collectorstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| [**collect**](collector.md#collect)|   [CollectRequest](collector.md#collectrequest) |   [JobInfo](collector.md#jobinfo) |  |
| [**add_schedule**](collector.md#add_schedule)|   [CreateScheduleRequest](collector.md#createschedulerequest) |   [ScheduleInfo](collector.md#scheduleinfo) |  |
| [**get_schedule**](collector.md#get_schedule)|   [ScheduleRequest](collector.md#schedulerequest) |   [ScheduleInfo](collector.md#scheduleinfo) |  |
| [**update_schedule**](collector.md#update_schedule)|   [UpdateScheduleRequest](collector.md#updateschedulerequest) |   [ScheduleInfo](collector.md#scheduleinfo) |  |
| [**delete_schedule**](collector.md#delete_schedule)|   [DeleteScheduleRequest](collector.md#deleteschedulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**list_schedules**](collector.md#list_schedules)|   [ScheduleQuery](collector.md#schedulequery) |   [SchedulesInfo](collector.md#schedulesinfo) |  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](collector.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateCollectorRequest](collector.md#createcollectorrequest)  </div> | <div style="width:200px; text-align:center;">   [CollectorInfo](collector.md#collectorinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](collector.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateCollectorRequest](collector.md#updatecollectorrequest)  </div> | <div style="width:200px; text-align:center;">   [CollectorInfo](collector.md#collectorinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update_plugin**](collector.md#update_plugin) </div> | <div style="width:200px; text-align:center;">    [UpdatePluginRequest](collector.md#updatepluginrequest)  </div> | <div style="width:200px; text-align:center;">   [CollectorInfo](collector.md#collectorinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**verify_plugin**](collector.md#verify_plugin) </div> | <div style="width:200px; text-align:center;">    [VerifyPluginRequest](collector.md#verifypluginrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](collector.md#delete) </div> | <div style="width:200px; text-align:center;">    [CollectorRequest](collector.md#collectorrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](collector.md#get) </div> | <div style="width:200px; text-align:center;">    [GetCollectorRequest](collector.md#getcollectorrequest)  </div> | <div style="width:200px; text-align:center;">   [CollectorInfo](collector.md#collectorinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**enable**](collector.md#enable) </div> | <div style="width:200px; text-align:center;">    [CollectorRequest](collector.md#collectorrequest)  </div> | <div style="width:200px; text-align:center;">   [CollectorInfo](collector.md#collectorinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**disable**](collector.md#disable) </div> | <div style="width:200px; text-align:center;">    [CollectorRequest](collector.md#collectorrequest)  </div> | <div style="width:200px; text-align:center;">   [CollectorInfo](collector.md#collectorinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](collector.md#list) </div> | <div style="width:200px; text-align:center;">    [CollectorQuery](collector.md#collectorquery)  </div> | <div style="width:200px; text-align:center;">   [CollectorsInfo](collector.md#collectorsinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](collector.md#stat) </div> | <div style="width:200px; text-align:center;">    [CollectorStatQuery](collector.md#collectorstatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**collect**](collector.md#collect) </div> | <div style="width:200px; text-align:center;">    [CollectRequest](collector.md#collectrequest)  </div> | <div style="width:200px; text-align:center;">   [JobInfo](collector.md#jobinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**add_schedule**](collector.md#add_schedule) </div> | <div style="width:200px; text-align:center;">    [CreateScheduleRequest](collector.md#createschedulerequest)  </div> | <div style="width:200px; text-align:center;">   [ScheduleInfo](collector.md#scheduleinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get_schedule**](collector.md#get_schedule) </div> | <div style="width:200px; text-align:center;">    [ScheduleRequest](collector.md#schedulerequest)  </div> | <div style="width:200px; text-align:center;">   [ScheduleInfo](collector.md#scheduleinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update_schedule**](collector.md#update_schedule) </div> | <div style="width:200px; text-align:center;">    [UpdateScheduleRequest](collector.md#updateschedulerequest)  </div> | <div style="width:200px; text-align:center;">   [ScheduleInfo](collector.md#scheduleinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete_schedule**](collector.md#delete_schedule) </div> | <div style="width:200px; text-align:center;">    [DeleteScheduleRequest](collector.md#deleteschedulerequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list_schedules**](collector.md#list_schedules) </div> | <div style="width:200px; text-align:center;">    [ScheduleQuery](collector.md#schedulequery)  </div> | <div style="width:200px; text-align:center;">   [SchedulesInfo](collector.md#schedulesinfo)  </div> | <div style="width:400px;">  </div> | 
 

 
### create
> **POST** /inventory/v1/collectors
>


| Type | Message |
| :--- | :--- |
| Request | [CreateCollectorRequest](collector.md#createcollectorrequest) |
| Response |  [CollectorInfo](collector.md#collectorinfo)  |
 
 

 
### update
> **PUT** /inventory/v1/collector/{collector_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateCollectorRequest](collector.md#updatecollectorrequest) |
| Response |  [CollectorInfo](collector.md#collectorinfo)  |
 
 

 
### update_plugin
> **PUT** /inventory/v1/collector/{collector_id}/plugin
>


| Type | Message |
| :--- | :--- |
| Request | [UpdatePluginRequest](collector.md#updatepluginrequest) |
| Response |  [CollectorInfo](collector.md#collectorinfo)  |
 
 

 
### verify_plugin
> **POST** /inventory/v1/collector/{collector_id}/plugin/verify
>


| Type | Message |
| :--- | :--- |
| Request | [VerifyPluginRequest](collector.md#verifypluginrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### delete
> **DELETE** /inventory/v1/collector/{collector_id}
>


| Type | Message |
| :--- | :--- |
| Request | [CollectorRequest](collector.md#collectorrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /inventory/v1/collector/{collector_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetCollectorRequest](collector.md#getcollectorrequest) |
| Response |  [CollectorInfo](collector.md#collectorinfo)  |
 
 

 
### enable
> **PUT** /inventory/v1/collector/{collector_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [CollectorRequest](collector.md#collectorrequest) |
| Response |  [CollectorInfo](collector.md#collectorinfo)  |
 
 

 
### disable
> **PUT** /inventory/v1/collector/{collector_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [CollectorRequest](collector.md#collectorrequest) |
| Response |  [CollectorInfo](collector.md#collectorinfo)  |
 
 

 
### list
> **GET** /inventory/v1/collectors
>
> **POST** /inventory/v1/collectors/search



| Type | Message |
| :--- | :--- |
| Request | [CollectorQuery](collector.md#collectorquery) |
| Response |  [CollectorsInfo](collector.md#collectorsinfo)  |
 
 

 
### stat
> **POST** /inventory/v1/collectors/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CollectorStatQuery](collector.md#collectorstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |
 
 

 
### collect
> **POST** /inventory/v1/collector/{collector_id}/collect
>


| Type | Message |
| :--- | :--- |
| Request | [CollectRequest](collector.md#collectrequest) |
| Response |  [JobInfo](collector.md#jobinfo)  |
 
 

 
### add_schedule
> **POST** /inventory/v1/collector/{collector_id}/schedule
>


| Type | Message |
| :--- | :--- |
| Request | [CreateScheduleRequest](collector.md#createschedulerequest) |
| Response |  [ScheduleInfo](collector.md#scheduleinfo)  |
 
 

 
### get_schedule
> **GET** /inventory/v1/collector/{collector_id}/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](collector.md#schedulerequest) |
| Response |  [ScheduleInfo](collector.md#scheduleinfo)  |
 
 

 
### update_schedule
> **POST** /inventory/v1/collector/{collector_id}/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateScheduleRequest](collector.md#updateschedulerequest) |
| Response |  [ScheduleInfo](collector.md#scheduleinfo)  |
 
 

 
### delete_schedule
> **DELETE** /inventory/v1/collector/{collector_id}/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DeleteScheduleRequest](collector.md#deleteschedulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### list_schedules
> **GET** /inventory/v1/collector/{collector_id}/schedules
>
> **POST** /inventory/v1/collector/{collector_id}/schedules/search



| Type | Message |
| :--- | :--- |
| Request | [ScheduleQuery](collector.md#schedulequery) |
| Response |  [SchedulesInfo](collector.md#schedulesinfo)  |


## 

## Message

### CollectRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| collector_id |string|✅| |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| secret_id |string|❌| |
| collect_mode |string|❌| |
| domain_id |string|✅| |
| use_cache |bool|❌| |

### CollectorInfo
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
      <td style="text-align:left">collector_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">name</td>
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
      <td style="text-align:left">plugin_info</td>
      <td style="text-align:left"><a href="collector.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">priority</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">last_collected_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">is_public</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### CollectorQuery
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
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">collector_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">name</td>
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
      <td style="text-align:left">priority</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### CollectorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| collector_id |string|✅| |
| domain_id |string|✅| |

### CollectorStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### CollectorsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CollectorInfo](collector.md#collectorinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateCollectorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| plugin_info |[PluginInfo](collector.md#plugininfo)|✅| |
| priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
| is_public |bool|❌| default is true|
| project_id |string|✅| if is_public is false, project_id is requireremained as is_public | True | False|

### CreateScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✅| |
| collector_id |string|✅| |
| name |string|❌| |
| collect_mode |string|❌| |
| schedule |[Scheduled](collector.md#scheduled)|✅| |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### DeleteScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✅| |
| schedule_id |string|✅| |
| collector_id |string|✅| |

### ErrorInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| error_code |string | |
| message |string | |
| additional |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### GetCollectorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| collector_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### JobInfo
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
      <td style="text-align:left">job_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">status</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>CREATED</li>
          	<li>CANCELED</li>
          	<li>IN_PROGRESS</li>
          	<li>SUCCESS</li>
          	<li>ERROR</li>
          	<li>TIMEOUT</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">filter</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">total_tasks</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">remained_tasks</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">errors</td>
      <td style="text-align:left"><a href="collector.md#errorinfo">list of ErrorInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">collector_info</td>
      <td style="text-align:left"><a href="collector.md#collectorinfo">CollectorInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
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
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">finished_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### PluginInfo
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
      <td style="text-align:left">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">secret_group_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">service_account_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">metadata</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>MANUAL</li>
          	<li>AUTO</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### ScheduleInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| domain_id |string | |
| schedule_id |string | |
| name |string | |
| collect_mode |string | |
| schedule |[Scheduled](collector.md#scheduled) | |
| created_at |string | |
| last_scheduled_at |string | |
| collector_info |[CollectorInfo](collector.md#collectorinfo) | |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### ScheduleQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| collector_id |string|✅| |
| schedule_id |string|❌| |
| domain_id |string|✅| |

### ScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✅| |
| schedule_id |string|✅| |
| collector_id |string|✅| |

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
| results |[list of ScheduleInfo](collector.md#scheduleinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateCollectorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| collector_id |string|✅| |
| name |string|❌| |
| plugin_info |[PluginInfo](collector.md#plugininfo)|❌| |
| priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### UpdatePluginRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">collector_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>MANUAL</li>
          	<li>AUTO</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### UpdateScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✅| |
| schedule_id |string|✅| |
| collector_id |string|✅| |
| name |string|❌| |
| collect_mode |string|❌| |
| schedule |[Scheduled](collector.md#scheduled)|❌| |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### VerifyInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| status |bool | |

### VerifyPluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| collector_id |string|✅| |
| secret_id |string|❌| |
| domain_id |string|✅| |
