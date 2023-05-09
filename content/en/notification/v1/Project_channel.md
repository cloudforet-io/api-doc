---
title: "Project_channel"
linkTitle: "Project_channel"
weight: 3
bookFlatSection: true
---
# [Project_channel](#Project_channel)
desc: A ProjectChannel is a destination  where Notifications are delivered. Notifications are generated via the Protocol set by each Project.


>  **Package : spaceone.api.notification.v1**

<br>
<br>

## Project_channel





**ProjectChannel Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./ProjectChannel#create) | [CreateProjectChannelRequest](ProjectChannel#createprojectchannelrequest) | [ProjectChannelInfo](./ProjectChannel#projectchannelinfo) |
| [**update**](./ProjectChannel#update) | [UpdateProjectChannelRequest](ProjectChannel#updateprojectchannelrequest) | [ProjectChannelInfo](./ProjectChannel#projectchannelinfo) |
| [**set_schedule**](./ProjectChannel#set_schedule) | [UpdateProjectChannelScheduleRequest](ProjectChannel#updateprojectchannelschedulerequest) | [ProjectChannelInfo](./ProjectChannel#projectchannelinfo) |
| [**set_subscription**](./ProjectChannel#set_subscription) | [UpdateProjectChannelSubscriptionRequest](ProjectChannel#updateprojectchannelsubscriptionrequest) | [ProjectChannelInfo](./ProjectChannel#projectchannelinfo) |
| [**enable**](./ProjectChannel#enable) | [ProjectChannelRequest](ProjectChannel#projectchannelrequest) | [ProjectChannelInfo](./ProjectChannel#projectchannelinfo) |
| [**disable**](./ProjectChannel#disable) | [ProjectChannelRequest](ProjectChannel#projectchannelrequest) | [ProjectChannelInfo](./ProjectChannel#projectchannelinfo) |
| [**delete**](./ProjectChannel#delete) | [ProjectChannelRequest](ProjectChannel#projectchannelrequest) | [Empty](./ProjectChannel#empty) |
| [**get**](./ProjectChannel#get) | [GetProjectChannelRequest](ProjectChannel#getprojectchannelrequest) | [ProjectChannelInfo](./ProjectChannel#projectchannelinfo) |
| [**list**](./ProjectChannel#list) | [ProjectChannelQuery](ProjectChannel#projectchannelquery) | [ProjectChannelsInfo](./ProjectChannel#projectchannelsinfo) |
| [**stat**](./ProjectChannel#stat) | [ProjectChannelStatQuery](ProjectChannel#projectchannelstatquery) | [Struct](./ProjectChannel#struct) |



    
<br>

### create

desc: Creates a new ProjectChannel. ProjectChannel is a channel that delivers a Notification to the Project when the Notification is created. When creating a ProjectChannel, one Protocol must be selected, and a Notification is dispatched via the selected Protocol.
request_example: >-
{
"protocol_id": "protocol-ab94ea7d574e",
"name": "sms-test",
"data": {
"phone_number": "01011112222"
},
"is_subscribe": true,
"subscriptions": ["monitoring.Alert"],
"notification_level": "LV1",
"is_scheduled": true,
"schedule": {
"day_of_week": [
"MON",
"TUE",
"WED",
"THU",
"FRI"
],
"end_hour": 9
},
"project_id": "project-52a423012d5e"
}
response_example: >-
{
"project_channel_id": "project-ch-488df94d026d",
"name": "sms-test",
"state": "ENABLED",
"data": {
"phone_number": "01011112222"
},
"notification_level": "LV1",
"tags": {},
"protocol_id": "protocol-ab94ea7d574e",
"project_id": "project-aa723eed3d69",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-13T07:35:28.305Z"
}



> **POST** /notification/v1/project-channel/create
>






    
<br>

### update

desc: Updates a specific ProjectChannel. A ProjectChannel that has already been configured cannot be changed. Instead, the data required for dispatching Notifications to a ProjectChannel can be updated.
request_example: >-
{
"project_channel_id": "project-ch-488df94d026d",
"name": "sms2-test",
"data": {
"phone_number": "01033334444"
},
"notification_level": "LV2",
"tags": {
"a": "b"
}
}
response_example: >-
{
"project_channel_id": "project-ch-488df94d026d",
"name": "sms2-test",
"state": "ENABLED",
"data": {
"phone_number": "01033334444"
},
"notification_level": "LV2",
"tags": {
"a": "b"
},
"protocol_id": "protocol-ab94ea7d574e",
"project_id": "project-aa723eed3d69",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-13T07:35:28.305Z"
}



> **PUT** /notification/v1/project-channel/update
>






    
<br>

### set_schedule

desc: Sets a schedule for a ProjectChannel. A schedule defines the time to receive a Notification. When a Notification is created, you can set the day of the week and time you want to receive it. When you set the day of the week, you can receive a notification only on the day of the week you set. If you also set the start time and end time with the day of the week, you can receive a Notification only at the scheduled time on the day of the week you set. If there is no schedule set in a ProjectChannel, Notifications will be dispatched at all times via the ProjectChannel.
request_example: >-
{
"project_channel_id": "project-ch-488df94d026d",
"is_scheduled": true,
"schedule": {
"day_of_week": [
"MON",
"WED",
"FRI"
],
"end_hour": 9
}
}
response_example: >-
{
"project_channel_id": "project-ch-488df94d026d",
"name": "sms2-test",
"state": "ENABLED",
"data": {
"phone_number": "01033334444"
},
"notification_level": "LV2",
"is_scheduled": true,
"schedule": {
"day_of_week": [
"MON",
"WED",
"FRI"
],
"end_hour": 9
},
"tags": {
"a": "b"
},
"protocol_id": "protocol-ab94ea7d574e",
"project_id": "project-aa723eed3d69",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-13T07:35:28.305Z"
}



> **POST** /notification/v1/project-channel/set-schedule
>






    
<br>

### set_subscription

desc: Sets a subscription for a ProjectChannel. A subscription is a topic for channels to subscribe to and get notified about. If a ProjectChannel has subscriptions, a Notification is dispatched only if the topic of the Notification is the same as the one set in the subscriptions. If there is no subscription in a ProjectChannel, all Notifications will be dispatched.
request_example: >-
{
"project_channel_id": "project-ch-cff007433a23",
"is_subscribe": true,
"subscriptions": [
"monitoring.Alert"
]
}
response_example: >-
{
"project_channel_id": "project-ch-cff007433a23",
"name": "sms-test",
"state": "ENABLED",
"data": {
"phone_number": "01033334444"
},
"is_subscribe": true,
"subscriptions": [
"monitoring.Alert"
],
"notification_level": "LV1",
"is_scheduled": true,
"schedule": {
"day_of_week": [
"MON",
"TUE",
"WED",
"THU",
"FRI"
],
"end_hour": 9
},
"tags": {},
"protocol_id": "protocol-ab94ea7d574e",
"project_id": "project-52a423012d5e",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-20T06:03:09.177Z"
}



> **POST** /notification/v1/project-channel/set-subscription
>






    
<br>

### enable

desc: Enables a specific ProjectChannel. If a ProjectChannel is enabled, the ProjectChannel can be used and the Notification can be dispatched. Even if a ProjectChannel is enabled, if the Protocol used in the ProjectChannel is disabled, the Notification is not dispatched.
request_example: >-
{
"project_channel_id": "project-ch-ffdb1d6cc774"
}



> **POST** /notification/v1/project-channel/enable
>






    
<br>

### disable

desc: Disables a specific ProjectChannel. If a ProjectChannel is disabled, the Notification is not dispatched, even if it is created.
request_example: >-
{
"project_channel_id": "project-ch-ffdb1d6cc774"
}



> **POST** /notification/v1/project-channel/disable
>






    
<br>

### delete

desc: Deletes a specific ProjectChannel.
request_example: >-
{
"project_channel_id": "project-ch-ffdb1d6cc774"
}



> **POST** /notification/v1/project-channel/delete
>






    
<br>

### get

desc: Gets a specific ProjectChannel. Prints detailed information about the ProjectChannel.
request_example: >-
{
"project_channel_id": "project-ch-ffdb1d6cc774"
}
response_example: >-
{
"project_channel_id": "project-ch-ffdb1d6cc774",
"name": "personal_email",
"state": "ENABLED",
"data": {
"email": "user1@cloudforet.io"
},
"notification_level": "LV1",
"tags": {},
"protocol_id": "protocol-e000a677ebdb",
"project_id": "project-52a423012d5e",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-20T04:40:21.264Z"
}



> **POST** /notification/v1/project-channel/get
>






    
<br>

### list

desc: Gets a list of all ProjectChannels. You can use a query to get a filtered list of ProjectChannels.
request_example: >-
{
"query": {
"filter": [
{
"key": "state",
"value": "ENABLED",
"operator": "eq"
}
]
}
}
response_example: >-
{
"results": [
{
"project_channel_id": "project-ch-473efcfde4b1",
"name": "Email Groups",
"state": "ENABLED",
"data": {
"email": "sykim1@cloudforet.io, sykim2@cloudforet.io"
},
"notification_level": "LV1",
"tags": {},
"protocol_id": "protocol-e000a677ebdb",
"project_id": "project-28cf4f2e6645",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-04-18T01:22:01.182Z"
},
{
"project_channel_id": "project-ch-98845ba0f975",
"name": "Song Email",
"state": "ENABLED",
"data": {
"email": "sykim@mz.co.kr"
},
"notification_level": "LV1",
"tags": {},
"protocol_id": "protocol-e000a677ebdb",
"project_id": "project-28cf4f2e6645",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-04-18T01:17:40.741Z"
}
],
"total_count": 2
}



> **POST** /notification/v1/project-channel/list
>






    
<br>

### stat





> **POST** /notification/v1/project-channel/stat
>






    


<br>
<br>

## Message



### CreateProjectChannelRequest
* **protocol_id** (string)  `Required` 

  *is_required: true
desc: The ID of protocol that will be set in project channel.*

    
* **name** (string)  `Required` 

  *is_required: true
desc: The name of Project Channel. It can have a maximum of 255 characters.*

    
* **data** (Struct)  `Required` 

  *is_required: true
desc: The data for using project channel.
This data is encrypted and stored in the Secret service if JSON schema in the protocol's metadata is set to SECRET type.
In this case, the secret ID that is stored in the security service will be returned and the data value will be empty.
if JSON schema in the protocol's metadata is set to PLAIN_TEXT type, This data is not encrypted and stored directly in the DB.*

    
* **is_subscribe** (bool)  `Required` 

  *is_required: false
desc: Indicates whether subscriptions will be used.*

    
* **subscriptions** (string)  `Required` 

  *is_required: false
desc: When using subscriptions, it indicates the topic list to subscription.
If is_subscribe is set to false, this value is ignored.*

    
* **notification_level** (NotificationLevel)  `Required` 

  *is_required: false
desc: Set the level of notification.
If a notification has a level and a notification level that this channel can receive is set, a notification is dispatched only if the notification level is the same.*

    
* **is_scheduled** (bool)  `Required` 

  *is_required: false
desc: Indicates whether schedule will be used.*

    
* **schedule** (ProjectChannelSchedule)  `Required` 

  *is_required: false
desc: Schedule for which you want to receive notifications through the project channel.*

    
* **tags** (Struct)  `Required` 

  *is_required: false
desc: The tags for project channel.*

    
* **project_id** (string)  `Required` 

  *is_required: true
desc: The ID of project to which the project channel belongs.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### GetProjectChannelRequest
* **project_channel_id** (string)  `Required` 

  *is_required: true
desc: The ID of project channel.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    
* **only** (string)  `Required` 

  *is_required: false
desc: The list of the project channel information column you want to be returned. It must be specified in the ProjectChannelInfo.*

    <br>

### ProjectChannelInfo
* **project_channel_id** (string)  `Required` 

  *desc: The ID of project channel.*

    
* **name** (string)  `Required` 

  *desc: The name of project channel*

    
* **state** (ProjectChannelState)  `Required` 

  *desc: The state of project channel. ENABLED or DISABLED only.*

    
* **data** (Struct)  `Required` 

  *desc: The data for using project channel.*

    
* **secret_id** (string)  `Required` 

  *The ID of secret encrypted data in the security service*

    
* **is_subscribe** (bool)  `Required` 

  *desc: Indicates whether subscriptions will be used.*

    
* **subscriptions** (string)  `Required` 

  *desc: The topic list to subscription.*

    
* **notification_level** (NotificationLevel)  `Required` 

  *desc: Set the level of notification.*

    
* **is_scheduled** (bool)  `Required` 

  *desc: Indicates whether schedule will be used.*

    
* **schedule** (ProjectChannelSchedule)  `Required` 

  *desc: Schedule for which you want to receive notifications through the project channel.*

    
* **tags** (Struct)  `Required` 

  *desc: The tags for project channel.*

    
* **protocol_id** (string)  `Required` 

  *desc: The ID of protocol set in the project channel.*

    
* **project_id** (string)  `Required` 

  *desc: The ID of project to which the project channel belongs.*

    
* **domain_id** (string)  `Required` 

  *desc: The ID of domain.*

    
* **created_at** (string)  `Required` 

  *desc: Project channel creation time.*

    <br>

### ProjectChannelQuery
* **query** (Query)  `Required` 

  *is_required: false
desc: Query format provided by SpaceONE. Please check the link for more information.*

    
* **project_channel_id** (string)  `Required` 

  *is_required: false
desc: The ID of project channel.*

    
* **name** (string)  `Required` 

  *is_required: false
desc: The name of project channel.*

    
* **state** (ProjectChannelState)  `Required` 

  *is_required: false
desc: The state of project channel. ENABLED or DISABLED only.*

    
* **secret_id** (string)  `Required` 

  *is_required: false
The ID of secret encrypted data in the security service*

    
* **notification_level** (NotificationLevel)  `Required` 

  *is_required: false
desc: The level of notification.*

    
* **protocol_id** (string)  `Required` 

  *is_required: false
desc: The ID of protocol set in the project channel.*

    
* **project_id** (string)  `Required` 

  *is_required: false
desc: The ID of project to which the project channel belongs.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### ProjectChannelRequest
* **project_channel_id** (string)  `Required` 

  *is_required: true
desc: The ID of project channel.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### ProjectChannelSchedule
* **day_of_week** (DayOfWeek)  `Required` 

  *desc: Day of the week to be notified.
As a list type, only types that can be specified from MON to SUN can be set.*

    
* **start_hour** (int32)  `Required` 

  *desc: Start time to receive notifications.
Only integer type can be set, and 0 to 23 can be.*

    
* **end_hour** (int32)  `Required` 

  *desc: End time to receive notifications.
Only integer type can be set, and 1 to 24 can be.*

    <br>

### ProjectChannelStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true
desc: Statistics Query format provided by SpaceONE. Please check the link for more information.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### ProjectChannelsInfo
* **results** (ProjectChannelInfo)  `Required` 

  *desc : List of queried project channels.*

    
* **total_count** (int32)  `Required` 

  *desc : Total counts of queried project channels.*

    <br>

### UpdateProjectChannelRequest
* **project_channel_id** (string)  `Required` 

  *is_required: true
desc: The ID of project channel.*

    
* **name** (string)  `Required` 

  *is_required: false
desc: The name of Project Channel. It can have a maximum of 255 characters.*

    
* **data** (Struct)  `Required` 

  *is_required: false
desc: The data for using project channel.
This data is encrypted and stored in the Secret service if JSON schema in the protocol's metadata is set to SECRET type.
In this case, the secret ID that is stored in the security service will be returned and the data value will be empty.
if JSON schema in the protocol's metadata is set to PLAIN_TEXT type, This data is not encrypted and stored directly in the DB.*

    
* **notification_level** (NotificationLevel)  `Required` 

  *is_required: false
desc: Set the level of notification.
If a notification has a level and a notification level that this channel can receive is set, a notification is dispatched only if the notification level is the same.*

    
* **tags** (Struct)  `Required` 

  *is_required: false
desc: The tags for project channel.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### UpdateProjectChannelScheduleRequest
* **project_channel_id** (string)  `Required` 

  *is_required: true
desc: The ID of project channel.*

    
* **is_scheduled** (bool)  `Required` 

  *is_required: true
desc: Indicates whether schedule will be used.*

    
* **schedule** (ProjectChannelSchedule)  `Required` 

  *is_required: false
desc: Schedule for which you want to receive notifications through the project channel.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### UpdateProjectChannelSubscriptionRequest
* **project_channel_id** (string)  `Required` 

  *is_required: true
desc: The ID of project channel.*

    
* **is_subscribe** (bool)  `Required` 

  *is_required: true
desc: Indicates whether subscriptions will be used.*

    
* **subscriptions** (string)  `Required` 

  *is_required: false
desc: When using subscriptions, it indicates the topic list to subscription.
If is_subscribe is set to false, this value is ignored.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>
