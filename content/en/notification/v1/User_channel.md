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

desc: Creates a new UserChannel. A UserChannel is a channel that delivers a Notification to users when the Notification is created. When creating a UserChannel, one Protocol must be selected, and an Notification is dispatched via the selected Protocol.
request_example: >-
{
"protocol_id": "protocol-123456789012",
"name": "Email",
"data": {
"email": "user1@email.com"
},
"user_id": "user1@email.com",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"user_channel_id": "user-ch-123456789012",
"name": "Email",
"state": "ENABLED",
"data": {
"email": "user1@email.com"
},
"protocol_id": "protocol-123456789012",
"user_id": "user1@email.com",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T08:28:49.108Z"
}



> **POST** /notification/v1/user-channel/create
>






    
<br>

### update

desc: Updates a specific UserChannel. A UserChannel that has already been configured cannot be changed. Instead, the data required for dispatching Notifications to a UserChannel can be updated.
request_example: >-
{
"user_channel_id": "user-ch-123456789012",
"name": "Email2",
"data": {
"email": "user1@gmail.com"
},
"tags": {
"type": "test"
}
}
response_example: >-
{
"user_channel_id": "user-ch-123456789012",
"name": "Email2",
"state": "ENABLED",
"data": {
"email": "user1@gmail.com"
},
"protocol_id": "protocol-123456789012",
"user_id": "user1@email.com",
"tags": {
"type": "test"
},
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T08:28:49.108Z"
}



> **POST** /notification/v1/user-channel/update
>






    
<br>

### set_schedule

desc: Sets a schedule for a UserChannel. A schedule defines the time to receive a Notification. When a Notification is created, you can set the day of the week and time you want to receive it. When you set the day of the week, you can receive a notification only on the day of the week you set. If you also set the start time and end time with the day of the week, you can receive a Notification only at the scheduled time on the day of the week you set. If there is no schedule set in a UserChannel, Notifications will be dispatched at all times via the UserChannel.
request_example: >-
{
"user_channel_id": "user-ch-28097e8d5d59",
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
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"user_channel_id": "user-ch-28097e8d5d59",
"name": "my-email",
"state": "ENABLED",
"data": {
"email": "seolmin@mz.co.kr"
},
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
"protocol_id": "protocol-e000a677ebdb",
"user_id": "user1@cloudforet.io",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-03T08:28:49.108Z"
}



> **POST** /notification/v1/user-channel/set-schedule
>






    
<br>

### set_subscription

desc: Sets a subscription for a UserChannel. A subscription is a topic for channels to subscribe to and get notified about. If a UserChannel has subscriptions, a Notification is dispatched only if the topic of the Notification is the same as the one set in the subscriptions. If there is no subscription in a UserChannel, all Notifications will be dispatched.
request_example: >-
{
"user_channel_id": "user-ch-28097e8d5d59",
"is_subscribe": true,
"subscriptions": [
"monitoring.Alert"
],
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"user_channel_id": "user-ch-28097e8d5d59",
"name": "my-email",
"state": "ENABLED",
"data": {
"email": "user1@cloudforet.io"
},
"is_subscribe": true,
"subscriptions": [
"monitoring.Alert"
],
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
"protocol_id": "protocol-e000a677ebdb",
"user_id": "user1@cloudforet.io",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-03T08:28:49.108Z"
}



> **POST** /notification/v1/user-channel/set-subscription
>






    
<br>

### enable

desc: Enables a specific UserChannel. If a UserChannel is enabled, the UserChannel can be used and the Notification can be dispatched. Even if a UserChannel is enabled, if the Protocol used in the UserChannel is disabled, the Notification is not dispatched.
request_example: >-
{
"user_channel_id": "user-ch-123456789012"
}
response_example: >-
{
"user_channel_id": "user-ch-123456789012",
"name": "Email",
"state": "ENABLED",
"data": {
"email": "user1@email.com"
},
"protocol_id": "protocol-123456789012",
"user_id": "user1@email.com",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T08:28:49.108Z"
}



> **POST** /notification/v1/user-channel/enable
>






    
<br>

### disable

desc: Disables a specific UserChannel. If a UserChannel is disabled, the Notification is not dispatched, even if it is created.
request_example: >-
{
"user_channel_id": "user-ch-123456789012"
}
response_example: >-
{
"user_channel_id": "user-ch-123456789012",
"name": "Email",
"state": "DISABLED",
"data": {
"email": "user1@email.com"
},
"protocol_id": "protocol-123456789012",
"user_id": "user1@email.com",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T08:28:49.108Z"
}



> **POST** /notification/v1/user-channel/disable
>






    
<br>

### delete

desc: Deletes a specific UserChannel. You must specify the `user_channel_id` of the UserChannel to delete.
request_example: >-
{
"user_channel_id": "user-ch-123456789012"
}



> **POST** /notification/v1/user-channel/delete
>






    
<br>

### get

desc: Gets a specific UserChannel. Prints detailed information about the UserChannel, including the Protocol configured and the Notification settings.
request_example: >-
{
"user_channel_id": "user-ch-123456789012"
}
response_example: >-
{
"user_channel_id": "user-ch-123456789012",
"name": "Email",
"state": "ENABLED",
"data": {
"email": "user1@email.com"
},
"protocol_id": "protocol-123456789012",
"user_id": "user1@email.com",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T08:28:49.108Z"
}



> **POST** /notification/v1/user-channel/get
>






    
<br>

### list

desc: Gets a list of all UserChannels. You can use a query to get a filtered list of UserChannels.
request_example: >-
{
"query": {}
}
response_example: >-
{
"results": [
{
"user_channel_id": "user-ch-123456789012",
"name": "Email",
"state": "ENABLED",
"data": {
"email": "user1@email.com"
},
"protocol_id": "protocol-123456789012",
"user_id": "user1@email.com",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T08:28:49.108Z"
},
{
"user_channel_id": "user-ch-98765432109",
"name": "Email",
"state": "ENABLED",
"data": {
"email": "user2@email.com"
},
"is_scheduled": true,
"schedule": {
"day_of_week": [
"MON",
"TUE",
"WED",
"THU",
"FRI"
],
"start_hour": 3,
"end_hour": 23
},
"protocol_id": "protocol-123456789012",
"user_id": "user2@email.com",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T06:45:57.260Z"
}
],
"total_count": 2
}



> **POST** /notification/v1/user-channel/list
>






    
<br>

### stat





> **POST** /notification/v1/user-channel/stat
>






    


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
