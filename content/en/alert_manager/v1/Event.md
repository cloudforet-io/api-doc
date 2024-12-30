---
title: "Event"
linkTitle: "Event"
weight: 3
bookFlatSection: true
---
# [Event](#Event)



>  **Package : spaceone.api.alert_manager.v1**

<br>
<br>

## Event





**Event Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Event#create) | [EventCreateRequest](Event#eventcreaterequest) | [Empty](Event#empty) |



    
<br>

### create





> **POST** /alert-manager/v1/comment/create
>






    


<br>
<br>

## Message



### EventCreateRequest
* **webhook_id** (string)   `Required` 

    
* **access_key** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    <br>

### EventInfo
* **event_key** (string)   `Required` 

    
* **event_type** (EventType)   `Required` 

    
* **title** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **severity** (EventSeverity)   `Required` 

    
* **rule** (string)   `Required` 

    
* **image_url** (string)   `Required` 

    
* **resources** (string)  `Repeated`    `Required` 

    
* **additional_info** (Struct)   `Required` 

    
* **raw_data** (Struct)   `Required` 

    
* **webhook_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **occurred_at** (string)   `Required` 

    <br>
