---
title: "NamespaceGroup"
linkTitle: "NamespaceGroup"
weight: 3
bookFlatSection: true
---
# [NamespaceGroup](#NamespaceGroup)



>  **Package : spaceone.api.inventory_v2.v1**

<br>
<br>

## NamespaceGroup





**NamespaceGroup Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./NamespaceGroup#create) | [CreateNamespaceGroupRequest](NamespaceGroup#createnamespacegrouprequest) | [NamespaceGroupInfo](NamespaceGroup#namespacegroupinfo) |
| [**update**](./NamespaceGroup#update) | [UpdateNamespaceGroupRequest](NamespaceGroup#updatenamespacegrouprequest) | [NamespaceGroupInfo](NamespaceGroup#namespacegroupinfo) |
| [**delete**](./NamespaceGroup#delete) | [NamespaceGroupRequest](NamespaceGroup#namespacegrouprequest) | [Empty](NamespaceGroup#empty) |
| [**get**](./NamespaceGroup#get) | [NamespaceGroupRequest](NamespaceGroup#namespacegrouprequest) | [NamespaceGroupInfo](NamespaceGroup#namespacegroupinfo) |
| [**list**](./NamespaceGroup#list) | [NamespaceGroupQuery](NamespaceGroup#namespacegroupquery) | [NamespaceGroupsInfo](NamespaceGroup#namespacegroupsinfo) |
| [**stat**](./NamespaceGroup#stat) | [NamespaceGroupStatQuery](NamespaceGroup#namespacegroupstatquery) | [Struct](NamespaceGroup#struct) |



    
<br>

### create





> **POST** /inventory-v2/v1/namespace-group/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateNamespaceGroupRequest](./NamespaceGroup#createnamespacegrouprequest)

* **name** (string)   `Required` 


* **icon** (string)   `Required` 


* **resource_group** (string)   `Required` 


* **namespace_group_id** (string)  


* **description** (string)  


* **tags** (Struct)  


* **workspace_id** (string)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NamespaceGroupInfo](#NAMESPACEGROUPINFO)
* **namespace_group_id** (string)   `Required` 

* **name** (string)   `Required` 

* **icon** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **resource_group** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **description** (string)  

* **tags** (Struct)  



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update





> **POST** /inventory-v2/v1/namespace-group/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateNamespaceGroupRequest](./NamespaceGroup#updatenamespacegrouprequest)

* **namespace_group_id** (string)   `Required` 


* **name** (string)  


* **icon** (string)  


* **description** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NamespaceGroupInfo](#NAMESPACEGROUPINFO)
* **namespace_group_id** (string)   `Required` 

* **name** (string)   `Required` 

* **icon** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **resource_group** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **description** (string)  

* **tags** (Struct)  



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /inventory-v2/v1/namespace-group/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[NamespaceGroupRequest](./NamespaceGroup#namespacegrouprequest)

* **namespace_group_id** (string)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /inventory-v2/v1/namespace-group/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[NamespaceGroupRequest](./NamespaceGroup#namespacegrouprequest)

* **namespace_group_id** (string)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NamespaceGroupInfo](#NAMESPACEGROUPINFO)
* **namespace_group_id** (string)   `Required` 

* **name** (string)   `Required` 

* **icon** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **resource_group** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **description** (string)  

* **tags** (Struct)  



{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /inventory-v2/v1/namespace-group/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[NamespaceGroupQuery](./NamespaceGroup#namespacegroupquery)

* **query** (Query)  


* **namespace_group_id** (string)  


* **exist_only** (bool)  


* **workspace_id** (string)  





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### stat





> **POST** /inventory-v2/v1/namespace-group/stat
>






    


<br>
<br>

## Message



### CreateNamespaceGroupRequest
* **name** (string)   `Required` 

    
* **icon** (string)   `Required` 

    
* **resource_group** (string)   `Required` 

    
* **namespace_group_id** (string)  

    
* **description** (string)  

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    <br>

### NamespaceGroupInfo
* **namespace_group_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **icon** (string)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **resource_group** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    
* **description** (string)  

    
* **tags** (Struct)  

    <br>

### NamespaceGroupQuery
* **query** (Query)  

    
* **namespace_group_id** (string)  

    
* **exist_only** (bool)  

    
* **workspace_id** (string)  

    <br>

### NamespaceGroupRequest
* **namespace_group_id** (string)   `Required` 

    <br>

### NamespaceGroupStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### NamespaceGroupsInfo
* **results** (NamespaceGroupInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateNamespaceGroupRequest
* **namespace_group_id** (string)   `Required` 

    
* **name** (string)  

    
* **icon** (string)  

    
* **description** (string)  

    
* **tags** (Struct)  

    <br>
