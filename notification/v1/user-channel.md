---
description:  
---
# User channel

>  **Package : spaceone.api.notification.v1**

## UserChannel

{% hint style="info" %}
**UserChannel Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](user-channel.md#create)|   [CreateUserChannelRequest](user-channel.md#createuserchannelrequest) |   [UserChannelInfo](user-channel.md#userchannelinfo) |
| [**update**](user-channel.md#update)|   [UpdateUserChannelRequest](user-channel.md#updateuserchannelrequest) |   [UserChannelInfo](user-channel.md#userchannelinfo) |
| [**set_schedule**](user-channel.md#set_schedule)|   [UpdateUserChannelScheduleRequest](user-channel.md#updateuserchannelschedulerequest) |   [UserChannelInfo](user-channel.md#userchannelinfo) |
| [**set_subscription**](user-channel.md#set_subscription)|   [UpdateUserChannelSubscriptionRequest](user-channel.md#updateuserchannelsubscriptionrequest) |   [UserChannelInfo](user-channel.md#userchannelinfo) |
| [**enable**](user-channel.md#enable)|   [UserChannelRequest](user-channel.md#userchannelrequest) |   [UserChannelInfo](user-channel.md#userchannelinfo) |
| [**disable**](user-channel.md#disable)|   [UserChannelRequest](user-channel.md#userchannelrequest) |   [UserChannelInfo](user-channel.md#userchannelinfo) |
| [**delete**](user-channel.md#delete)|   [UserChannelRequest](user-channel.md#userchannelrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](user-channel.md#get)|   [GetUserChannelRequest](user-channel.md#getuserchannelrequest) |   [UserChannelInfo](user-channel.md#userchannelinfo) |
| [**list**](user-channel.md#list)|   [UserChannelQuery](user-channel.md#userchannelquery) |   [UserChannelsInfo](user-channel.md#userchannelsinfo) |
| [**stat**](user-channel.md#stat)|   [UserChannelStatQuery](user-channel.md#userchannelstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /notification/v1/user-channels
>

> Creates a new User Channel.User channel is the definition of the channel that delivers the notification to users when the notification is created.When creating a User Channel, one of the protocols must be selected, and an notification is dispatched through the selected protocol.

| Type | Message |
| :--- | :--- |
| Request | [CreateUserChannelRequest](user-channel.md#createuserchannelrequest) |
| Response |  [UserChannelInfo](user-channel.md#userchannelinfo)  |
 
 

 
### update
> **PUT** /notification/v1/user-channel/{user_channel_id}
>

> Updates a User Channel information.Protocol that has already been set cannot be changed. Instead, the data required to be dispatched notification for user channel is can be updated.

| Type | Message |
| :--- | :--- |
| Request | [UpdateUserChannelRequest](user-channel.md#updateuserchannelrequest) |
| Response |  [UserChannelInfo](user-channel.md#userchannelinfo)  |
 
 

 
### set_schedule
> **PUT** /notification/v1/user-channel/{user_channel_id}/schedule
>

> Schedule settings for user channels.When a notification is created, you can set the day and time you want to receive it through the schedule.When you set the day of the week in the schedule, you can receive a notification only on the set day of the week.If you also set the start time and end time with day of the week, you can receive a notification only at the set time on the set day of the week.If there is no schedule, notifications will be dispatched at all times through user channel.

| Type | Message |
| :--- | :--- |
| Request | [UpdateUserChannelScheduleRequest](user-channel.md#updateuserchannelschedulerequest) |
| Response |  [UserChannelInfo](user-channel.md#userchannelinfo)  |
 
 

 
### set_subscription
> **PUT** /notification/v1/user-channel/{user_channel_id}/subscription
>

> Subscription settings for user channelsIf the user channel have subscriptions, notification is dispatched only if the topic of the notification is the same as the one set in the subscriptions.If no subscriptions in user channel, notifications will be dispatched all.

| Type | Message |
| :--- | :--- |
| Request | [UpdateUserChannelSubscriptionRequest](user-channel.md#updateuserchannelsubscriptionrequest) |
| Response |  [UserChannelInfo](user-channel.md#userchannelinfo)  |
 
 

 
### enable
> **PUT** /notification/v1/user-channel/{user_channel_id}/enable
>

> Enables a User Channel.If the disabled user channel is enabled, the user channel can be used again and the notification can be dispatched.Even if the user channel is enabled, if the protocol being used in the user channel is disabled, the notification is not dispatched.

| Type | Message |
| :--- | :--- |
| Request | [UserChannelRequest](user-channel.md#userchannelrequest) |
| Response |  [UserChannelInfo](user-channel.md#userchannelinfo)  |
 
 

 
### disable
> **PUT** /notification/v1/user-channel/{user_channel_id}/disable
>

> Disables a User Channel.If you disable the user channel, the notification will not be dispatched, even if they are created.

| Type | Message |
| :--- | :--- |
| Request | [UserChannelRequest](user-channel.md#userchannelrequest) |
| Response |  [UserChannelInfo](user-channel.md#userchannelinfo)  |
 
 

 
### delete
> **DELETE** /notification/v1/user-channel/{user_channel_id}
>

> Delete the User Channel.

| Type | Message |
| :--- | :--- |
| Request | [UserChannelRequest](user-channel.md#userchannelrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /notification/v1/user-channel/{user_channel_id}
>

> Gets a single User Channel.

| Type | Message |
| :--- | :--- |
| Request | [GetUserChannelRequest](user-channel.md#getuserchannelrequest) |
| Response |  [UserChannelInfo](user-channel.md#userchannelinfo)  |
 
 

 
### list
> **GET** /notification/v1/user-channels
>
> **POST** /notification/v1/user-channels/search


> Lists the specified User Channel.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages.

| Type | Message |
| :--- | :--- |
| Request | [UserChannelQuery](user-channel.md#userchannelquery) |
| Response |  [UserChannelsInfo](user-channel.md#userchannelsinfo)  |
 
 

 
### stat
> **POST** /notification/v1/user-channels/stat
>


| Type | Message |
| :--- | :--- |
| Request | [UserChannelStatQuery](user-channel.md#userchannelstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateUserChannelRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| protocol_id |string|✔| The ID of protocol that will be set in user channel.|
| name |string|✔| The name of User Channel. It can have a maximum of 255 characters.|
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| The data for using user channel.This data is encrypted and stored in the Secret service if JSON schema in the protocol's metadata is set to SECRET type.In this case, the secret ID that is stored in the security service will be returned and the data value will be empty.if JSON schema in the protocol's metadata is set to PLAIN_TEXT type, This data is not encrypted and stored directly in the DB.|
| is_subscribe |bool|✘| Indicates whether subscriptions will be used.|
| subscriptions |list of string|✔| When using subscriptions, it indicates the topic list to subscription.If is_subscribe is set to false, this value is ignored.|
| is_scheduled |bool|✘| Indicates whether schedule will be used.|
| schedule |[UserChannelSchedule](user-channel.md#userchannelschedule)|✘| Schedule for which you want to receive notifications through the user channel.|
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| The tags for user channel.|
| user_id |string|✔| The ID of user|
| domain_id |string|✔| The ID of domain.|

### GetUserChannelRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_channel_id |string|✔| The ID of user channel.|
| domain_id |string|✔| The ID of domain.|
| only |list of string|✘| The list of the user channel information column you want to be returned. It must be specified in the UserChannelInfo.|

### UpdateUserChannelRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_channel_id |string|✔| The ID of user channel.|
| name |string|✘| The name of user channel. It can have a maximum of 255 characters.|
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| The data for using user channel.This data is encrypted and stored in the Secret service if JSON schema in the protocol's metadata is set to SECRET type.In this case, the secret ID that is stored in the security service will be returned and the data value will be empty.if JSON schema in the protocol's metadata is set to PLAIN_TEXT type, This data is not encrypted and stored directly in the DB.|
| schedule |[UserChannelSchedule](user-channel.md#userchannelschedule)|✔| Set the level of notification.If a notification has a level and a notification level that this channel can receive is set, a notification is dispatched only if the notification level is the same.|
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| The tags for user channel.|
| domain_id |string|✔| The ID of domain.|

### UpdateUserChannelScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_channel_id |string|✔| The ID of user channel.|
| is_scheduled |bool|✔| Indicates whether schedule will be used.|
| schedule |[UserChannelSchedule](user-channel.md#userchannelschedule)|✘| Schedule for which you want to receive notifications through the user channel.|
| domain_id |string|✔| The ID of domain.|

### UpdateUserChannelSubscriptionRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_channel_id |string|✔| The ID of user channel.|
| is_subscribe |bool|✔| Indicates whether subscriptions will be used.|
| subscriptions |list of string|✔| |
| domain_id |string|✔| The ID of domain.|

### UserChannelInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">user_channel_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of user channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The name of user channel</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left">The state of user channel. ENABLED or DISABLED only.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The data for using user channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of secret encrypted data in the security service</td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_subscribe</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left">Indicates whether subscriptions will be used.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">subscriptions</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left">The topic list to subscription.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_scheduled</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left">Indicates whether schedule will be used.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schedule</td>
      <td style="text-align:left"><a href="user-channel.md#userchannelschedule">UserChannelSchedule</a></td>
<td style="text-align:left">Schedule for which you want to receive notifications through the user channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The tags for user channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of protocol set in the user channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of user using the user channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of domain.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">User channel creation time.</td>
   </tr>
  </tbody>
</table>



### UserChannelQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left">Query format provided by SpaceONE. Please check the link for more information.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_channel_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The ID of user channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The name of user channel. It can have a maximum of 255 characters.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The state of user channel. ENABLED or DISABLED only.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The ID of protocol set in the user channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The ID of user using the user channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The ID of domain.</td>
   </tr>
  </tbody>
</table>



### UserChannelRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_channel_id |string|✔| The ID of user channel.|
| domain_id |string|✔| The ID of domain.|

### UserChannelSchedule
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">day_of_week</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>MON</li>
          	<li>TUE</li>
          	<li>WED</li>
          	<li>THU</li>
          	<li>FRI</li>
          	<li>SAT</li>
          	<li>SUN</li>
        </ul></td>
<td style="text-align:left">Day of the week to be notified.As a list type, only types that can be specified from MON to SUN can be set.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">start_hour</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left">Start time to receive notifications.Only integer type can be set, and 0 to 23 can be.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">end_hour</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left">End time to receive notifications.Only integer type can be set, and 1 to 24 can be.</td>
   </tr>
  </tbody>
</table>



### UserChannelStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| domain_id |string|✔| The ID of domain.|

### UserChannelsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of UserChannelInfo](user-channel.md#userchannelinfo) | List of queried user channels.|
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried user channels.|
