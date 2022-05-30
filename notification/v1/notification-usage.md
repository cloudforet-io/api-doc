---
description:  
---
# Notification usage

>  **Package : spaceone.api.notification.v1**

## NotificationUsage

{% hint style="info" %}
**NotificationUsage Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**list**](notification-usage.md#list)|   [NotificationUsageQuery](notification-usage.md#notificationusagequery) |   [NotificationUsagesInfo](notification-usage.md#notificationusagesinfo) | Lists for the Notification usage information.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages. |
| [**stat**](notification-usage.md#stat)|   [NotificationUsageStatQuery](notification-usage.md#notificationusagestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   NotificationUsageQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   NotificationUsagesInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">Lists for the Notification usage information.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages.</td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   NotificationUsageStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
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
