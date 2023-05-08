---
title: "Notification"
linkTitle: "Notification"
weight: 3
bookFlatSection: true
---
# [Notification](#Notification)
desc: A Notification is a resource delivering data from a Protocol plugin instance to a nofitication tool of an external user.


>  **Package : spaceone.api.notification.plugin**

<br>
<br>

## Notification


**Notification Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**dispatch**](./Notification#dispatch) | [PluginDispatchRequest](Notification#plugindispatchrequest) | [Empty](./Notification#empty) |



    
<br>

### dispatch




 {{< tabs " dispatch " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### PluginDispatchRequest
* **options** (Struct)  `Required` 

  *is_required: true
desc: Option value required for notification delivery.*

    
* **message** (Struct)  `Required` 

  *is_required: true
desc: Message containing notification information*

    
* **notification_type** (NotificationType)  `Required` 

  *is_required: true
desc: The type of Notification*

    
* **secret_data** (Struct)  `Required` 

  *is_required: true
desc: Secret value required for notification delivery.
The secret data usually includes the credential information required for the plugin to access the external system.*

    
* **channel_data** (Struct)  `Required` 

  *is_required: true
desc: Channel data required for notification delivery.*

    <br>
