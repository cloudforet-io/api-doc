---
description:  
---
# Notification

>  **Package : spaceone.api.notification.v1**

## Notification

{% hint style="info" %}
**Notification Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](notification.md#create)|   [CreateNotificationRequest](notification.md#createnotificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| Creates a new Notification.A notification is a definition of an event to be delivered to the user.When a notification is created, it is propagated through the channel of the project to which the notification belongs,and if an internal channel or user channel is set, the notification is also propagated to the user. |
| 2 | [**delete**](notification.md#delete)|   [NotificationRequest](notification.md#notificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| Delete the Notification. |
| 3 | [**set_read**](notification.md#set_read)|   [SetReadNotificationRequest](notification.md#setreadnotificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| Change the notifications to read status.When the notification is created, the is_read value is False, and when the set_read method is used, the read state can be changed. |
| 4 | [**get**](notification.md#get)|   [GetNotificationRequest](notification.md#getnotificationrequest) |   [NotificationInfo](notification.md#notificationinfo) | Gets a single Notification. |
| 5 | [**list**](notification.md#list)|   [NotificationQuery](notification.md#notificationquery) |   [NotificationsInfo](notification.md#notificationsinfo) | Lists the specified notifications.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages. |
| 6 | [**stat**](notification.md#stat)|   [NotificationStatQuery](notification.md#notificationstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /notification/v1/notifications
>

> Creates a new Notification.A notification is a definition of an event to be delivered to the user.When a notification is created, it is propagated through the channel of the project to which the notification belongs,and if an internal channel or user channel is set, the notification is also propagated to the user.

| Type | Message |
| :--- | :--- |
| Request | [CreateNotificationRequest](notification.md#createnotificationrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### delete
> **DELETE** /notification/v1/notification/{notification_id}
>

> Delete the Notification.

| Type | Message |
| :--- | :--- |
| Request | [NotificationRequest](notification.md#notificationrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### set_read
> **POST** /notification/v1/notifications/read
>

> Change the notifications to read status.When the notification is created, the is_read value is False, and when the set_read method is used, the read state can be changed.

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


> Lists the specified notifications.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages.

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
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">resource_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">topic</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left">The topic of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">message</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">notification_type</td>
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
      <td style="text-align:left">6</td>
      <td style="text-align:left">notification_level</td>
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
      <td style="text-align:left">7</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### GetNotificationRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | notification_id |string|✅| The ID of Notification.|
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| The list of the notification information column you want to be returned. It must be specified in the NotificationInfo.|

### NotificationInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">notification_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of notification.</td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">topic</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The topic of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">message</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The contents of notification.This message is used for each protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">notification_type</td>
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
      <td style="text-align:left">5</td>
      <td style="text-align:left">notification_level</td>
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
      <td style="text-align:left">6</td>
      <td style="text-align:left">is_read</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left">Whether or not to check the notification.If notification has been returned at least once through the Get or List method, is_read is changed to True.</td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of user to whom the notification was dispatched.</td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of domain</td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">Notification creation time.</td>
   </tr>
  </tbody>
</table>



### NotificationQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left">Query format provided by SpaceONE. Please check the link for more information.</td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">notification_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The ID of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">topic</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The topic of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">notification_type</td>
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
      <td style="text-align:left">5</td>
      <td style="text-align:left">notification_level</td>
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
      <td style="text-align:left">6</td>
      <td style="text-align:left">is_read</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✅</td>
<td style="text-align:left">Whether or not to check the notification.If is_read is False, the user has not checked the notification yet.</td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">parent_notification_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### NotificationRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | notification_id |string|✅| The ID of Notification.|
| 2 | domain_id |string|✅| |

### NotificationStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| 2 | domain_id |string|✅| |

### NotificationsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of NotificationInfo](notification.md#notificationinfo) | List of queried notifications.|
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried notifications.|

### SetReadNotificationRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | notifications |list of string|✅| The ID list of notification that want to change read status.|
| 2 | domain_id |string|✅| |
