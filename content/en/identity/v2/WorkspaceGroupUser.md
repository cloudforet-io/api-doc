---
title: "WorkspaceGroupUser"
linkTitle: "WorkspaceGroupUser"
weight: 3
bookFlatSection: true
---
# [WorkspaceGroupUser](#WorkspaceGroupUser)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## WorkspaceGroupUser





**WorkspaceGroupUser Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**add**](./WorkspaceGroupUser#add) | [WorkspaceGroupUsersRequest](WorkspaceGroupUser#workspacegroupusersrequest) | [WorkspaceGroupUserInfo](WorkspaceGroupUser#workspacegroupuserinfo) |
| [**remove**](./WorkspaceGroupUser#remove) | [WorkspaceGroupUsersRequest](WorkspaceGroupUser#workspacegroupusersrequest) | [WorkspaceGroupUserInfo](WorkspaceGroupUser#workspacegroupuserinfo) |
| [**update_role**](./WorkspaceGroupUser#update_role) | [WorkspaceGroupUserUpdateRoleRequest](WorkspaceGroupUser#workspacegroupuserupdaterolerequest) | [WorkspaceGroupUserInfo](WorkspaceGroupUser#workspacegroupuserinfo) |
| [**find**](./WorkspaceGroupUser#find) | [WorkspaceGroupUserFindRequest](WorkspaceGroupUser#workspacegroupuserfindrequest) | [WorkspaceGroupUsersSummaryInfo](WorkspaceGroupUser#workspacegroupuserssummaryinfo) |
| [**get**](./WorkspaceGroupUser#get) | [WorkspaceGroupUserRequest](WorkspaceGroupUser#workspacegroupuserrequest) | [WorkspaceGroupUserInfo](WorkspaceGroupUser#workspacegroupuserinfo) |
| [**list**](./WorkspaceGroupUser#list) | [WorkspaceGroupUserSearchQuery](WorkspaceGroupUser#workspacegroupusersearchquery) | [WorkspaceGroupUsersInfo](WorkspaceGroupUser#workspacegroupusersinfo) |
| [**stat**](./WorkspaceGroupUser#stat) | [WorkspaceGroupUserStatQuery](WorkspaceGroupUser#workspacegroupuserstatquery) | [Struct](WorkspaceGroupUser#struct) |



    
<br>

### add





> **POST** /identity/v2/workspace-group-user/add
>






    
<br>

### remove





> **POST** /identity/v2/workspace-group-user/remove
>






    
<br>

### update_role





> **POST** /identity/v2/workspace-group-user/update-role
>






    
<br>

### find





> **POST** /identity/v2/workspace-group-user/find
>






    
<br>

### get





> **POST** /identity/v2/workspace-group-user/get
>






    
<br>

### list





> **POST** /identity/v2/workspace-group-user/list
>






    
<br>

### stat





> **POST** /identity/v1/workspace-group-user/stat
>






    


<br>
<br>

## Message



### WorkspaceGroupUserFindRequest
* **workspace_group_id** (string)   `Required` 

    
* **keyword** (string)   `Required` 

    
* **state** (State)  

    
* **page** (Page)  

    <br>

### WorkspaceGroupUserInfo
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

### WorkspaceGroupUserRequest
* **workspace_group_id** (string)   `Required` 

    <br>

### WorkspaceGroupUserSearchQuery
* **query** (Query)  

    
* **workspace_group_id** (string)  

    
* **name** (string)  

    
* **created_by** (string)  

    
* **updated_by** (string)  

    <br>

### WorkspaceGroupUserStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **workspace_group_id** (string)   `Required` 

    <br>

### WorkspaceGroupUserSummaryInfo
* **user_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    <br>

### WorkspaceGroupUserUpdateRoleRequest
* **workspace_group_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    <br>

### WorkspaceGroupUsersInfo
* **results** (WorkspaceGroupUserInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### WorkspaceGroupUsersRequest
* **workspace_group_id** (string)   `Required` 

    
* **users** (UserWorkspaceGroup)  `Repeated`    `Required` 

    <br>

### WorkspaceGroupUsersSummaryInfo
* **results** (WorkspaceGroupUserSummaryInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
