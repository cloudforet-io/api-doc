---
description: A NotificationUsage is a resource indicating daily Protocol usage. The limit set by the resource Quota is applied based on the NotificationUsage.
---
# Notification usage

>  **Package : spaceone.api.notification.v1**

## NotificationUsage

{% hint style="info" %}
**NotificationUsage Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](notification-usage.md#list)|   [NotificationUsageQuery](notification-usage.md#notificationusagequery) |   [NotificationUsagesInfo](notification-usage.md#notificationusagesinfo) |
| [**stat**](notification-usage.md#stat)|   [NotificationUsageStatQuery](notification-usage.md#notificationusagestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### list
> **POST** /notification/v1/notification-usage/list
>

> Gets a list of all NotificationUsages. You can use a query to get a filtered list of Notification Usages.

| Type | Message |
| :--- | :--- |
| Request | [NotificationUsageQuery](notification-usage.md#notificationusagequery) |
| Response |  [NotificationUsagesInfo](notification-usage.md#notificationusagesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "protocol_id": "protocol-123456789012",
            "usage_date": "08",
            "usage_month": "2022-05",
            "count": 2,
            "domain_id": "domain-123456789012"
        },
        {
            "protocol_id": "protocol-123456789012",
            "usage_date": "18",
            "usage_month": "2022-05",
            "count": 7,
            "domain_id": "domain-123456789012"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /notification/v1/notification-usage/stat
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
| fail_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Fail count when dispatching notifications.|
| domain_id |string | The ID of domain|

### NotificationUsageQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| Query format provided by SpaceONE. Please check the link for more information.|
| protocol_id |string|✘| The ID of Protocol.|
| domain_id |string|✔| The ID of domain.|

### NotificationUsageStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| domain_id |string|✔| The ID of domain.|

### NotificationUsagesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of NotificationUsageInfo](notification-usage.md#notificationusageinfo) | List of queried Notification Usage.|
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried Notification Usage.|
