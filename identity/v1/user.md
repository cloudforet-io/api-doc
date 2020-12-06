---
description: User API which allows member management within project, company, and domain
---
# User

>  **Package : spaceone.api.identity.v1**

## User

{% hint style="info" %}
**User Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](user.md#create)|   [CreateUserRequest](user.md#createuserrequest) |   [UserInfo](user.md#userinfo) |  |
| 2 | [**update**](user.md#update)|   [UpdateUserRequest](user.md#updateuserrequest) |   [UserInfo](user.md#userinfo) | Update user info by given user_id |
| 3 | [**enable**](user.md#enable)|   [UserRequest](user.md#userrequest) |   [UserInfo](user.md#userinfo) |  |
| 4 | [**disable**](user.md#disable)|   [UserRequest](user.md#userrequest) |   [UserInfo](user.md#userinfo) |  |
| 5 | [**update_role**](user.md#update_role)|   [UpdateUserRoleRequest](user.md#updateuserrolerequest) |   [UserInfo](user.md#userinfo) |  |
| 6 | [**delete**](user.md#delete)|   [UserRequest](user.md#userrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 7 | [**get**](user.md#get)|   [GetUserRequest](user.md#getuserrequest) |   [UserInfo](user.md#userinfo) |  |
| 8 | [**list**](user.md#list)|   [UserQuery](user.md#userquery) |   [UsersInfo](user.md#usersinfo) |  |
| 9 | [**stat**](user.md#stat)|   [UserStatQuery](user.md#userstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| 10 | [**find**](user.md#find)|   [FindUserQuery](user.md#finduserquery) |   [FindUsersInfo](user.md#findusersinfo) |  |
| 11 | [**sync**](user.md#sync)|   [UserRequest](user.md#userrequest) |   [UserInfo](user.md#userinfo) |  | 
 

 
### create
> **POST** /identity/v1/users
>


| Type | Message |
| :--- | :--- |
| Request | [CreateUserRequest](user.md#createuserrequest) |
| Response |  [UserInfo](user.md#userinfo)  |
 
 

 
### update
> **PUT** /identity/v1/users
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
    "roles": [],
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
 
 

 
### enable
> **PUT** /identity/v1/user/{user_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [UserRequest](user.md#userrequest) |
| Response |  [UserInfo](user.md#userinfo)  |
 
 

 
### disable
> **PUT** /identity/v1/user/{user_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [UserRequest](user.md#userrequest) |
| Response |  [UserInfo](user.md#userinfo)  |
 
 

 
### update_role
> **PUT** /identity/v1/user/{user_id}/roles
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateUserRoleRequest](user.md#updateuserrolerequest) |
| Response |  [UserInfo](user.md#userinfo)  |
 
 

 
### delete
> **DELETE** /identity/v1/users
>


| Type | Message |
| :--- | :--- |
| Request | [UserRequest](user.md#userrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /identity/v1/user/{user_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetUserRequest](user.md#getuserrequest) |
| Response |  [UserInfo](user.md#userinfo)  |
 
 

 
### list
> **GET** /identity/v1/users
>
> **POST** /identity/v1/users/search



| Type | Message |
| :--- | :--- |
| Request | [UserQuery](user.md#userquery) |
| Response |  [UsersInfo](user.md#usersinfo)  |
 
 

 
### stat
> **POST** /identity/v1/users/stat
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
> **POST** /identity/v1/users/sync
>


| Type | Message |
| :--- | :--- |
| Request | [UserRequest](user.md#userrequest) |
| Response |  [UserInfo](user.md#userinfo)  |


## 

## Message

### CreateUserRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">password</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">email</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">user_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE_USER_TYPE</li>
          	<li>USER</li>
          	<li>API_USER</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">backend</td>
      <td style="text-align:left"><ul>
          	<li>NONE_BACKEND</li>
          	<li>LOCAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">language</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">timezone</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">list of spaceone.api.core.v1.Tag</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### FindUserInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | user_id |string | |
| 2 | name |string | |
| 3 | email |string | |
| 4 | tags |list of spaceone.api.core.v1.Tag | |

### FindUserQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | search |[FindUserSearch](user.md#findusersearch)|✅| |
| 2 | domain_id |string|✅| |

### FindUserSearch
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | user_id |string | |
| 2 | keyword |string | |

### FindUsersInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of FindUserInfo](user.md#finduserinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetUserRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### UpdateUserRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_id |string|✅| |
| 2 | password |string|❌| |
| 3 | name |string|❌| |
| 4 | email |string|❌| |
| 5 | language |string|❌| |
| 6 | timezone |string|❌| |
| 7 | tags |list of spaceone.api.core.v1.Tag|❌| |
| 8 | domain_id |string|✅| |

### UpdateUserRoleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_id |string|✅| |
| 2 | roles |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✅| |
| 3 | domain_id |string|✅| |

### UserInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
          	<li>PENDING</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">email</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">user_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE_USER_TYPE</li>
          	<li>USER</li>
          	<li>API_USER</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">backend</td>
      <td style="text-align:left"><ul>
          	<li>NONE_BACKEND</li>
          	<li>LOCAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">language</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">timezone</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">roles</td>
      <td style="text-align:left"><a href="user.md#roleinfo">list of RoleInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">list of spaceone.api.core.v1.Tag</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">last_accessed_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### UserQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">email</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">user_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE_USER_TYPE</li>
          	<li>USER</li>
          	<li>API_USER</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">backend</td>
      <td style="text-align:left"><ul>
          	<li>NONE_BACKEND</li>
          	<li>LOCAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">role_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### UserRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_id |string|✅| |
| 2 | domain_id |string|✅| |

### UserStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### UsersInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of UserInfo](user.md#userinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
