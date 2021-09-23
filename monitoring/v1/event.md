---
description:  
---
# Event

>  **Package : spaceone.api.monitoring.v1**

## Event

{% hint style="info" %}
**Event Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](event.md#create)|   [CreateEventRequest](event.md#createeventrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 2 | [**get**](event.md#get)|   [GetEventRequest](event.md#geteventrequest) |   [EventInfo](event.md#eventinfo) |  |
| 3 | [**list**](event.md#list)|   [EventQuery](event.md#eventquery) |   [EventsInfo](event.md#eventsinfo) |  |
| 4 | [**stat**](event.md#stat)|   [EventStatQuery](event.md#eventstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /monitoring/v1/webhook/{webhook_id}/{access_key}/events
>


| Type | Message |
| :--- | :--- |
| Request | [CreateEventRequest](event.md#createeventrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /monitoring/v1/event/{event_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetEventRequest](event.md#geteventrequest) |
| Response |  [EventInfo](event.md#eventinfo)  |
 
 

 
### list
> **GET** /monitoring/v1/events
>
> **POST** /monitoring/v1/events/search



| Type | Message |
| :--- | :--- |
| Request | [EventQuery](event.md#eventquery) |
| Response |  [EventsInfo](event.md#eventsinfo)  |
 
 

 
### stat
> **POST** /monitoring/v1/events/stat
>


| Type | Message |
| :--- | :--- |
| Request | [EventStatQuery](event.md#eventstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateEventRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | webhook_id |string|✅| |
| 2 | access_key |string|✅| |
| 3 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### EventInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | event_id |string | |
| 2 | event_key |string | |
| 3 | event_type |string | |
| 4 | title |string | |
| 5 | description |string | |
| 6 | severity |string | |
| 7 | rule |string | |
| 8 | resource |[EventResource](event.md#eventresource) | |
| 9 | raw_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 10 | additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 11 | image_url |string | |
| 12 | alert_id |string | |
| 13 | webhook_id |string | |
| 14 | project_id |string | |
| 15 | domain_id |string | |
| 16 | created_at |string | |
| 17 | occurred_at |string | |

### EventQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | event_id |string|❌| |
| 3 | event_key |string|❌| |
| 4 | event_type |string|❌| |
| 5 | severity |string|❌| |
| 6 | resource_id |string|❌| |
| 7 | alert_id |string|❌| |
| 8 | webhook_id |string|❌| |
| 9 | project_id |string|❌| |
| 10 | domain_id |string|❌| |

### EventResource
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | resource_id |string | |
| 2 | resource_type |string | |
| 3 | name |string | |

### EventStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### EventsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of EventInfo](event.md#eventinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetEventRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | event_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |
