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

desc: Creates a new Event. The Event creation process starts with validation checking whether the input data is from a webhook or not. After the input data is validated, the data is processed and used to create the Event.



> **POST** /monitoring/v1/event/create
>






    
<br>

### get

desc: Gets a specific Event matching the input parameters, `event_id` and `domain_id`. Prints detailed information about the Event.
request_example: >-
{
"event_id": "event-4e16ba3bd384",
"domain_id": "domain-58010aa2e451"
}
response_example: >-
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



> **POST** /monitoring/v1/event/get
>






    
<br>

### list

desc: Gets a list of all Events. You must specify the `domain_id`. You can use a query to get a filtered list of Events.
request_example: >-
{
"query": {},
"domain_id": "domain-58010aa2e451"
}
response_example: >-
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



> **POST** /monitoring/v1/event/list
>






    
<br>

### stat





> **POST** /monitoring/v1/event/stat
>






    


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
