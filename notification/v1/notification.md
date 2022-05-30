---
description:  
---
# Notification

>  **Package : spaceone.api.notification.v1**

## Notification

{% hint style="info" %}
**Notification Methods:**
desc: Notification service Methods
{%  endhint %}


| Method | Request | Response |
| :-----: | :--------: | :--------: |
| [**create**](notification.md#create)|   [CreateNotificationRequest](notification.md#createnotificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**push**](notification.md#push)|   [PushNotificationRequest](notification.md#pushnotificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**delete**](notification.md#delete)|   [NotificationRequest](notification.md#notificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**delete_all**](notification.md#delete_all)|   [NotificationDeleteAllRequest](notification.md#notificationdeleteallrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**set_read**](notification.md#set_read)|   [SetReadNotificationRequest](notification.md#setreadnotificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](notification.md#get)|   [GetNotificationRequest](notification.md#getnotificationrequest) |   [NotificationInfo](notification.md#notificationinfo) |
| [**list**](notification.md#list)|   [NotificationQuery](notification.md#notificationquery) |   [NotificationsInfo](notification.md#notificationsinfo) |
| [**stat**](notification.md#stat)|   [NotificationStatQuery](notification.md#notificationstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /notification/v1/notifications
>

> Create a new Notification.When a notification is created,it is propagated through the channel of the project to which the notification belongs,and if an internal channel or user channel is set,the notification is also propagated to the user.

| Type | Message |
| :--- | :--- |
| Request | [CreateNotificationRequest](notification.md#createnotificationrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "domain_id": "xxxx-aws-abcd",
    "tags": {
        "env": "dev"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "domain_id": "xxxx-aws-abcd"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### push
> **POST** /notification/v1/notifications/push
>

> Push a new Notification directly.

| Type | Message |
| :--- | :--- |
| Request | [PushNotificationRequest](notification.md#pushnotificationrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "domain_id": "xxxx-aws-abcd",
    "tags": {
        "env": "dev"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "domain_id": "xxxx-aws-abcd"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **DELETE** /notification/v1/notification/{notification_id}
>

> Delete the Notification.

| Type | Message |
| :--- | :--- |
| Request | [NotificationRequest](notification.md#notificationrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "domain_id": "xxxx-aws-abcd",
    "tags": {
        "env": "dev"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "domain_id": "xxxx-aws-abcd"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete_all
> **POST** /notification/v1/notification/delete_all
>

> Delete all Notifications.

| Type | Message |
| :--- | :--- |
| Request | [NotificationDeleteAllRequest](notification.md#notificationdeleteallrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "domain_id": "xxxx-aws-abcd",
    "tags": {
        "env": "dev"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "domain_id": "xxxx-aws-abcd"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### set_read
> **POST** /notification/v1/notifications/read
>

> Change the notifications to read status.

| Type | Message |
| :--- | :--- |
| Request | [SetReadNotificationRequest](notification.md#setreadnotificationrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /notification/v1/notification/{notification_id}
>

> Gets a single Notification.

| Type | Message |
| :--- | :--- |
| Request | [GetNotificationRequest](notification.md#getnotificationrequest) |
| Response |  [NotificationInfo](notification.md#notificationinfo)  |
 
 

 
### list
> **GET** /notification/v1/notifications
>
> **POST** /notification/v1/notifications/search


> Lists the specified notifications.

| Type | Message |
| :--- | :--- |
| Request | [NotificationQuery](notification.md#notificationquery) |
| Response |  [NotificationsInfo](notification.md#notificationsinfo)  |
 
 

 
### stat
> **POST** /notification/v1/notifications/stat
>


| Type | Message |
| :--- | :--- |
| Request | [NotificationStatQuery](notification.md#notificationstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateNotificationRequest
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
      <td style="text-align:left; width:100px;">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left">The type of resource to which the notification is dispatched.Currently, only "identity.Project" or "identity.User" can be set.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left">The ID of the resource to which notifications are dispatched.If resource_type is "identity.Project", then resource_id requires a project ID values.If resource_type is "identity.User", then resource_id requires a user ID value.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">topic</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left">The topic of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">message</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✅</td>
<td style="text-align:left">This message is used for each protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_type</td>
      <td style="text-align:left"><ul>
          	<li>NOTIFICATION_TYPE_NONE</li>
          	<li>INFO</li>
          	<li>ERROR</li>
          	<li>SUCCESS</li>
          	<li>WARNING</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The type of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_level</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ALL</li>
          	<li>LV1</li>
          	<li>LV2</li>
          	<li>LV3</li>
          	<li>LV4</li>
          	<li>LV5</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The level of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left">The ID of domain.</td>
   </tr>
  </tbody>
</table>



### GetNotificationRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| notification_id |string|✅| The ID of Notification.|
| domain_id |string|✅| The ID of domain.|
| only |list of string|❌| The list of the notification information column you want to be returned. It must be specified in the NotificationInfo.|

### NotificationDeleteAllRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| users |list of string|✅| ID list of users to be deleted|
| domain_id |string|| |

### NotificationInfo
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
      <td style="text-align:left; width:100px;">notification_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">topic</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The topic of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">message</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The contents of notification.This message is used for each protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_type</td>
      <td style="text-align:left"><ul>
          	<li>NOTIFICATION_TYPE_NONE</li>
          	<li>INFO</li>
          	<li>ERROR</li>
          	<li>SUCCESS</li>
          	<li>WARNING</li>
        </ul></td>
<td style="text-align:left">The type of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_level</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ALL</li>
          	<li>LV1</li>
          	<li>LV2</li>
          	<li>LV3</li>
          	<li>LV4</li>
          	<li>LV5</li>
        </ul></td>
<td style="text-align:left">The level of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_read</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left">Whether or not to check the notification.If notification has been returned at least once through the Get or List method, is_read is changed to True.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of user to whom the notification was dispatched.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of domain</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">Notification creation time.</td>
   </tr>
  </tbody>
</table>



### NotificationQuery
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
<td style="text-align:center">❌</td>
<td style="text-align:left">Query format provided by SpaceONE. Please check the link for more information.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The ID of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">topic</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The topic of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_type</td>
      <td style="text-align:left"><ul>
          	<li>NOTIFICATION_TYPE_NONE</li>
          	<li>INFO</li>
          	<li>ERROR</li>
          	<li>SUCCESS</li>
          	<li>WARNING</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The type of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_level</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ALL</li>
          	<li>LV1</li>
          	<li>LV2</li>
          	<li>LV3</li>
          	<li>LV4</li>
          	<li>LV5</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The level of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_read</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✅</td>
<td style="text-align:left">Whether or not to check the notification.If is_read is False, the user has not checked the notification yet.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">parent_notification_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The ID of parent notification. Not used yet.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The project ID to which the notification will be dispatched.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The ID of user.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left">The ID of domain.</td>
   </tr>
  </tbody>
</table>



### NotificationRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| notification_id |string|✅| The ID of Notification.|
| domain_id |string|✅| The ID of domain.|

### NotificationStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| domain_id |string|✅| The ID of domain.|

### NotificationsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of NotificationInfo](notification.md#notificationinfo) | List of queried notifications.|
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried notifications.|

### PushNotificationRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| protocol_id |string|✅| The ID of Protocol.|
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| message |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| notification_type |string|❌| |
| notification_level |string|❌| |
| domain_id |string|✅| |

### SetReadNotificationRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| notifications |list of string|✅| The ID list of notification that want to change read status.|
| domain_id |string|✅| The ID of domain.|
