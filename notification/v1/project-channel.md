---
description:  
---
# Project channel

>  **Package : spaceone.api.notification.v1**

## ProjectChannel

{% hint style="info" %}
**ProjectChannel Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](project-channel.md#create)|   [CreateProjectChannelRequest](project-channel.md#createprojectchannelrequest) |   [ProjectChannelInfo](project-channel.md#projectchannelinfo) |
| [**update**](project-channel.md#update)|   [UpdateProjectChannelRequest](project-channel.md#updateprojectchannelrequest) |   [ProjectChannelInfo](project-channel.md#projectchannelinfo) |
| [**set_schedule**](project-channel.md#set_schedule)|   [UpdateProjectChannelScheduleRequest](project-channel.md#updateprojectchannelschedulerequest) |   [ProjectChannelInfo](project-channel.md#projectchannelinfo) |
| [**set_subscription**](project-channel.md#set_subscription)|   [UpdateProjectChannelSubscriptionRequest](project-channel.md#updateprojectchannelsubscriptionrequest) |   [ProjectChannelInfo](project-channel.md#projectchannelinfo) |
| [**enable**](project-channel.md#enable)|   [ProjectChannelRequest](project-channel.md#projectchannelrequest) |   [ProjectChannelInfo](project-channel.md#projectchannelinfo) |
| [**disable**](project-channel.md#disable)|   [ProjectChannelRequest](project-channel.md#projectchannelrequest) |   [ProjectChannelInfo](project-channel.md#projectchannelinfo) |
| [**delete**](project-channel.md#delete)|   [ProjectChannelRequest](project-channel.md#projectchannelrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](project-channel.md#get)|   [GetProjectChannelRequest](project-channel.md#getprojectchannelrequest) |   [ProjectChannelInfo](project-channel.md#projectchannelinfo) |
| [**list**](project-channel.md#list)|   [ProjectChannelQuery](project-channel.md#projectchannelquery) |   [ProjectChannelsInfo](project-channel.md#projectchannelsinfo) |
| [**stat**](project-channel.md#stat)|   [ProjectChannelStatQuery](project-channel.md#projectchannelstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /notification/v1/project-channels
>

> Creates a new Project Channel.Project channel is the definition of the channel that delivers the notification to the project when the notification is created.When creating a Project Channel, one of the protocols must be selected, and an notification is dispatched through the selected protocol.

| Type | Message |
| :--- | :--- |
| Request | [CreateProjectChannelRequest](project-channel.md#createprojectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### update
> **PUT** /notification/v1/project-channel/{project_channel_id}
>

> Updates a Project Channel information.Protocol that has already been set cannot be changed. Instead, the data required to be dispatched notification for project channel is can be updated.

| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectChannelRequest](project-channel.md#updateprojectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### set_schedule
> **PUT** /notification/v1/project-channel/{project_channel_id}/schedule
>

> Schedule settings for project channels.When a notification is created, you can set the day and time you want to receive it through the schedule.When you set the day of the week in the schedule, you can receive a notification only on the set day of the week.If you also set the start time and end time with day of the week, you can receive a notification only at the set time on the set day of the week.If there is no schedule, notifications will be dispatched at all times through project channel.

| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectChannelScheduleRequest](project-channel.md#updateprojectchannelschedulerequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### set_subscription
> **PUT** /notification/v1/project-channel/{project_channel_id}/subscription
>

> Subscription settings for project channelsIf the project channel have subscriptions, notification is dispatched only if the topic of the notification is the same as the one set in the subscriptions.If no subscriptions in project channel, notifications will be dispatched all.

| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectChannelSubscriptionRequest](project-channel.md#updateprojectchannelsubscriptionrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### enable
> **PUT** /notification/v1/project-channel/{project_channel_id}/enable
>

> Enables a Project Channel.If the disabled project channel is enabled, the project channel can be used again and the notification can be dispatched.Even if the project channel is enabled, if the protocol being used in the project channel is disabled, the notification is not dispatched.

| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelRequest](project-channel.md#projectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### disable
> **PUT** /notification/v1/project-channel/{project_channel_id}/disable
>

> Disables a Project Channel.If you disable the project channel, the notification will not be dispatched, even if they are created.

| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelRequest](project-channel.md#projectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### delete
> **DELETE** /notification/v1/project-channel/{project_channel_id}
>

> Delete the Project Channel.

| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelRequest](project-channel.md#projectchannelrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /notification/v1/project-channel/{project_channel_id}
>

> Gets a single Project Channel.

| Type | Message |
| :--- | :--- |
| Request | [GetProjectChannelRequest](project-channel.md#getprojectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### list
> **GET** /notification/v1/project-channels
>
> **POST** /notification/v1/project-channels/search


> Lists the specified Project Channel.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages.

| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelQuery](project-channel.md#projectchannelquery) |
| Response |  [ProjectChannelsInfo](project-channel.md#projectchannelsinfo)  |
 
 

 
### stat
> **POST** /notification/v1/project-channels/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelStatQuery](project-channel.md#projectchannelstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateProjectChannelRequest
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
      <td style="text-align:left; width:100px;">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The ID of protocol that will be set in project channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The name of Project Channel. It can have a maximum of 255 characters.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The data for using project channel.This data is encrypted and stored in the Secret service if JSON schema in the protocol's metadata is set to SECRET type.In this case, the secret ID that is stored in the security service will be returned and the data value will be empty.if JSON schema in the protocol's metadata is set to PLAIN_TEXT type, This data is not encrypted and stored directly in the DB.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_subscribe</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">Indicates whether subscriptions will be used.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">subscriptions</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">When using subscriptions, it indicates the topic list to subscription.If is_subscribe is set to false, this value is ignored.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_level</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>LV1</li>
          	<li>LV2</li>
          	<li>LV3</li>
          	<li>LV4</li>
          	<li>LV5</li>
        </ul></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">Set the level of notification.If a notification has a level and a notification level that this channel can receive is set, a notification is dispatched only if the notification level is the same.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_scheduled</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">Indicates whether schedule will be used.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schedule</td>
      <td style="text-align:left"><a href="project-channel.md#projectchannelschedule">ProjectChannelSchedule</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left">Schedule for which you want to receive notifications through the project channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The tags for project channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The ID of project to which the project channel belongs.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The ID of domain.</td>
   </tr>
  </tbody>
</table>



### GetProjectChannelRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_channel_id |string|✔| The ID of project channel.|
| domain_id |string|✔| The ID of domain.|
| only |list of string|✘| The list of the project channel information column you want to be returned. It must be specified in the ProjectChannelInfo.|

### ProjectChannelInfo
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
      <td style="text-align:left; width:100px;">project_channel_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of project channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The name of project channel</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left">The state of project channel. ENABLED or DISABLED only.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The data for using project channel.</td>
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
      <td style="text-align:left; width:100px;">notification_level</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>LV1</li>
          	<li>LV2</li>
          	<li>LV3</li>
          	<li>LV4</li>
          	<li>LV5</li>
        </ul></td>
<td style="text-align:left">Set the level of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_scheduled</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left">Indicates whether schedule will be used.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schedule</td>
      <td style="text-align:left"><a href="project-channel.md#projectchannelschedule">ProjectChannelSchedule</a></td>
<td style="text-align:left">Schedule for which you want to receive notifications through the project channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The tags for project channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of protocol set in the project channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of project to which the project channel belongs.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of domain.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">Project channel creation time.</td>
   </tr>
  </tbody>
</table>



### ProjectChannelQuery
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
      <td style="text-align:left; width:100px;">project_channel_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The ID of project channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The name of project channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The state of project channel. ENABLED or DISABLED only.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_level</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>LV1</li>
          	<li>LV2</li>
          	<li>LV3</li>
          	<li>LV4</li>
          	<li>LV5</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The level of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The ID of protocol set in the project channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The ID of project to which the project channel belongs.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The ID of domain.</td>
   </tr>
  </tbody>
</table>



### ProjectChannelRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_channel_id |string|✔| The ID of project channel.|
| domain_id |string|✔| The ID of domain.|

### ProjectChannelSchedule
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



### ProjectChannelStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| domain_id |string|✔| The ID of domain.|

### ProjectChannelsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProjectChannelInfo](project-channel.md#projectchannelinfo) | List of queried project channels.|
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried project channels.|

### UpdateProjectChannelRequest
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
      <td style="text-align:left; width:100px;">project_channel_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The ID of project channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The name of Project Channel. It can have a maximum of 255 characters.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The data for using project channel.This data is encrypted and stored in the Secret service if JSON schema in the protocol's metadata is set to SECRET type.In this case, the secret ID that is stored in the security service will be returned and the data value will be empty.if JSON schema in the protocol's metadata is set to PLAIN_TEXT type, This data is not encrypted and stored directly in the DB.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_level</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>LV1</li>
          	<li>LV2</li>
          	<li>LV3</li>
          	<li>LV4</li>
          	<li>LV5</li>
        </ul></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">Set the level of notification.If a notification has a level and a notification level that this channel can receive is set, a notification is dispatched only if the notification level is the same.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The tags for project channel.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The ID of domain.</td>
   </tr>
  </tbody>
</table>



### UpdateProjectChannelScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_channel_id |string|✔| The ID of project channel.|
| is_scheduled |bool|✔| Indicates whether schedule will be used.|
| schedule |[ProjectChannelSchedule](project-channel.md#projectchannelschedule)|✘| Schedule for which you want to receive notifications through the project channel.|
| domain_id |string|✔| The ID of domain.|

### UpdateProjectChannelSubscriptionRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_channel_id |string|✔| The ID of project channel.|
| is_subscribe |bool|✔| Indicates whether subscriptions will be used.|
| subscriptions |list of string|✔| When using subscriptions, it indicates the topic list to subscription.If is_subscribe is set to false, this value is ignored.|
| domain_id |string|✔| The ID of domain.|
