---
title: "User"
linkTitle: "User"
weight: 3
bookFlatSection: true
---
# [User](#User)
desc: User API which allows member management within project, company, and domain
note: Administrator must register User first.


>  **Package : spaceone.api.identity.v1**

<br>
<br>

## User


**User Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./User#create) | [CreateUserRequest](User#createuserrequest) | [UserInfo](./User#userinfo) |
| [**update**](./User#update) | [UpdateUserRequest](User#updateuserrequest) | [UserInfo](./User#userinfo) |
| [**verify_email**](./User#verify_email) | [VerifyEmailRequest](User#verifyemailrequest) | [Empty](./User#empty) |
| [**confirm_email**](./User#confirm_email) | [ConfirmEmailRequest](User#confirmemailrequest) | [UserInfo](./User#userinfo) |
| [**reset_password**](./User#reset_password) | [UserRequest](User#userrequest) | [Empty](./User#empty) |
| [**set_required_actions**](./User#set_required_actions) | [SetRequiredActionsRequest](User#setrequiredactionsrequest) | [UserInfo](./User#userinfo) |
| [**enable**](./User#enable) | [UserRequest](User#userrequest) | [UserInfo](./User#userinfo) |
| [**disable**](./User#disable) | [UserRequest](User#userrequest) | [UserInfo](./User#userinfo) |
| [**delete**](./User#delete) | [UserRequest](User#userrequest) | [Empty](./User#empty) |
| [**get**](./User#get) | [GetUserRequest](User#getuserrequest) | [UserInfo](./User#userinfo) |
| [**list**](./User#list) | [UserQuery](User#userquery) | [UsersInfo](./User#usersinfo) |
| [**stat**](./User#stat) | [UserStatQuery](User#userstatquery) | [Struct](./User#struct) |
| [**find**](./User#find) | [FindUserQuery](User#finduserquery) | [FindUsersInfo](./User#findusersinfo) |
| [**sync**](./User#sync) | [UserRequest](User#userrequest) | [UserInfo](./User#userinfo) |



    
<br>

### create

> **POST** /identity/v1/user/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /identity/v1/user/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### verify_email

> **POST** /identity/v1/user/verify-email
>




 {{< tabs " verify_email " >}}




{{< /tabs >}}

    
<br>

### confirm_email

> **POST** /identity/v1/user/confirm-email
>




 {{< tabs " confirm_email " >}}




{{< /tabs >}}

    
<br>

### reset_password

> **POST** /identity/v1/user/reset-password
>




 {{< tabs " reset_password " >}}




{{< /tabs >}}

    
<br>

### set_required_actions

> **POST** /identity/v1/user/set-required-actions
>




 {{< tabs " set_required_actions " >}}




{{< /tabs >}}

    
<br>

### enable

> **POST** /identity/v1/user/enable
>




 {{< tabs " enable " >}}




{{< /tabs >}}

    
<br>

### disable

> **POST** /identity/v1/user/disable
>




 {{< tabs " disable " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /identity/v1/user/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /identity/v1/user/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /identity/v1/user/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /identity/v1/user/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    
<br>

### find

> **POST** /identity/v1/users/find
>




 {{< tabs " find " >}}




{{< /tabs >}}

    
<br>

### sync

> **POST** /identity/v1/user/sync
>




 {{< tabs " sync " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### ConfirmEmailRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **verify_code** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CreateUserRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **password** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **email** (string)  `Required` 

  *is_required: false*

    
* **user_type** (UserType)  `Required` 

  *is_required: false*

    
* **backend** (UserBackend)  `Required` 

  *is_required: true*

    
* **language** (string)  `Required` 

  *is_required: false*

    
* **timezone** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **reset_password** (bool)  `Required` 

  *is_required: false*

    <br>

### FindUserInfo
* **user_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **email** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    <br>

### FindUserQuery
* **search** (FindUserSearch)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### FindUserSearch
* **user_id** (string)  `Required` 

    
* **keyword** (string)  `Required` 

    <br>

### FindUsersInfo
* **results** (FindUserInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### GetUserRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### SetRequiredActionsRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **actions** (UserRequiredAction)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateUserRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **password** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **email** (string)  `Required` 

  *is_required: false*

    
* **language** (string)  `Required` 

  *is_required: false*

    
* **timezone** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **reset_password** (bool)  `Required` 

  *is_required: false*

    <br>

### UserInfo
* **user_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **email** (string)  `Required` 

    
* **user_type** (UserType)  `Required` 

    
* **backend** (UserBackend)  `Required` 

    
* **language** (string)  `Required` 

    
* **timezone** (string)  `Required` 

    
* **required_actions** (UserRequiredAction)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **last_accessed_at** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **email_verified** (bool)  `Required` 

    <br>

### UserQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **state** (string)  `Required` 

  *is_required: false*

    
* **email** (string)  `Required` 

  *is_required: false*

    
* **user_type** (UserType)  `Required` 

  *is_required: false*

    
* **backend** (UserBackend)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### UserRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UserStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UsersInfo
* **results** (UserInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### VerifyEmailRequest
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **email** (string)  `Required` 

  *is_required: false*

    
* **force** (bool)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
