---
title: "Event"
linkTitle: "Event"
weight: 3
bookFlatSection: true
---
# [Event](#Event)
An Event is an alarm raised by an external monitoring system and collected by a Cloudforet plugin.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Event





**Event Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Event#create) | [CreateEventRequest](Event#createeventrequest) | [Empty](Event#empty) |
| [**get**](./Event#get) | [GetEventRequest](Event#geteventrequest) | [EventInfo](Event#eventinfo) |
| [**list**](./Event#list) | [EventQuery](Event#eventquery) | [EventsInfo](Event#eventsinfo) |
| [**stat**](./Event#stat) | [EventStatQuery](Event#eventstatquery) | [Struct](Event#struct) |



    
<br>

### create

Creates a new Event. The Event creation process starts with validation checking whether the input data is from a webhook or not. After the input data is validated, the data is processed and used to create the Event.



> **POST** /monitoring/v1/event/create
>






    
<br>

### get

Gets a specific Event matching the input parameters, `event_id` and `domain_id`. Prints detailed information about the Event.



> **POST** /monitoring/v1/event/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetEventRequest](./Event#geteventrequest)

* **event_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **only** (string)  `Repeated`   





{{< highlight json >}}
{
   "event_id": "event-4e16ba3bd384",
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[EventInfo](#EVENTINFO)
* **event_id** (string)   `Required` 

* **event_key** (string)   `Required` 

* **event_type** (string)   `Required` 

* **title** (string)   `Required` 

* **description** (string)   `Required` 

* **severity** (string)   `Required` 

* **rule** (string)   `Required` 

* **resource** (EventResource)   `Required` 

* **provider** (string)   `Required` 

* **account** (string)   `Required` 

* **image_url** (string)   `Required` 

* **raw_data** (Struct)   `Required` 

* **additional_info** (Struct)   `Required` 

* **alert_id** (string)   `Required` 

* **webhook_id** (string)   `Required` 

* **project_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **occurred_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Events. You must specify the `domain_id`. You can use a query to get a filtered list of Events.



> **POST** /monitoring/v1/event/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[EventQuery](./Event#eventquery)

* **query** (Query)  


* **event_id** (string)  


* **event_key** (string)  


* **event_type** (string)  


* **severity** (string)  


* **resource_id** (string)  


* **provider** (string)  


* **account** (string)  


* **alert_id** (string)  


* **webhook_id** (string)  


* **project_id** (string)  


* **domain_id** (string)  





{{< highlight json >}}
{
   "query": {},
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[EventsInfo](#EVENTSINFO)
* **results** (EventInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /monitoring/v1/event/stat
>






    


<br>
<br>

## Message



### CreateEventRequest
* **webhook_id** (string)   `Required` 

    
* **access_key** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    <br>

### EventInfo
* **event_id** (string)   `Required` 

    
* **event_key** (string)   `Required` 

    
* **event_type** (string)   `Required` 

    
* **title** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **severity** (string)   `Required` 

    
* **rule** (string)   `Required` 

    
* **resource** (EventResource)   `Required` 

    
* **provider** (string)   `Required` 

    
* **account** (string)   `Required` 

    
* **image_url** (string)   `Required` 

    
* **raw_data** (Struct)   `Required` 

    
* **additional_info** (Struct)   `Required` 

    
* **alert_id** (string)   `Required` 

    
* **webhook_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **occurred_at** (string)   `Required` 

    <br>

### EventQuery
* **query** (Query)  

    
* **event_id** (string)  

    
* **event_key** (string)  

    
* **event_type** (string)  

    
* **severity** (string)  

    
* **resource_id** (string)  

    
* **provider** (string)  

    
* **account** (string)  

    
* **alert_id** (string)  

    
* **webhook_id** (string)  

    
* **project_id** (string)  

    
* **domain_id** (string)  

    <br>

### EventResource
* **resource_id** (string)   `Required` 

    
* **resource_type** (string)   `Required` 

    
* **name** (string)   `Required` 

    <br>

### EventStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### EventsInfo
* **results** (EventInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### GetEventRequest
* **event_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>
