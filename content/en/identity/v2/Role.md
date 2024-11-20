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
| [**list_basic_role**](./Role#list_basic_role) | [RoleSearchQuery](Role#rolesearchquery) | [RolesInfo](Role#rolesinfo) |
| [**stat**](./Role#stat) | [RoleStatQuery](Role#rolestatquery) | [Struct](Role#struct) |



    
<br>

### create





> **POST** /identity/v2/role/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateRoleRequest](./Role#createrolerequest)

* **name** (string)   `Required` 


* **role_type** (RoleType)   `Required` 


* **permissions** (string)  `Repeated`   


* **page_access** (string)  `Repeated`   


* **tags** (Struct)  





{{< highlight json >}}
{
 "name": "Cloudforet User",
 "role_type": "WORKSPACE_MEMBER",
 "page_access": [
   "dashboards:restricted.*",
   "project:writable.*",
   "asset_inventory:writable.*",
   "cost_explorer:readonly.*",
   "alert_manager:restricted.*"
 ]
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RoleInfo](#ROLEINFO)
* **role_id** (string)   `Required` 

* **name** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **permissions** (string)  `Repeated`   `Required` 

* **page_access** (string)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **state** (State)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-14T02:44:56.211Z",
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "Cloudforet User",
 "page_access": [
   "dashboards:restricted.*",
   "project:writable.*",
   "asset_inventory:writable.*",
   "cost_explorer:readonly.*",
   "alert_manager:restricted.*"
 ],
 "role_id": "role-5ce484d4b750",
 "role_type": "WORKSPACE_MEMBER",
 "state": "ENABLED",
 "updated_at": "2024-11-14T02:44:56.211Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update





> **POST** /identity/v2/role/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateRoleRequest](./Role#updaterolerequest)

* **role_id** (string)   `Required` 


* **name** (string)  


* **permissions** (ListValue)  


* **page_access** (ListValue)  


* **tags** (Struct)  





{{< highlight json >}}
{
 "name": "Cloudforet User",
 "role_type": "WORKSPACE_MEMBER",
 "page_access": [
   "dashboards:restricted.*",
   "project:writable.*",
   "asset_inventory:writable.*",
   "cost_explorer:readonly.*",
   "alert_manager:restricted.*"
 ]
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RoleInfo](#ROLEINFO)
* **role_id** (string)   `Required` 

* **name** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **permissions** (string)  `Repeated`   `Required` 

* **page_access** (string)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **state** (State)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-14T02:44:56.211Z",
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "Cloudforet User",
 "page_access": [
   "dashboards:restricted.*",
   "project:writable.*",
   "asset_inventory:writable.*",
   "cost_explorer:readonly.*",
   "alert_manager:restricted.*"
 ],
 "role_id": "role-5ce484d4b750",
 "role_type": "WORKSPACE_MEMBER",
 "state": "ENABLED",
 "updated_at": "2024-11-14T02:44:56.211Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
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
 "role_id": "role-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RoleInfo](#ROLEINFO)
* **role_id** (string)   `Required` 

* **name** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **permissions** (string)  `Repeated`   `Required` 

* **page_access** (string)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **state** (State)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-14T02:44:56.211Z",
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "Cloudforet User",
 "page_access": [
   "dashboards:restricted.*",
   "project:writable.*",
   "asset_inventory:writable.*",
   "cost_explorer:readonly.*",
   "alert_manager:restricted.*"
 ],
 "role_id": "role-5ce484d4b750",
 "role_type": "WORKSPACE_MEMBER",
 "state": "ENABLED",
 "updated_at": "2024-11-14T02:44:56.211Z"
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
 "role_id": "role-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RoleInfo](#ROLEINFO)
* **role_id** (string)   `Required` 

* **name** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **permissions** (string)  `Repeated`   `Required` 

* **page_access** (string)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **state** (State)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-14T02:44:56.211Z",
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "Cloudforet User",
 "page_access": [
   "dashboards:restricted.*",
   "project:writable.*",
   "asset_inventory:writable.*",
   "cost_explorer:readonly.*",
   "alert_manager:restricted.*"
 ],
 "role_id": "role-5ce484d4b750",
 "role_type": "WORKSPACE_MEMBER",
 "state": "ENABLED",
 "updated_at": "2024-11-14T02:44:56.211Z"
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
 "role_id": "role-a1b2c3d4e5f6"
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
 "role_id": "role-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RoleInfo](#ROLEINFO)
* **role_id** (string)   `Required` 

* **name** (string)   `Required` 

* **role_type** (RoleType)   `Required` 

* **permissions** (string)  `Repeated`   `Required` 

* **page_access** (string)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **is_managed** (bool)   `Required` 

* **state** (State)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
 "created_at": "2024-11-14T02:44:56.211Z",
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "Cloudforet User",
 "page_access": [
   "dashboards:restricted.*",
   "project:writable.*",
   "asset_inventory:writable.*",
   "cost_explorer:readonly.*",
   "alert_manager:restricted.*"
 ],
 "role_id": "role-5ce484d4b750",
 "role_type": "WORKSPACE_MEMBER",
 "state": "ENABLED",
 "updated_at": "2024-11-14T02:44:56.211Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /identity/v2/role/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[RoleSearchQuery](./Role#rolesearchquery)

* **query** (Query)  


* **role_id** (string)  


* **name** (string)  


* **role_type** (RoleType)  


* **state** (State)  





{{< highlight json >}}
{
 "state": "ENABLED",
 "query": {
   "page": {
     "start": 1,
     "limit": 10
   },
   "sort": [
     {
       "key": "role_type",
       "desc": true
     }
   ]
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RolesInfo](#ROLESINFO)
* **results** (RoleInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
 "results": [
   {
     "created_at": "2024-11-12T04:46:40.902Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "is_managed": true,
     "name": "Workspace Owner",
     "role_id": "managed-workspace-owner",
     "role_type": "WORKSPACE_OWNER",
     "state": "ENABLED",
     "updated_at": "2024-11-12T04:46:40.902Z"
   },
   {
     "created_at": "2024-11-14T02:47:08.065Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "Cloudforet Onwer",
     "page_access": [
       "dashboards:restricted.*",
       "project:writable.*",
       "asset_inventory:writable.*",
       "cost_explorer:readonly.*",
       "alert_manager:restricted.*"
     ],
     "role_id": "role-93a6d387e7ed",
     "role_type": "WORKSPACE_OWNER",
     "state": "ENABLED",
     "updated_at": "2024-11-14T02:47:08.065Z"
   },
   {
     "created_at": "2024-11-12T04:46:40.894Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "is_managed": true,
     "name": "Workspace Member",
     "role_id": "managed-workspace-member",
     "role_type": "WORKSPACE_MEMBER",
     "state": "ENABLED",
     "updated_at": "2024-11-12T04:46:40.895Z"
   },
   {
     "created_at": "2024-11-14T02:44:56.211Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "Cloudforet User",
     "page_access": [
       "dashboards:restricted.*",
       "project:writable.*",
       "asset_inventory:writable.*",
       "cost_explorer:readonly.*",
       "alert_manager:restricted.*"
     ],
     "role_id": "role-5ce484d4b750",
     "role_type": "WORKSPACE_MEMBER",
     "state": "ENABLED",
     "updated_at": "2024-11-14T02:44:56.211Z"
   },
   {
     "created_at": "2024-11-14T02:51:23.638Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "Wonny Project Member",
     "page_access": [
       "dashboards:restricted.*",
       "project:writable.*",
       "asset_inventory:writable.*"
     ],
     "role_id": "role-4b8283a42890",
     "role_type": "WORKSPACE_MEMBER",
     "state": "ENABLED",
     "updated_at": "2024-11-14T02:51:23.638Z"
   },
   {
     "created_at": "2024-11-14T02:51:34.751Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "SpaceONE Project Member",
     "page_access": [
       "dashboards:restricted.*",
       "project:writable.*",
       "asset_inventory:writable.*"
     ],
     "role_id": "role-3365600e3e0e",
     "role_type": "WORKSPACE_MEMBER",
     "state": "ENABLED",
     "updated_at": "2024-11-14T02:51:34.751Z"
   },
   {
     "created_at": "2024-11-12T04:46:40.885Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "is_managed": true,
     "name": "Domain Admin",
     "role_id": "managed-domain-admin",
     "role_type": "DOMAIN_ADMIN",
     "state": "ENABLED",
     "updated_at": "2024-11-12T04:46:40.885Z"
   }
 ],
 "total_count": 7
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list_basic_role





> **POST** /identity/v2/role/list-basic-role
>





 {{< tabs " list_basic_role " >}}

 {{< tab "Request Example" >}}



[RoleSearchQuery](./Role#rolesearchquery)

* **query** (Query)  


* **role_id** (string)  


* **name** (string)  


* **role_type** (RoleType)  


* **state** (State)  





{{< highlight json >}}
{
 "state": "ENABLED",
 "query": {
   "page": {
     "start": 1,
     "limit": 10
   },
   "sort": [
     {
       "key": "role_type",
       "desc": true
     }
   ]
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RolesInfo](#ROLESINFO)
* **results** (RoleInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
 "results": [
   {
     "created_at": "2024-11-12T04:46:40.902Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "is_managed": true,
     "name": "Workspace Owner",
     "role_id": "managed-workspace-owner",
     "role_type": "WORKSPACE_OWNER",
     "state": "ENABLED",
     "updated_at": "2024-11-12T04:46:40.902Z"
   },
   {
     "created_at": "2024-11-14T02:47:08.065Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "Cloudforet Onwer",
     "page_access": [
       "dashboards:restricted.*",
       "project:writable.*",
       "asset_inventory:writable.*",
       "cost_explorer:readonly.*",
       "alert_manager:restricted.*"
     ],
     "role_id": "role-93a6d387e7ed",
     "role_type": "WORKSPACE_OWNER",
     "state": "ENABLED",
     "updated_at": "2024-11-14T02:47:08.065Z"
   },
   {
     "created_at": "2024-11-12T04:46:40.894Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "is_managed": true,
     "name": "Workspace Member",
     "role_id": "managed-workspace-member",
     "role_type": "WORKSPACE_MEMBER",
     "state": "ENABLED",
     "updated_at": "2024-11-12T04:46:40.895Z"
   },
   {
     "created_at": "2024-11-14T02:44:56.211Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "Cloudforet User",
     "page_access": [
       "dashboards:restricted.*",
       "project:writable.*",
       "asset_inventory:writable.*",
       "cost_explorer:readonly.*",
       "alert_manager:restricted.*"
     ],
     "role_id": "role-5ce484d4b750",
     "role_type": "WORKSPACE_MEMBER",
     "state": "ENABLED",
     "updated_at": "2024-11-14T02:44:56.211Z"
   },
   {
     "created_at": "2024-11-14T02:51:23.638Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "Wonny Project Member",
     "page_access": [
       "dashboards:restricted.*",
       "project:writable.*",
       "asset_inventory:writable.*"
     ],
     "role_id": "role-4b8283a42890",
     "role_type": "WORKSPACE_MEMBER",
     "state": "ENABLED",
     "updated_at": "2024-11-14T02:51:23.638Z"
   },
   {
     "created_at": "2024-11-14T02:51:34.751Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "name": "SpaceONE Project Member",
     "page_access": [
       "dashboards:restricted.*",
       "project:writable.*",
       "asset_inventory:writable.*"
     ],
     "role_id": "role-3365600e3e0e",
     "role_type": "WORKSPACE_MEMBER",
     "state": "ENABLED",
     "updated_at": "2024-11-14T02:51:34.751Z"
   },
   {
     "created_at": "2024-11-12T04:46:40.885Z",
     "domain_id": "domain-a1b2c3d4e5f6",
     "is_managed": true,
     "name": "Domain Admin",
     "role_id": "managed-domain-admin",
     "role_type": "DOMAIN_ADMIN",
     "state": "ENABLED",
     "updated_at": "2024-11-12T04:46:40.885Z"
   }
 ],
 "total_count": 7
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /identity/v2/role/stat
>






    


<br>
<br>

## Message



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

    
* **permissions** (ListValue)  

    
* **page_access** (ListValue)  

    
* **tags** (Struct)  

    <br>
