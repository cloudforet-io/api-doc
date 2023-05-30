---
title: "ResourceGroup"
linkTitle: "ResourceGroup"
weight: 3
bookFlatSection: true
---
# [ResourceGroup](#ResourceGroup)
A ResourceGroup is a group of `resource`s from various `provider`s.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## ResourceGroup





**ResourceGroup Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./ResourceGroup#create) | [CreateResourceGroupRequest](ResourceGroup#createresourcegrouprequest) | [ResourceGroupInfo](ResourceGroup#resourcegroupinfo) |
| [**update**](./ResourceGroup#update) | [UpdateResourceGroupRequest](ResourceGroup#updateresourcegrouprequest) | [ResourceGroupInfo](ResourceGroup#resourcegroupinfo) |
| [**delete**](./ResourceGroup#delete) | [ResourceGroupRequest](ResourceGroup#resourcegrouprequest) | [Empty](ResourceGroup#empty) |
| [**get**](./ResourceGroup#get) | [GetResourceGroupRequest](ResourceGroup#getresourcegrouprequest) | [ResourceGroupInfo](ResourceGroup#resourcegroupinfo) |
| [**list**](./ResourceGroup#list) | [ResourceGroupQuery](ResourceGroup#resourcegroupquery) | [ResourceGroupsInfo](ResourceGroup#resourcegroupsinfo) |
| [**stat**](./ResourceGroup#stat) | [ResourceGroupStatQuery](ResourceGroup#resourcegroupstatquery) | [Struct](ResourceGroup#struct) |



    
<br>

### create

Creates a new ResourceGroup. You can integrate `resource`s from different `provider`s by specifying the cloud resources to be grouped in the `resources` parameter.



> **POST** /inventory/v1/resource-group/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateResourceGroupRequest](./ResourceGroup#createresourcegrouprequest)

* **name** (string)   `Required` 


* **resources** (Resource)  `Repeated`    `Required` 


* **project_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **options** (Struct)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "name": "azure-group-1",
   "resources": [
       {
           "resource_type": "inventory.Server?provider=azure&cloud_service_group=Compute&cloud_service_type=VirtualMachine",
           "filter": [
               {"o": "eq", "k": "provider", "v": "azure"},
               {"o": "eq", "k": "cloud_service_group", "v": "Compute"},
               {"o": "eq", "k": "cloud_service_type", "v": "VirtualMachine"}
           ]
       }
   ],
   "options": {
       "raw_filter": []
   },
   "tags": {
       "a": "b"
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ResourceGroupInfo](#RESOURCEGROUPINFO)
* **resource_group_id** (string)   `Required` 

* **name** (string)   `Required` 

* **resources** (Resource)  `Repeated`   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **project_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "resource_group_id": "rsc-grp-7d46a1fc7738",
   "name": "azure-group-1",
   "resources": [
       {
           "resource_type": "inventory.Server?provider=azure&cloud_service_group=Compute&cloud_service_type=VirtualMachine",
           "filter": [
               {
                   "k": "provider",
                   "v": "azure",
                   "o": "eq"
               },
               {
                   "k": "cloud_service_group",
                   "v": "Compute",
                   "o": "eq"
               },
               {
                   "k": "cloud_service_type",
                   "v": "VirtualMachine",
                   "o": "eq"
               }
           ]
       }
   ],
   "options": {
       "raw_filter": []
   },
   "tags": {
       "a": "b"
   },
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-06-23T01:50:33.152Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific ResourceGroup. You can make changes in ResourceGroup settings, including `name`, `tags`, and grouped resources in the ResourceGroup.



> **POST** /inventory/v1/resource-group/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateResourceGroupRequest](./ResourceGroup#updateresourcegrouprequest)

* **resource_group_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **name** (string)  


* **resources** (Resource)  `Repeated`   


* **options** (Struct)  


* **tags** (Struct)  


* **release_project** (bool)  


* **project_id** (string)  





{{< highlight json >}}
{
   "resource_group_id": "rsc-grp-7d46a1fc7738",
   "name": "azure-grp-test2",
   "resources": [
       {
           "resource_type": "inventory.Server?provider=azure&cloud_service_group=Compute&cloud_service_type=VirtualMachine",
           "filter": [
               {"k": "provider", "v": "azure", "o": "eq"},
               {"o": "eq", "k": "cloud_service_group", "v": "Compute"},
               {"v": "VirtualMachine", "k": "cloud_service_type", "o": "eq"}
           ]
       }
   ],
   "options": {},
   "tags": {
       "b": "c"
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ResourceGroupInfo](#RESOURCEGROUPINFO)
* **resource_group_id** (string)   `Required` 

* **name** (string)   `Required` 

* **resources** (Resource)  `Repeated`   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **project_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "resource_group_id": "rsc-grp-7d46a1fc7738",
   "name": "azure-group-1",
   "resources": [
       {
           "resource_type": "inventory.Server?provider=azure&cloud_service_group=Compute&cloud_service_type=VirtualMachine",
           "filter": [
               {
                   "k": "provider",
                   "v": "azure",
                   "o": "eq"
               },
               {
                   "k": "cloud_service_group",
                   "v": "Compute",
                   "o": "eq"
               },
               {
                   "k": "cloud_service_type",
                   "v": "VirtualMachine",
                   "o": "eq"
               }
           ]
       }
   ],
   "options": {
       "raw_filter": []
   },
   "tags": {
       "a": "b"
   },
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-06-23T01:50:33.152Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific ResourceGroup. You must specify the `resource_group_id` of the ResourceGroup to delete.



> **POST** /inventory/v1/resource-group/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[ResourceGroupRequest](./ResourceGroup#resourcegrouprequest)

* **resource_group_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "resource_group_id": "rsc-grp-aa3c4ca465b2"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific ResourceGroup. Prints detailed information about the ResourceGroup, including the information of the grouped cloud resources.



> **POST** /inventory/v1/resource-group/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetResourceGroupRequest](./ResourceGroup#getresourcegrouprequest)

* **resource_group_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **only** (string)  `Repeated`   





{{< highlight json >}}
{
   "resource_group_id": "rsc-grp-aa3c4ca465b2"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ResourceGroupInfo](#RESOURCEGROUPINFO)
* **resource_group_id** (string)   `Required` 

* **name** (string)   `Required` 

* **resources** (Resource)  `Repeated`   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **project_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "resource_group_id": "rsc-grp-7d46a1fc7738",
   "name": "azure-group-1",
   "resources": [
       {
           "resource_type": "inventory.Server?provider=azure&cloud_service_group=Compute&cloud_service_type=VirtualMachine",
           "filter": [
               {
                   "k": "provider",
                   "v": "azure",
                   "o": "eq"
               },
               {
                   "k": "cloud_service_group",
                   "v": "Compute",
                   "o": "eq"
               },
               {
                   "k": "cloud_service_type",
                   "v": "VirtualMachine",
                   "o": "eq"
               }
           ]
       }
   ],
   "options": {
       "raw_filter": []
   },
   "tags": {
       "a": "b"
   },
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-06-23T01:50:33.152Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all ResourceGroups. You can use a query to get a filtered list of ResourceGroups.



> **POST** /inventory/v1/resource-group/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[ResourceGroupQuery](./ResourceGroup#resourcegroupquery)

* **domain_id** (string)   `Required` 


* **query** (Query)  


* **resource_group_id** (string)  


* **name** (string)  


* **project_id** (string)  





{{< highlight json >}}
{
   "query": {
       "filter": [
           {
               "key": "name",
               "value": [
                   "azure-vmss-group",
                   "stset"
               ],
               "operator": "in"
           }
       ]
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ResourceGroupsInfo](#RESOURCEGROUPSINFO)
* **results** (ResourceGroupInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
       {
           "resource_group_id": "rsc-grp-4c86e071e0f0",
           "name": "azure-vmss-group",
           "resources": [
               {
                  "resource_type": "inventory.CloudService?provider=azure&cloud_service_group=Compute&cloud_service_type=VmScaleSet",
                   "filter": [
                       {
                           "k": "provider",
                           "v": "azure",
                           "o": "eq"
                       },
                       {
                           "v": "Compute",
                           "k": "cloud_service_group",
                           "o": "eq"
                       },
                       {
                           "k": "cloud_service_type",
                           "v": "VmScaleSet",
                           "o": "eq"
                       }
                   ]
               }
           ],
           "options": {
               "raw_filter": []
           },
           "tags": {},
           "project_id": "project-9074eea97d7e",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2021-04-23T03:23:40.037Z"
       },
       {
           "resource_group_id": "rsc-grp-aa3c4ca465b2",
           "name": "stset",
           "resources": [
               {
                   "resource_type": "inventory.Server?provider=aws&cloud_service_group=EC2&cloud_service_type=Instance",
                   "filter": [
                       {
                           "k": "provider",
                           "v": "aws",
                           "o": "eq"
                       },
                       {
                           "v": "EC2",
                           "k": "cloud_service_group",
                           "o": "eq"
                       },
                       {
                           "k": "cloud_service_type",
                           "v": "Instance",
                           "o": "eq"
                       }
                   ],
                   "keyword": "test"
               }
           ],
           "options": {
               "raw_filter": [
                   [
                       "test"
                   ]
               ]
           },
           "tags": {},
           "project_id": "project-18655561c535",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2021-06-01T10:23:20.537Z"
       }
   ],
   "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /inventory/v1/resource-group/stat
>






    


<br>
<br>

## Message



### CreateResourceGroupRequest
* **name** (string)   `Required` 

    
* **resources** (Resource)  `Repeated`    `Required` 

    
* **project_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>

### GetResourceGroupRequest
* **resource_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### Resource
* **resource_type** (string)   `Required` 

    
* **filter** (ListValue)  

    
* **keyword** (string)  

    <br>

### ResourceGroupInfo
* **resource_group_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **resources** (Resource)  `Repeated`    `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### ResourceGroupQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **resource_group_id** (string)  

    
* **name** (string)  

    
* **project_id** (string)  

    <br>

### ResourceGroupRequest
* **resource_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### ResourceGroupStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### ResourceGroupsInfo
* **results** (ResourceGroupInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateResourceGroupRequest
* **resource_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **resources** (Resource)  `Repeated`   

    
* **options** (Struct)  

    
* **tags** (Struct)  

    
* **release_project** (bool)  

    
* **project_id** (string)  

    <br>
