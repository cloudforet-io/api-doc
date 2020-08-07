---
description:  
---
# Schedule

>  **Package : spaceone.api.report.v1**

## Schedule

{% hint style="info" %}
**Schedule Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**get**](schedule.md#get)|   [GetScheduleRequest](schedule.md#getschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| 2 | [**list**](schedule.md#list)|   [ScheduleQuery](schedule.md#schedulequery) |   [SchedulesInfo](schedule.md#schedulesinfo) |  |
| 3 | [**add**](schedule.md#add)|   [AddScheduleRequest](schedule.md#addschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| 4 | [**delete**](schedule.md#delete)|   [DeleteScheduleRequest](schedule.md#deleteschedulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**enable**](schedule.md#enable)|   [EnableScheduleRequest](schedule.md#enableschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| 6 | [**disable**](schedule.md#disable)|   [DisableScheduleRequest](schedule.md#disableschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| 7 | [**stat**](schedule.md#stat)|   [ScheduleStatQuery](schedule.md#schedulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### get
> **GET** /report/v1/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetScheduleRequest](schedule.md#getschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### list
> **GET** /report/v1/schedules
>
> **POST** /report/v1/schedules/search



| Type | Message |
| :--- | :--- |
| Request | [ScheduleQuery](schedule.md#schedulequery) |
| Response |  [SchedulesInfo](schedule.md#schedulesinfo)  |
 
 

 
### add
> **POST** /report/v1/schedule
>


| Type | Message |
| :--- | :--- |
| Request | [AddScheduleRequest](schedule.md#addschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### delete
> **DELETE** /report/v1/schedule/{schedule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DeleteScheduleRequest](schedule.md#deleteschedulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### enable
> **PUT** /report/v1/schedule/{schedule_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [EnableScheduleRequest](schedule.md#enableschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### disable
> **PUT** /report/v1/schedule/{schedule_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [DisableScheduleRequest](schedule.md#disableschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
 
 

 
### stat
> **POST** /report/v1/schedules/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleStatQuery](schedule.md#schedulestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### AddScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | name |string|✅| |
| 3 | template_id |string|✅| |
| 4 | storage_id |string|✅| |
| 5 | schedule |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 6 | template_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### DeleteScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | schedule_id |string|✅| |

### DisableScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | schedule_id |string|✅| |

### EnableScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | schedule_id |string|✅| |

### GetScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | schedule_id |string|✅| |
| 3 | only |string|❌| |

### ScheduleInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | domain_id |string| |
| 2 | schedule_id |string| |
| 3 | name |string| |
| 4 | template_id |string| |
| 5 | template_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| |
| 6 | storage_id |string| |
| 7 | schedule |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| |
| 8 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto)| |
| 9 | last_schedule_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto)| |

### ScheduleQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 3 | schedule_id |string|❌| |
| 4 | name |string|❌| |
| 5 | template_id |string|❌| |
| 6 | storage_id |string|❌| |
| 7 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto)|❌| |

### ScheduleStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### SchedulesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[ScheduleInfo](schedule.md#scheduleinfo)| |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)| |
