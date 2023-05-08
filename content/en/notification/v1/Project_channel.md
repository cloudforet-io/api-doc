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

> **POST** /notification/v1/project-channel/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **PUT** /notification/v1/project-channel/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### set_schedule

> **POST** /notification/v1/project-channel/set-schedule
>




 {{< tabs " set_schedule " >}}




{{< /tabs >}}

    
<br>

### set_subscription

> **POST** /notification/v1/project-channel/set-subscription
>




 {{< tabs " set_subscription " >}}




{{< /tabs >}}

    
<br>

### enable

> **POST** /notification/v1/project-channel/enable
>




 {{< tabs " enable " >}}




{{< /tabs >}}

    
<br>

### disable

> **POST** /notification/v1/project-channel/disable
>




 {{< tabs " disable " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /notification/v1/project-channel/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /notification/v1/project-channel/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /notification/v1/project-channel/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /notification/v1/project-channel/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


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
