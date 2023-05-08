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

> **POST** /inventory/v1/resource-group/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /inventory/v1/resource-group/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /inventory/v1/resource-group/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /inventory/v1/resource-group/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /inventory/v1/resource-group/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /inventory/v1/resource-group/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


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
