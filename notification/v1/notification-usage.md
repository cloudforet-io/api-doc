---
description:  
---
# Notification usage

>  **Package : spaceone.api.notification.v1**

## NotificationUsage

{% hint style="info" %}
**NotificationUsage Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**list**](notification-usage.md#list)|   [NotificationUsageQuery](notification-usage.md#notificationusagequery) |   [NotificationUsagesInfo](notification-usage.md#notificationusagesinfo) | Lists for the Notification usage information.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages. |
| [**stat**](notification-usage.md#stat)|   [NotificationUsageStatQuery](notification-usage.md#notificationusagestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**list**](notification-usage.md#list) </div> | <div style="width:200px; text-align:center;">    [NotificationUsageQuery](notification-usage.md#notificationusagequery)  </div> | <div style="width:200px; text-align:center;">   [NotificationUsagesInfo](notification-usage.md#notificationusagesinfo)  </div> | <div style="width:400px;"> Lists for the Notification usage information.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages. </div> |
|<div style="width:70px; text-align:center;">  [**stat**](notification-usage.md#stat) </div> | <div style="width:200px; text-align:center;">    [NotificationUsageStatQuery](notification-usage.md#notificationusagestatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
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
| Field | Type |  Description |
| :--- | :--- | :--- |
| protocol_id |string | The ID of Protocol.|
| usage_date |string | Usage Date.|
| usage_month |string | Usage Month.|
| count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Usage count using actual notifications.|
| domain_id |string | The ID of domain|

### NotificationUsageQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| Query format provided by SpaceONE. Please check the link for more information.|
| protocol_id |string|❌| The ID of Protocol.|
| domain_id |string|✅| The ID of domain.|

### NotificationUsageStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| domain_id |string|✅| The ID of domain.|

### NotificationUsagesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of NotificationUsageInfo](notification-usage.md#notificationusageinfo) | List of queried Notification Usage.|
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried Notification Usage.|
