---
title: "WorkspaceGroup"
linkTitle: "WorkspaceGroup"
weight: 3
bookFlatSection: true
---
# [WorkspaceGroup](#WorkspaceGroup)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## WorkspaceGroup





**WorkspaceGroup Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./WorkspaceGroup#create) | [CreateWorkspaceGroupRequest](WorkspaceGroup#createworkspacegrouprequest) | [WorkspaceGroupInfo](WorkspaceGroup#workspacegroupinfo) |
| [**update**](./WorkspaceGroup#update) | [UpdateWorkspaceGroupRequest](WorkspaceGroup#updateworkspacegrouprequest) | [WorkspaceGroupInfo](WorkspaceGroup#workspacegroupinfo) |
| [**delete**](./WorkspaceGroup#delete) | [WorkspaceGroupRequest](WorkspaceGroup#workspacegrouprequest) | [Empty](WorkspaceGroup#empty) |
| [**add_workspaces**](./WorkspaceGroup#add_workspaces) | [WorkspacesWorkspaceGroupRequest](WorkspaceGroup#workspacesworkspacegrouprequest) | [WorkspaceGroupInfo](WorkspaceGroup#workspacegroupinfo) |
| [**remove_workspaces**](./WorkspaceGroup#remove_workspaces) | [WorkspacesWorkspaceGroupRequest](WorkspaceGroup#workspacesworkspacegrouprequest) | [WorkspaceGroupInfo](WorkspaceGroup#workspacegroupinfo) |
| [**add_users**](./WorkspaceGroup#add_users) | [UsersWorkspaceGroupRequest](WorkspaceGroup#usersworkspacegrouprequest) | [WorkspaceGroupInfo](WorkspaceGroup#workspacegroupinfo) |
| [**remove_users**](./WorkspaceGroup#remove_users) | [UsersWorkspaceGroupRequest](WorkspaceGroup#usersworkspacegrouprequest) | [WorkspaceGroupInfo](WorkspaceGroup#workspacegroupinfo) |
| [**update_role**](./WorkspaceGroup#update_role) | [WorkspaceGroupUpdateRoleRequest](WorkspaceGroup#workspacegroupupdaterolerequest) | [WorkspaceGroupInfo](WorkspaceGroup#workspacegroupinfo) |
| [**get**](./WorkspaceGroup#get) | [WorkspaceGroupRequest](WorkspaceGroup#workspacegrouprequest) | [WorkspaceGroupInfo](WorkspaceGroup#workspacegroupinfo) |
| [**list**](./WorkspaceGroup#list) | [WorkspaceGroupSearchQuery](WorkspaceGroup#workspacegroupsearchquery) | [WorkspaceGroupsInfo](WorkspaceGroup#workspacegroupsinfo) |
| [**stat**](./WorkspaceGroup#stat) | [WorkspaceGroupStatQuery](WorkspaceGroup#workspacegroupstatquery) | [Struct](WorkspaceGroup#struct) |



    
<br>

### create





> **POST** /identity/v2/workspace-group/create
>






    
<br>

### update





> **POST** /identity/v2/workspace-group/update
>






    
<br>

### delete





> **POST** /identity/v2/workspace-group/delete
>






    
<br>

### add_workspaces





> **POST** /identity/v2/workspace-group/add-workspaces
>






    
<br>

### remove_workspaces





> **POST** /identity/v2/workspace-group/remove-workspaces
>






    
<br>

### add_users





> **POST** /identity/v2/workspace-group/add-users
>






    
<br>

### remove_users





> **POST** /identity/v2/workspace-group/remove-users
>






    
<br>

### update_role





> **POST** /identity/v2/workspace-group/update-role
>






    
<br>

### get





> **POST** /identity/v2/workspace-group/get
>






    
<br>

### list





> **POST** /identity/v2/workspace-group/list
>






    
<br>

### stat





> **POST** /identity/v2/workspace-group/stat
>






    


<br>
<br>

## Message



### CreateWorkspaceGroupRequest
* **name** (string)   `Required` 

    
* **tags** (Struct)  

    <br>

### UpdateWorkspaceGroupRequest
* **workspace_group_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### UserWorkspaceGroup
* **user_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    
* **role_type** (string)   `Required` 

    
* **user_name** (string)   `Required` 

    
* **state** (string)   `Required` 

    <br>

### UsersWorkspaceGroupRequest
* **workspace_group_id** (string)   `Required` 

    
* **users** (UserWorkspaceGroup)  `Repeated`    `Required` 

    <br>

### WorkspaceGroupInfo
* **workspace_group_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **workspaces** (string)  `Repeated`    `Required` 

    
* **users** (UserWorkspaceGroup)  `Repeated`    `Required` 

    
* **tags** (Struct)   `Required` 

    
* **created_by** (string)   `Required` 

    
* **updated_by** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### WorkspaceGroupRequest
* **workspace_group_id** (string)   `Required` 

    <br>

### WorkspaceGroupSearchQuery
* **query** (Query)  

    
* **workspace_group_id** (string)  

    
* **name** (string)  

    
* **created_by** (string)  

    
* **updated_by** (string)  

    <br>

### WorkspaceGroupStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### WorkspaceGroupUpdateRoleRequest
* **workspace_group_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    <br>

### WorkspaceGroupsInfo
* **results** (WorkspaceGroupInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### WorkspacesWorkspaceGroupRequest
* **workspace_group_id** (string)   `Required` 

    
* **workspaces** (string)  `Repeated`    `Required` 

    <br>
