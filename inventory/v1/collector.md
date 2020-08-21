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
| 1 | [**create**](collector.md#create)|   [CreateCollectorRequest](collector.md#createcollectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |  |
| 2 | [**update**](collector.md#update)|   [UpdateCollectorRequest](collector.md#updatecollectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |  |
| 3 | [**update_plugin**](collector.md#update_plugin)|   [UpdatePluginRequest](collector.md#updatepluginrequest) |   [CollectorInfo](collector.md#collectorinfo) |  |
| 4 | [**verify_plugin**](collector.md#verify_plugin)|   [VerifyPluginRequest](collector.md#verifypluginrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**delete**](collector.md#delete)|   [CollectorRequest](collector.md#collectorrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 6 | [**get**](collector.md#get)|   [GetCollectorRequest](collector.md#getcollectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |  |
| 7 | [**enable**](collector.md#enable)|   [CollectorRequest](collector.md#collectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |  |
| 8 | [**disable**](collector.md#disable)|   [CollectorRequest](collector.md#collectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |  |
| 9 | [**list**](collector.md#list)|   [CollectorQuery](collector.md#collectorquery) |   [CollectorsInfo](collector.md#collectorsinfo) |  |
| 10 | [**stat**](collector.md#stat)|   [CollectorStatQuery](collector.md#collectorstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| 11 | [**collect**](collector.md#collect)|   [CollectRequest](collector.md#collectrequest) |   [JobInfo](collector.md#jobinfo) |  |
| 12 | [**add_schedule**](collector.md#add_schedule)|   [CreateScheduleRequest](collector.md#createschedulerequest) |   [ScheduleInfo](collector.md#scheduleinfo) |  |
| 13 | [**get_schedule**](collector.md#get_schedule)|   [ScheduleRequest](collector.md#schedulerequest) |   [ScheduleInfo](collector.md#scheduleinfo) |  |
| 14 | [**update_schedule**](collector.md#update_schedule)|   [UpdateScheduleRequest](collector.md#updateschedulerequest) |   [ScheduleInfo](collector.md#scheduleinfo) |  |
| 15 | [**delete_schedule**](collector.md#delete_schedule)|   [DeleteScheduleRequest](collector.md#deleteschedulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 16 | [**list_schedules**](collector.md#list_schedules)|   [ScheduleQuery](collector.md#schedulequery) |   [SchedulesInfo](collector.md#schedulesinfo) |  | 
 

 
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
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | collector_id |string|✅| |
| 2 | filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 3 | secret_id |string|❌| |
| 4 | collect_mode |string|❌| |
| 5 | domain_id |string|✅| |
| 6 | use_cache |bool|❌| |

### CollectorInfo
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
      <td style="text-align:left">collector_id</td>
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
      <td style="text-align:left">plugin_info</td>
      <td style="text-align:left"><a href="collector.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">priority</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">last_collected_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">is_public</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">13</td>
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
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">collector_id</td>
      <td style="text-align:left">string</td>
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
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">priority</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### CollectorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | collector_id |string|✅| |
| 2 | domain_id |string|✅| |

### CollectorStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### CollectorsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[CollectorInfo](collector.md#collectorinfo)| |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)| |

### CreateCollectorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | plugin_info |[PluginInfo](collector.md#plugininfo)|✅| |
| 3 | priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | domain_id |string|✅| |
| 6 | is_public |bool|❌| default is true|
| 7 | project_id |string|❌| if is_public is false, project_id is required|

### CreateScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | collector_id |string|✅| |
| 3 | name |string|❌| |
| 4 | collect_mode |string|❌| |
| 5 | schedule |[Scheduled](collector.md#scheduled)|✅| |
| 6 | filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### DeleteScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | schedule_id |string|✅| |
| 3 | collector_id |string|✅| |

### ErrorInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | error_code |string| |
| 2 | message |string| |
| 3 | additional |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| |

### GetCollectorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | collector_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |string|❌| |

### JobInfo
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
      <td style="text-align:left">job_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
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
      <td style="text-align:left">3</td>
      <td style="text-align:left">filter</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">total_tasks</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">remained_tasks</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">errors</td>
      <td style="text-align:left"><a href="collector.md#errorinfo">ErrorInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">collector_info</td>
      <td style="text-align:left"><a href="collector.md#collectorinfo">CollectorInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">finished_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### PluginInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | plugin_id |string| |
| 2 | version |string| |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| |
| 4 | secret_id |string| |
| 5 | secret_group_id |string| |
| 6 | provider |string| |
| 7 | service_account_id |string| |
| 8 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| |

### ScheduleInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | domain_id |string| |
| 2 | schedule_id |string| |
| 3 | name |string| |
| 4 | collect_mode |string| |
| 5 | schedule |[Scheduled](collector.md#scheduled)| |
| 6 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto)| |
| 7 | last_scheduled_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto)| |
| 8 | collector_info |[CollectorInfo](collector.md#collectorinfo)| |
| 9 | filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| |

### ScheduleQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | collector_id |string|✅| |
| 3 | schedule_id |string|❌| |
| 4 | domain_id |string|✅| |

### ScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | schedule_id |string|✅| |
| 3 | collector_id |string|✅| |

### Scheduled
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | cron |string| |
| 2 | interval |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)| |
| 3 | minutes |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)| |
| 4 | hours |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)| |

### SchedulesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[ScheduleInfo](collector.md#scheduleinfo)| |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)| |

### UpdateCollectorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | collector_id |string|✅| |
| 2 | name |string|❌| |
| 3 | plugin_info |[PluginInfo](collector.md#plugininfo)|❌| |
| 4 | priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 6 | domain_id |string|✅| |

### UpdatePluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | collector_id |string|✅| |
| 2 | version |string|❌| |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | domain_id |string|✅| |

### UpdateScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | schedule_id |string|✅| |
| 3 | collector_id |string|✅| |
| 4 | name |string|❌| |
| 5 | collect_mode |string|❌| |
| 6 | schedule |[Scheduled](collector.md#scheduled)|❌| |
| 7 | filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### VerifyInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | status |bool| |

### VerifyPluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | collector_id |string|✅| |
| 2 | secret_id |string|❌| |
| 3 | domain_id |string|✅| |
