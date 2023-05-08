---
title: "Role"
linkTitle: "Role"
weight: 3
bookFlatSection: true
---
# [Role](#Role)



>  **Package : spaceone.api.identity.v1**

<br>
<br>

## Role


**Role Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Role#create) | [CreateRoleRequest](Role#createrolerequest) | [RoleInfo](./Role#roleinfo) |
| [**update**](./Role#update) | [UpdateRoleRequest](Role#updaterolerequest) | [RoleInfo](./Role#roleinfo) |
| [**delete**](./Role#delete) | [RoleRequest](Role#rolerequest) | [Empty](./Role#empty) |
| [**get**](./Role#get) | [GetRoleRequest](Role#getrolerequest) | [RoleInfo](./Role#roleinfo) |
| [**list**](./Role#list) | [RoleQuery](Role#rolequery) | [RolesInfo](./Role#rolesinfo) |
| [**stat**](./Role#stat) | [RoleStatQuery](Role#rolestatquery) | [Struct](./Role#struct) |



    
<br>

### create

> **POST** /identity/v1/role/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /identity/v1/role/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /identity/v1/role/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /identity/v1/role/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /identity/v1/role/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /identity/v1/role/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateRoleRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **role_type** (RoleType)  `Required` 

  *is_required: true*

    
* **policies** (RolePolicy)  `Required` 

  *is_required: true*

    
* **page_permissions** (PagePermission)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetRoleRequest
* **role_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### PagePermission
* **page** (string)  `Required` 

    
* **permission** (Permission)  `Required` 

    <br>

### RoleInfo
* **role_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **role_type** (RoleType)  `Required` 

    
* **policies** (RolePolicy)  `Required` 

    
* **page_permissions** (PagePermission)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **deleted_at** (string)  `Required` 

    <br>

### RolePolicy
* **policy_type** (PolicyType)  `Required` 

    
* **policy_id** (string)  `Required` 

    <br>

### RoleQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **role_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **role_type** (RoleType)  `Required` 

  *is_required: false*

    
* **policy_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### RoleRequest
* **role_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### RoleStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### RolesInfo
* **results** (RoleInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateRoleRequest
* **role_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **policies** (RolePolicy)  `Required` 

  *is_required: false*

    
* **page_permissions** (PagePermission)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **release_page_permissions** (bool)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
