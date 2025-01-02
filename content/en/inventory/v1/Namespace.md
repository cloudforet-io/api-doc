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

Create a new namespace.



> **POST** /inventory/v1/namespace/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateNamespaceRequest](./Namespace#createnamespacerequest)

* **name** (string)   `Required` 


* **category** (string)   `Required` 


* **resource_type** (string)   `Required` 


* **resource_group** (ResourceGroup)   `Required` 


* **namespace_id** (string)  


* **group** (string)  


* **icon** (string)  


* **tags** (Struct)  


* **workspace_id** (string)  





{{< highlight json >}}
{
    "namespace_id": "ns-azure-aks-cluster",
    "name": "AKS/Cluster",
    "category": "ASSET",
    "resource_type": "inventory.CloudService:azure.AKS.Cluster",
    "group": "azure",
    "icon": "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/azure/aks.svg",
    "tags": {},
    "is_managed": true,
    "resource_group": "DOMAIN",
    "domain_id": "domain-286776a1516a",
    "workspace_id": "*",
    "created_at": "2024-09-27T14:40:58.290Z",
    "updated_at": "2024-09-27T14:40:58.290Z"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NamespaceInfo](#NAMESPACEINFO)
* **namespace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **category** (string)   `Required` 

* **resource_type** (string)   `Required` 

* **group** (string)   `Required` 

* **icon** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
    "namespace_id": "ns-azure-aks-cluster",
    "name": "AKS/Cluster",
    "category": "ASSET",
    "resource_type": "inventory.CloudService:azure.AKS.Cluster",
    "group": "azure",
    "icon": "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/azure/aks.svg",
    "tags": {},
    "is_managed": true,
    "resource_group": "DOMAIN",
    "domain_id": "domain-286776a1516a",
    "workspace_id": "*",
    "created_at": "2024-09-27T14:40:58.290Z",
    "updated_at": "2024-09-27T14:40:58.290Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Update a specific namespace.



> **POST** /inventory/v1/namespace/update
>





 {{< tabs " update " >}}



 {{< tab "Response Example" >}}

[NamespaceInfo](#NAMESPACEINFO)
* **namespace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **category** (string)   `Required` 

* **resource_type** (string)   `Required` 

* **group** (string)   `Required` 

* **icon** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
    "namespace_id": "ns-azure-aks-cluster",
    "name": "AKS/Cluster",
    "category": "ASSET",
    "resource_type": "inventory.CloudService:azure.AKS.Cluster",
    "group": "azure",
    "icon": "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/azure/aks.svg",
    "tags": {},
    "is_managed": true,
    "resource_group": "DOMAIN",
    "domain_id": "domain-286776a1516a",
    "workspace_id": "*",
    "created_at": "2024-09-27T14:40:58.290Z",
    "updated_at": "2024-09-27T14:40:58.290Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Delete a specific namespace.



> **POST** /inventory/v1/namespace/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[NamespaceRequest](./Namespace#namespacerequest)

* **namespace_id** (string)   `Required` 





{{< highlight json >}}
{
    "namespace_id": "ns-azure-aks-cluster",
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Get a specific namespace.



> **POST** /inventory/v1/namespace/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[NamespaceRequest](./Namespace#namespacerequest)

* **namespace_id** (string)   `Required` 





{{< highlight json >}}
{
    "namespace_id": "ns-azure-aks-cluster",
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NamespaceInfo](#NAMESPACEINFO)
* **namespace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **category** (string)   `Required` 

* **resource_type** (string)   `Required` 

* **group** (string)   `Required` 

* **icon** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
    "namespace_id": "ns-azure-aks-cluster",
    "name": "AKS/Cluster",
    "category": "ASSET",
    "resource_type": "inventory.CloudService:azure.AKS.Cluster",
    "group": "azure",
    "icon": "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/azure/aks.svg",
    "tags": {},
    "is_managed": true,
    "resource_group": "DOMAIN",
    "domain_id": "domain-286776a1516a",
    "workspace_id": "*",
    "created_at": "2024-09-27T14:40:58.290Z",
    "updated_at": "2024-09-27T14:40:58.290Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

List namespaces.



> **POST** /inventory/v1/namespace/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[NamespaceQuery](./Namespace#namespacequery)

* **query** (Query)  


* **namespace_id** (string)  


* **category** (string)  


* **resource_type** (string)  


* **group** (string)  


* **is_managed** (string)  


* **workspace_id** (string)  





{{< highlight json >}}
{
   "query": {
       "filter": [
           {
               "key": "namespace_id",
               "value": "Key",
               "operator": "eq"
           }
       ]
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[NamespacesInfo](#NAMESPACESINFO)
* **results** (NamespaceInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
    "results": [
      {
        "namespace_id": "ns-azure-aks-cluster",
        "name": "AKS/Cluster",
        "category": "ASSET",
        "resource_type": "inventory.CloudService:azure.AKS.Cluster",
        "group": "azure",
        "icon": "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/azure/aks.svg",
        "tags": {},
        "is_managed": true,
        "resource_group": "DOMAIN",
        "domain_id": "domain-286776a1516a",
        "workspace_id": "*",
        "created_at": "2024-09-27T14:40:58.290Z",
        "updated_at": "2024-09-27T14:40:58.290Z"
      }
    ],
    "total_count": 89
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat

Get statistics of namespaces.



> **POST** /inventory/v1/namespace/stat
>






    


<br>
<br>

## Message



### CreateNamespaceRequest
* **name** (string)   `Required` 

    
* **category** (string)   `Required` 

    
* **resource_type** (string)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **namespace_id** (string)  

    
* **group** (string)  

    
* **icon** (string)  

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    <br>

### NamespaceInfo
* **namespace_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **category** (string)   `Required` 

    
* **resource_type** (string)   `Required` 

    
* **group** (string)   `Required` 

    
* **icon** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### NamespaceQuery
* **query** (Query)  

    
* **namespace_id** (string)  

    
* **category** (string)  

    
* **resource_type** (string)  

    
* **group** (string)  

    
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

    
* **icon** (string)  

    
* **tags** (Struct)  

    <br>
