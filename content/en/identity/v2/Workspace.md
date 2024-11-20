---
title: "Workspace"
linkTitle: "Workspace"
weight: 3
bookFlatSection: true
---
# [Workspace](#Workspace)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Workspace





**Workspace Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Workspace#create) | [CreateWorkSpaceRequest](Workspace#createworkspacerequest) | [WorkspaceInfo](Workspace#workspaceinfo) |
| [**update**](./Workspace#update) | [UpdateWorkSpaceRequest](Workspace#updateworkspacerequest) | [WorkspaceInfo](Workspace#workspaceinfo) |
| [**change_workspace_group**](./Workspace#change_workspace_group) | [ChangeWorkspaceGroupRequest](Workspace#changeworkspacegrouprequest) | [WorkspaceInfo](Workspace#workspaceinfo) |
| [**delete**](./Workspace#delete) | [WorkspaceDeleteRequest](Workspace#workspacedeleterequest) | [Empty](Workspace#empty) |
| [**enable**](./Workspace#enable) | [WorkspaceRequest](Workspace#workspacerequest) | [WorkspaceInfo](Workspace#workspaceinfo) |
| [**disable**](./Workspace#disable) | [WorkspaceRequest](Workspace#workspacerequest) | [WorkspaceInfo](Workspace#workspaceinfo) |
| [**add_package**](./Workspace#add_package) | [WorkspacePackageRequest](Workspace#workspacepackagerequest) | [WorkspaceInfo](Workspace#workspaceinfo) |
| [**remove_package**](./Workspace#remove_package) | [WorkspacePackageRequest](Workspace#workspacepackagerequest) | [WorkspaceInfo](Workspace#workspaceinfo) |
| [**get**](./Workspace#get) | [WorkspaceRequest](Workspace#workspacerequest) | [WorkspaceInfo](Workspace#workspaceinfo) |
| [**check**](./Workspace#check) | [WorkspaceCheckRequest](Workspace#workspacecheckrequest) | [Empty](Workspace#empty) |
| [**list**](./Workspace#list) | [WorkspaceSearchQuery](Workspace#workspacesearchquery) | [WorkspacesInfo](Workspace#workspacesinfo) |
| [**stat**](./Workspace#stat) | [WorkspaceStatQuery](Workspace#workspacestatquery) | [Struct](Workspace#struct) |



    
<br>

### create





> **POST** /identity/v2/workspace/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateWorkSpaceRequest](./Workspace#createworkspacerequest)

* **name** (string)   `Required` 


* **tags** (Struct)   `Required` 





{{< highlight json >}}
{
 "name": "Cloudforet Workspace"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[WorkspaceInfo](#WORKSPACEINFO)
* **workspace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **tags** (Struct)   `Required` 

* **created_by** (string)   `Required` 

* **references** (string)  `Repeated`   `Required` 

* **is_managed** (bool)   `Required` 

* **packages** (string)  `Repeated`   `Required` 

* **is_dormant** (bool)   `Required` 

* **dormant_ttl** (int32)   `Required` 

* **service_account_count** (int32)   `Required` 

* **user_count** (int32)   `Required` 

* **cost_info** (WorkspaceCostInfo)   `Required` 

* **workspace_group_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 

* **dormant_updated_at** (string)   `Required` 

* **changed_at** (string)   `Required` 



{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "name": "Cloudforet Workspace",
 "state": "ENABLED",
 "created_by": "cloudforet@cloudforet.io",
 "dormant_ttl": -1,
 "cost_info": {},
 "workspace_group_id": "wg-a1b2c3d4e5f6",
 "domain_id": "domain-a1b2c3d4e5f6",
 "created_at": "2024-11-12T08:14:04.011Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update





> **POST** /identity/v2/workspace/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateWorkSpaceRequest](./Workspace#updateworkspacerequest)

* **workspace_id** (string)   `Required` 


* **name** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "name": "Cloudforet Workspace"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[WorkspaceInfo](#WORKSPACEINFO)
* **workspace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **tags** (Struct)   `Required` 

* **created_by** (string)   `Required` 

* **references** (string)  `Repeated`   `Required` 

* **is_managed** (bool)   `Required` 

* **packages** (string)  `Repeated`   `Required` 

* **is_dormant** (bool)   `Required` 

* **dormant_ttl** (int32)   `Required` 

* **service_account_count** (int32)   `Required` 

* **user_count** (int32)   `Required` 

* **cost_info** (WorkspaceCostInfo)   `Required` 

* **workspace_group_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 

* **dormant_updated_at** (string)   `Required` 

* **changed_at** (string)   `Required` 



{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "name": "Cloudforet Workspace",
 "state": "ENABLED",
 "created_by": "cloudforet@cloudforet.io",
 "dormant_ttl": -1,
 "cost_info": {},
 "workspace_group_id": "wg-a1b2c3d4e5f6",
 "domain_id": "domain-a1b2c3d4e5f6",
 "created_at": "2024-11-12T08:14:04.011Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### change_workspace_group





> **POST** /identity/v2/workspace/change-workspace-group
>





 {{< tabs " change_workspace_group " >}}

 {{< tab "Request Example" >}}



[ChangeWorkspaceGroupRequest](./Workspace#changeworkspacegrouprequest)

* **workspace_id** (string)   `Required` 


* **workspace_group_id** (string)  





{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "workspace_group_id": "wg-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[WorkspaceInfo](#WORKSPACEINFO)
* **workspace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **tags** (Struct)   `Required` 

* **created_by** (string)   `Required` 

* **references** (string)  `Repeated`   `Required` 

* **is_managed** (bool)   `Required` 

* **packages** (string)  `Repeated`   `Required` 

* **is_dormant** (bool)   `Required` 

* **dormant_ttl** (int32)   `Required` 

* **service_account_count** (int32)   `Required` 

* **user_count** (int32)   `Required` 

* **cost_info** (WorkspaceCostInfo)   `Required` 

* **workspace_group_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 

* **dormant_updated_at** (string)   `Required` 

* **changed_at** (string)   `Required` 



{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "name": "Cloudforet Workspace",
 "state": "ENABLED",
 "created_by": "cloudforet@cloudforet.io",
 "dormant_ttl": -1,
 "cost_info": {},
 "workspace_group_id": "wg-a1b2c3d4e5f6",
 "domain_id": "domain-a1b2c3d4e5f6",
 "created_at": "2024-11-12T08:14:04.011Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /identity/v2/workspace/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[WorkspaceDeleteRequest](./Workspace#workspacedeleterequest)

* **workspace_id** (string)   `Required` 


* **force** (bool)   `Required` 





{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "force": true
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### enable





> **POST** /identity/v2/workspace/enable
>





 {{< tabs " enable " >}}

 {{< tab "Request Example" >}}



[WorkspaceRequest](./Workspace#workspacerequest)

* **workspace_id** (string)   `Required` 





{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[WorkspaceInfo](#WORKSPACEINFO)
* **workspace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **tags** (Struct)   `Required` 

* **created_by** (string)   `Required` 

* **references** (string)  `Repeated`   `Required` 

* **is_managed** (bool)   `Required` 

* **packages** (string)  `Repeated`   `Required` 

* **is_dormant** (bool)   `Required` 

* **dormant_ttl** (int32)   `Required` 

* **service_account_count** (int32)   `Required` 

* **user_count** (int32)   `Required` 

* **cost_info** (WorkspaceCostInfo)   `Required` 

* **workspace_group_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 

* **dormant_updated_at** (string)   `Required` 

* **changed_at** (string)   `Required` 



{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "name": "Cloudforet Workspace",
 "state": "ENABLED",
 "created_by": "cloudforet@cloudforet.io",
 "dormant_ttl": -1,
 "cost_info": {},
 "workspace_group_id": "wg-a1b2c3d4e5f6",
 "domain_id": "domain-a1b2c3d4e5f6",
 "created_at": "2024-11-12T08:14:04.011Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### disable





> **POST** /identity/v2/workspace/disable
>





 {{< tabs " disable " >}}

 {{< tab "Request Example" >}}



[WorkspaceRequest](./Workspace#workspacerequest)

* **workspace_id** (string)   `Required` 





{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[WorkspaceInfo](#WORKSPACEINFO)
* **workspace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **tags** (Struct)   `Required` 

* **created_by** (string)   `Required` 

* **references** (string)  `Repeated`   `Required` 

* **is_managed** (bool)   `Required` 

* **packages** (string)  `Repeated`   `Required` 

* **is_dormant** (bool)   `Required` 

* **dormant_ttl** (int32)   `Required` 

* **service_account_count** (int32)   `Required` 

* **user_count** (int32)   `Required` 

* **cost_info** (WorkspaceCostInfo)   `Required` 

* **workspace_group_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 

* **dormant_updated_at** (string)   `Required` 

* **changed_at** (string)   `Required` 



{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "name": "Cloudforet Workspace",
 "state": "ENABLED",
 "created_by": "cloudforet@cloudforet.io",
 "dormant_ttl": -1,
 "cost_info": {},
 "workspace_group_id": "wg-a1b2c3d4e5f6",
 "domain_id": "domain-a1b2c3d4e5f6",
 "created_at": "2024-11-12T08:14:04.011Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### add_package





> **POST** /identity/v2/workspace/add-package
>





 {{< tabs " add_package " >}}

 {{< tab "Request Example" >}}



[WorkspacePackageRequest](./Workspace#workspacepackagerequest)

* **workspace_id** (string)   `Required` 


* **package_id** (string)   `Required` 





{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "package_id": "package-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[WorkspaceInfo](#WORKSPACEINFO)
* **workspace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **tags** (Struct)   `Required` 

* **created_by** (string)   `Required` 

* **references** (string)  `Repeated`   `Required` 

* **is_managed** (bool)   `Required` 

* **packages** (string)  `Repeated`   `Required` 

* **is_dormant** (bool)   `Required` 

* **dormant_ttl** (int32)   `Required` 

* **service_account_count** (int32)   `Required` 

* **user_count** (int32)   `Required` 

* **cost_info** (WorkspaceCostInfo)   `Required` 

* **workspace_group_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 

* **dormant_updated_at** (string)   `Required` 

* **changed_at** (string)   `Required` 



{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "name": "Cloudforet Workspace",
 "state": "ENABLED",
 "created_by": "cloudforet@cloudforet.io",
 "dormant_ttl": -1,
 "cost_info": {},
 "workspace_group_id": "wg-a1b2c3d4e5f6",
 "domain_id": "domain-a1b2c3d4e5f6",
 "created_at": "2024-11-12T08:14:04.011Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### remove_package





> **POST** /identity/v2/workspace/remove-package
>





 {{< tabs " remove_package " >}}

 {{< tab "Request Example" >}}



[WorkspacePackageRequest](./Workspace#workspacepackagerequest)

* **workspace_id** (string)   `Required` 


* **package_id** (string)   `Required` 





{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "package_id": "package-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[WorkspaceInfo](#WORKSPACEINFO)
* **workspace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **tags** (Struct)   `Required` 

* **created_by** (string)   `Required` 

* **references** (string)  `Repeated`   `Required` 

* **is_managed** (bool)   `Required` 

* **packages** (string)  `Repeated`   `Required` 

* **is_dormant** (bool)   `Required` 

* **dormant_ttl** (int32)   `Required` 

* **service_account_count** (int32)   `Required` 

* **user_count** (int32)   `Required` 

* **cost_info** (WorkspaceCostInfo)   `Required` 

* **workspace_group_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 

* **dormant_updated_at** (string)   `Required` 

* **changed_at** (string)   `Required` 



{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "name": "Cloudforet Workspace",
 "state": "ENABLED",
 "created_by": "cloudforet@cloudforet.io",
 "dormant_ttl": -1,
 "cost_info": {},
 "workspace_group_id": "wg-a1b2c3d4e5f6",
 "domain_id": "domain-a1b2c3d4e5f6",
 "created_at": "2024-11-12T08:14:04.011Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v2/workspace/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[WorkspaceRequest](./Workspace#workspacerequest)

* **workspace_id** (string)   `Required` 





{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[WorkspaceInfo](#WORKSPACEINFO)
* **workspace_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **tags** (Struct)   `Required` 

* **created_by** (string)   `Required` 

* **references** (string)  `Repeated`   `Required` 

* **is_managed** (bool)   `Required` 

* **packages** (string)  `Repeated`   `Required` 

* **is_dormant** (bool)   `Required` 

* **dormant_ttl** (int32)   `Required` 

* **service_account_count** (int32)   `Required` 

* **user_count** (int32)   `Required` 

* **cost_info** (WorkspaceCostInfo)   `Required` 

* **workspace_group_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 

* **dormant_updated_at** (string)   `Required` 

* **changed_at** (string)   `Required` 



{{< highlight json >}}
{
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "name": "Cloudforet Workspace",
 "state": "ENABLED",
 "created_by": "cloudforet@cloudforet.io",
 "dormant_ttl": -1,
 "cost_info": {},
 "workspace_group_id": "wg-a1b2c3d4e5f6",
 "domain_id": "domain-a1b2c3d4e5f6",
 "created_at": "2024-11-12T08:14:04.011Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### check










    
<br>

### list





> **POST** /identity/v2/workspace/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[WorkspaceSearchQuery](./Workspace#workspacesearchquery)

* **query** (Query)  


* **workspace_id** (string)  


* **name** (string)  


* **state** (State)  


* **created_by** (string)  


* **is_managed** (bool)  


* **is_dormant** (bool)  


* **workspace_group_id** (string)  





{{< highlight json >}}
{
 "query": {
   "page": {
     "start": 1,
     "limit": 10
   }
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[WorkspacesInfo](#WORKSPACESINFO)
* **results** (WorkspaceInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
 "results": [
 {
   "workspace_id": "workspace-a1b2c3d4e5f6",
   "name": "Cloudforet Workspace",
   "state": "ENABLED",
   "created_by": "wonny@cloudforet.io",
   "dormant_ttl": -1,
   "service_account_count": 0,
   "user_count": 0,
   "cost_info": {},
   "domain_id": "domain-a1b2c3d4e5f6",
   "created_at": "2024-11-12T08:25:08.762Z"
 },
 {
   "workspace_id": "workspace-g7h8i9j1k2l3",
   "name": "Wonny Workspace",
   "state": "ENABLED",
   "created_by": "cloudforet@cloudforet.io",
   "dormant_ttl": 0,
   "service_account_count": 0,
   "user_count": 0,
   "cost_info": {},
   "workspace_group_id": "wg-a1b2c3d4e5f6",
   "domain_id": "domain-g7h8i9j1k2l3",
   "created_at": "2024-11-12T08:14:04.011Z",
   "changed_at": "2024-11-12T08:43:39.945Z"
 }
 ],
 "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /identity/v2/workspace/stat
>






    


<br>
<br>

## Message



### ChangeWorkspaceGroupRequest
* **workspace_id** (string)   `Required` 

    
* **workspace_group_id** (string)  

    <br>

### CreateWorkSpaceRequest
* **name** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    <br>

### UpdateWorkSpaceRequest
* **workspace_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### WorkspaceCheckRequest
* **workspace_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### WorkspaceCostInfo
* **day** (float)   `Required` 

    
* **month** (float)   `Required` 

    <br>

### WorkspaceDeleteRequest
* **workspace_id** (string)   `Required` 

    
* **force** (bool)   `Required` 

    <br>

### WorkspaceInfo
* **workspace_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **created_by** (string)   `Required` 

    
* **references** (string)  `Repeated`    `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **packages** (string)  `Repeated`    `Required` 

    
* **is_dormant** (bool)   `Required` 

    
* **dormant_ttl** (int32)   `Required` 

    
* **service_account_count** (int32)   `Required` 

    
* **user_count** (int32)   `Required` 

    
* **cost_info** (WorkspaceCostInfo)   `Required` 

    
* **workspace_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **trusted_account_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_synced_at** (string)   `Required` 

    
* **dormant_updated_at** (string)   `Required` 

    
* **changed_at** (string)   `Required` 

    <br>

### WorkspacePackageRequest
* **workspace_id** (string)   `Required` 

    
* **package_id** (string)   `Required` 

    <br>

### WorkspaceRequest
* **workspace_id** (string)   `Required` 

    <br>

### WorkspaceSearchQuery
* **query** (Query)  

    
* **workspace_id** (string)  

    
* **name** (string)  

    
* **state** (State)  

    
* **created_by** (string)  

    
* **is_managed** (bool)  

    
* **is_dormant** (bool)  

    
* **workspace_group_id** (string)  

    <br>

### WorkspaceStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### WorkspacesInfo
* **results** (WorkspaceInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
