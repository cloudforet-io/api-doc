---
title: "Quota"
linkTitle: "Quota"
weight: 3
bookFlatSection: true
---
# [Quota](#Quota)
A Quota is a limit on protocol usage for a day or a month. You can manage the use of the protocol with a Quota.


>  **Package : spaceone.api.notification.v1**

<br>
<br>

## Quota





**Quota Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Quota#create) | [CreateQuotaRequest](Quota#createquotarequest) | [QuotaInfo](./Quota#quotainfo) |
| [**update**](./Quota#update) | [UpdateQuotaRequest](Quota#updatequotarequest) | [QuotaInfo](./Quota#quotainfo) |
| [**delete**](./Quota#delete) | [QuotaRequest](Quota#quotarequest) | [Empty](./Quota#empty) |
| [**get**](./Quota#get) | [QuotaRequest](Quota#quotarequest) | [QuotaInfo](./Quota#quotainfo) |
| [**list**](./Quota#list) | [QuotaQuery](Quota#quotaquery) | [QuotasInfo](./Quota#quotasinfo) |
| [**stat**](./Quota#stat) | [QuotaStatQuery](Quota#quotastatquery) | [Struct](./Quota#struct) |



    
<br>

### create

Creates a new Quota limiting the use of a selected Protocol for a day or a month. If the parameter `limit` has no value, it will be deemed unlimited. If a Protocol has not set a Quota, the default Quota set in the Config will be applied.



> **POST** /notification/v1/quota/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateQuotaRequest](./Quota#createquotarequest)

* **protocol_id** (string)  `Required` 


* **limit** (Struct)  `Required` 

  *The information about Quota limitation.*


* **domain_id** (string)  `Required` 

  *The ID of domain.*





{{< highlight json >}}
{
   "protocol_id": "protocol-123456789012",
   "limit": {
       "day": 5.0,
       "month": 7.0
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[QuotaInfo](#QUOTAINFO)
* **quota_id** (string)  `Required` 

  The ID of Quota.

* **protocol_id** (string)  `Required` 

  The ID of Protocol.

* **limit** (Struct)  `Required` 

  The information about Quota limitation.

* **domain_id** (string)  `Required` 

  The ID of domain



{{< highlight json >}}
{
   "quota_id": "quota-123456789012",
   "protocol_id": "protocol-123456789012",
   "limit": {
       "day": 5.0,
       "month": 7.0
   },
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Quota. You can make changes in Quota `limit`, managing the use of the Protocol.



> **POST** /notification/v1/quota/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateQuotaRequest](./Quota#updatequotarequest)

* **quota_id** (string)  `Required` 

  *The ID of Quota.*


* **limit** (Struct)  `Required` 

  *The information about Quota limitation.*


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "quota_id": "quota-123456789012",
   "limit": {
       "day": 10.0,
       "month": 15.0
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[QuotaInfo](#QUOTAINFO)
* **quota_id** (string)  `Required` 

  The ID of Quota.

* **protocol_id** (string)  `Required` 

  The ID of Protocol.

* **limit** (Struct)  `Required` 

  The information about Quota limitation.

* **domain_id** (string)  `Required` 

  The ID of domain



{{< highlight json >}}
{
   "quota_id": "quota-123456789012",
   "protocol_id": "protocol-123456789012",
   "limit": {
       "day": 5.0,
       "month": 7.0
   },
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific Quota. The default Quota set in the Config will be applied to the Protocol you deleted the Quota of.



> **POST** /notification/v1/quota/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[QuotaRequest](./Quota#quotarequest)

* **quota_id** (string)  `Required` 

  *The ID of Quota.*


* **domain_id** (string)  `Required` 

  *The ID of domain.*





{{< highlight json >}}
{
   "quota_id": "quota-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Quota. Prints detailed information about the Quota, including the `limit` and the Protocol limited by the Quota.



> **POST** /notification/v1/quota/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[QuotaRequest](./Quota#quotarequest)

* **quota_id** (string)  `Required` 

  *The ID of Quota.*


* **domain_id** (string)  `Required` 

  *The ID of domain.*





{{< highlight json >}}
{
   "quota_id": "quota-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[QuotaInfo](#QUOTAINFO)
* **quota_id** (string)  `Required` 

  The ID of Quota.

* **protocol_id** (string)  `Required` 

  The ID of Protocol.

* **limit** (Struct)  `Required` 

  The information about Quota limitation.

* **domain_id** (string)  `Required` 

  The ID of domain



{{< highlight json >}}
{
   "quota_id": "quota-123456789012",
   "protocol_id": "protocol-123456789012",
   "limit": {
       "day": 5.0,
       "month": 7.0
   },
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Quotas. You can use a query to get a filtered list of Quotas.



> **POST** /notification/v1/quota/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[QuotaQuery](./Quota#quotaquery)

* **domain_id** (string)  `Required` 

  *The ID of domain.*


* **query** (Query) 

  *Query format provided by SpaceONE. Please check the link for more information.*


* **quota_id** (string) 

  *The ID of Quota.*


* **protocol_id** (string) 

  *The ID of Protocol.*





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[QuotasInfo](#QUOTASINFO)
* **results** (QuotaInfo)  `Required` 

  List of queried Quota.

* **total_count** (int32)  `Required` 

  Total counts of queried Quota.



{{< highlight json >}}
{
   "results": [
       {
           "quota_id": "quota-123456789012",
           "protocol_id": "protocol-123456789012",
           "limit": {
               "day": 10.0,
               "month": 15.0
           },
           "domain_id": "domain-123456789012"
       },
       {
           "quota_id": "quota-987654321098",
           "protocol_id": "protocol-987654321098",
           "limit": {
               "day": 5.0,
               "month": 7.0
           },
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





> **POST** /notification/v1/quota/stat
>






    


<br>
<br>

## Message



### CreateQuotaRequest
* **protocol_id** (string)  `Required` 

    
* **limit** (Struct)  `Required` 

  *The information about Quota limitation.*

    
* **domain_id** (string)  `Required` 

  *The ID of domain.*

    <br>

### QuotaInfo
* **quota_id** (string)  `Required` 

  *The ID of Quota.*

    
* **protocol_id** (string)  `Required` 

  *The ID of Protocol.*

    
* **limit** (Struct)  `Required` 

  *The information about Quota limitation.*

    
* **domain_id** (string)  `Required` 

  *The ID of domain*

    <br>

### QuotaQuery
* **domain_id** (string)  `Required` 

  *The ID of domain.*

    
* **query** (Query) 

  *Query format provided by SpaceONE. Please check the link for more information.*

    
* **quota_id** (string) 

  *The ID of Quota.*

    
* **protocol_id** (string) 

  *The ID of Protocol.*

    <br>

### QuotaRequest
* **quota_id** (string)  `Required` 

  *The ID of Quota.*

    
* **domain_id** (string)  `Required` 

  *The ID of domain.*

    <br>

### QuotaStatQuery
* **query** (StatisticsQuery)  `Required` 

  *Statistics Query format provided by SpaceONE. Please check the link for more information.*

    
* **domain_id** (string)  `Required` 

  *The ID of domain.*

    <br>

### QuotasInfo
* **results** (QuotaInfo)  `Required` 

  *List of queried Quota.*

    
* **total_count** (int32)  `Required` 

  *Total counts of queried Quota.*

    <br>

### UpdateQuotaRequest
* **quota_id** (string)  `Required` 

  *The ID of Quota.*

    
* **limit** (Struct)  `Required` 

  *The information about Quota limitation.*

    
* **domain_id** (string)  `Required` 

    <br>
