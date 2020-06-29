---
description:  
---
# User

>  **Package : spaceone.api.identity.v1**

## User

{% hint style="info" %}
**User Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](User.md#create)| [CreateUserRequest](User.md#createuserrequest) | [UserInfo](User.md#userinfo) |  |
| 2 | [update](User.md#update)| [UpdateUserRequest](User.md#updateuserrequest) | [UserInfo](User.md#userinfo) |  |
| 3 | [enable](User.md#enable)| [UserRequest](User.md#userrequest) | [UserInfo](User.md#userinfo) |  |
| 4 | [disable](User.md#disable)| [UserRequest](User.md#userrequest) | [UserInfo](User.md#userinfo) |  |
| 5 | [update_role](User.md#update_role)| [UpdateUserRoleRequest](User.md#updateuserrolerequest) | [UserInfo](User.md#userinfo) |  |
| 6 | [delete](User.md#delete)| [UserRequest](User.md#userrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 7 | [get](User.md#get)| [GetUserRequest](User.md#getuserrequest) | [UserInfo](User.md#userinfo) |  |
| 8 | [list](User.md#list)| [UserQuery](User.md#userquery) | [UsersInfo](User.md#usersinfo) |  |
| 9 | [stat](User.md#stat)| [UserStatQuery](User.md#userstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| 10 | [find](User.md#find)| [FindUserQuery](User.md#finduserquery) | [FindUsersInfo](User.md#findusersinfo) |  |
| 11 | [sync](User.md#sync)| [UserRequest](User.md#userrequest) | [UserInfo](User.md#userinfo) |  |

### create
> **POST** /identity/v1/users
>



| Type | Message |
| :--- | :--- |
| Request | [CreateUserRequest](User.md#createuserrequest) |
| Response |  [UserInfo](User.md#userinfo)  |



### update
> **PUT** /identity/v1/users
>

> Update user info by given user_id


| Type | Message |
| :--- | :--- |
| Request | [UpdateUserRequest](User.md#updateuserrequest) |
| Response |  [UserInfo](User.md#userinfo)  |


{% tabs %}
{% tab title="Request Example" %}
```text
{
    "user_id": "dkang@mz.co.kr",
    "tags": {
        "user1": "Reuters",
        "user2": "Bloomberg"
    },
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
    "mobile": "",
    "group": "",
    "language": "en",
    "timezone": "UTC",
    "tags": {
        "user1": "Reuters",
        "user2": "Bloomberg"
    },
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
| Request | [UserRequest](User.md#userrequest) |
| Response |  [UserInfo](User.md#userinfo)  |



### disable
> **PUT** /identity/v1/user/{user_id}/disable
>



| Type | Message |
| :--- | :--- |
| Request | [UserRequest](User.md#userrequest) |
| Response |  [UserInfo](User.md#userinfo)  |



### update_role
> **PUT** /identity/v1/user/{user_id}/roles
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateUserRoleRequest](User.md#updateuserrolerequest) |
| Response |  [UserInfo](User.md#userinfo)  |



### delete
> **DELETE** /identity/v1/users
>



| Type | Message |
| :--- | :--- |
| Request | [UserRequest](User.md#userrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /identity/v1/user/{user_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetUserRequest](User.md#getuserrequest) |
| Response |  [UserInfo](User.md#userinfo)  |



### list
> **GET** /identity/v1/users
>
> **POST** /identity/v1/users/search




| Type | Message |
| :--- | :--- |
| Request | [UserQuery](User.md#userquery) |
| Response |  [UsersInfo](User.md#usersinfo)  |



### stat
> **POST** /identity/v1/users/stat
>



| Type | Message |
| :--- | :--- |
| Request | [UserStatQuery](User.md#userstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |



### find
> **POST** /identity/v1/users/find
>



| Type | Message |
| :--- | :--- |
| Request | [FindUserQuery](User.md#finduserquery) |
| Response |  [FindUsersInfo](User.md#findusersinfo)  |



### sync
> **POST** /identity/v1/users/sync
>



| Type | Message |
| :--- | :--- |
| Request | [UserRequest](User.md#userrequest) |
| Response |  [UserInfo](User.md#userinfo)  |





## Message

### CreateUserRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_id |string | |required|
| 2 | password |string | |optional|
| 3 | name |string | |optional|
| 4 | email |string | |optional|
| 5 | mobile |string | |optional|
| 6 | group |string | |optional|
| 7 | language |string | |optional|
| 8 | timezone |string | |optional|
| 9 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |optional|
| 10 | domain_id |string | |optional|

### FindUserInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_id |string | ||
| 2 | name |string | ||
| 3 | email |string | ||
| 4 | mobile |string | ||
| 5 | group |string | ||
| 6 | state |string | ||

### FindUserQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | search |[FindUserSearch](User.md#findusersearch) | ||
| 2 | domain_id |string | ||

### FindUserSearch
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_id |string | ||
| 2 | keyword |string | ||

### FindUsersInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[FindUserInfo](User.md#finduserinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### GetUserRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### UpdateUserRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_id |string | ||
| 2 | password |string | ||
| 3 | name |string | ||
| 4 | email |string | ||
| 5 | mobile |string | ||
| 6 | group |string | ||
| 7 | language |string | ||
| 8 | timezone |string | ||
| 9 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 10 | domain_id |string | ||

### UpdateUserRoleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_id |string | ||
| 2 | roles |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | ||
| 3 | domain_id |string | ||

### UserInfo
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
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">
<p>UserInfo.State</p>
        <ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
          	<li>UNIDENTIFIED</li>
        </ul>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">email</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">mobile</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">group</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">language</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">timezone</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">roles</td>
      <td style="text-align:left">
<a href="User.md#roleinfo">RoleInfo</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">last_accessed_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
  </tbody>
</table>


### UserQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | user_id |string |❌ ||
| 3 | name |string |❌ ||
| 4 | state |string |❌ ||
| 5 | email |string |❌ ||
| 6 | mobile |string |❌ ||
| 7 | group |string |❌ ||
| 8 | role_id |string |❌ ||
| 9 | project_id |string |❌ ||
| 10 | project_group_id |string |❌ ||
| 11 | domain_id |string |❌ ||

### UserRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### UserStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### UsersInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[UserInfo](User.md#userinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||
