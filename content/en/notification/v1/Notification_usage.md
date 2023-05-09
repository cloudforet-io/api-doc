---
title: "Notification_usage"
linkTitle: "Notification_usage"
weight: 3
bookFlatSection: true
---
# [Notification_usage](#Notification_usage)
desc: A NotificationUsage is a resource indicating daily Protocol usage. The limit set by the resource Quota is applied based on the NotificationUsage.


>  **Package : spaceone.api.notification.v1**

<br>
<br>

## Notification_usage





**NotificationUsage Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./NotificationUsage#list) | [NotificationUsageQuery](NotificationUsage#notificationusagequery) | [NotificationUsagesInfo](./NotificationUsage#notificationusagesinfo) |
| [**stat**](./NotificationUsage#stat) | [NotificationUsageStatQuery](NotificationUsage#notificationusagestatquery) | [Struct](./NotificationUsage#struct) |



    
<br>

### list

desc: Gets a list of all NotificationUsages. You can use a query to get a filtered list of Notification Usages.
request_example: >-
{
"query": {}
}
response_example: >-
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



> **POST** /notification/v1/notification-usage/list
>






    
<br>

### stat





> **POST** /notification/v1/notification-usage/stat
>






    


<br>
<br>

## Message



### NotificationUsageInfo
* **protocol_id** (string)  `Required` 

  *desc: The ID of Protocol.*

    
* **usage_date** (string)  `Required` 

  *desc: Usage Date.*

    
* **usage_month** (string)  `Required` 

  *desc: Usage Month.*

    
* **count** (int32)  `Required` 

  *desc: Usage count using actual notifications.*

    
* **fail_count** (int32)  `Required` 

  *desc: Fail count when dispatching notifications.*

    
* **domain_id** (string)  `Required` 

  *desc: The ID of domain*

    <br>

### NotificationUsageQuery
* **query** (Query)  `Required` 

  *is_required: false
desc: Query format provided by SpaceONE. Please check the link for more information.*

    
* **protocol_id** (string)  `Required` 

  *is_required: false
desc: The ID of Protocol.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### NotificationUsageStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true
desc: Statistics Query format provided by SpaceONE. Please check the link for more information.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### NotificationUsagesInfo
* **results** (NotificationUsageInfo)  `Required` 

  *desc: List of queried Notification Usage.*

    
* **total_count** (int32)  `Required` 

  *desc: Total counts of queried Notification Usage.*

    <br>
