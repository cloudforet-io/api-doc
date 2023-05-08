---
title: "User_channel"
linkTitle: "User_channel"
weight: 3
bookFlatSection: true
---
# [User_channel](#User_channel)
desc: A UserChannel is a destination where Notifications are delivered. Notifications are generated via the Protocol set by each User.


>  **Package : spaceone.api.notification.v1**

<br>
<br>

## User_channel


**UserChannel Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./UserChannel#create) | [CreateUserChannelRequest](UserChannel#createuserchannelrequest) | [UserChannelInfo](./UserChannel#userchannelinfo) |
| [**update**](./UserChannel#update) | [UpdateUserChannelRequest](UserChannel#updateuserchannelrequest) | [UserChannelInfo](./UserChannel#userchannelinfo) |
| [**set_schedule**](./UserChannel#set_schedule) | [UpdateUserChannelScheduleRequest](UserChannel#updateuserchannelschedulerequest) | [UserChannelInfo](./UserChannel#userchannelinfo) |
| [**set_subscription**](./UserChannel#set_subscription) | [UpdateUserChannelSubscriptionRequest](UserChannel#updateuserchannelsubscriptionrequest) | [UserChannelInfo](./UserChannel#userchannelinfo) |
| [**enable**](./UserChannel#enable) | [UserChannelRequest](UserChannel#userchannelrequest) | [UserChannelInfo](./UserChannel#userchannelinfo) |
| [**disable**](./UserChannel#disable) | [UserChannelRequest](UserChannel#userchannelrequest) | [UserChannelInfo](./UserChannel#userchannelinfo) |
| [**delete**](./UserChannel#delete) | [UserChannelRequest](UserChannel#userchannelrequest) | [Empty](./UserChannel#empty) |
| [**get**](./UserChannel#get) | [GetUserChannelRequest](UserChannel#getuserchannelrequest) | [UserChannelInfo](./UserChannel#userchannelinfo) |
| [**list**](./UserChannel#list) | [UserChannelQuery](UserChannel#userchannelquery) | [UserChannelsInfo](./UserChannel#userchannelsinfo) |
| [**stat**](./UserChannel#stat) | [UserChannelStatQuery](UserChannel#userchannelstatquery) | [Struct](./UserChannel#struct) |



    
<br>

### create

> **POST** /notification/v1/user-channel/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /notification/v1/user-channel/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### set_schedule

> **POST** /notification/v1/user-channel/set-schedule
>




 {{< tabs " set_schedule " >}}




{{< /tabs >}}

    
<br>

### set_subscription

> **POST** /notification/v1/user-channel/set-subscription
>




 {{< tabs " set_subscription " >}}




{{< /tabs >}}

    
<br>

### enable

> **POST** /notification/v1/user-channel/enable
>




 {{< tabs " enable " >}}




{{< /tabs >}}

    
<br>

### disable

> **POST** /notification/v1/user-channel/disable
>




 {{< tabs " disable " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /notification/v1/user-channel/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /notification/v1/user-channel/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /notification/v1/user-channel/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /notification/v1/user-channel/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateUserChannelRequest
* **protocol_id** (string)  `Required` 

  *is_required: true
desc: The ID of protocol that will be set in user channel.*

    
* **name** (string)  `Required` 

  *is_required: true
desc: The name of User Channel. It can have a maximum of 255 characters.*

    
* **data** (Struct)  `Required` 

  *is_required: true
desc: The data for using user channel.
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

    
* **is_scheduled** (bool)  `Required` 

  *is_required: false
desc: Indicates whether schedule will be used.*

    
* **schedule** (UserChannelSchedule)  `Required` 

  *is_required: false
desc: Schedule for which you want to receive notifications through the user channel.*

    
* **tags** (Struct)  `Required` 

  *is_required: false
desc: The tags for user channel.*

    
* **user_id** (string)  `Required` 

  *is_required: true
desc: The ID of user*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### GetUserChannelRequest
* **user_channel_id** (string)  `Required` 

  *is_required: true
desc: The ID of user channel.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    
* **only** (string)  `Required` 

  *is_required: false
desc: The list of the user channel information column you want to be returned. It must be specified in the UserChannelInfo.*

    <br>

### UpdateUserChannelRequest
* **user_channel_id** (string)  `Required` 

  *is_required: true
desc: The ID of user channel.*

    
* **name** (string)  `Required` 

  *is_required: false
desc: The name of user channel. It can have a maximum of 255 characters.*

    
* **data** (Struct)  `Required` 

  *is_required: false
desc: The data for using user channel.
This data is encrypted and stored in the Secret service if JSON schema in the protocol's metadata is set to SECRET type.
In this case, the secret ID that is stored in the security service will be returned and the data value will be empty.
if JSON schema in the protocol's metadata is set to PLAIN_TEXT type, This data is not encrypted and stored directly in the DB.*

    
* **schedule** (UserChannelSchedule)  `Required` 

  *is_required: false
desc: Set the level of notification.
If a notification has a level and a notification level that this channel can receive is set, a notification is dispatched only if the notification level is the same.*

    
* **tags** (Struct)  `Required` 

  *is_required: false
desc: The tags for user channel.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### UpdateUserChannelScheduleRequest
* **user_channel_id** (string)  `Required` 

  *is_required: true
desc: The ID of user channel.*

    
* **is_scheduled** (bool)  `Required` 

  *is_required: true
desc: Indicates whether schedule will be used.*

    
* **schedule** (UserChannelSchedule)  `Required` 

  *is_required: false
desc: Schedule for which you want to receive notifications through the user channel.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### UpdateUserChannelSubscriptionRequest
* **user_channel_id** (string)  `Required` 

  *is_required: true
desc: The ID of user channel.*

    
* **is_subscribe** (bool)  `Required` 

  *is_required: true
desc: Indicates whether subscriptions will be used.*

    
* **subscriptions** (string)  `Required` 

  *is_required: false
If is_subscribe is set to false, this value is ignored.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### UserChannelInfo
* **user_channel_id** (string)  `Required` 

  *desc: The ID of user channel.*

    
* **name** (string)  `Required` 

  *desc: The name of user channel*

    
* **state** (UserChannelState)  `Required` 

  *desc: The state of user channel. ENABLED or DISABLED only.*

    
* **data** (Struct)  `Required` 

  *desc: The data for using user channel.*

    
* **secret_id** (string)  `Required` 

  *The ID of secret encrypted data in the security service*

    
* **is_subscribe** (bool)  `Required` 

  *desc: Indicates whether subscriptions will be used.*

    
* **subscriptions** (string)  `Required` 

  *desc: The topic list to subscription.*

    
* **is_scheduled** (bool)  `Required` 

  *desc: Indicates whether schedule will be used.*

    
* **schedule** (UserChannelSchedule)  `Required` 

  *desc: Schedule for which you want to receive notifications through the user channel.*

    
* **tags** (Struct)  `Required` 

  *desc: The tags for user channel.*

    
* **protocol_id** (string)  `Required` 

  *desc: The ID of protocol set in the user channel.*

    
* **user_id** (string)  `Required` 

  *desc: The ID of user using the user channel.*

    
* **domain_id** (string)  `Required` 

  *desc: The ID of domain.*

    
* **created_at** (string)  `Required` 

  *desc: User channel creation time.*

    <br>

### UserChannelQuery
* **query** (Query)  `Required` 

  *is_required: false
desc: Query format provided by SpaceONE. Please check the link for more information.*

    
* **user_channel_id** (string)  `Required` 

  *is_required: false
desc: The ID of user channel.*

    
* **name** (string)  `Required` 

  *is_required: false
desc: The name of user channel. It can have a maximum of 255 characters.*

    
* **state** (UserChannelState)  `Required` 

  *is_required: false
desc: The state of user channel. ENABLED or DISABLED only.*

    
* **secret_id** (string)  `Required` 

  *is_required: false
The ID of secret encrypted data in the security service*

    
* **protocol_id** (string)  `Required` 

  *is_required: false
desc: The ID of protocol set in the user channel.*

    
* **user_id** (string)  `Required` 

  *is_required: false
desc: The ID of user using the user channel.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### UserChannelRequest
* **user_channel_id** (string)  `Required` 

  *is_required: true
desc: The ID of user channel.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### UserChannelSchedule
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

### UserChannelStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true
desc: Statistics Query format provided by SpaceONE. Please check the link for more information.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### UserChannelsInfo
* **results** (UserChannelInfo)  `Required` 

  *desc : List of queried user channels.*

    
* **total_count** (int32)  `Required` 

  *desc : Total counts of queried user channels.*

    <br>
