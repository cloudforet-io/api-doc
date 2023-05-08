---
title: "Notification"
linkTitle: "Notification"
weight: 3
bookFlatSection: true
---
# [Notification](#Notification)
desc: A Notification is a service that delivers event data generated in Cloudforet to a Project or User.


>  **Package : spaceone.api.notification.v1**

<br>
<br>

## Notification


**Notification Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Notification#create) | [CreateNotificationRequest](Notification#createnotificationrequest) | [Empty](./Notification#empty) |
| [**push**](./Notification#push) | [PushNotificationRequest](Notification#pushnotificationrequest) | [Empty](./Notification#empty) |
| [**delete**](./Notification#delete) | [NotificationRequest](Notification#notificationrequest) | [Empty](./Notification#empty) |
| [**set_read**](./Notification#set_read) | [SetReadNotificationRequest](Notification#setreadnotificationrequest) | [Empty](./Notification#empty) |
| [**get**](./Notification#get) | [GetNotificationRequest](Notification#getnotificationrequest) | [NotificationInfo](./Notification#notificationinfo) |
| [**list**](./Notification#list) | [NotificationQuery](Notification#notificationquery) | [NotificationsInfo](./Notification#notificationsinfo) |
| [**stat**](./Notification#stat) | [NotificationStatQuery](Notification#notificationstatquery) | [Struct](./Notification#struct) |



    
<br>

### create

> **POST** /notification/v1/notification/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### push

> **POST** /notification/v1/notification/push
>




 {{< tabs " push " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /notification/v1/notification/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### set_read

> **POST** /notification/v1/notification/set-read
>




 {{< tabs " set_read " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /notification/v1/notification/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /notification/v1/notification/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /notification/v1/notification/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateNotificationRequest
* **resource_type** (string)  `Required` 

  *is_required: true
desc: The type of resource to which the notification is dispatched.
Currently, only "identity.Project" or "identity.User" can be set.*

    
* **resource_id** (string)  `Required` 

  *is_required: true
desc: The ID of the resource to which notifications are dispatched.
If resource_type is "identity.Project", then resource_id requires a project ID values.
If resource_type is "identity.User", then resource_id requires a user ID value.*

    
* **topic** (string)  `Required` 

  *is_required: true
desc: The topic of notification.*

    
* **message** (Struct)  `Required` 

  *is_required: true
desc: This message is used for each protocol.*

    
* **notification_type** (NotificationType)  `Required` 

  *is_required: false
desc: The type of notification.*

    
* **notification_level** (NotificationLEVEL)  `Required` 

  *is_required: false
desc: The level of notification.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### GetNotificationRequest
* **notification_id** (string)  `Required` 

  *is_required: true
desc: The ID of Notification.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    
* **only** (string)  `Required` 

  *is_required: false
desc: The list of the notification information column you want to be returned. It must be specified in the NotificationInfo.*

    <br>

### NotificationInfo
* **notification_id** (string)  `Required` 

  *desc: The ID of notification.*

    
* **topic** (string)  `Required` 

  *desc: The topic of notification.*

    
* **message** (Struct)  `Required` 

  *desc: The contents of notification.
This message is used for each protocol.*

    
* **notification_type** (NotificationType)  `Required` 

  *desc: The type of notification.*

    
* **notification_level** (NotificationLEVEL)  `Required` 

  *desc: The level of notification.*

    
* **is_read** (bool)  `Required` 

  *desc: Whether or not to check the notification.
If notification has been returned at least once through the Get or List method, is_read is changed to True.*

    
* **user_id** (string)  `Required` 

  *desc: The ID of user to whom the notification was dispatched.*

    
* **domain_id** (string)  `Required` 

  *desc: The ID of domain*

    
* **created_at** (string)  `Required` 

  *desc: Notification creation time.*

    <br>

### NotificationQuery
* **query** (Query)  `Required` 

  *is_required: false
desc: Query format provided by SpaceONE. Please check the link for more information.*

    
* **notification_id** (string)  `Required` 

  *is_required: false
desc: The ID of notification.*

    
* **topic** (string)  `Required` 

  *is_required: false
desc: The topic of notification.*

    
* **notification_type** (NotificationType)  `Required` 

  *is_required: false
desc: The type of notification.*

    
* **notification_level** (NotificationLEVEL)  `Required` 

  *is_required: false
desc: The level of notification.*

    
* **is_read** (bool)  `Required` 

  *is_required: false
desc: Whether or not to check the notification.
If is_read is False, the user has not checked the notification yet.*

    
* **parent_notification_id** (string)  `Required` 

  *is_required: false
desc: The ID of parent notification. Not used yet.*

    
* **project_id** (string)  `Required` 

  *is_required: false
desc: The project ID to which the notification will be dispatched.*

    
* **user_id** (string)  `Required` 

  *is_required: false
desc: The ID of user.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### NotificationRequest
* **notifications** (string)  `Required` 

  *is_required: true
desc: ID list of Notifications.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### NotificationStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true
desc: Statistics Query format provided by SpaceONE. Please check the link for more information.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### NotificationsInfo
* **results** (NotificationInfo)  `Required` 

  *desc: List of queried notifications.*

    
* **total_count** (int32)  `Required` 

  *desc: Total counts of queried notifications.*

    <br>

### PushNotificationRequest
* **protocol_id** (string)  `Required` 

  *is_required: true
desc: The ID of Protocol.*

    
* **data** (Struct)  `Required` 

  *is_required: true*

    
* **message** (Struct)  `Required` 

  *is_required: true*

    
* **notification_type** (string)  `Required` 

  *is_required: false*

    
* **notification_level** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SetReadNotificationRequest
* **notifications** (string)  `Required` 

  *is_required: true
desc: The ID list of notification that want to change read status.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>
