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

desc: Creates a new Notification. When a Notification is created, it is delivered to a UserChannel or a ProjectChannel depending on the parameter `resource_type`. If a Notification is delivered to a UserChannel, the `resource_type` is `identity.User`, and if a Notification is delivered to a ProjectChannel, the `resource_type` is `identity.Project`.
request_example: >-
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
response_example: >-
{
"notification_id": "notification-123456789012",
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
"notification_level": "LV2",
"is_read": true,
"user_id": "Cloudforet@mz.co.kr",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T17:12:40.990Z"
}



> **POST** /notification/v1/notification/create
>






    
<br>

### push

desc: Manually raises a Notification. A Notification is raised with a message to be sent using a valid specific Protocol, and data used for a specific Protocol such as a phone number.
request_example: >-
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



> **POST** /notification/v1/notification/push
>






    
<br>

### delete

desc: Deletes multiple Notifications. You must specify `notifications` of the list of Notifications to delete.
request_example: >-
{
"notifications": [
"notification-4025c1b61225",
"notification-13hk3fh32534",
"notification-4kth40jth5jy"
]
}



> **POST** /notification/v1/notification/delete
>






    
<br>

### set_read

desc: Marks a Notification as read. When a Notification is raised and if the Notification has been acknowledged, it can be marked as read with the method.
request_example: >-
{
"notifications": [
"notification-6c548a37ee77",
"notification-4j3jt9384fnf"
]
}



> **POST** /notification/v1/notification/set-read
>






    
<br>

### get

desc: Gets a specific Notification. Prints detailed information about the Notification, including not only the message contents(`title`, `description`) but also related data such as created time and urgency.
request_example: >-
{
"notification_id": "notification-4025c1b61225"
}
response_example: >-
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



> **POST** /notification/v1/notification/get
>






    
<br>

### list

desc: Gets a list of all Notifications. You can use a query to get a filtered list of Notifications.
request_example: >-
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
response_example: >-
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



> **POST** /notification/v1/notification/list
>






    
<br>

### stat





> **POST** /notification/v1/notification/stat
>






    


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
