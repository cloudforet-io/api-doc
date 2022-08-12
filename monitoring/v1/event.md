---
description: An Event is an alarm raised by an external monitoring system and collected by a Cloudforet plugin.
---
# Event

>  **Package : spaceone.api.monitoring.v1**

## Event

{% hint style="info" %}
**Event Methods:**

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

> Creates a new Event. The Event creation process starts with validation checking whether the input data is from a webhook or not. After the input data is validated, the data is processed and used to create the Event.

| Type | Message |
| :--- | :--- |
| Request | [CreateEventRequest](event.md#createeventrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /monitoring/v1/event/{event_id}
>

> Gets a specific Event matching the input parameters, `event_id` and `domain_id`. Prints detailed information about the Event.

| Type | Message |
| :--- | :--- |
| Request | [GetEventRequest](event.md#geteventrequest) |
| Response |  [EventInfo](event.md#eventinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "event_id": "event-4e16ba3bd384",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "event_id": "event-4e16ba3bd384",
    "event_key": "cfbdd0cee08f0f2664dbef297c370017",
    "event_type": "ALERT",
    "title": "Notification of access to the SpaceONE bastion Host",
    "description": "SSH Access to stargate-dev-kubectl-amzl2 from spaceoneadm",
    "severity": "INFO",
    "resource": {
        "resource_id": "server-1187737cc0d9",
        "resource_type": "inventory.Server",
        "name": "stargate-dev-kubectl-amzl2"
    },
    "raw_data": {
        "resource": {
            "name": "stargate-dev-kubectl-amzl2",
            "resource_id": "server-1187737cc0d9",
            "resource_type": "inventory.Server"
        },
        "event_key": "cfbdd0cee08f0f2664dbef297c370017",
        "title": "Notification of access to the SpaceONE bastion Host",
        "severity": "INFO",
        "description": "SSH Access to stargate-dev-kubectl-amzl2 from spaceoneadm",
        "event_type": "ALERT",
        "additional_info": {
            "host": [],
            "user": "spaceoneadm"
        }
    },
    "additional_info": {
        "host": "[]",
        "user": "spaceoneadm"
    },
    "alert_id": "alert-06462f6cb54e",
    "webhook_id": "webhook-ff9e2eda678a",
    "project_id": "project-18655561c535",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-21T00:34:58.034Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /monitoring/v1/events
>
> **POST** /monitoring/v1/events/search


> Gets a list of all Events. You must specify the `domain_id`. You can use a query to get a filtered list of Events.

| Type | Message |
| :--- | :--- |
| Request | [EventQuery](event.md#eventquery) |
| Response |  [EventsInfo](event.md#eventsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "event_id": "event-4e16ba3bd384",
            "event_key": "cfbdd0cee08f0f2664dbef297c370017",
            "event_type": "ALERT",
            "title": "Notification of access to the SpaceONE bastion Host",
            "description": "SSH Access to stargate-dev-kubectl-amzl2 from spaceoneadm",
            "severity": "INFO",
            "resource": {
                "resource_id": "server-1187737cc0d9",
                "resource_type": "inventory.Server",
                "name": "stargate-dev-kubectl-amzl2"
            },
            "raw_data": {
                "resource": {
                    "name": "stargate-dev-kubectl-amzl2",
                    "resource_type": "inventory.Server",
                    "resource_id": "server-1187737cc0d9"
                },
                "event_key": "cfbdd0cee08f0f2664dbef297c370017",
                "additional_info": {
                    "user": "spaceoneadm",
                    "host": []
                },
                "severity": "INFO",
                "description": "SSH Access to stargate-dev-kubectl-amzl2 from spaceoneadm",
                "title": "Notification of access to the SpaceONE bastion Host",
                "event_type": "ALERT"
            },
            "additional_info": {
                "user": "spaceoneadm",
                "host": "[]"
            },
            "alert_id": "alert-06462f6cb54e",
            "webhook_id": "webhook-ff9e2eda678a",
            "project_id": "project-18655561c535",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-06-21T00:34:58.034Z"
        },
        {
            "event_id": "event-b178e1b71daf",
            "event_key": "abc16e5455c26ab7611bf8aa8d1020cc",
            "event_type": "ALERT",
            "title": "Notification of access to the SpaceONE bastion Host",
            "description": "SSH Access to stargate-dev-kubectl-amzl2 from glee@mz.co.kr",
            "severity": "INFO",
            "resource": {
                "resource_id": "server-1187737cc0d9",
                "resource_type": "inventory.Server",
                "name": "stargate-dev-kubectl-amzl2"
            },
            "raw_data": {
                "additional_info": {
                    "host": [
                        "125.131.104.40"
                    ],
                    "user": "glee@mz.co.kr"
                },
                "description": "SSH Access to stargate-dev-kubectl-amzl2 from glee@mz.co.kr",
                "severity": "INFO",
                "event_type": "ALERT",
                "title": "Notification of access to the SpaceONE bastion Host",
                "resource": {
                    "resource_type": "inventory.Server",
                    "name": "stargate-dev-kubectl-amzl2",
                    "resource_id": "server-1187737cc0d9"
                },
                "event_key": "abc16e5455c26ab7611bf8aa8d1020cc"
            },
            "additional_info": {
                "user": "glee@mz.co.kr",
                "host": "['125.131.104.40']"
            },
            "alert_id": "alert-332617cf2894",
            "webhook_id": "webhook-ff9e2eda678a",
            "project_id": "project-18655561c535",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-06-21T00:34:52.822Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
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
