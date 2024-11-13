---
title: "ProjectGroup"
linkTitle: "ProjectGroup"
weight: 3
bookFlatSection: true
---
# [ProjectGroup](#ProjectGroup)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## ProjectGroup





**ProjectGroup Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./ProjectGroup#create) | [CreateProjectGroupRequest](ProjectGroup#createprojectgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**update**](./ProjectGroup#update) | [UpdateProjectGroupRequest](ProjectGroup#updateprojectgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**change_parent_group**](./ProjectGroup#change_parent_group) | [ChangeParentGroupRequest](ProjectGroup#changeparentgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**delete**](./ProjectGroup#delete) | [ProjectGroupRequest](ProjectGroup#projectgrouprequest) | [Empty](ProjectGroup#empty) |
| [**add_users**](./ProjectGroup#add_users) | [UsersProjectGroupRequest](ProjectGroup#usersprojectgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**remove_users**](./ProjectGroup#remove_users) | [UsersProjectGroupRequest](ProjectGroup#usersprojectgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**get**](./ProjectGroup#get) | [ProjectGroupRequest](ProjectGroup#projectgrouprequest) | [ProjectGroupInfo](ProjectGroup#projectgroupinfo) |
| [**list**](./ProjectGroup#list) | [ProjectGroupSearchQuery](ProjectGroup#projectgroupsearchquery) | [ProjectGroupsInfo](ProjectGroup#projectgroupsinfo) |
| [**stat**](./ProjectGroup#stat) | [ProjectGroupStatQuery](ProjectGroup#projectgroupstatquery) | [Struct](ProjectGroup#struct) |



    
<br>

### create





> **POST** /identity/v2/project-group/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateProjectGroupRequest](./ProjectGroup#createprojectgrouprequest)

* **name** (string)   `Required` 


* **tags** (Struct)  


* **parent_group_id** (string)  





{{< highlight json >}}
{
 "name": "Cloudforet Company",
 "tags": {
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectGroupInfo](#PROJECTGROUPINFO)
* **project_group_id** (string)   `Required` 

* **name** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **users** (string)  `Repeated`   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **parent_group_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 



{{< highlight json >}}
{
   "project_group_id": "pg-7120aabb662c",
   "name": "Cloudforet Core Team",
   "tags": {},
   "domain_id": "domain-186446b1516b",
   "workspace_id": "workspace-1a02ebcb3eb2",
   "parent_group_id": "pg-10efea238292",
   "created_at": "2024-07-12T03:31:02.222Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update





> **POST** /identity/v2/project-group/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateProjectGroupRequest](./ProjectGroup#updateprojectgrouprequest)

* **project_group_id** (string)   `Required` 


* **name** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
 "project_group_id": "pg-7120aabb662c",
 "name": "Cloudforet Core Team"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectGroupInfo](#PROJECTGROUPINFO)
* **project_group_id** (string)   `Required` 

* **name** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **users** (string)  `Repeated`   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **parent_group_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 



{{< highlight json >}}
{
   "project_group_id": "pg-7120aabb662c",
   "name": "Cloudforet Core Team",
   "tags": {},
   "domain_id": "domain-186446b1516b",
   "workspace_id": "workspace-1a02ebcb3eb2",
   "parent_group_id": "pg-10efea238292",
   "created_at": "2024-07-12T03:31:02.222Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### change_parent_group





> **POST** /identity/v2/project-group/change-parent-group
>





 {{< tabs " change_parent_group " >}}

 {{< tab "Request Example" >}}



[ChangeParentGroupRequest](./ProjectGroup#changeparentgrouprequest)

* **project_group_id** (string)   `Required` 


* **parent_group_id** (string)   `Required` 





{{< highlight json >}}
{
 "project_group_id": "pg-7120aabb662c",
 "parent_group_id": "pg-10efea238292"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectGroupInfo](#PROJECTGROUPINFO)
* **project_group_id** (string)   `Required` 

* **name** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **users** (string)  `Repeated`   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **parent_group_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 



{{< highlight json >}}
{
   "project_group_id": "pg-7120aabb662c",
   "name": "Cloudforet Core Team",
   "tags": {},
   "domain_id": "domain-186446b1516b",
   "workspace_id": "workspace-1a02ebcb3eb2",
   "parent_group_id": "pg-10efea238292",
   "created_at": "2024-07-12T03:31:02.222Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /identity/v2/project-group/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[ProjectGroupRequest](./ProjectGroup#projectgrouprequest)

* **project_group_id** (string)   `Required` 





{{< highlight json >}}
{
 "project_group_id": "pg-7120aabb662c"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### add_users





> **POST** /identity/v2/project-group/add-users
>





 {{< tabs " add_users " >}}

 {{< tab "Request Example" >}}



[UsersProjectGroupRequest](./ProjectGroup#usersprojectgrouprequest)

* **project_group_id** (string)   `Required` 


* **users** (string)  `Repeated`    `Required` 





{{< highlight json >}}
{
   "project_group_id": "pg-7120aabb662c",
   "users": ["wonny@cloudforet.io", "bolby@cloudforet.io"]
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectGroupInfo](#PROJECTGROUPINFO)
* **project_group_id** (string)   `Required` 

* **name** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **users** (string)  `Repeated`   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **parent_group_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 



{{< highlight json >}}
{
   "project_group_id": "pg-7120aabb662c",
   "name": "Cloudforet Core Team",
   "tags": {},
   "domain_id": "domain-186446b1516b",
   "workspace_id": "workspace-1a02ebcb3eb2",
   "parent_group_id": "pg-10efea238292",
   "created_at": "2024-07-12T03:31:02.222Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### remove_users





> **POST** /identity/v2/project-group/remove-users
>





 {{< tabs " remove_users " >}}

 {{< tab "Request Example" >}}



[UsersProjectGroupRequest](./ProjectGroup#usersprojectgrouprequest)

* **project_group_id** (string)   `Required` 


* **users** (string)  `Repeated`    `Required` 





{{< highlight json >}}
{
   "project_group_id": "pg-7120aabb662c",
   "users": ["wonny@cloudforet.io", "bolby@cloudforet.io"]
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectGroupInfo](#PROJECTGROUPINFO)
* **project_group_id** (string)   `Required` 

* **name** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **users** (string)  `Repeated`   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **parent_group_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 



{{< highlight json >}}
{
   "project_group_id": "pg-7120aabb662c",
   "name": "Cloudforet Core Team",
   "tags": {},
   "domain_id": "domain-186446b1516b",
   "workspace_id": "workspace-1a02ebcb3eb2",
   "parent_group_id": "pg-10efea238292",
   "created_at": "2024-07-12T03:31:02.222Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v2/project-group/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[ProjectGroupRequest](./ProjectGroup#projectgrouprequest)

* **project_group_id** (string)   `Required` 





{{< highlight json >}}
{
 "project_group_id": "pg-7120aabb662c"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectGroupInfo](#PROJECTGROUPINFO)
* **project_group_id** (string)   `Required` 

* **name** (string)   `Required` 

* **tags** (Struct)   `Required` 

* **users** (string)  `Repeated`   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **parent_group_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 



{{< highlight json >}}
{
   "project_group_id": "pg-7120aabb662c",
   "name": "Cloudforet Core Team",
   "tags": {},
   "domain_id": "domain-186446b1516b",
   "workspace_id": "workspace-1a02ebcb3eb2",
   "parent_group_id": "pg-10efea238292",
   "created_at": "2024-07-12T03:31:02.222Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /identity/v2/project-group/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[ProjectGroupSearchQuery](./ProjectGroup#projectgroupsearchquery)

* **query** (Query)  


* **project_group_id** (string)  


* **name** (string)  


* **workspace_id** (string)  


* **parent_group_id** (string)  





{{< highlight json >}}
{
   "query": {
       "page": {
           "start":1,
           "limit":10
       }
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectGroupsInfo](#PROJECTGROUPSINFO)
* **results** (ProjectGroupInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
       {
           "project_group_id": "pg-7120aabb662c",
           "name": "Cloudforet Core Team",
           "tags": {},
           "domain_id": "domain-186446b1516b",
           "workspace_id": "workspace-1a02ebcb3eb2",
           "parent_group_id": "pg-10efea238292",
           "created_at": "2024-07-12T03:31:02.222Z"
       }
   ],
   "total_count": 1
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /identity/v2/project-group/stat
>






    


<br>
<br>

## Message



### ChangeParentGroupRequest
* **project_group_id** (string)   `Required` 

    
* **parent_group_id** (string)   `Required` 

    <br>

### CreateProjectGroupRequest
* **name** (string)   `Required` 

    
* **tags** (Struct)  

    
* **parent_group_id** (string)  

    <br>

### ProjectGroupInfo
* **project_group_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **users** (string)  `Repeated`    `Required` 

    
* **reference_id** (string)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **parent_group_id** (string)   `Required` 

    
* **trusted_account_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_synced_at** (string)   `Required` 

    <br>

### ProjectGroupRequest
* **project_group_id** (string)   `Required` 

    <br>

### ProjectGroupSearchQuery
* **query** (Query)  

    
* **project_group_id** (string)  

    
* **name** (string)  

    
* **workspace_id** (string)  

    
* **parent_group_id** (string)  

    <br>

### ProjectGroupStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### ProjectGroupsInfo
* **results** (ProjectGroupInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateProjectGroupRequest
* **project_group_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### UsersProjectGroupRequest
* **project_group_id** (string)   `Required` 

    
* **users** (string)  `Repeated`    `Required` 

    <br>
