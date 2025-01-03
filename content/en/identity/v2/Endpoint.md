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

Get gRPC endpoint list.
+noauth



> **POST** /identity/v2/endpoint/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[EndpointSearchQuery](./Endpoint#endpointsearchquery)

* **query** (Query)  


* **service** (string)  


* **endpoint_type** (EndpointType)  





{{< highlight json >}}
{
 "service": "inventory",
 "endpoint_type": "PUBLIC",
 "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[EndpointsInfo](#ENDPOINTSINFO)
* **results** (EndpointInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
       {
           "name": "Inventory Service",
           "service": "inventory",
           "endpoint": "grpc://localhost:50051",
       }
   ],
   "total_count": 1
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    


<br>
<br>

## Message



### EndpointInfo
* **name** (string)   `Required` 

    
* **service** (string)   `Required` 

    
* **endpoint** (string)   `Required` 

    
* **internal_endpoint** (string)   `Required` 

    
* **state** (EndpointState)   `Required` 

    
* **version** (string)   `Required` 

    <br>

### EndpointSearchQuery
* **query** (Query)  

    
* **service** (string)  

    
* **endpoint_type** (EndpointType)  

    <br>

### EndpointsInfo
* **results** (EndpointInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
