---
title: "Notification"
linkTitle: "Notification"
weight: 3
bookFlatSection: true
---
# [Notification](#Notification)



>  **Package : spaceone.api.alert_manager.plugin**

<br>
<br>

## Notification





**Notification Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**dispatch**](./Notification#dispatch) | [DispatchRequest](Notification#dispatchrequest) | [Empty](Notification#empty) |



    
<br>

### dispatch










    


<br>
<br>

## Message



### DispatchRequest
* **options** (Struct)   `Required` 

    
* **secret_data** (Struct)   `Required` 

    
* **channel_data** (Struct)   `Required` 

    
* **message** (NotificationMessage)   `Required` 

    
* **notification_type** (NotificationType)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### NotificationCallback
* **label** (string)   `Required` 

    
* **url** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    <br>

### NotificationMessage
* **title** (string)   `Required` 

    
* **link** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **image_url** (string)   `Required` 

    
* **tags** (NotificationTag)  `Repeated`    `Required` 

    
* **callbacks** (NotificationCallback)  `Repeated`    `Required` 

    
* **occurred_at** (string)   `Required` 

    <br>

### NotificationTag
* **key** (string)   `Required` 

    
* **value** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    <br>
