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
| 3 | [**delete**](schedule.md#delete)|   [ScheduleRequest](schedule.md#schedulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](schedule.md#get)|   [GetScheduleRequest](schedule.md#getschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |  |
| 5 | [**list**](schedule.md#list)|   [ScheduleQuery](schedule.md#schedulequery) |   [SchedulesInfo](schedule.md#schedulesinfo) |  |
| 6 | [**stat**](schedule.md#stat)|   [ScheduleStatQuery](schedule.md#schedulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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

### CreateScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 3 | project_id |string|✅| |
| 4 | domain_id |string|✅| |

### GetScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | schedule_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |string|❌| |

### ResourceGroup
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | resource_group_id |string| |
| 2 | priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)| |

### ScheduleInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | schedule_id |string| |
| 2 | name |string| |
| 3 | state |string| |
| 4 | resource_groups |[ResourceGroup](schedule.md#resourcegroup)| |
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| |
| 6 | project_id |string| |
| 7 | domain_id |string| |
| 8 | created_by |string| |
| 9 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto)| |

### ScheduleQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | schedule_id |string|❌| |
| 3 | name |string|❌| |
| 4 | state |string|✅| |
| 5 | resource_group_id |string|✅| |
| 6 | project_id |string|✅| |
| 7 | domain_id |string|✅| |

### ScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | schedule_id |string|✅| |
| 2 | domain_id |string|✅| |

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

### UpdateScheduleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | schedule_id |string|✅| |
| 2 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 3 | domain_id |string|✅| |
