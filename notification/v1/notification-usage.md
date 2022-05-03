---
description:  
---
# Notification usage

>  **Package : spaceone.api.notification.v1**

## NotificationUsage

{% hint style="info" %}
**NotificationUsage Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**list**](notification-usage.md#list)|   [NotificationUsageQuery](notification-usage.md#notificationusagequery) |   [NotificationUsagesInfo](notification-usage.md#notificationusagesinfo) | Lists for the Notification usage information.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages. |
| 2 | [**stat**](notification-usage.md#stat)|   [NotificationUsageStatQuery](notification-usage.md#notificationusagestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### list
> **GET** /notification/v1/notification-usages
>
> **POST** /notification/v1/notification-usages/search


> Lists for the Notification usage information.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages.

| Type | Message |
| :--- | :--- |
| Request | [NotificationUsageQuery](notification-usage.md#notificationusagequery) |
| Response |  [NotificationUsagesInfo](notification-usage.md#notificationusagesinfo)  |
 
 

 
### stat
> **POST** /notification/v1/notification-usages/stat
>


| Type | Message |
| :--- | :--- |
| Request | [NotificationUsageStatQuery](notification-usage.md#notificationusagestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### NotificationUsageInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | protocol_id |string | The ID of Protocol.|
| 2 | usage_date |string | Usage Date.|
| 3 | usage_month |string | Usage Month.|
| 4 | count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Usage count using actual notifications.|
| 5 | domain_id |string | The ID of domain|

### NotificationUsageQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| Query format provided by SpaceONE. Please check the link for more information.|
| 2 | protocol_id |string|❌| The ID of Protocol.|
| 3 | domain_id |string|✅| The ID of domain.|

### NotificationUsageStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| 2 | domain_id |string|✅| The ID of domain.|

### NotificationUsagesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of NotificationUsageInfo](notification-usage.md#notificationusageinfo) | List of queried Notification Usage.|
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried Notification Usage.|
