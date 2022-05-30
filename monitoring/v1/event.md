---
description:  
---
# Event

>  **Package : spaceone.api.monitoring.v1**

## Event

{% hint style="info" %}
**{{ service.name }} Methods:**
{{ service.description }}
{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](event.md#create)|   [CreateEventRequest](event.md#createeventrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](event.md#get)|   [GetEventRequest](event.md#geteventrequest) |   [EventInfo](event.md#eventinfo) |
| [**list**](event.md#list)|   [EventQuery](event.md#eventquery) |   [EventsInfo](event.md#eventsinfo) |
| [**stat**](event.md#stat)|   [EventStatQuery](event.md#eventstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
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
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| webhook_id |string|✔| |
| access_key |string|✔| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |

### EventInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| event_id |string | |
| event_key |string | |
| event_type |string | |
| title |string | |
| description |string | |
| severity |string | |
| rule |string | |
| resource |[EventResource](event.md#eventresource) | |
| provider |string | |
| account |string | |
| image_url |string | |
| raw_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| alert_id |string | |
| webhook_id |string | |
| project_id |string | |
| domain_id |string | |
| created_at |string | |
| occurred_at |string | |

### EventQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| event_id |string|✘| |
| event_key |string|✘| |
| event_type |string|✘| |
| severity |string|✘| |
| resource_id |string|✘| |
| provider |string|✘| |
| account |string|✘| |
| alert_id |string|✘| |
| webhook_id |string|✘| |
| project_id |string|✘| |
| domain_id |string|✘| |

### EventResource
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_id |string | |
| resource_type |string | |
| name |string | |

### EventStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### EventsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of EventInfo](event.md#eventinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetEventRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| event_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |
