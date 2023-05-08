---
title: "Role_binding"
linkTitle: "Role_binding"
weight: 3
bookFlatSection: true
---
# [Role_binding](#Role_binding)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## Role_binding


**RoleBinding Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./RoleBinding#create) | [CreateRoleBindingRequest](RoleBinding#createrolebindingrequest) | [RoleBindingInfo](./RoleBinding#rolebindinginfo) |
| [**update**](./RoleBinding#update) | [UpdateRoleBindingRequest](RoleBinding#updaterolebindingrequest) | [RoleBindingInfo](./RoleBinding#rolebindinginfo) |
| [**delete**](./RoleBinding#delete) | [RoleBindingRequest](RoleBinding#rolebindingrequest) | [Empty](./RoleBinding#empty) |
| [**get**](./RoleBinding#get) | [GetRoleBindingRequest](RoleBinding#getrolebindingrequest) | [RoleBindingInfo](./RoleBinding#rolebindinginfo) |
| [**list**](./RoleBinding#list) | [RoleBindingQuery](RoleBinding#rolebindingquery) | [RoleBindingsInfo](./RoleBinding#rolebindingsinfo) |
| [**stat**](./RoleBinding#stat) | [RoleBindingStatQuery](RoleBinding#rolebindingstatquery) | [Struct](./RoleBinding#struct) |



    
<br>

### create

> **POST** /identity/v1/role-binding/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /identity/v1/role-binding/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /identity/v1/role-binding/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /identity/v1/role-binding/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /identity/v1/role-binding/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /identity/v1/role-binding/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateRoleBindingRequest
* **resource_type** (string)  `Required` 

  *is_required: true*

    
* **resource_id** (string)  `Required` 

  *is_required: true*

    
* **role_id** (string)  `Required` 

  *is_required: true*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **project_group_id** (string)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetRoleBindingRequest
* **role_binding_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### RoleBindingInfo
* **role_binding_id** (string)  `Required` 

    
* **resource_type** (string)  `Required` 

    
* **resource_id** (string)  `Required` 

    
* **role_info** (RoleInfo)  `Required` 

    
* **project_info** (ProjectInfo)  `Required` 

    
* **project_group_info** (ProjectGroupInfo)  `Required` 

    
* **labels** (ListValue)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### RoleBindingQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **role_binding_id** (string)  `Required` 

  *is_required: false*

    
* **resource_type** (string)  `Required` 

  *is_required: false*

    
* **resource_id** (string)  `Required` 

  *is_required: false*

    
* **role_id** (string)  `Required` 

  *is_required: false*

    
* **role_type** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **project_group_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### RoleBindingRequest
* **role_binding_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### RoleBindingStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### RoleBindingsInfo
* **results** (RoleBindingInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateRoleBindingRequest
* **role_binding_id** (string)  `Required` 

  *is_required: true*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
