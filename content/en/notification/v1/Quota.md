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

desc: Creates a new Quota limiting the use of a selected Protocol for a day or a month. If the parameter `limit` has no value, it will be deemed unlimited. If a Protocol has not set a Quota, the default Quota set in the Config will be applied.
request_example: >-
{
"protocol_id": "protocol-123456789012",
"limit": {
"day": 5.0,
"month": 7.0
}
}
response_example: >-
{
"quota_id": "quota-123456789012",
"protocol_id": "protocol-123456789012",
"limit": {
"day": 5.0,
"month": 7.0
},
"domain_id": "domain-123456789012"
}



> **POST** /notification/v1/quota/create
>






    
<br>

### update

desc: Updates a specific Quota. You can make changes in Quota `limit`, managing the use of the Protocol.
request_example: >-
{
"quota_id": "quota-123456789012",
"limit": {
"day": 10.0,
"month": 15.0
}
}
response_example: >-
{
"quota_id": "quota-123456789012",
"protocol_id": "protocol-123456789012",
"limit": {
"day": 10.0,
"month": 15.0
},
"domain_id": "domain-123456789012"
}



> **POST** /notification/v1/quota/update
>






    
<br>

### delete

desc: Deletes a specific Quota. The default Quota set in the Config will be applied to the Protocol you deleted the Quota of.
request_example: >-
{
"quota_id": "quota-123456789012"
}



> **POST** /notification/v1/quota/delete
>






    
<br>

### get

desc: Gets a specific Quota. Prints detailed information about the Quota, including the `limit` and the Protocol limited by the Quota.
request_example: >-
{
"quota_id": "quota-123456789012"
}
response_example: >-
{
"quota_id": "quota-123456789012",
"protocol_id": "protocol-123456789012",
"limit": {
"day": 10.0,
"month": 15.0
},
"domain_id": "domain-123456789012"
}



> **POST** /notification/v1/quota/get
>






    
<br>

### list

desc: Gets a list of all Quotas. You can use a query to get a filtered list of Quotas.
request_example: >-
{
"query": {}
}
response_example: >-
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



> **POST** /notification/v1/quota/list
>






    
<br>

### stat





> **POST** /notification/v1/quota/stat
>






    


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
