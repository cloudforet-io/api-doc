---
description: User API which allows member management within project, company, and domain
---
# User

>  **Package : spaceone.api.identity.v1**

## User

{% hint style="info" %}
**User Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](user.md#create)|   [CreateUserRequest](user.md#createuserrequest) |   [UserInfo](user.md#userinfo) |
| [**update**](user.md#update)|   [UpdateUserRequest](user.md#updateuserrequest) |   [UserInfo](user.md#userinfo) |
| [**verify_email**](user.md#verify_email)|   [VerifyEmailRequest](user.md#verifyemailrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**confirm_email**](user.md#confirm_email)|   [ConfirmEmailRequest](user.md#confirmemailrequest) |   [UserInfo](user.md#userinfo) |
| [**reset_password**](user.md#reset_password)|   [UserRequest](user.md#userrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**set_required_actions**](user.md#set_required_actions)|   [SetRequiredActionsRequest](user.md#setrequiredactionsrequest) |   [UserInfo](user.md#userinfo) |
| [**enable**](user.md#enable)|   [UserRequest](user.md#userrequest) |   [UserInfo](user.md#userinfo) |
| [**disable**](user.md#disable)|   [UserRequest](user.md#userrequest) |   [UserInfo](user.md#userinfo) |
| [**delete**](user.md#delete)|   [UserRequest](user.md#userrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](user.md#get)|   [GetUserRequest](user.md#getuserrequest) |   [UserInfo](user.md#userinfo) |
| [**list**](user.md#list)|   [UserQuery](user.md#userquery) |   [UsersInfo](user.md#usersinfo) |
| [**stat**](user.md#stat)|   [UserStatQuery](user.md#userstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|
| [**find**](user.md#find)|   [FindUserQuery](user.md#finduserquery) |   [FindUsersInfo](user.md#findusersinfo) |
| [**sync**](user.md#sync)|   [UserRequest](user.md#userrequest) |   [UserInfo](user.md#userinfo) | 
 

 
### create
> **POST** /identity/v1/user/create
>


| Type | Message |
| :--- | :--- |
| Request | [CreateUserRequest](user.md#createuserrequest) |
| Response |  [UserInfo](user.md#userinfo)  |
 
 

 
### update
> **POST** identity/v1/user/update
>

> Update user info by given user_id

| Type | Message |
| :--- | :--- |
| Request | [UpdateUserRequest](user.md#updateuserrequest) |
| Response |  [UserInfo](user.md#userinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "user_id": "dkang@mz.co.kr",
    "tags": [
        {
            "key": "user1",
            "value": "Reuters"
        },
        {
            "key": "user2",
            "value": "Bloomberg"
        }
    ],
    "domain_id": "{{DOMAIN_ID}}"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "user_id": "dkang@mz.co.kr",
    "name": "Dong Yoo kang",
    "state": "ENABLED",
    "email": "dkang@mz.co.kr",
    "language": "en",
    "timezone": "UTC",
    "tags": [
        {
            "key": "user1",
            "value": "Reuters"
        },
        {
            "key": "user2",
            "value": "Bloomberg"
        }
    ],
    "last_accessed_at": {
        "seconds": "1593161630",
        "nanos": 79000000
    },
    "created_at": {
        "seconds": "1593161630",
        "nanos": 79000000
    },
    "domain_id": "domain-fd6e23a5ae36"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### verify_email
> **POST** identity/v1/user/verify-email
>


| Type | Message |
| :--- | :--- |
| Request | [VerifyEmailRequest](user.md#verifyemailrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### confirm_email
> **POST** identity/v1/user/confirm-email
>


| Type | Message |
| :--- | :--- |
| Request | [ConfirmEmailRequest](user.md#confirmemailrequest) |
| Response |  [UserInfo](user.md#userinfo)  |
 
 

 
### reset_password
> **POST** identity/v1/user/reset-password
>


| Type | Message |
| :--- | :--- |
| Request | [UserRequest](user.md#userrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### set_required_actions
> **POST** identity/v1/user/set-required-actions
>


| Type | Message |
| :--- | :--- |
| Request | [SetRequiredActionsRequest](user.md#setrequiredactionsrequest) |
| Response |  [UserInfo](user.md#userinfo)  |
 
 

 
### enable
> **POST** /identity/v1/user/enable
>


| Type | Message |
| :--- | :--- |
| Request | [UserRequest](user.md#userrequest) |
| Response |  [UserInfo](user.md#userinfo)  |
 
 

 
### disable
> **POST** /identity/v1/user/disable
>


| Type | Message |
| :--- | :--- |
| Request | [UserRequest](user.md#userrequest) |
| Response |  [UserInfo](user.md#userinfo)  |
 
 

 
### delete
> **POST** /identity/v1/user/delete
>


| Type | Message |
| :--- | :--- |
| Request | [UserRequest](user.md#userrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **POST** /identity/v1/user/get
>


| Type | Message |
| :--- | :--- |
| Request | [GetUserRequest](user.md#getuserrequest) |
| Response |  [UserInfo](user.md#userinfo)  |
 
 

 
### list
> **POST** /identity/v1/user/list
>


| Type | Message |
| :--- | :--- |
| Request | [UserQuery](user.md#userquery) |
| Response |  [UsersInfo](user.md#usersinfo)  |
 
 

 
### stat
> **POST** /identity/v1/user/stat
>


| Type | Message |
| :--- | :--- |
| Request | [UserStatQuery](user.md#userstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |
 
 

 
### find
> **POST** /identity/v1/users/find
>


| Type | Message |
| :--- | :--- |
| Request | [FindUserQuery](user.md#finduserquery) |
| Response |  [FindUsersInfo](user.md#findusersinfo)  |
 
 

 
### sync
> **POST** /identity/v1/user/sync
>


| Type | Message |
| :--- | :--- |
| Request | [UserRequest](user.md#userrequest) |
| Response |  [UserInfo](user.md#userinfo)  |


## 

## Message

### ConfirmEmailRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_id |string|✔| |
| verify_code |string|✔| |
| domain_id |string|✔| |

### CreateUserRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">password</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">email</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE_USER_TYPE</li>
          	<li>USER</li>
          	<li>API_USER</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">backend</td>
      <td style="text-align:left"><ul>
          	<li>NONE_BACKEND</li>
          	<li>LOCAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">language</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">timezone</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">reset_password</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### FindUserInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| user_id |string | |
| name |string | |
| email |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### FindUserQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| search |[FindUserSearch](user.md#findusersearch)|✔| |
| domain_id |string|✔| |

### FindUserSearch
| Field | Type |  Description |
| :--- | :--- | :--- |
| user_id |string | |
| keyword |string | |

### FindUsersInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of FindUserInfo](user.md#finduserinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetUserRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### SetRequiredActionsRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">actions</td>
      <td style="text-align:left"><ul>
          	<li>UPDATE_PASSWORD</li>
        </ul></td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### UpdateUserRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_id |string|✔| |
| password |string|✘| |
| name |string|✘| |
| email |string|✘| |
| language |string|✘| |
| timezone |string|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
| reset_password |bool|✘| |

### UserInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
          	<li>PENDING</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">email</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE_USER_TYPE</li>
          	<li>USER</li>
          	<li>API_USER</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">backend</td>
      <td style="text-align:left"><ul>
          	<li>NONE_BACKEND</li>
          	<li>LOCAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">language</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">timezone</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">required_actions</td>
      <td style="text-align:left"><ul>
          	<li>UPDATE_PASSWORD</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">last_accessed_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">email_verified</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### UserQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">email</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE_USER_TYPE</li>
          	<li>USER</li>
          	<li>API_USER</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">backend</td>
      <td style="text-align:left"><ul>
          	<li>NONE_BACKEND</li>
          	<li>LOCAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### UserRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_id |string|✔| |
| domain_id |string|✔| |

### UserStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### UsersInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of UserInfo](user.md#userinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### VerifyEmailRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_id |string|✔| |
| email |string|✘| |
| force |bool|✘| |
| domain_id |string|✔| |
