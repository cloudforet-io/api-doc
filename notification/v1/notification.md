---
description: A Notification is a service that delivers event data generated in Cloudforet to a Project or User.
---
# Notification

>  **Package : spaceone.api.notification.v1**

## Notification

{% hint style="info" %}
**Notification Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](notification.md#create)|   [CreateNotificationRequest](notification.md#createnotificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**push**](notification.md#push)|   [PushNotificationRequest](notification.md#pushnotificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**delete**](notification.md#delete)|   [NotificationRequest](notification.md#notificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**set_read**](notification.md#set_read)|   [SetReadNotificationRequest](notification.md#setreadnotificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](notification.md#get)|   [GetNotificationRequest](notification.md#getnotificationrequest) |   [NotificationInfo](notification.md#notificationinfo) |
| [**list**](notification.md#list)|   [NotificationQuery](notification.md#notificationquery) |   [NotificationsInfo](notification.md#notificationsinfo) |
| [**stat**](notification.md#stat)|   [NotificationStatQuery](notification.md#notificationstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /notification/v1/notifications
>

> Creates a new Notification. When a Notification is created, it is delivered to a UserChannel or a ProjectChannel depending on the parameter `resource_type`. If a Notification is delivered to a UserChannel, the `resource_type` is `identity.User`, and if a Notification is delivered to a ProjectChannel, the `resource_type` is `identity.Project`.

| Type | Message |
| :--- | :--- |
| Request | [CreateNotificationRequest](notification.md#createnotificationrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
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
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### push
> **POST** /notification/v1/notifications/push
>

> Manually raises a Notification. A Notification is raised with a message to be sent using a valid specific Protocol, and data used for a specific Protocol such as a phone number.

| Type | Message |
| :--- | :--- |
| Request | [PushNotificationRequest](notification.md#pushnotificationrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **DELETE** /notification/v1/notification/{notifications}
>

> Deletes multiple Notifications. You must specify `notifications` of the list of Notifications to delete.

| Type | Message |
| :--- | :--- |
| Request | [NotificationRequest](notification.md#notificationrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "notifications": [
        "notification-4025c1b61225",
        "notification-13hk3fh32534",
        "notification-4kth40jth5jy"
    ]
}
```
{% endtab %}
{% endtabs %}
 
 

 
### set_read
> **POST** /notification/v1/notifications/read
>


| Type | Message |
| :--- | :--- |
| Request | [SetReadNotificationRequest](notification.md#setreadnotificationrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /notification/v1/notification/{notification_id}
>

> Gets a specific Notification. Prints detailed information about the Notification, including not only the message contents(`title`, `description`) but also related data such as created time and urgency.

| Type | Message |
| :--- | :--- |
| Request | [GetNotificationRequest](notification.md#getnotificationrequest) |
| Response |  [NotificationInfo](notification.md#notificationinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "notification_id": "notification-4025c1b61225"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /notification/v1/notifications
>
> **POST** /notification/v1/notifications/search



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
<td style="text-align:center">✔</td>
<td style="text-align:left">The type of resource to which the notification is dispatched.Currently, only "identity.Project" or "identity.User" can be set.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The ID of the resource to which notifications are dispatched.If resource_type is "identity.Project", then resource_id requires a project ID values.If resource_type is "identity.User", then resource_id requires a user ID value.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">topic</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The topic of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">message</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✔</td>
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
<td style="text-align:center">✘</td>
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
<td style="text-align:center">✘</td>
<td style="text-align:left">The level of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The ID of domain.</td>
   </tr>
  </tbody>
</table>



### GetNotificationRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| notification_id |string|✔| The ID of Notification.|
| domain_id |string|✔| The ID of domain.|
| only |list of string|✘| The list of the notification information column you want to be returned. It must be specified in the NotificationInfo.|

### NotificationDeleteAllRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| notifications |list of string|✔| ID list of users to be deleted|
| user_id |string|| |
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
<td style="text-align:center">✘</td>
<td style="text-align:left">Query format provided by SpaceONE. Please check the link for more information.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The ID of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">topic</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
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
<td style="text-align:center">✘</td>
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
<td style="text-align:center">✘</td>
<td style="text-align:left">The level of notification.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_read</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">Whether or not to check the notification.If is_read is False, the user has not checked the notification yet.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">parent_notification_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The ID of parent notification. Not used yet.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The project ID to which the notification will be dispatched.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left">The ID of user.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The ID of domain.</td>
   </tr>
  </tbody>
</table>



### NotificationRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| notification_id |string|✔| The ID of Notification.|
| domain_id |string|✔| The ID of domain.|

### NotificationStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| domain_id |string|✔| The ID of domain.|

### NotificationsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of NotificationInfo](notification.md#notificationinfo) | List of queried notifications.|
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried notifications.|

### PushNotificationRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| protocol_id |string|✔| The ID of Protocol.|
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| message |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| notification_type |string|✘| |
| notification_level |string|✘| |
| domain_id |string|✔| |

### SetReadNotificationRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| notifications |list of string|✔| The ID list of notification that want to change read status.|
| domain_id |string|✔| The ID of domain.|
