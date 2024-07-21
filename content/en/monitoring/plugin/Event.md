---
title: "Event"
linkTitle: "Event"
weight: 3
bookFlatSection: true
---
# [Event](#Event)
An Event is data created by an external monitoring system and collected by a Webhook plugin.


>  **Package : spaceone.api.monitoring.plugin**

<br>
<br>

## Event





**Event Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**parse**](./Event#parse) | [ParseRequest](Event#parserequest) | [EventsInfo](Event#eventsinfo) |



    
<br>

### parse

Parses a specific Event resource and transforms the resource from external data collected to data available in Cloudforet internally. The `parse` method standardizes all different data from external monitoring systems.








    


<br>
<br>

## Message



### EventInfo
* **event_key** (string)   `Required` 

    
* **event_type** (string)   `Required` 

    
* **title** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **severity** (Severity)   `Required` 

    
* **resource** (Struct)   `Required` 

    
* **rule** (string)   `Required` 

    
* **occurred_at** (string)   `Required` 

    
* **additional_info** (Struct)   `Required` 

    
* **image_url** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **account** (string)   `Required` 

    
* **resources** (string)  `Repeated`    `Required` 

    <br>

### EventsInfo
* **results** (EventInfo)  `Repeated`    `Required` 

    <br>

### ParseRequest
* **options** (Struct)   `Required` 

    
* **data** (Struct)   `Required` 

  *Unpredictable data format that comes from Webhook*

    <br>
