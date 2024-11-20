---
title: "Project"
linkTitle: "Project"
weight: 3
bookFlatSection: true
---
# [Project](#Project)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Project





**Project Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Project#create) | [CreateProjectRequest](Project#createprojectrequest) | [ProjectInfo](Project#projectinfo) |
| [**update**](./Project#update) | [UpdateProjectRequest](Project#updateprojectrequest) | [ProjectInfo](Project#projectinfo) |
| [**update_project_type**](./Project#update_project_type) | [UpdateProjectTypeRequest](Project#updateprojecttyperequest) | [ProjectInfo](Project#projectinfo) |
| [**change_project_group**](./Project#change_project_group) | [ChangeProjectGroupRequest](Project#changeprojectgrouprequest) | [ProjectInfo](Project#projectinfo) |
| [**delete**](./Project#delete) | [ProjectRequest](Project#projectrequest) | [Empty](Project#empty) |
| [**add_users**](./Project#add_users) | [UsersProjectRequest](Project#usersprojectrequest) | [ProjectInfo](Project#projectinfo) |
| [**remove_users**](./Project#remove_users) | [UsersProjectRequest](Project#usersprojectrequest) | [ProjectInfo](Project#projectinfo) |
| [**get**](./Project#get) | [ProjectRequest](Project#projectrequest) | [ProjectInfo](Project#projectinfo) |
| [**list**](./Project#list) | [ProjectSearchQuery](Project#projectsearchquery) | [ProjectsInfo](Project#projectsinfo) |
| [**stat**](./Project#stat) | [ProjectStatQuery](Project#projectstatquery) | [Struct](Project#struct) |



    
<br>

### create





> **POST** /identity/v2/project/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateProjectRequest](./Project#createprojectrequest)

* **name** (string)   `Required` 


* **project_type** (ProjectType)   `Required` 


* **tags** (Struct)  


* **project_group_id** (string)  





{{< highlight json >}}
{
 "name": "Cloudforet Project",
 "project_type": "PUBLIC"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectInfo](#PROJECTINFO)
* **project_id** (string)   `Required` 

* **name** (string)   `Required` 

* **project_type** (ProjectType)   `Required` 

* **tags** (Struct)   `Required` 

* **users** (string)  `Repeated`   `Required` 

* **created_by** (string)   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_group_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 



{{< highlight json >}}
{
 "project_id": "project-a1b2c3d4e5f6",
 "name": "Cloudforet Project",
 "project_type": "PUBLIC",
 "created_by": "wonny@cloudforet.io",
 "domain_id": "domain-a1b2c3d4e5f6",
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "created_at": "2024-11-13T06:35:11.877Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update





> **POST** /identity/v2/project/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateProjectRequest](./Project#updateprojectrequest)

* **project_id** (string)   `Required` 


* **name** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
 "project_id": "project-a1b2c3d4e5f6",
 "name": "Wonny Project"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectInfo](#PROJECTINFO)
* **project_id** (string)   `Required` 

* **name** (string)   `Required` 

* **project_type** (ProjectType)   `Required` 

* **tags** (Struct)   `Required` 

* **users** (string)  `Repeated`   `Required` 

* **created_by** (string)   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_group_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 



{{< highlight json >}}
{
 "project_id": "project-a1b2c3d4e5f6",
 "name": "Cloudforet Project",
 "project_type": "PUBLIC",
 "created_by": "wonny@cloudforet.io",
 "domain_id": "domain-a1b2c3d4e5f6",
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "created_at": "2024-11-13T06:35:11.877Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update_project_type





> **POST** /identity/v2/project/update-project-type
>





 {{< tabs " update_project_type " >}}

 {{< tab "Request Example" >}}



[UpdateProjectTypeRequest](./Project#updateprojecttyperequest)

* **project_id** (string)   `Required` 


* **project_type** (ProjectType)   `Required` 





{{< highlight json >}}
{
 "project_id": "project-a1b2c3d4e5f6",
 "project_type": "PRIVATE"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectInfo](#PROJECTINFO)
* **project_id** (string)   `Required` 

* **name** (string)   `Required` 

* **project_type** (ProjectType)   `Required` 

* **tags** (Struct)   `Required` 

* **users** (string)  `Repeated`   `Required` 

* **created_by** (string)   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_group_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 



{{< highlight json >}}
{
 "project_id": "project-a1b2c3d4e5f6",
 "name": "Cloudforet Project",
 "project_type": "PUBLIC",
 "created_by": "wonny@cloudforet.io",
 "domain_id": "domain-a1b2c3d4e5f6",
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "created_at": "2024-11-13T06:35:11.877Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### change_project_group





> **POST** /identity/v2/project/change-project-group
>





 {{< tabs " change_project_group " >}}

 {{< tab "Request Example" >}}



[ChangeProjectGroupRequest](./Project#changeprojectgrouprequest)

* **project_id** (string)   `Required` 


* **project_group_id** (string)   `Required` 





{{< highlight json >}}
{
 "project_group_id": "pg-a1b2c3d4e5f6",
 "project_id": "project-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectInfo](#PROJECTINFO)
* **project_id** (string)   `Required` 

* **name** (string)   `Required` 

* **project_type** (ProjectType)   `Required` 

* **tags** (Struct)   `Required` 

* **users** (string)  `Repeated`   `Required` 

* **created_by** (string)   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_group_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 



{{< highlight json >}}
{
 "project_id": "project-a1b2c3d4e5f6",
 "name": "Cloudforet Project",
 "project_type": "PUBLIC",
 "created_by": "wonny@cloudforet.io",
 "domain_id": "domain-a1b2c3d4e5f6",
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "created_at": "2024-11-13T06:35:11.877Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /identity/v2/project/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[ProjectRequest](./Project#projectrequest)

* **project_id** (string)   `Required` 





{{< highlight json >}}
{
 "project_id": "project-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### add_users





> **POST** /identity/v2/project/add-users
>





 {{< tabs " add_users " >}}

 {{< tab "Request Example" >}}



[UsersProjectRequest](./Project#usersprojectrequest)

* **project_id** (string)   `Required` 


* **users** (string)  `Repeated`    `Required` 





{{< highlight json >}}
{
 "project_id": "project-a1b2c3d4e5f6",
 "users": ["cloudforet@cloudforet.io", "wonny@cloudforet.io"]
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectInfo](#PROJECTINFO)
* **project_id** (string)   `Required` 

* **name** (string)   `Required` 

* **project_type** (ProjectType)   `Required` 

* **tags** (Struct)   `Required` 

* **users** (string)  `Repeated`   `Required` 

* **created_by** (string)   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_group_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 



{{< highlight json >}}
{
 "project_id": "project-a1b2c3d4e5f6",
 "name": "Cloudforet Project",
 "project_type": "PUBLIC",
 "created_by": "wonny@cloudforet.io",
 "domain_id": "domain-a1b2c3d4e5f6",
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "created_at": "2024-11-13T06:35:11.877Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### remove_users





> **POST** /identity/v2/project/remove-users
>





 {{< tabs " remove_users " >}}

 {{< tab "Request Example" >}}



[UsersProjectRequest](./Project#usersprojectrequest)

* **project_id** (string)   `Required` 


* **users** (string)  `Repeated`    `Required` 





{{< highlight json >}}
{
 "project_id": "project-a1b2c3d4e5f6",
 "users": ["cloudforet@cloudforet.io", "wonny@cloudforet.io"]
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectInfo](#PROJECTINFO)
* **project_id** (string)   `Required` 

* **name** (string)   `Required` 

* **project_type** (ProjectType)   `Required` 

* **tags** (Struct)   `Required` 

* **users** (string)  `Repeated`   `Required` 

* **created_by** (string)   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_group_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 



{{< highlight json >}}
{
 "project_id": "project-a1b2c3d4e5f6",
 "name": "Cloudforet Project",
 "project_type": "PUBLIC",
 "created_by": "wonny@cloudforet.io",
 "domain_id": "domain-a1b2c3d4e5f6",
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "created_at": "2024-11-13T06:35:11.877Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v2/project/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[ProjectRequest](./Project#projectrequest)

* **project_id** (string)   `Required` 





{{< highlight json >}}
{
 "project_id": "project-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectInfo](#PROJECTINFO)
* **project_id** (string)   `Required` 

* **name** (string)   `Required` 

* **project_type** (ProjectType)   `Required` 

* **tags** (Struct)   `Required` 

* **users** (string)  `Repeated`   `Required` 

* **created_by** (string)   `Required` 

* **reference_id** (string)   `Required` 

* **is_managed** (bool)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **project_group_id** (string)   `Required` 

* **trusted_account_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_synced_at** (string)   `Required` 



{{< highlight json >}}
{
 "project_id": "project-a1b2c3d4e5f6",
 "name": "Cloudforet Project",
 "project_type": "PUBLIC",
 "created_by": "wonny@cloudforet.io",
 "domain_id": "domain-a1b2c3d4e5f6",
 "workspace_id": "workspace-a1b2c3d4e5f6",
 "created_at": "2024-11-13T06:35:11.877Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list





> **POST** /identity/v2/project/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[ProjectSearchQuery](./Project#projectsearchquery)

* **query** (Query)  


* **project_id** (string)  


* **name** (string)  


* **project_type** (ProjectType)  


* **created_by** (string)  


* **include_children** (bool)  


* **workspace_id** (string)  


* **project_group_id** (string)  


* **user_id** (string)  





{{< highlight json >}}
{
 "project_type": "PRIVATE",
 "query": {
   "page": {
     "start": 1,
     "limit": 10
   },
   "sort": [{
     "key": "created_at",
     "desc": true
   }]
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ProjectsInfo](#PROJECTSINFO)
* **results** (ProjectInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
 "results": [
 {
   "created_at": "2024-11-13T07:01:56.295Z",
   "created_by": "wonny@cloudforet.io",
   "domain_id": "domain-a1b2c3d4e5f6",
   "name": "Wonny Project",
   "project_group_id": "pg-a1b2c3d4e5f6",
   "project_id": "project-a1b2c3d4e5f6",
   "project_type": "PRIVATE",
   "users": [
     "wonny@cloudforet.io"
   ],
   "workspace_id": "workspace-a1b2c3d4e5f6"
 },
 {
   "created_at": "2024-11-13T06:35:11.877Z",
   "created_by": "cloudforet@cloudforet.io",
   "domain_id": "domain-a1b2c3d4e5f6",
   "name": "Cloudforet Project",
   "project_group_id": "pg-a1b2c3d4e5f6",
   "project_id": "project-g7h8i9j1k2l3",
   "project_type": "PRIVATE",
   "users": [
     "cloudforet@cloudforet.io",
     "wonny@cloudforet.io"
   ],
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





> **POST** /identity/v2/project/stat
>






    


<br>
<br>

## Message



### ChangeProjectGroupRequest
* **project_id** (string)   `Required` 

    
* **project_group_id** (string)   `Required` 

    <br>

### CreateProjectRequest
* **name** (string)   `Required` 

    
* **project_type** (ProjectType)   `Required` 

    
* **tags** (Struct)  

    
* **project_group_id** (string)  

    <br>

### ProjectInfo
* **project_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **project_type** (ProjectType)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **users** (string)  `Repeated`    `Required` 

    
* **created_by** (string)   `Required` 

    
* **reference_id** (string)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_group_id** (string)   `Required` 

    
* **trusted_account_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_synced_at** (string)   `Required` 

    <br>

### ProjectRequest
* **project_id** (string)   `Required` 

    <br>

### ProjectSearchQuery
* **query** (Query)  

    
* **project_id** (string)  

    
* **name** (string)  

    
* **project_type** (ProjectType)  

    
* **created_by** (string)  

    
* **include_children** (bool)  

    
* **workspace_id** (string)  

    
* **project_group_id** (string)  

    
* **user_id** (string)  

    <br>

### ProjectStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### ProjectsInfo
* **results** (ProjectInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateProjectRequest
* **project_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### UpdateProjectTypeRequest
* **project_id** (string)   `Required` 

    
* **project_type** (ProjectType)   `Required` 

    <br>

### UsersProjectRequest
* **project_id** (string)   `Required` 

    
* **users** (string)  `Repeated`    `Required` 

    <br>
