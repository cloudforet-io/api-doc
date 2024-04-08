---
title: "Namespace"
linkTitle: "Namespace"
weight: 3
bookFlatSection: true
---
# [Namespace](#Namespace)



>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Namespace





**Namespace Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Namespace#create) | [CreateNamespaceRequest](Namespace#createnamespacerequest) | [NamespaceInfo](Namespace#namespaceinfo) |
| [**update**](./Namespace#update) | [UpdateNamespaceRequest](Namespace#updatenamespacerequest) | [NamespaceInfo](Namespace#namespaceinfo) |
| [**delete**](./Namespace#delete) | [NamespaceRequest](Namespace#namespacerequest) | [Empty](Namespace#empty) |
| [**get**](./Namespace#get) | [NamespaceRequest](Namespace#namespacerequest) | [NamespaceInfo](Namespace#namespaceinfo) |
| [**list**](./Namespace#list) | [NamespaceQuery](Namespace#namespacequery) | [NamespacesInfo](Namespace#namespacesinfo) |
| [**stat**](./Namespace#stat) | [NamespaceStatQuery](Namespace#namespacestatquery) | [Struct](Namespace#struct) |



    
<br>

### create





> **POST** /inventory/v1/namespace/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateNamespaceRequest](./Namespace#createnamespacerequest)

* **name** (string)   `Required` 


* **category** (string)   `Required` 


* **namespace_id** (string)  


* **provider** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NamespaceInfo](#NAMESPACEINFO)
* **namespace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **category** (string)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update





> **POST** /inventory/v1/namespace/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateNamespaceRequest](./Namespace#updatenamespacerequest)

* **namespace_id** (string)   `Required` 


* **name** (string)  


* **category** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NamespaceInfo](#NAMESPACEINFO)
* **namespace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **category** (string)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /inventory/v1/namespace/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[NamespaceRequest](./Namespace#namespacerequest)

* **namespace_id** (string)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /inventory/v1/namespace/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[NamespaceRequest](./Namespace#namespacerequest)

* **namespace_id** (string)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NamespaceInfo](#NAMESPACEINFO)
* **namespace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **category** (string)   `Required` 

* **provider** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /inventory/v1/namespace/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[NamespaceQuery](./Namespace#namespacequery)

* **query** (Query)  


* **namespace_id** (string)  


* **category** (string)  


* **provider** (string)  


* **is_managed** (string)  


* **workspace_id** (string)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### stat





> **POST** /inventory/v1/namespace/stat
>






    


<br>
<br>

## Message



### CreateNamespaceRequest
* **name** (string)   `Required` 

    
* **category** (string)   `Required` 

    
* **namespace_id** (string)  

    
* **provider** (string)  

    
* **tags** (Struct)  

    <br>

### NamespaceInfo
* **namespace_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **category** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### NamespaceQuery
* **query** (Query)  

    
* **namespace_id** (string)  

    
* **category** (string)  

    
* **provider** (string)  

    
* **is_managed** (string)  

    
* **workspace_id** (string)  

    <br>

### NamespaceRequest
* **namespace_id** (string)   `Required` 

    <br>

### NamespaceStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### NamespacesInfo
* **results** (NamespaceInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateNamespaceRequest
* **namespace_id** (string)   `Required` 

    
* **name** (string)  

    
* **category** (string)  

    
* **tags** (Struct)  

    <br>
