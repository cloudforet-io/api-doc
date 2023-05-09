---
title: "Endpoint"
linkTitle: "Endpoint"
weight: 3
bookFlatSection: true
---
# [Endpoint](#Endpoint)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## Endpoint





**Endpoint Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./Endpoint#list) | [EndpointQuery](Endpoint#endpointquery) | [EndpointsInfo](./Endpoint#endpointsinfo) |



    
<br>

### list





> **POST** /identity/v1/endpoint/list
>






    


<br>
<br>

## Message



### EndpointInfo
* **service** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **endpoint** (string)  `Required` 

    
* **state** (EndpointState)  `Required` 

    
* **version** (string)  `Required` 

    <br>

### EndpointQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **service** (string)  `Required` 

  *is_required: false*

    
* **endpoint_type** (string)  `Required` 

  *is_required: false
example: public | internal*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### EndpointsInfo
* **results** (EndpointInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>
