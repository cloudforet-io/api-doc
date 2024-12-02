---
title: "Event"
linkTitle: "Event"
weight: 3
bookFlatSection: true
---
# [Event](#Event)



>  **Package : spaceone.api.opsflow.v1**

<br>
<br>

## Event





**Event Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./Event#list) | [EventSearchQuery](Event#eventsearchquery) | [EventsInfo](Event#eventsinfo) |
| [**stat**](./Event#stat) | [EventStatQuery](Event#eventstatquery) | [Struct](Event#struct) |



    
<br>

### list





> **POST** /opsflow/v1/event/list
>






    
<br>

### stat





> **POST** /opsflow/v1/event/stat
>






    


<br>
<br>

## Message



### EventInfo
* **event_id** (string)   `Required` 

    
* **event_type** (EventType)   `Required` 

    
* **name** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **user_type** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **task_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### EventSearchQuery
* **query** (Query)  

    
* **task_id** (string)  

    
* **event_type** (EventType)  

    
* **user_type** (string)  

    
* **event_id** (string)  

    
* **user_id** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### EventStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### EventsInfo
* **results** (EventInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
