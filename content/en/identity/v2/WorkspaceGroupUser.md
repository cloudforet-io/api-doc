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
| [**add**](./WorkspaceGroupUser#add) | [WorkspaceGroupUsersRequest](WorkspaceGroupUser#workspacegroupusersrequest) | [WorkspaceGroupInfo](WorkspaceGroupUser#workspacegroupinfo) |
| [**remove**](./WorkspaceGroupUser#remove) | [WorkspaceGroupUsersRequest](WorkspaceGroupUser#workspacegroupusersrequest) | [WorkspaceGroupInfo](WorkspaceGroupUser#workspacegroupinfo) |
| [**update_role**](./WorkspaceGroupUser#update_role) | [WorkspaceGroupUserUpdateRoleRequest](WorkspaceGroupUser#workspacegroupuserupdaterolerequest) | [WorkspaceGroupInfo](WorkspaceGroupUser#workspacegroupinfo) |
| [**find**](./WorkspaceGroupUser#find) | [WorkspaceGroupUserFindRequest](WorkspaceGroupUser#workspacegroupuserfindrequest) | [WorkspaceGroupUsersSummaryInfo](WorkspaceGroupUser#workspacegroupuserssummaryinfo) |
| [**get**](./WorkspaceGroupUser#get) | [WorkspaceGroupUserRequest](WorkspaceGroupUser#workspacegroupuserrequest) | [WorkspaceGroupInfo](WorkspaceGroupUser#workspacegroupinfo) |
| [**list**](./WorkspaceGroupUser#list) | [WorkspaceGroupUserSearchQuery](WorkspaceGroupUser#workspacegroupusersearchquery) | [WorkspaceGroupsInfo](WorkspaceGroupUser#workspacegroupsinfo) |
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

    
* **target_user_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    <br>

### WorkspaceGroupUsersRequest
* **workspace_group_id** (string)   `Required` 

    
* **users** (UserWorkspaceGroup)  `Repeated`    `Required` 

    <br>

### WorkspaceGroupUsersSummaryInfo
* **results** (WorkspaceGroupUserSummaryInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
