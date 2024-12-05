---
title: "Event"
linkTitle: "Event"
weight: 3
bookFlatSection: true
---
# [Event](#Event)



>  **Package : spaceone.api.alert_manager.plugin**

<br>
<br>

## Event





**Event Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**parse**](./Event#parse) | [ParseRequest](Event#parserequest) | [EventsInfo](Event#eventsinfo) |



    
<br>

### parse










    


<br>
<br>

## Message



### EventInfo
* **event_key** (string)   `Required` 

    
* **event_type** (EventType)   `Required` 

    
* **title** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **severity** (EventSeverity)   `Required` 

    
* **rule** (string)   `Required` 

    
* **image_url** (string)   `Required` 

    
* **resources** (string)  `Repeated`    `Required` 

    
* **provider** (string)   `Required` 

    
* **account** (string)   `Required` 

    
* **additional_info** (Struct)   `Required` 

    
* **occurred_at** (string)   `Required` 

    <br>

### EventResource
* **resource_id** (string)  

    
* **resource_type** (string)  

    
* **name** (string)  

    <br>

### EventsInfo
* **results** (EventInfo)  `Repeated`    `Required` 

    <br>

### ParseRequest
* **options** (Struct)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>
