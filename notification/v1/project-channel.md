---
description: A ProjectChannel is a destination  where Notifications are delivered. Notifications are generated via the Protocol set by each Project.
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

> Creates a new ProjectChannel. ProjectChannel is a channel that delivers a Notification to the Project when the Notification is created. When creating a ProjectChannel, one Protocol must be selected, and a Notification is dispatched via the selected Protocol.

| Type | Message |
| :--- | :--- |
| Request | [CreateProjectChannelRequest](project-channel.md#createprojectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "protocol_id": "protocol-ab94ea7d574e",
    "name": "sms-test",
    "data": {
        "phone_number": "01011112222"
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
    "project_id": "project-52a423012d5e"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /notification/v1/project-channel/{project_channel_id}
>

> Updates a specific ProjectChannel. A ProjectChannel that has already been configured cannot be changed. Instead, the data required for dispatching Notifications to a ProjectChannel can be updated.

| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectChannelRequest](project-channel.md#updateprojectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
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
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### set_schedule
> **PUT** /notification/v1/project-channel/{project_channel_id}/schedule
>

> Sets a schedule for a ProjectChannel. A schedule defines the time to receive a Notification. When a Notification is created, you can set the day of the week and time you want to receive it. When you set the day of the week, you can receive a notification only on the day of the week you set. If you also set the start time and end time with the day of the week, you can receive a Notification only at the scheduled time on the day of the week you set. If there is no schedule set in a ProjectChannel, Notifications will be dispatched at all times via the ProjectChannel.

| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectChannelScheduleRequest](project-channel.md#updateprojectchannelschedulerequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
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
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### set_subscription
> **PUT** /notification/v1/project-channel/{project_channel_id}/subscription
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectChannelSubscriptionRequest](project-channel.md#updateprojectchannelsubscriptionrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### enable
> **PUT** /notification/v1/project-channel/{project_channel_id}/enable
>

> Enables a specific ProjectChannel. If a ProjectChannel is enabled, the ProjectChannel can be used and the Notification can be dispatched. Even if a ProjectChannel is enabled, if the Protocol used in the ProjectChannel is disabled, the Notification is not dispatched.

| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelRequest](project-channel.md#projectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "project_channel_id": "project-ch-ffdb1d6cc774"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### disable
> **PUT** /notification/v1/project-channel/{project_channel_id}/disable
>

> Disables a specific ProjectChannel. If a ProjectChannel is disabled, the Notification is not dispatched, even if it is created.

| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelRequest](project-channel.md#projectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "project_channel_id": "project-ch-ffdb1d6cc774"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **DELETE** /notification/v1/project-channel/{project_channel_id}
>

> Deletes a specific ProjectChannel.

| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelRequest](project-channel.md#projectchannelrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "project_channel_id": "project-ch-ffdb1d6cc774"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /notification/v1/project-channel/{project_channel_id}
>

> Gets a specific ProjectChannel. Prints detailed information about the ProjectChannel.

| Type | Message |
| :--- | :--- |
| Request | [GetProjectChannelRequest](project-channel.md#getprojectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "project_channel_id": "project-ch-ffdb1d6cc774"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /notification/v1/project-channels
>
> **POST** /notification/v1/project-channels/search


> Gets a list of all ProjectChannels. You can use a query to get a filtered list of ProjectChannels.

| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelQuery](project-channel.md#projectchannelquery) |
| Response |  [ProjectChannelsInfo](project-channel.md#projectchannelsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
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
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
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
