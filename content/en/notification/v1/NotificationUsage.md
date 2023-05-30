---
title: "NotificationUsage"
linkTitle: "NotificationUsage"
weight: 3
bookFlatSection: true
---
# [NotificationUsage](#NotificationUsage)
A NotificationUsage is a resource indicating daily Protocol usage. The limit set by the resource Quota is applied based on the NotificationUsage.


>  **Package : spaceone.api.notification.v1**

<br>
<br>

## NotificationUsage





**NotificationUsage Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./NotificationUsage#list) | [NotificationUsageQuery](NotificationUsage#notificationusagequery) | [NotificationUsagesInfo](./NotificationUsage#notificationusagesinfo) |
| [**stat**](./NotificationUsage#stat) | [NotificationUsageStatQuery](NotificationUsage#notificationusagestatquery) | [Struct](./NotificationUsage#struct) |



    
<br>

### list

Gets a list of all NotificationUsages. You can use a query to get a filtered list of Notification Usages.



> **POST** /notification/v1/notification-usage/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[NotificationUsageQuery](./NotificationUsage#notificationusagequery)

* **domain_id** (string)  `Required` 

  *The ID of domain.*


* **query** (Query) 

  *Query format provided by SpaceONE. Please check the link for more information.*


* **protocol_id** (string) 

  *The ID of Protocol.*





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NotificationUsagesInfo](#NOTIFICATIONUSAGESINFO)
* **results** (NotificationUsageInfo)  `Required` 

  List of queried Notification Usage.

* **total_count** (int32)  `Required` 

  Total counts of queried Notification Usage.



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /notification/v1/notification-usage/stat
>






    


<br>
<br>

## Message



### NotificationUsageInfo
* **protocol_id** (string)  `Required` 

  *The ID of Protocol.*

    
* **usage_date** (string)  `Required` 

  *Usage Date.*

    
* **usage_month** (string)  `Required` 

  *Usage Month.*

    
* **count** (int32)  `Required` 

  *Usage count using actual notifications.*

    
* **fail_count** (int32)  `Required` 

  *Fail count when dispatching notifications.*

    
* **domain_id** (string)  `Required` 

  *The ID of domain*

    <br>

### NotificationUsageQuery
* **domain_id** (string)  `Required` 

  *The ID of domain.*

    
* **query** (Query) 

  *Query format provided by SpaceONE. Please check the link for more information.*

    
* **protocol_id** (string) 

  *The ID of Protocol.*

    <br>

### NotificationUsageStatQuery
* **query** (StatisticsQuery)  `Required` 

  *Statistics Query format provided by SpaceONE. Please check the link for more information.*

    
* **domain_id** (string)  `Required` 

  *The ID of domain.*

    <br>

### NotificationUsagesInfo
* **results** (NotificationUsageInfo)  `Required` 

  *List of queried Notification Usage.*

    
* **total_count** (int32)  `Required` 

  *Total counts of queried Notification Usage.*

    <br>
