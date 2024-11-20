---
title: "RoleBinding"
linkTitle: "RoleBinding"
weight: 3
bookFlatSection: true
---
# [RoleBinding](#RoleBinding)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## RoleBinding





**RoleBinding Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./RoleBinding#create) | [CreateRoleBindingRequest](RoleBinding#createrolebindingrequest) | [RoleBindingInfo](RoleBinding#rolebindinginfo) |
| [**update_role**](./RoleBinding#update_role) | [UpdateRoleBindingRequest](RoleBinding#updaterolebindingrequest) | [RoleBindingInfo](RoleBinding#rolebindinginfo) |
| [**delete**](./RoleBinding#delete) | [RoleBindingRequest](RoleBinding#rolebindingrequest) | [Empty](RoleBinding#empty) |
| [**get**](./RoleBinding#get) | [RoleBindingRequest](RoleBinding#rolebindingrequest) | [RoleBindingInfo](RoleBinding#rolebindinginfo) |
| [**list**](./RoleBinding#list) | [RoleBindingSearchQuery](RoleBinding#rolebindingsearchquery) | [RoleBindingsInfo](RoleBinding#rolebindingsinfo) |
| [**stat**](./RoleBinding#stat) | [RoleBindingStatQuery](RoleBinding#rolebindingstatquery) | [Struct](RoleBinding#struct) |



    
<br>

### create





> **POST** /identity/v1/role-binding/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateRoleBindingRequest](./RoleBinding#createrolebindingrequest)

* **user_id** (string)   `Required` 


* **role_id** (string)   `Required` 


* **resource_group** (ResourceGroup)   `Required` 


* **workspace_id** (string)  





{{< highlight json >}}
{
 "user_id": "wonny@cloudforet.io",
 "role_id": "managed-workspace-owner",
 "resource_group": "WORKSPACE",
 "workspace_id": "workspace-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RoleBindingInfo](#ROLEBINDINGINFO)
* **role_binding_id** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_group_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **role_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T04:23:18.121Z",
 "domain_id": "domain-a1b2c3d4e5f6",
 "resource_group": "WORKSPACE",
 "role_binding_id": "rb-a1b2c3d4e5f6",
 "role_id": "managed-workspace-owner",
 "role_type": "WORKSPACE_OWNER",
 "user_id": "wonny@cloudforet.io",
 "workspace_id": "workspace-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update_role





> **POST** /identity/v1/role-binding/update-role
>





 {{< tabs " update_role " >}}

 {{< tab "Request Example" >}}



[UpdateRoleBindingRequest](./RoleBinding#updaterolebindingrequest)

* **role_binding_id** (string)   `Required` 


* **role_id** (string)   `Required` 





{{< highlight json >}}
{
 "roleBindingId": "rb-a1b2c3d4e5f6",
 "roleId": "managed-workspace-owner"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RoleBindingInfo](#ROLEBINDINGINFO)
* **role_binding_id** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_group_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **role_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T04:23:18.121Z",
 "domain_id": "domain-a1b2c3d4e5f6",
 "resource_group": "WORKSPACE",
 "role_binding_id": "rb-a1b2c3d4e5f6",
 "role_id": "managed-workspace-owner",
 "role_type": "WORKSPACE_OWNER",
 "user_id": "wonny@cloudforet.io",
 "workspace_id": "workspace-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /identity/v1/role-binding/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[RoleBindingRequest](./RoleBinding#rolebindingrequest)

* **role_binding_id** (string)   `Required` 





{{< highlight json >}}
{
 "roleBindingId": "rb-a1b2c3d4e5f6",
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v1/role-binding/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[RoleBindingRequest](./RoleBinding#rolebindingrequest)

* **role_binding_id** (string)   `Required` 





{{< highlight json >}}
{
 "roleBindingId": "rb-a1b2c3d4e5f6",
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RoleBindingInfo](#ROLEBINDINGINFO)
* **role_binding_id** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_group_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **role_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-18T04:23:18.121Z",
 "domain_id": "domain-a1b2c3d4e5f6",
 "resource_group": "WORKSPACE",
 "role_binding_id": "rb-a1b2c3d4e5f6",
 "role_id": "managed-workspace-owner",
 "role_type": "WORKSPACE_OWNER",
 "user_id": "wonny@cloudforet.io",
 "workspace_id": "workspace-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /identity/v1/role-binding/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[RoleBindingSearchQuery](./RoleBinding#rolebindingsearchquery)

* **query** (Query)  


* **role_binding_id** (string)  


* **role_type** (RoleType)  


* **workspace_id** (string)  


* **role_id** (string)  


* **user_id** (string)  





{{< highlight json >}}
{
 "roleType": "WORKSPACE_MEMBER",
 "query": {
   "page": {
     "start": 1,
     "limit": 10
   },
   "sort": [
     {
       "key": "created_at",
       "desc": true
     }
   ]
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RoleBindingsInfo](#ROLEBINDINGSINFO)
* **results** (RoleBindingInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
 "results": [
   {
     "created_at": "2024-11-18T05:00:52.870Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "resource_group": "WORKSPACE",
     "role_binding_id": "rb-a1b2c3d4e5f6",
     "role_id": "managed-workspace-member",
     "role_type": "WORKSPACE_MEMBER",
     "user_id": "wonny@cloudforet.io",
     "workspace_id": "workspace-a1b2c3d4e5f6"
   },
   {
     "created_at": "2024-11-18T04:42:33.285Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "resource_group": "WORKSPACE",
     "role_binding_id": "rb-g7h8i9j1k2l3",
     "role_id": "managed-workspace-owner",
     "role_type": "WORKSPACE_OWNER",
     "user_id": "wonny@cloudforet.io",
     "workspace_id": "workspace-a1b2c3d4e5f6"
   }
 ],
 "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /identity/v1/role-binding/stat
>






    


<br>
<br>

## Message



### CreateRoleBindingRequest
* **user_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **workspace_id** (string)  

    <br>

### RoleBindingInfo
* **role_binding_id** (string)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_group_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### RoleBindingRequest
* **role_binding_id** (string)   `Required` 

    <br>

### RoleBindingSearchQuery
* **query** (Query)  

    
* **role_binding_id** (string)  

    
* **role_type** (RoleType)  

    
* **workspace_id** (string)  

    
* **role_id** (string)  

    
* **user_id** (string)  

    <br>

### RoleBindingStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### RoleBindingsInfo
* **results** (RoleBindingInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateRoleBindingRequest
* **role_binding_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    <br>
