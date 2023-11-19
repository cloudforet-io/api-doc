---
title: "UserGroup"
linkTitle: "UserGroup"
weight: 3
bookFlatSection: true
---
# [UserGroup](#UserGroup)
User API which allows member management within project, company, and domain
note: Administrator must register User first.


>  **Package : spaceone.api.identity.v2**

<br>
<br>

## UserGroup





**UserGroup Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./UserGroup#create) | [CreateUserGroupRequest](UserGroup#createusergrouprequest) | [UserGroupInfo](UserGroup#usergroupinfo) |
| [**update**](./UserGroup#update) | [UpdateUserGroupRequest](UserGroup#updateusergrouprequest) | [UserGroupInfo](UserGroup#usergroupinfo) |
| [**delete**](./UserGroup#delete) | [UserGroupRequest](UserGroup#usergrouprequest) | [Empty](UserGroup#empty) |
| [**add_users**](./UserGroup#add_users) | [UsersUserGroupRequest](UserGroup#usersusergrouprequest) | [UserGroupInfo](UserGroup#usergroupinfo) |
| [**remove_users**](./UserGroup#remove_users) | [UsersUserGroupRequest](UserGroup#usersusergrouprequest) | [UserGroupInfo](UserGroup#usergroupinfo) |
| [**get**](./UserGroup#get) | [UserGroupRequest](UserGroup#usergrouprequest) | [UserGroupInfo](UserGroup#usergroupinfo) |
| [**list**](./UserGroup#list) | [UserGroupSearchQuery](UserGroup#usergroupsearchquery) | [UserGroupsInfo](UserGroup#usergroupsinfo) |
| [**stat**](./UserGroup#stat) | [UserGroupStatQuery](UserGroup#usergroupstatquery) | [Struct](UserGroup#struct) |



    
<br>

### create





> **POST** /identity/v2/user-group/create
>






    
<br>

### update





> **POST** /identity/v2/user-group/update
>






    
<br>

### delete





> **POST** /identity/v2/user-group/delete
>






    
<br>

### add_users





> **POST** /identity/v2/user-group/add-users
>






    
<br>

### remove_users





> **POST** /identity/v2/user-group/remove-users
>






    
<br>

### get





> **POST** /identity/v2/user-group/get
>






    
<br>

### list





> **POST** /identity/v2/user-group/list
>






    
<br>

### stat





> **POST** /identity/v1/user-group/stat
>






    


<br>
<br>

## Message



### CreateUserGroupRequest
* **name** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **tags** (Struct)  

    <br>

### UpdateUserGroupRequest
* **user_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### UserGroupInfo
* **user_group_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **users** (string)  `Repeated`    `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### UserGroupRequest
* **user_group_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    <br>

### UserGroupSearchQuery
* **query** (Query)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **user_group_id** (string)  

    
* **name** (string)  

    
* **workspace_id** (string)  

    
* **user_id** (string)  

    <br>

### UserGroupStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)  

    <br>

### UserGroupsInfo
* **results** (UserGroupInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UsersUserGroupRequest
* **user_group_id** (string)   `Required` 

    
* **users** (string)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    <br>
