---
title: "Endpoint"
linkTitle: "Endpoint"
weight: 3
bookFlatSection: true
---
# [Endpoint](#Endpoint)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Endpoint





**Endpoint Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./Endpoint#list) | [EndpointSearchQuery](Endpoint#endpointsearchquery) | [EndpointsInfo](Endpoint#endpointsinfo) |



    
<br>

### list

+noauth



> **POST** /identity/v2/endpoint/list
>






    


<br>
<br>

## Message



### EndpointInfo
* **name** (string)   `Required` 

    
* **service** (string)   `Required` 

    
* **endpoint** (string)   `Required` 

    
* **state** (EndpointState)   `Required` 

    
* **version** (string)   `Required` 

    <br>

### EndpointSearchQuery
* **query** (Query)  

    
* **service** (string)  

    <br>

### EndpointsInfo
* **results** (EndpointInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
