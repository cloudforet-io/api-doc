---
title: "Role"
linkTitle: "Role"
weight: 3
bookFlatSection: true
---
# [Role](#Role)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Role





**Role Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Role#create) | [CreateRoleRequest](Role#createrolerequest) | [RoleInfo](Role#roleinfo) |
| [**update**](./Role#update) | [UpdateRoleRequest](Role#updaterolerequest) | [RoleInfo](Role#roleinfo) |
| [**enable**](./Role#enable) | [RoleRequest](Role#rolerequest) | [RoleInfo](Role#roleinfo) |
| [**disable**](./Role#disable) | [RoleRequest](Role#rolerequest) | [RoleInfo](Role#roleinfo) |
| [**delete**](./Role#delete) | [RoleRequest](Role#rolerequest) | [Empty](Role#empty) |
| [**get**](./Role#get) | [RoleRequest](Role#rolerequest) | [RoleInfo](Role#roleinfo) |
| [**list**](./Role#list) | [RoleSearchQuery](Role#rolesearchquery) | [RolesInfo](Role#rolesinfo) |
| [**list_basic_role**](./Role#list_basic_role) | [RoleSearchQuery](Role#rolesearchquery) | [BasicRolesInfo](Role#basicrolesinfo) |
| [**stat**](./Role#stat) | [RoleStatQuery](Role#rolestatquery) | [Struct](Role#struct) |



    
<br>

### create





> **POST** /identity/v2/role/create
>






    
<br>

### update





> **POST** /identity/v2/role/update
>






    
<br>

### enable





> **POST** /identity/v2/role/enable
>





 {{< tabs " enable " >}}

 {{< tab "Request Example" >}}



[RoleRequest](./Role#rolerequest)

* **role_id** (string)   `Required` 





{{< highlight json >}}
{
 "role_id": "role-a12335a6a4fe"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### disable





> **POST** /identity/v2/role/disable
>





 {{< tabs " disable " >}}

 {{< tab "Request Example" >}}



[RoleRequest](./Role#rolerequest)

* **role_id** (string)   `Required` 





{{< highlight json >}}
{
 "role_id": "role-a12335a6a4fe"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### delete





> **POST** /identity/v2/role/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[RoleRequest](./Role#rolerequest)

* **role_id** (string)   `Required` 





{{< highlight json >}}
{
 "role_id": "role-a12335a6a4fe"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v2/role/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[RoleRequest](./Role#rolerequest)

* **role_id** (string)   `Required` 





{{< highlight json >}}
{
 "role_id": "role-a12335a6a4fe"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### list





> **POST** /identity/v2/role/list
>






    
<br>

### list_basic_role





> **POST** /identity/v2/role/list-basic-role
>






    
<br>

### stat





> **POST** /identity/v2/role/stat
>






    


<br>
<br>

## Message



### BasicRoleInfo
* **role_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### BasicRolesInfo
* **results** (BasicRoleInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CreateRoleRequest
* **name** (string)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **permissions** (string)  `Repeated`   

    
* **page_access** (string)  `Repeated`   

    
* **tags** (Struct)  

    <br>

### RoleInfo
* **role_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **permissions** (string)  `Repeated`    `Required` 

    
* **page_access** (string)  `Repeated`    `Required` 

    
* **tags** (Struct)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **state** (State)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### RoleRequest
* **role_id** (string)   `Required` 

    <br>

### RoleSearchQuery
* **query** (Query)  

    
* **role_id** (string)  

    
* **name** (string)  

    
* **role_type** (RoleType)  

    
* **state** (State)  

    <br>

### RoleStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### RolesInfo
* **results** (RoleInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateRoleRequest
* **role_id** (string)   `Required` 

    
* **name** (string)  

    
* **permissions** (string)  `Repeated`   

    
* **page_access** (string)  `Repeated`   

    
* **tags** (Struct)  

    <br>
