---
title: "Quota"
linkTitle: "Quota"
weight: 3
bookFlatSection: true
---
# [Quota](#Quota)
desc: A Quota is a limit on protocol usage for a day or a month. You can manage the use of the protocol with a Quota.


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

> **POST** /notification/v1/quota/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /notification/v1/quota/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /notification/v1/quota/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /notification/v1/quota/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /notification/v1/quota/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /notification/v1/quota/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateQuotaRequest
* **protocol_id** (string)  `Required` 

  *is_required: true*

    
* **limit** (Struct)  `Required` 

  *is_required: true
desc: The information about Quota limitation.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### QuotaInfo
* **quota_id** (string)  `Required` 

  *desc: The ID of Quota.*

    
* **protocol_id** (string)  `Required` 

  *desc: The ID of Protocol.*

    
* **limit** (Struct)  `Required` 

  *desc: The information about Quota limitation.*

    
* **domain_id** (string)  `Required` 

  *desc: The ID of domain*

    <br>

### QuotaQuery
* **query** (Query)  `Required` 

  *is_required: false
desc: Query format provided by SpaceONE. Please check the link for more information.*

    
* **quota_id** (string)  `Required` 

  *is_required: false
desc: The ID of Quota.*

    
* **protocol_id** (string)  `Required` 

  *is_required: false
desc: The ID of Protocol.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### QuotaRequest
* **quota_id** (string)  `Required` 

  *is_required: true
desc: The ID of Quota.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### QuotaStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true
desc: Statistics Query format provided by SpaceONE. Please check the link for more information.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain.*

    <br>

### QuotasInfo
* **results** (QuotaInfo)  `Required` 

  *desc: List of queried Quota.*

    
* **total_count** (int32)  `Required` 

  *desc: Total counts of queried Quota.*

    <br>

### UpdateQuotaRequest
* **quota_id** (string)  `Required` 

  *is_required: true
desc: The ID of Quota.*

    
* **limit** (Struct)  `Required` 

  *is_required: true
desc: The information about Quota limitation.*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
