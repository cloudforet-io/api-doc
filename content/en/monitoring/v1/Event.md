---
title: "Event"
linkTitle: "Event"
weight: 3
bookFlatSection: true
---
# [Event](#Event)
desc: An Event is an alarm raised by an external monitoring system and collected by a Cloudforet plugin.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Event


**Event Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Event#create) | [CreateEventRequest](Event#createeventrequest) | [Empty](./Event#empty) |
| [**get**](./Event#get) | [GetEventRequest](Event#geteventrequest) | [EventInfo](./Event#eventinfo) |
| [**list**](./Event#list) | [EventQuery](Event#eventquery) | [EventsInfo](./Event#eventsinfo) |
| [**stat**](./Event#stat) | [EventStatQuery](Event#eventstatquery) | [Struct](./Event#struct) |



    
<br>

### create

> **POST** /monitoring/v1/event/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /monitoring/v1/event/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /monitoring/v1/event/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /monitoring/v1/event/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateEventRequest
* **webhook_id** (string)  `Required` 

  *is_required: true*

    
* **access_key** (string)  `Required` 

  *is_required: true*

    
* **data** (Struct)  `Required` 

  *is_required: true*

    <br>

### EventInfo
* **event_id** (string)  `Required` 

    
* **event_key** (string)  `Required` 

    
* **event_type** (string)  `Required` 

    
* **title** (string)  `Required` 

    
* **description** (string)  `Required` 

    
* **severity** (string)  `Required` 

    
* **rule** (string)  `Required` 

    
* **resource** (EventResource)  `Required` 

    
* **provider** (string)  `Required` 

    
* **account** (string)  `Required` 

    
* **image_url** (string)  `Required` 

    
* **raw_data** (Struct)  `Required` 

    
* **additional_info** (Struct)  `Required` 

    
* **alert_id** (string)  `Required` 

    
* **webhook_id** (string)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **occurred_at** (string)  `Required` 

    <br>

### EventQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **event_id** (string)  `Required` 

  *is_required: false*

    
* **event_key** (string)  `Required` 

  *is_required: false*

    
* **event_type** (string)  `Required` 

  *is_required: false*

    
* **severity** (string)  `Required` 

  *is_required: false*

    
* **resource_id** (string)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **account** (string)  `Required` 

  *is_required: false*

    
* **alert_id** (string)  `Required` 

  *is_required: false*

    
* **webhook_id** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### EventResource
* **resource_id** (string)  `Required` 

    
* **resource_type** (string)  `Required` 

    
* **name** (string)  `Required` 

    <br>

### EventStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### EventsInfo
* **results** (EventInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### GetEventRequest
* **event_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>
