---
title: "Resource_group"
linkTitle: "Resource_group"
weight: 3
bookFlatSection: true
---
# [Resource_group](#Resource_group)
desc: A ResourceGroup is a group of `resource`s from various `provider`s.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Resource_group





**ResourceGroup Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./ResourceGroup#create) | [CreateResourceGroupRequest](ResourceGroup#createresourcegrouprequest) | [ResourceGroupInfo](./ResourceGroup#resourcegroupinfo) |
| [**update**](./ResourceGroup#update) | [UpdateResourceGroupRequest](ResourceGroup#updateresourcegrouprequest) | [ResourceGroupInfo](./ResourceGroup#resourcegroupinfo) |
| [**delete**](./ResourceGroup#delete) | [ResourceGroupRequest](ResourceGroup#resourcegrouprequest) | [Empty](./ResourceGroup#empty) |
| [**get**](./ResourceGroup#get) | [GetResourceGroupRequest](ResourceGroup#getresourcegrouprequest) | [ResourceGroupInfo](./ResourceGroup#resourcegroupinfo) |
| [**list**](./ResourceGroup#list) | [ResourceGroupQuery](ResourceGroup#resourcegroupquery) | [ResourceGroupsInfo](./ResourceGroup#resourcegroupsinfo) |
| [**stat**](./ResourceGroup#stat) | [ResourceGroupStatQuery](ResourceGroup#resourcegroupstatquery) | [Struct](./ResourceGroup#struct) |



    
<br>

### create

desc: Creates a new ResourceGroup. You can integrate `resource`s from different `provider`s by specifying the cloud resources to be grouped in the `resources` parameter.
request_example: >-
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
response_example: >-
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



> **POST** /inventory/v1/resource-group/create
>






    
<br>

### update

desc: Updates a specific ResourceGroup. You can make changes in ResourceGroup settings, including `name`, `tags`, and grouped resources in the ResourceGroup.
request_example: >-
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
response_example: >-
{
"resource_group_id": "rsc-grp-7d46a1fc7738",
"name": "azure-grp-test2",
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



> **POST** /inventory/v1/resource-group/update
>






    
<br>

### delete

desc: Deletes a specific ResourceGroup. You must specify the `resource_group_id` of the ResourceGroup to delete.
request_example: >-
{
"resource_group_id": "rsc-grp-aa3c4ca465b2"
}



> **POST** /inventory/v1/resource-group/delete
>






    
<br>

### get

desc: Gets a specific ResourceGroup. Prints detailed information about the ResourceGroup, including the information of the grouped cloud resources.
request_example: >-
{
"resource_group_id": "rsc-grp-aa3c4ca465b2"
}
response_example: >-
{
"resource_group_id": "rsc-grp-aa3c4ca465b2",
"name": "stset",
"resources": [
{
"resource_type": "inventory.Server?provider=aws&cloud_service_group=EC2&cloud_service_type=Instance",
"filter": [
{
"k": "provider",
"o": "eq",
"v": "aws"
},
{
"v": "EC2",
"k": "cloud_service_group",
"o": "eq"
},
{
"o": "eq",
"k": "cloud_service_type",
"v": "Instance"
}
],
"keyword": "test"
}
],
"options": {
"raw_filter": []
},
"tags": {},
"project_id": "project-18655561c535",
"domain_id": "domain-58010aa2e451",
"created_at": "2021-06-01T10:23:20.537Z"
}



> **POST** /inventory/v1/resource-group/get
>






    
<br>

### list

desc: Gets a list of all ResourceGroups. You can use a query to get a filtered list of ResourceGroups.
request_example: >-
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
response_example: >-
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



> **POST** /inventory/v1/resource-group/list
>






    
<br>

### stat





> **POST** /inventory/v1/resource-group/stat
>






    


<br>
<br>

## Message



### CreateResourceGroupRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **resources** (Resource)  `Required` 

  *is_required: true*

    
* **options** (Struct)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetResourceGroupRequest
* **resource_group_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### Resource
* **resource_type** (string)  `Required` 

  *is_required: true*

    
* **filter** (ListValue)  `Required` 

  *is_required: false*

    
* **keyword** (string)  `Required` 

  *is_required: false*

    <br>

### ResourceGroupInfo
* **resource_group_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **resources** (Resource)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### ResourceGroupQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **resource_group_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ResourceGroupRequest
* **resource_group_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ResourceGroupStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ResourceGroupsInfo
* **results** (ResourceGroupInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateResourceGroupRequest
* **resource_group_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **resources** (Resource)  `Required` 

  *is_required: false*

    
* **options** (Struct)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **release_project** (bool)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
