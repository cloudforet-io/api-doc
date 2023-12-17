---
title: "Notification"
linkTitle: "Notification"
weight: 3
bookFlatSection: true
---
# [Notification](#Notification)
A Notification is a service that delivers event data generated in Cloudforet to a Project or User.


>  **Package : spaceone.api.notification.v1**

<br>
<br>

## Notification





**Notification Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Notification#create) | [CreateNotificationRequest](Notification#createnotificationrequest) | [Empty](Notification#empty) |
| [**push**](./Notification#push) | [PushNotificationRequest](Notification#pushnotificationrequest) | [Empty](Notification#empty) |
| [**delete**](./Notification#delete) | [NotificationRequest](Notification#notificationrequest) | [Empty](Notification#empty) |
| [**set_read**](./Notification#set_read) | [SetReadNotificationRequest](Notification#setreadnotificationrequest) | [Empty](Notification#empty) |
| [**get**](./Notification#get) | [GetNotificationRequest](Notification#getnotificationrequest) | [NotificationInfo](Notification#notificationinfo) |
| [**list**](./Notification#list) | [NotificationQuery](Notification#notificationquery) | [NotificationsInfo](Notification#notificationsinfo) |
| [**stat**](./Notification#stat) | [NotificationStatQuery](Notification#notificationstatquery) | [Struct](Notification#struct) |



    
<br>

### create

Creates a new Notification. When a Notification is created, it is delivered to a UserChannel or a ProjectChannel depending on the parameter `resource_type`. If a Notification is delivered to a UserChannel, the `resource_type` is `identity.User`, and if a Notification is delivered to a ProjectChannel, the `resource_type` is `identity.Project`.



> **POST** /notification/v1/notification/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateNotificationRequest](./Notification#createnotificationrequest)

* **resource_type** (string)   `Required` 

  *is_required: true
The type of resource to which the notification is dispatched.
Currently, only "identity.Project" or "identity.User" can be set.*


* **resource_id** (string)   `Required` 

  *is_required: true
The ID of the resource to which notifications are dispatched.
If resource_type is "identity.Project", then resource_id requires a project ID values.
If resource_type is "identity.User", then resource_id requires a user ID value.*


* **topic** (string)   `Required` 

  *is_required: true
The topic of notification.*


* **message** (Struct)   `Required` 

  *is_required: true
This message is used for each protocol.*


* **notification_type** (NotificationType)  

  *is_required: false
The type of notification.*


* **notification_level** (NotificationLEVEL)  

  *is_required: false
The level of notification.*





{{< highlight json >}}
{
   "resource_type": "identity.Project",
   "resource_id": "resource-123456789012",
   "topic": "monitoring.Alert",
   "message": {
       "title": "[Alerting] Not Running Pods 0:OK alert",
       "description": "[spaceone-dev] Not Running Pods 0 is OK\n\nFailure level : WorkerNode\nPanel ... ",
       "tags": {
           "urgency": "LOW",
           "resource_id": "pod",
           "assignee": "user1@email.com",
           "created_at": "2022-01-01T17:12:45.990Z",
           "state": "ACKNOWLEDGED",
           "project_id": "project-123456789012"
       }
   },
   "notification_type": "INFO",
   "notification_level": "LV2"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### push

Manually raises a Notification. A Notification is raised with a message to be sent using a valid specific Protocol, and data used for a specific Protocol such as a phone number.



> **POST** /notification/v1/notification/push
>





 {{< tabs " push " >}}

 {{< tab "Request Example" >}}



[PushNotificationRequest](./Notification#pushnotificationrequest)

* **protocol_id** (string)   `Required` 

  *is_required: true
The ID of Protocol.*


* **data** (string)   `Required` 

  *is_required: true*


* **message** (Struct)   `Required` 

  *is_required: true*


* **notification_type** (string)  

  *is_required: false*


* **notification_level** (string)  

  *is_required: false*


* **topic** (string)  





{{< highlight json >}}
{
   "protocol_id": "protocol-fb30cb6c28d6",
   "data": {
       "phone_number": "01012345678"
   },
   "message": {
       "tags": [
           {
               "key": "project_id",
               "value": "project-xxxx"
           },
           {
               "key": "project_name",
               "value": "Test Project"
           },
           {
               "key": "resource_id",
               "value": "server-yyyyy"
           },
           {
               "key": "resource_name",
               "value": "web-server-001"
           }
       ],
       "description": "This is Sample Message",
       "title": "Sample"
   }
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### delete

Deletes multiple Notifications. You must specify `notifications` of the list of Notifications to delete.



> **POST** /notification/v1/notification/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[NotificationRequest](./Notification#notificationrequest)

* **notifications** (string)  `Repeated`    `Required` 

  *is_required: true
ID list of Notifications.*





{{< highlight json >}}
{
   "notifications": [
       "notification-4025c1b61225",
       "notification-13hk3fh32534",
       "notification-4kth40jth5jy"
   ]
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### set_read

Marks a Notification as read. When a Notification is raised and if the Notification has been acknowledged, it can be marked as read with the method.



> **POST** /notification/v1/notification/set-read
>





 {{< tabs " set_read " >}}

 {{< tab "Request Example" >}}



[SetReadNotificationRequest](./Notification#setreadnotificationrequest)

* **notifications** (string)  `Repeated`    `Required` 

  *is_required: true
The ID list of notification that want to change read status.*





{{< highlight json >}}
{
   "notifications": [
       "notification-6c548a37ee77",
       "notification-4j3jt9384fnf"
   ]
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Notification. Prints detailed information about the Notification, including not only the message contents(`title`, `description`) but also related data such as created time and urgency.



> **POST** /notification/v1/notification/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetNotificationRequest](./Notification#getnotificationrequest)

* **notification_id** (string)   `Required` 

  *is_required: true
The ID of Notification.*


* **set_read** (bool)  





{{< highlight json >}}
{
   "notification_id": "notification-4025c1b61225"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NotificationInfo](#NOTIFICATIONINFO)
* **notification_id** (string)   `Required` 

  The ID of notification.

* **topic** (string)   `Required` 

  The topic of notification.

* **message** (Struct)   `Required` 

  The contents of notification.
This message is used for each protocol.

* **notification_type** (NotificationType)   `Required` 

  The type of notification.

* **notification_level** (NotificationLEVEL)   `Required` 

  The level of notification.

* **is_read** (bool)   `Required` 

  Whether or not to check the notification.
If notification has been returned at least once through the Get or List method, is_read is changed to True.

* **user_id** (string)   `Required` 

  The ID of user to whom the notification was dispatched.

* **domain_id** (string)   `Required` 

  The ID of domain

* **created_at** (string)   `Required` 

  Notification creation time.



{{< highlight json >}}
{
   "notification_id": "notification-4025c1b61225",
   "topic": "monitoring.Alert",
   "message": {
       "tags": {
           "project_id": "project-18655561c535",
           "created_at": null,
           "urgency": "LOW",
           "state": "TRIGGERED",
           "resource_id": "AWS/NetworkELB",
           "resource_name": "[Asia Pacific (Seoul)]:[AWS/NetworkELB]: net/af83f347171a044af46453ebb34c8225/743a23562a96c595"
       },
       "title": "[Asia Pacific (Seoul)]: NLB-TCP_Target_Reset_Count-Alert",
       "description": "Threshold Crossed: 1 out of the last 1 datapoints [200.0 (25/06/21 06:38:00)] was not greater than the threshold (200.0)"
   },
   "notification_type": "INFO",
   "notification_level": "ALL",
   "is_read": true,
   "user_id": "user1@spaceone.dev",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2021-06-25T06:42:05.867Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Notifications. You can use a query to get a filtered list of Notifications.



> **POST** /notification/v1/notification/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[NotificationQuery](./Notification#notificationquery)

* **query** (Query)  

  *is_required: false
Query format provided by SpaceONE. Please check the link for more information.*


* **notification_id** (string)  

  *is_required: false
The ID of notification.*


* **topic** (string)  

  *is_required: false
The topic of notification.*


* **notification_type** (NotificationType)  

  *is_required: false
The type of notification.*


* **notification_level** (NotificationLEVEL)  

  *is_required: false
The level of notification.*


* **is_read** (bool)  

  *is_required: false
Whether or not to check the notification.
If is_read is False, the user has not checked the notification yet.*


* **parent_notification_id** (string)  

  *is_required: false
The ID of parent notification. Not used yet.*


* **project_id** (string)  

  *is_required: false
The project ID to which the notification will be dispatched.*





{{< highlight json >}}
{
   "query": {
       "filter": [
           {
               "key": "notification_type",
               "value": "INFO",
               "operator": "eq"
           }
       ]
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NotificationsInfo](#NOTIFICATIONSINFO)
* **results** (NotificationInfo)  `Repeated`   `Required` 

  List of queried notifications.

* **total_count** (int32)   `Required` 

  Total counts of queried notifications.



{{< highlight json >}}
{
   "results": [
       {
           "notification_id": "notification-9f1476af11b7",
           "topic": "monitoring.Alert",
           "message": {
               "tags": {
                   "state": "ACKNOWLEDGED",
                   "resource_id": "pod",
                   "project_id": "project-18655561c535",
                   "urgency": "LOW",
                   "created_at": null,
                   "assignee": "yuda@test.co"
               },
               "title": "[Alerting] Not Running Pods 0:OK alert",
               "description": "[cloudone-dev-v1-eks-cluster] Not Running Pods 0 is OK"
           },
           "notification_type": "INFO",
           "notification_level": "LV2",
           "is_read": true,
           "user_id": "user33@spaceone.dev",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2021-06-21T17:13:39.570Z"
       },
       {
           "notification_id": "notification-4025c1b61225",
           "topic": "monitoring.Alert",
           "message": {
               "title": "[Asia Pacific (Seoul)]: NLB-TCP_Target_Reset_Count-Alert",
               "description": "Threshold Crossed: 1 out of the last 1 datapoints [200.0 (25/06/21 06:38:00)] was not greater than the threshold (200.0)",
               "tags": {
                   "resource_id": "AWS/NetworkELB",
                   "resource_name": "[Asia Pacific (Seoul)]:[AWS/NetworkELB]: net/dfsbvs/advdr32rwqdsvzc",
                   "created_at": null,
                   "state": "TRIGGERED",
                   "project_id": "project-18655561c535",
                   "urgency": "LOW"
               }
           },
           "notification_type": "INFO",
           "notification_level": "ALL",
           "is_read": true,
           "user_id": "user1@cloudforet.io",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2021-06-25T06:42:05.867Z"
       }
   ],
   "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /notification/v1/notification/stat
>






    


<br>
<br>

## Message



### CreateNotificationRequest
* **resource_type** (string)   `Required` 

  *is_required: true
The type of resource to which the notification is dispatched.
Currently, only "identity.Project" or "identity.User" can be set.*

    
* **resource_id** (string)   `Required` 

  *is_required: true
The ID of the resource to which notifications are dispatched.
If resource_type is "identity.Project", then resource_id requires a project ID values.
If resource_type is "identity.User", then resource_id requires a user ID value.*

    
* **topic** (string)   `Required` 

  *is_required: true
The topic of notification.*

    
* **message** (Struct)   `Required` 

  *is_required: true
This message is used for each protocol.*

    
* **notification_type** (NotificationType)  

  *is_required: false
The type of notification.*

    
* **notification_level** (NotificationLEVEL)  

  *is_required: false
The level of notification.*

    <br>

### GetNotificationRequest
* **notification_id** (string)   `Required` 

  *is_required: true
The ID of Notification.*

    
* **set_read** (bool)  

    <br>

### NotificationInfo
* **notification_id** (string)   `Required` 

  *The ID of notification.*

    
* **topic** (string)   `Required` 

  *The topic of notification.*

    
* **message** (Struct)   `Required` 

  *The contents of notification.
This message is used for each protocol.*

    
* **notification_type** (NotificationType)   `Required` 

  *The type of notification.*

    
* **notification_level** (NotificationLEVEL)   `Required` 

  *The level of notification.*

    
* **is_read** (bool)   `Required` 

  *Whether or not to check the notification.
If notification has been returned at least once through the Get or List method, is_read is changed to True.*

    
* **user_id** (string)   `Required` 

  *The ID of user to whom the notification was dispatched.*

    
* **domain_id** (string)   `Required` 

  *The ID of domain*

    
* **created_at** (string)   `Required` 

  *Notification creation time.*

    <br>

### NotificationQuery
* **query** (Query)  

  *is_required: false
Query format provided by SpaceONE. Please check the link for more information.*

    
* **notification_id** (string)  

  *is_required: false
The ID of notification.*

    
* **topic** (string)  

  *is_required: false
The topic of notification.*

    
* **notification_type** (NotificationType)  

  *is_required: false
The type of notification.*

    
* **notification_level** (NotificationLEVEL)  

  *is_required: false
The level of notification.*

    
* **is_read** (bool)  

  *is_required: false
Whether or not to check the notification.
If is_read is False, the user has not checked the notification yet.*

    
* **parent_notification_id** (string)  

  *is_required: false
The ID of parent notification. Not used yet.*

    
* **project_id** (string)  

  *is_required: false
The project ID to which the notification will be dispatched.*

    <br>

### NotificationRequest
* **notifications** (string)  `Repeated`    `Required` 

  *is_required: true
ID list of Notifications.*

    <br>

### NotificationStatQuery
* **query** (StatisticsQuery)   `Required` 

  *is_required: true
Statistics Query format provided by SpaceONE. Please check the link for more information.*

    <br>

### NotificationsInfo
* **results** (NotificationInfo)  `Repeated`    `Required` 

  *List of queried notifications.*

    
* **total_count** (int32)   `Required` 

  *Total counts of queried notifications.*

    <br>

### PushNotificationRequest
* **protocol_id** (string)   `Required` 

  *is_required: true
The ID of Protocol.*

    
* **data** (string)   `Required` 

  *is_required: true*

    
* **message** (Struct)   `Required` 

  *is_required: true*

    
* **notification_type** (string)  

  *is_required: false*

    
* **notification_level** (string)  

  *is_required: false*

    
* **topic** (string)  

    <br>

### SetReadNotificationRequest
* **notifications** (string)  `Repeated`    `Required` 

  *is_required: true
The ID list of notification that want to change read status.*

    <br>
