---
title: "UserProfile"
linkTitle: "UserProfile"
weight: 3
bookFlatSection: true
---
# [UserProfile](#UserProfile)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## UserProfile





**UserProfile Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**update**](./UserProfile#update) | [UpdateUserProfileRequest](UserProfile#updateuserprofilerequest) | [UserInfo](UserProfile#userinfo) |
| [**verify_email**](./UserProfile#verify_email) | [VerifyEmailRequest](UserProfile#verifyemailrequest) | [Empty](UserProfile#empty) |
| [**confirm_email**](./UserProfile#confirm_email) | [ConfirmEmailRequest](UserProfile#confirmemailrequest) | [UserInfo](UserProfile#userinfo) |
| [**reset_password**](./UserProfile#reset_password) | [UserPasswordResetRequest](UserProfile#userpasswordresetrequest) | [Empty](UserProfile#empty) |
| [**enable_mfa**](./UserProfile#enable_mfa) | [EnableMFARequest](UserProfile#enablemfarequest) | [UserInfo](UserProfile#userinfo) |
| [**disable_mfa**](./UserProfile#disable_mfa) | [DisableMFARequest](UserProfile#disablemfarequest) | [UserInfo](UserProfile#userinfo) |
| [**confirm_mfa**](./UserProfile#confirm_mfa) | [ConfirmMFARequest](UserProfile#confirmmfarequest) | [UserInfo](UserProfile#userinfo) |
| [**get**](./UserProfile#get) | [UserProfileRequest](UserProfile#userprofilerequest) | [UserInfo](UserProfile#userinfo) |
| [**get_workspaces**](./UserProfile#get_workspaces) | [UserProfileRequest](UserProfile#userprofilerequest) | [MyWorkspacesInfo](UserProfile#myworkspacesinfo) |



    
<br>

### update





> **POST** /identity/v2/user-profile/update
>






    
<br>

### verify_email





> **POST** /identity/v2/user-profile/verify-email
>






    
<br>

### confirm_email





> **POST** /identity/v2/user-profile/confirm-email
>






    
<br>

### reset_password

+noauth



> **POST** /identity/v2/user-profile/reset-password
>






    
<br>

### enable_mfa

Enable MFA for user. If this api is called, send email to user.



> **POST** /identity/v2/user-profile/enable-mfa
>





 {{< tabs " enable_mfa " >}}

 {{< tab "Request Example" >}}



[EnableMFARequest](./UserProfile#enablemfarequest)

* **mfa_type** (string)   `Required` 

  *EMAIL*


* **options** (Struct)   `Required` 

  *If mfa_type is EMAIL, email is required in options. options will be saved in mfa's options field.*





{{< highlight json >}}
{
 "user_id": "example@cloudforet.com",
 "mfa_type": "EMAIL",
 "options": {"email": "wonny@cloudforet.com"},
 "domain_id": "domain-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### disable_mfa

Disable MFA for user. If this api is called, send email to user.



> **POST** /identity/v2/user-profile/disable-mfa
>





 {{< tabs " disable_mfa " >}}

 {{< tab "Request Example" >}}



[DisableMFARequest](./UserProfile#disablemfarequest)




{{< highlight json >}}
{
 "user_id": "example@cloudforet.com",
 "force": false,
 "domain_id": "domain-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### confirm_mfa

Confirm MFA for user by given verify_code which is sent by your authentication method.



> **POST** /identity/v2/user-profile/confirm-mfa
>





 {{< tabs " confirm_mfa " >}}

 {{< tab "Request Example" >}}



[ConfirmMFARequest](./UserProfile#confirmmfarequest)

* **verify_code** (string)   `Required` 





{{< highlight json >}}
{
 "user_id": "example@cloudforet",
 "verify_code": "123456",
 "domain_id": "domain-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v2/user-profile/get
>






    
<br>

### get_workspaces





> **POST** /identity/v2/user-profile/get-workspaces
>






    


<br>
<br>

## Message



### ConfirmEmailRequest
* **verify_code** (string)   `Required` 

    <br>

### ConfirmMFARequest
* **verify_code** (string)   `Required` 

    <br>

### DisableMFARequest<br>

### EnableMFARequest
* **mfa_type** (string)   `Required` 

  *EMAIL*

    
* **options** (Struct)   `Required` 

  *If mfa_type is EMAIL, email is required in options. options will be saved in mfa's options field.*

    <br>

### MyWorkspaceInfo
* **workspace_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **role_name** (string)   `Required` 

    
* **role_type** (RoleType)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **created_by** (string)   `Required` 

    
* **reference_id** (string)   `Required` 

    
* **is_managed** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **role_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_synced_at** (string)   `Required` 

    <br>

### MyWorkspacesInfo
* **results** (MyWorkspaceInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateUserProfileRequest
* **password** (string)  

    
* **name** (string)  

    
* **email** (string)  

    
* **language** (string)  

    
* **timezone** (string)  

    
* **tags** (Struct)  

    <br>

### UserPasswordResetRequest
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UserProfileRequest<br>

### VerifyEmailRequest
* **email** (string)  

    <br>
